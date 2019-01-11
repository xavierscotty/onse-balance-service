@worker
Feature: Update the account balance
  As a client I want to get the latest account balance details so that I can check whether account has sufficient funds.

  Scenario: Account recently created
    Given a newly created bank account
    When I deposit the account "9890" with "8" credits
    Then the account "9890" should has "8" credit(s)

  Scenario: Balance debited and credited
    Given I deposit and withdraw credits multiple times from account "827354235"
    When I deposit the account with "1" credit
    And I deposit the account with "9" credit
    And I withdrawn from the account with "-9" credit
    Then the account should has "1" credit(s)

