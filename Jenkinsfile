def github_id = 'ONSdigital'

def namespace = github_id.toLowerCase()
def app_image_name = "onsetraining/${namespace}-balance-service"
def worker_image_name = "onsetraining/${namespace}-balance-service-worker"
def git_repository = "https://github.com/${github_id}/onse-balance-service"

def kaniko_image = 'gcr.io/kaniko-project/executor:debug-b0e7c0e8cd07ef3ad2b7181e0779af9fcb312f0b'
def kubectl_image = 'aklearning/onse-eks-kubectl-deployer:0.0.1'

def git_commit = ''

def label = "build-${UUID.randomUUID().toString()}"
def build_pod_template = """
kind: Pod
metadata:
  name: build-pod
spec:
  containers:
  - name: app-image-builder
    image: ${kaniko_image}
    imagePullPolicy: Always
    command:
    - /busybox/cat
    tty: true
    volumeMounts:
      - name: jenkins-docker-cfg
        mountPath: /root/.docker

  - name: worker-image-builder
    image: ${kaniko_image}
    imagePullPolicy: Always
    command:
    - /busybox/cat
    tty: true
    volumeMounts:
      - name: jenkins-docker-cfg
        mountPath: /root/.docker

  - name: kubectl
    image: ${kubectl_image}
    imagePullPolicy: Always
    tty: true

  - name: python-test
    image: aklearning/onse-pg-python:0.0.1
    tty: true

  volumes:
  - name: jenkins-docker-cfg
    projected:
      sources:
      - secret:
          name: regcred
          items:
            - key: dockerconfigjson
              path: config.json
"""

podTemplate(name: "${namespace}-balance-service-build", label: label, yaml: build_pod_template) {
  node(label) {
    git git_repository

    stage('Test') {
        container(name: 'python-test', shell: '/bin/sh') {
            sh 'pipenv install --dev'
            sh 'bin/run_tests.sh'
        }
    }

    stage('Build App Image') {
      git_commit = sh (
        script: 'git rev-parse HEAD',
        returnStdout: true
      ).trim()
      app_image_name += ":${git_commit}"
      container(name: 'app-image-builder', shell: '/busybox/sh') {
        withEnv(['PATH+EXTRA=/busybox:/kaniko']) {
          echo "Building app image ${app_image_name}"
          sh """#!/busybox/sh
          /kaniko/executor -f `pwd`/Dockerfile.app -c `pwd` --skip-tls-verify --cache=true --destination=${app_image_name}
          """
        }
      }
    }

    stage('Build Worker Image') {
      git_commit = sh (
        script: 'git rev-parse HEAD',
        returnStdout: true
      ).trim()
      worker_image_name += ":${git_commit}"
      container(name: 'worker-image-builder', shell: '/busybox/sh') {
        withEnv(['PATH+EXTRA=/busybox:/kaniko']) {
          echo "Building worker image ${worker_image_name}"
          sh """#!/busybox/sh
          /kaniko/executor -f `pwd`/Dockerfile.worker -c `pwd` --skip-tls-verify --cache=true --destination=${worker_image_name}
          """
        }
      }
    }

    stage('Deploy to Kubernetes') {
      withCredentials([
        string(credentialsId: 'AWS_ACCESS_KEY_ID', variable: 'AWS_ACCESS_KEY_ID'),
        string(credentialsId: 'AWS_SECRET_ACCESS_KEY', variable: 'AWS_SECRET_ACCESS_KEY'),
        string(credentialsId: 'KUBERNETES_SERVER', variable: 'KUBERNETES_SERVER'),
        file(credentialsId: 'KUBERNETES_CA', variable: 'KUBERNETES_CA')
      ]) {
        container(name: 'kubectl', shell: '/bin/sh') {
          sh '''kubectl config \
              set-cluster kubernetes \
              --server=$KUBERNETES_SERVER \
              --certificate-authority=$KUBERNETES_CA
          '''
          sh "yq.v2 w -i kubernetes/app-deployment.yml 'spec.template.spec.containers[0].image' ${app_image_name}"
          sh "yq.v2 w -i kubernetes/worker-deployment.yml 'spec.template.spec.containers[0].image' ${worker_image_name}"
          sh "kubectl create namespace ${namespace} || true"
          sh "kubectl apply -n ${namespace} -f kubernetes/"
        }
      }
    }
  }
}
