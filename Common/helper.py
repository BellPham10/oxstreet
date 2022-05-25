import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
# options.add_argument('--headless')
# options.add_argument('window-size=1400,1024')
options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(
    '/Users/my.pham/Documents/GitHub/oxstreet/Resources/chromedriver',
    options=options)


def open_page(url):
    driver.maximize_window()
    driver.get(url)


def wait_for_element_located(xpath='', id='', class_name='', text='', timeout=10):
    if xpath:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    if id:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, id))
        )
    if class_name:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_name))
        )
    if text:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.LINK_TEXT, text))
        )


def is_displayed(element):
    status = driver.find_element_by_name(element).is_displayed()
    return status


def send_keys(xpath='', id='', class_name='', keys=''):
    for c in keys:
        if class_name:
            driver.find_element_by_class_name(class_name).send_keys(c)
        if xpath:
            driver.find_element_by_id(xpath).send_keys(c)
        if id:
            driver.find_element_by_id(id).send_keys(c)


def click(xpath='', class_name='', id='', text=''):
    if class_name:
        driver.find_element_by_class_name(class_name).click()
    if xpath:
        driver.find_element_by_xpath(xpath).click()
    if id:
        driver.find_element_by_id(id).click()
    if text:
        driver.find_element_by_link_text(text).click()
    time.sleep(0.1)


def run_js(js):
    log = driver.execute_script(js)
    return log


def get_content_from_xpath(xpath):
    js = 'return document.evaluate(\'' + xpath + '\', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;'
    content = driver.execute_script(js)
    print('---->')
    print(content)
    return content


def get_text(xpath):
    text = driver.find_element_by_xpath(xpath).text
    return text


def get_text_by_class_name(class_name):
    text = driver.find_element_by_class_name(class_name).text
    return text


def get_submit_text(xpath):
    text = driver.find_element_by_xpath(xpath).get_property(
        "value"
    )
    return text


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def get_random_digits(length):
    letters = string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


# def save_bank_info():
#     key = value
#     return key

def is_displayed(xpath='', id='', class_name=''):
    if class_name:
        status = driver.find_element_by_class_name(class_name).is_displayed()
        return status
    if xpath:
        status = driver.find_element_by_xpath(xpath).is_displayed()
        return status
    if id:
        status = driver.find_element_by_id(id).is_displayed()
        return status

def entering(class_name=''):
     if class_name:
        elem = driver.find_element_by_class_name(class_name)
        elem.clear()
        # return elem
        elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
    # if xpath:
    #     status = driver.find_element_by_xpath(xpath).is_displayed()
    #     return status
    # if id:
    #     status = driver.find_element_by_id(id).is_displayed()
    #     return status
    # driver = webdriver.Firefox()
    # driver.get("http://www.python.org")
    # assert "Python" in driver.title
    # elem = driver.find_element_by_name("q")
    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)