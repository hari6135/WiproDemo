Feature: Leave Workflow

  Background:
    Given user logs into OrangeHRM

  Scenario: Apply Leave

    When user applies leave

    Then success toast message should appear

    And leave balance should reduce by 1
