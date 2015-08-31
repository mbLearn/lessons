### Created BY May07 ###
Feature: Regression tests for Amazon.com
#
#  Scenario: Navigate to Departments page
#    Then Click the "Shop by" link



  Scenario Outline: Verify the presence of a file on a system [0-3]
    Then Click on <link> and assert <page>

    Examples:
    | link      | page                  |
    | Brand     | Featured Brands       |
    | Character    | Featured Character |
