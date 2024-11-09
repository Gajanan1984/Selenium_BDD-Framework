Feature: Register Account Funtionality

  Scenario:Register with mandatory fields
    Given I navigate to Register page
    When I enter details into mandatory fields
    And I click on Continue button
    Then Account should get created

  Scenario: Register with all fields
    Given I navigate to Register page
    When I enter details into all fields
    And I click on Continue button
    Then Account should get created

   Scenario: Register with a duplicate email address
     Given I navigate to Register page
     When I enter details into all fields except email field
     And I enter existing accounts email into email field
     And I click on Continue button
     Then I should get proper warning message

   Scenario: Register without providing any details
     Given I navigate to Register page
     When I dont enter anything into fields
     And I click on Continue button
     Then I should get proper warning message

