*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${CART_BUTTON}    id:shopping_cart_container

*** Keywords ***
Open Cart
    Click Element    ${CART_BUTTON}