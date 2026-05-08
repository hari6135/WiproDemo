Feature: Admin Search Functionality

  Background:
    Given user logs into OrangeHRM application

  Scenario: Search admin user with multiple filters

    When user searches user with below details
      | Username  | Admin   |
      | User Role | Admin   |
      | Status    | Enabled |
    Then matching records should be displayed