Feature: Employee Management

  Background:
    Given user logs into OrangeHRM application

  Scenario Outline: Add multiple employees

    When user opens PIM module
    And user clicks Add Employee
    And user enters firstname "<FirstName>"
    And user enters lastname "<LastName>"
    And user clicks save employee button
    Then employee added successfully

    Examples:
      | FirstName | LastName |
      | Hari      | Kumar    |
      | Arun      | Raj      |
      | Vicky     | Kumar    |