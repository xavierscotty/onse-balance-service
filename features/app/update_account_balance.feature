@worker
Feature: Update the account balance
  As a client
  I want to get the latest account balance details
  So that I can check whether account has sufficient funds

  Scenario: Account recently created
    Given a newly created bank account "9890"
    When a balance update message is received for account "9890" with 8 credits
    Then the account "9890" should have 8 credits

