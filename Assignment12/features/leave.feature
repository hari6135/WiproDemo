Feature: Leave Application Workflow

  Background:
    Given user logs into OrangeHRM application

  Scenario: Apply medical leave

    When user opens Leave module
    And user applies leave
    Then success toast should appear
    And leave status should be Pending Approval
    And leave balance should be reduced