Feature: Orange HRM logo

  Scenario: Logo presence on the Orange home page
    Given Launch chrome browser
    When open orange page
    Then verify that the logo present
    And close browser
