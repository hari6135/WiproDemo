Feature: Login Functionality

  Scenario: Successful Login

    Given user navigates to OrangeHRM login page

    When user enters username "Admin"
    And user enters password "admin123"
    And user clicks login button

    Then dashboard page should be displayed