# Created by my.pham at 10/07/2021
Feature: Add bank account
  Scenario: [CP-592] Navigate to Add bank account page
    Given authentication successfully without 2FA
    Then I go to Setting page
    Then I choose Bank accounts tab
    Then system navigate to Bank account page

  Scenario: [CP-592] Check UI bank account list page
    Given authentication successfully without 2FA
    Then I go to Setting page
    Then I choose Bank accounts tab
    Then system navigate to Bank account page
    Then check UI bank account list

  Scenario: [CP-587] Check UI Add bank account page
    Given authentication successfully without 2FA
    Then I go to Setting page
    Then I choose Bank accounts tab
    Then system navigate to Bank account page
    Then check UI add bank account

  Scenario: [CP-587] TC02 Verify that able to add bank account successfully
    Given authentication successfully without 2FA
    Then I go to Setting page
    Then I choose Bank accounts tab
    Then system navigate to Bank account page
    Then I click Add bank account button
    Then I enter valid data into all required fields
    Then I click Submit button
    Then system show Email popup
#    Then I click OK button
#    Then system navigate to Bank account page
    Then I check new bank account was added
#    Then I verify new bank account '<bank_name>' is correct
#    Examples:
#      | bank_name |

  Scenario: [CP-587] TC03 Verify that “Submit” button is enabled when all required fields are inputted
    Given authentication successfully without 2FA
    Then I go to Setting page
    Then I choose Bank accounts tab
    Then system navigate to Bank account page
    Then I click Add bank account button
    Then I verify 


