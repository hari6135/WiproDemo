Feature: Login Functionality

  Background:
    Given user navigates to OrangeHRM login page

  Scenario: Successful login with valid credentials

    When user enters username "Admin"
    And user enters password "admin123"
    And user clicks login button
    Then dashboard page should be displayed

  Scenario: Unsuccessful login with invalid password

    When user enters username "Admin"
    And user enters password "wrongpass"
    And user clicks login button
    Then invalid credential message should be displayed