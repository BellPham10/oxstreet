import csv
import re
from Common.helper import *
from Pages import sign_in as signin
from Common import certificate as cer
from Common import localization as language

def test_text():
    url = 'https://oxstreet.com/'
    open_page(url=url)
    wait_for_element_located(xpath=signin.title)
    click(xpath=signin.title)
    wait_for_element_located(xpath=signin.login_btn)
    click(xpath=signin.login_btn)

    wait_for_element_located(id=signin.usernameId)
    wait_for_element_located(id=signin.passwordId)
    wait_for_element_located(xpath=signin.btnLogin)

    send_keys(id=signin.usernameId, keys=cer.valid_email)
    send_keys(id=signin.passwordId, keys=cer.valid_pwd)

    click(xpath=signin.submitCl)

    wait_for_element_located(id=signin.searchId)
    send_keys(id=signin.searchId, keys=cer.searchKey)
    wait_for_element_located(class_name=signin.searchResultClassname)
    assert get_text_by_class_name(class_name=signin.searchResultClassname) == language.en['login']['searchResult']
