@Smoke
@Regression

Feature: Profile Update

  Background:
    Given user logs into OrangeHRM

  Scenario: Upload Profile Photo

    When user uploads profile image

    Then profile should update successfully