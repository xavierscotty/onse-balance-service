@app
Feature: Get the account balance
  As a client I want to get the account balance details so that I can check whether account has sufficient funds.

  Scenario: Account has sufficient funds
    Given a bank account "12345" with balance "809"
    When I request the account "12345" balance
    Then the account balance should be "809"

  Scenario: Account not exists
    Given a bank account "12345" with balance "809"
    When I request the account "00000" balance
    Then the account data not found