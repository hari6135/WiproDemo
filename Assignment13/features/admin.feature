Feature: Admin Search

  Background:
    Given user logs into OrangeHRM

  Scenario: Search User

    When I enter the following search criteria:

      | Username  | Admin   |
      | User Role | Admin   |
      | Status    | Enabled |

    Then matching admin records should appear