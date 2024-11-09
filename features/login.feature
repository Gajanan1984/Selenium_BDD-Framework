Feature: Login Funtionality


  Scenario:Login with valid credentials
    Given I navigated to login page
    When I enter valid email address and valid password into the fields
    And I click on ok button
    Then I should succussfully loged in


  Scenario:Login with invalid email address and valid password
    Given I navigated to login page
    When I enter invalid email address and valid password
    And I click on ok button
    Then I should get proper warning message


  Scenario: Login with valid email address and invaid password
    Given I navigated to login page
    When I enter valid email address and invaid password
    And I click on ok button
    Then I should get Proper warning message


  Scenario: Login with invalid credentials
    Given I navigated to login page
    When I enter invalid email address and password
    And I click on ok button
    Then I should get Proper warning message


  Scenario: Login without entering any credentials
    Given I navigated to login page
    When I dont enter anything into search fields
    And I click on ok button
    Then I should get Proper warning message


