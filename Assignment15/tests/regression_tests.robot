*** Settings ***
Resource    ../Resources/common.resource
Resource    ../Resources/login_page.resource

Library     ../Libraries/ProductPage.py


Suite Setup       Open Browser To SauceDemo
Suite Teardown    Close Browser Session
Test Teardown     Capture Failure Screenshot

*** Test Cases ***
Invalid User
    Invalid Login Scenario
    ...    invalid_user
    ...    secret_sauce
    ...    Epic sadface: Username and password do not match any user in this service

Locked User
    Invalid Login Scenario
    ...    locked_out_user
    ...    secret_sauce
    ...    Epic sadface: Sorry, this user has been locked out.

Problem User
    Invalid Login Scenario
    ...    problem_user
    ...    wrong_password
    ...    Epic sadface: Username and password do not match any user in this service

Price Validation Test
    [Tags]    Critical    Regression

    Login To Application    standard_user    secret_sauce

    ${price1}=    Get Product Price By Name    Sauce Labs Backpack
    ${price2}=    Get Product Price By Name    Sauce Labs Bike Light

    ${total}=    Evaluate    ${price1}+${price2}

    Log To Console    Total Price = ${total}

    Should Be Equal As Numbers    ${total}    39.98