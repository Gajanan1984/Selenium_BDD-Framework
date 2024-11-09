Feature: Search Functionality

@test
  Scenario: Search for a valid product
    Given I got navigated to Home page
    When I enter valid product into the search box field
    And I click on search button
    Then Valid product should get displayed in search field

  Scenario:Search for an invalid product
    Given I got navigated to Home page
    When I enter invalid product into the search box field
    And I click on search button
    Then Proper message should be displayed in search result

  Scenario:Search without entering any product
    Given I got navigated to Home page
    When I dont enter into search box field
    And I click on search button
    Then Proper message should be displayed in search result