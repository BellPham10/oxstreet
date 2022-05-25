import time

from behave import *
from selenium.common.exceptions import NoSuchElementException

from Common.helper import *
from Pages import sign_in as signin
from Common import certificate as cer
from Common import localization as language
from Pages import RFQ as RFQ
from Pages import setting as setting

use_step_matcher("re")

@then("I go to Setting page")
def step_impl(context):
    wait_for_element_located(id=RFQ.profileDropdownId)
    click(id=RFQ.profileDropdownId)
    click(text=RFQ.settingItem)
    wait_for_element_located(id=setting.APItokentabId)


@then("I choose Bank accounts tab")
def step_impl(context):
    click(text=setting.BankAccountstab)


@then("system navigate to Bank account page")
def step_impl(context):
    wait_for_element_located(xpath=setting.xpathTitleBankAccount)
    assert get_text(xpath=setting.xpathTitleBankAccount) == language.en["settings"]["titleBankAccounts"]
    wait_for_element_located(xpath=setting.xpathContentBankAccount)
    assert get_text(xpath=setting.xpathContentBankAccount) == language.en["settings"]["contentBankAccounts"]


@then("check UI bank account list")
def step_impl(context):
    try:
        elem = driver.find_element_by_xpath(setting.noAddressIconXpath)
        if elem.is_displayed():
            wait_for_element_located(xpath=setting.emptyIcon)
            wait_for_element_located(class_name=setting.nobankAccounAdded)
            wait_for_element_located(xpath=setting.emptyAddBCbt)
            assert get_text(xpath=setting.emptyAddBCbt) == language.en["settings"]["addBankAccountButton"]
            assert get_text(xpath=setting.noAddressIconXpath) == language.en["settings"]["emptyBankAccountList"]


    except NoSuchElementException:
        wait_for_element_located(class_name=setting.bankAccountList)
        wait_for_element_located(xpath=setting.currencySettingBankaccountId)
        wait_for_element_located(xpath=setting.benNameSettingBankaccountid)
        wait_for_element_located(xpath=setting.bankNameSettingBankaccountId)
        wait_for_element_located(xpath=setting.bankNoSettingBankAccountId)
        wait_for_element_located(xpath=setting.statusSettingBankaccountId)
        assert get_text(xpath=setting.currencySettingBankaccountId) == language.en["settings"]["currencyBA"]
        assert get_text(xpath=setting.benNameSettingBankaccountid) == language.en["settings"]["benNameBA"]
        assert get_text(xpath=setting.bankNameSettingBankaccountId) == language.en["settings"]["bankName"]
        assert get_text(xpath=setting.bankNoSettingBankAccountId) == language.en["settings"]["bankNo"]
        assert get_text(xpath=setting.statusSettingBankaccountId) == language.en["settings"]["status"]


@then("check UI add bank account")
def step_impl(context):
    wait_for_element_located(text=language.en["settings"]["addBankAccountButton"])
    click(text=language.en["settings"]["addBankAccountButton"])
    wait_for_element_located(text=language.en["settings"]["createBATitle"])
    # wait_for_element_located(text=language.en["settings"]["benNameBA"])
    # wait_for_element_located(text=language.en["settings"]["bankName"])
    # wait_for_element_located(text=language.en["settings"]["bankNo"])
    # wait_for_element_located(text=language.en["settings"]["status"])
    # wait_for_element_located(text=language.en["settings"]["bankBranchName"])
    # wait_for_element_located(text=language.en["settings"]["bankCountry"])
    # wait_for_element_located(text=language.en["settings"]["bankAddress"])
    # wait_for_element_located(text=language.en["settings"]["SWIFT/BIC/ABA"])
    # wait_for_element_located(text=language.en["settings"]["reference"])
    # wait_for_element_located(text=language.en["settings"]["interBankName"])
    # wait_for_element_located(text=language.en["settings"]["interBankSwiftBic"])
    # wait_for_element_located(text=language.en["settings"]["interBankAddress"])

    wait_for_element_located(id=setting.currencyId)
    wait_for_element_located(id=setting.bankCountryId)
    wait_for_element_located(id=setting.inpBankName)
    wait_for_element_located(id=setting.inpBranchName)
    wait_for_element_located(id=setting.inpAccountNumber)
    wait_for_element_located(id=setting.inpBeneficiaryName)
    wait_for_element_located(id=setting.inpBankAddress)
    wait_for_element_located(id=setting.inpReference)
    wait_for_element_located(id=setting.inpInterBankName)
    wait_for_element_located(id=setting.inpInterBankSwift)
    wait_for_element_located(id=setting.inpInterBankAddress)
    wait_for_element_located(id=setting.btnCancel)
    wait_for_element_located(id=setting.btnSubmit)


@then("I enter valid data into all required fields")
def step_impl(context):
    wait_for_element_located(id=setting.currencyId)
    wait_for_element_located(id=setting.bankCountryId)
    wait_for_element_located(id=setting.inpBankName)
    bank_name = get_random_string(6) + cer.inpBankName
    send_keys(id=setting.inpBankName, keys=bank_name)
    wait_for_element_located(id=setting.inpAccountNumber)
    bank_no = get_random_digits(9)
    send_keys(id=setting.inpAccountNumber, keys=bank_no)
    wait_for_element_located(id=setting.inpBeneficiaryName)
    ben_name = cer.inpBeneficiaryName + get_random_string(6)
    send_keys(id=setting.inpBeneficiaryName, keys=ben_name)
    # save_bank_info(bank_name,bank_no,ben_name)
    # check is_displayed
@then("I click Submit button")
def step_impl(context):
    wait_for_element_located(id=setting.btnSubmit)
    click(id=setting.btnSubmit)


@then("I click Add bank account button")
def step_impl(context):
    # wait_for_element_located(text=language.en["settings"]["addBankAccountButton"])
    click(text=language.en["settings"]["addBankAccountButton"])


@then("system show Email popup")
def step_impl(context):
    # time.sleep(5)
    wait_for_element_located(class_name=setting.popupClass)
    wait_for_element_located(xpath=setting.contentPopupxpath)

@then("I click OK button")
def step_impl(context):
    click(text=language.en["settings"]["btnOK"])


