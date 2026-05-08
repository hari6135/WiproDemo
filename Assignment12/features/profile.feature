@Smoke
@Regression
@Profile

Feature: Profile Update

  Background:
    Given user logs into OrangeHRM application

  Scenario: Update nickname and upload profile photo

    When user opens My Info page
    And user updates nickname "Hari"
    And user uploads image "profile.jpg"
    And user clicks profile save button
    Then profile updated successfully