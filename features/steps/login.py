from behave import *

from Common.helper import *
from Pages import sign_in as signin
from Common import certificate as cer
from Common import localization as language
from Pages import RFQ as RFQ

use_step_matcher("re")


@given("Launch browser at sign in screen")
def step_impl(context):
    url = cer.url
    open_page(url=url)


@when("Input valid username and valid password")
def step_impl(context):
    wait_for_element_located(id=signin.usernameId)
    wait_for_element_located(id=signin.passwordId)
    send_keys(id=signin.usernameId, keys=cer.valid_username)
    send_keys(id=signin.passwordId, keys=cer.valid_pwd)


@step("I Click login button")
def step_impl(context):
    wait_for_element_located(class_name=signin.submitCl)
    click(class_name=signin.submitCl)


@step("I Disable Google Captcha")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I Disable Google Captcha')


@step("Authenticate TwoFAThen Verify wallet screen is displayed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Authenticate TwoFAThen Verify wallet screen is displayed')


@step("I log out the account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I log out the account')


@when("Input valid username")
def step_impl(context):
    wait_for_element_located(id=signin.usernameId)
    send_keys(id=signin.usernameId, keys=cer.valid_username)
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When Input valid username')


@then("Verify Error Message")
def step_impl(context):
    wait_for_element_located(xpath=signin.xpath_error_message)
    assert get_text(xpath=signin.xpath_error_message) == language.en['login']['error_message']
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Verify Error Message')


@when("Input valid password")
def step_impl(context):
    wait_for_element_located(id=signin.passwordId)
    send_keys(id=signin.passwordId, keys=cer.valid_pwd)
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When Input valid password')


@when("Input invalid username and invalid password")
def step_impl(context):
    wait_for_element_located(id=signin.usernameId)
    wait_for_element_located(id=signin.passwordId)
    send_keys(id=signin.usernameId, keys=cer.invalid_username)
    send_keys(id=signin.passwordId, keys=cer.invalid_pwd)
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When Input invalid username and invalid password')


@then("Verify RFQ screen is displayed")
def step_impl(context):
    wait_for_element_located(xpath=signin.xpath_success_message)
    assert get_text(xpath=signin.xpath_success_message) == language.en['login']['success_message']

    wait_for_element_located(id=RFQ.RFQId)


@when("Input valid email into username")
def step_impl(context):
    wait_for_element_located(id=signin.usernameId)
    wait_for_element_located(id=signin.passwordId)
    send_keys(id=signin.usernameId, keys=cer.valid_email)
    send_keys(id=signin.passwordId, keys=cer.valid_pwd)
    raise NotImplementedError(u'STEP: When Input valid email into username')


@given("authentication successfully without 2FA")
def step_impl(context):
    url = cer.url
    open_page(url=url)

    wait_for_element_located(id=signin.usernameId)
    wait_for_element_located(id=signin.passwordId)
    wait_for_element_located(class_name=signin.submitCl)
    send_keys(id=signin.usernameId, keys=cer.valid_username)
    send_keys(id=signin.passwordId, keys=cer.valid_pwd)

    click(class_name=signin.submitCl)

    wait_for_element_located(id=RFQ.RFQId)
