Feature: Employee Management

  Background:
    Given user logs into OrangeHRM

  Scenario Outline: Add Employees

    When I enter "<FirstName>" and "<LastName>"

    Then employee should be created successfully

    Examples:
      | FirstName | LastName |
      | Hari      | Kumar    |
      | Arun      | Raj      |
      | Vicky     | Kumar    |