Feature: As a user, i would like to login
  Scenario: without data
  Given Launch browser at sign in screen
    And I Click login button
    Then Verify Error Message

  Scenario: with empty password
    Given Launch browser at sign in screen
    When Input valid username
    And I Click login button
    Then Verify Error Message

  Scenario: with empty username
    Given Launch browser at sign in screen
    When Input valid password
    And I Click login button
    Then Verify Error Message

  Scenario: with invalid certification
    Given Launch browser at sign in screen
    When Input invalid username and invalid password
    And I Click login button
    Then Verify Error Message

  Scenario: with email input
    Given Launch browser at sign in screen
    When Input valid email into username
    And I Click login button
    Then Verify Error Message

  Scenario: with valid certificate
    Given Launch browser at sign in screen
    When Input valid username and valid password
    And I Click login button
    Then Verify RFQ screen is displayed

  Scenario: Authentication successfully without 2FA
    Given Authentication successfully without 2FA
