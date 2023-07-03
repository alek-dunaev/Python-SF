# Run tests:
# python -m pytest -v --driver Chrome --driver-path C:/project/chromedriver.exe tests/test_auth_page_rostelekom.py

import pytest
import random
import time
import string
from pages.auth_page import AuthPage
from settings import valid_email, valid_password, valid_login, valid_phone, valid_LS
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


# TC-RT-001 Регистрация по электронной почте. Позитивный тест.
def test_registration_email(web_browser):
    page = AuthPage(web_browser)

    page.registration.click()
    page.name.send_keys('Александр')
    page.lastname.send_keys('Дунаев')
    time.sleep(3)
    page.region.send_keys('Пермский край')
    page.email_or_phone.send_keys(valid_email)
    page.password.send_keys(valid_password)
    page.confirmation.send_keys(valid_password)
    page.register.click()
    page.auth_code.send_keys(valid_email)
    page.get_code.click()

    page2 = pytest.driver.get('https://e.mail.ru/inbox/')
    element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span', 'Ваш код')
    )
    page2.element.click()
    element2 = driver.find_element(By.TAG_NAME, 'div > p')
    for i in element2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()

    page = AuthPage(web_browser)
    page.rt_code.send_keys(my_code)

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=3011e2b2-06d5-47d4-94be-2571e7f6356d&client_id=account_b2c&theme=light#/'


# TC-RT-002 Регистрация по номеру телефона. Позитивный тест.
def test_registration_phone(web_browser):
    page = AuthPage(web_browser)

    page.registration.click()
    page.name.send_keys('Александр')
    page.lastname.send_keys('Дунаев')
    page.region.send_keys('Пермский край')
    page.email_or_phone.send_keys(valid_phone)
    page.password.send_keys(valid_password)
    page.confirmation.send_keys(valid_password)
    page.register.click()
    page.auth_code.send_keys(valid_phone)
    page.get_code.click()
    page.rt_code.send_keys()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=3011e2b2-06d5-47d4-94be-2571e7f6356d&client_id=account_b2c&theme=light#/'


# TC-RT-003 Регистрация по номеру телефона. Негативный тест.
def test_registration_phone_negativ(web_browser):
    page = AuthPage(web_browser)

    page.registration.click()
    page.name.send_keys('Александр')
    page.lastname.send_keys('Дунаев')
    page.region.send_keys('Пермский край')
    page.email_or_phone.send_keys(valid_phone)
    page.password.send_keys(valid_password)
    page.confirmation.send_keys(generate_random_string(8))
    page.register.click()
    page.auth_code.send_keys(valid_phone)
    page.get_code.click()
    page.rt_code.send_keys()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=3011e2b2-06d5-47d4-94be-2571e7f6356d&client_id=account_b2c&theme=light#/'


# TC-RT-004 Авторизация по логину. Позитивный тест.
def test_authorisation_login(web_browser):
    page = AuthPage(web_browser)

    page.login.send_keys(valid_login)
    page.password.send_keys(valid_password)
    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=3011e2b2-06d5-47d4-94be-2571e7f6356d&client_id=account_b2c&theme=light#/'


# TC-RT-005 Авторизация по логину. Негативный тест.
def test_authorisation_login_negativ(web_browser):
    page = AuthPage(web_browser)

    page.login.send_keys(generate_random_string(8))
    page.password.send_keys(valid_password)
    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=3011e2b2-06d5-47d4-94be-2571e7f6356d&client_id=account_b2c&theme=light#/'


# TC-RT-006 Авторизация по электронной почте.
def test_authorisation_email(web_browser):
    page = AuthPage(web_browser)

    page.email.send_keys(valid_email)
    page.password.send_keys(valid_password)
    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=3011e2b2-06d5-47d4-94be-2571e7f6356d&client_id=account_b2c&theme=light#/'


# TC-RT-007 Авторизация по номеру телефона.
def test_authorisation_phone(web_browser):
    page = AuthPage(web_browser)

    page.phone.send_keys(valid_phone)
    page.password.send_keys(valid_password)
    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=3011e2b2-06d5-47d4-94be-2571e7f6356d&client_id=account_b2c&theme=light#/'


# TC-RT-008 Авторизация по номеру лицевого счёта.
def test_authorisation_LS(web_browser):
    page = AuthPage(web_browser)

    page.pa.send_keys(valid_LS)
    page.password.send_keys(valid_password)
    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=3011e2b2-06d5-47d4-94be-2571e7f6356d&client_id=account_b2c&theme=light#/'


# TC-RT-009 Авторизация по электронной почте с кодом подтверждения.
def test_authorisation_code_email(web_browser):
    page = AuthPage(web_browser)

    page.code.click()
    page.auth_code.send_keys(valid_email)
    page.get_code.click()

    page2 = pytest.driver.get('https://e.mail.ru/inbox/')
    element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span', 'Ваш код')
    )
    page2.element.click()
    element2 = driver.find_element(By.TAG_NAME, 'div > p')
    for i in element2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()

    page = AuthPage(web_browser)
    page.rt_code.send_keys(my_code)

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=3011e2b2-06d5-47d4-94be-2571e7f6356d&client_id=account_b2c&theme=light#/'


# TC-RT-010 Авторизация по номеру телефона с кодом подтверждения.
def test_authorisation_code_phone(web_browser):
    page = AuthPage(web_browser)

    page.code.click()
    page.auth_code.send_keys(valid_phone)
    page.get_code.click()
    page.rt_code.send_keys()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=3011e2b2-06d5-47d4-94be-2571e7f6356d&client_id=account_b2c&theme=light#/'


# TC-RT-011 Восстановление пароля по номеру телефона.
def test_pass_recovery_phone(web_browser):
    page = AuthPage(web_browser)

    page.recovery.click()
    page.phone.send_keys(valid_phone)
    symbols = page.captcha.get_text()
    page.symbol.send_keys(symbols)
    page.contin.click()
    page.rt_code.send_keys()
    new_pass = random
    page.new_pass.send_keys(new_pass)
    page.confirm.send_keys(new_pass)
    page.save.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=3011e2b2-06d5-47d4-94be-2571e7f6356d&client_id=account_b2c&theme=light#/'


# TC-RT-012 Восстановление пароля по адресу электронной почты. Позитивный тест
def test_pass_recovery_email(web_browser):
    page = AuthPage(web_browser)

    page.recovery.click()
    page.email.send_keys(valid_email)
    symbols = page.captcha.get_text()
    page.symbol.send_keys(symbols)
    page.contin.click()

    page2 = pytest.driver.get('https://e.mail.ru/inbox/')
    element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span', 'Ваш код')
    )
    page2.element.click()
    element2 = driver.find_element(By.TAG_NAME, 'div > p')
    for i in element2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()

    page = AuthPage(web_browser)

    page.rt_code.send_keys(my_code)
    new_pass = random
    page.new_pass.send_keys(new_pass)
    page.confirm.send_keys(new_pass)
    page.save.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=3011e2b2-06d5-47d4-94be-2571e7f6356d&client_id=account_b2c&theme=light#/'


# TC-RT-013 Восстановление пароля по адресу электронной почты. Негативный тест
def test_pass_recovery_email_negativ(web_browser):
    page = AuthPage(web_browser)

    page.recovery.click()
    page.email.send_keys(valid_email)
    symbols = page.captcha.get_text()
    page.symbol.send_keys(symbols)
    page.contin.click()

    page2 = pytest.driver.get('https://e.mail.ru/inbox/')
    element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span', 'Ваш код')
    )
    page2.element.click()
    element2 = driver.find_element(By.TAG_NAME, 'div > p')
    for i in element2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()

    page = AuthPage(web_browser)
    page.rt_code.send_keys(my_code)
    new_pass = random
    page.new_pass.send_keys(new_pass)
    page.confirm.send_keys(new_pass)
    page.save.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=3011e2b2-06d5-47d4-94be-2571e7f6356d&client_id=account_b2c&theme=light#/'


# TC-RT-014 Восстановление пароля проверка.
def test_pass_recovery_check(web_browser):
    page = AuthPage(web_browser)

    page.recovery.click()
    page.pa.send_keys(valid_LS)
    symbols = page.captcha.get_text()
    page.symbol.send_keys(symbols)
    page.contin.click()

    page2 = pytest.driver.get('https://e.mail.ru/inbox/')
    element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span', 'Ваш код')
    )
    page2.element.click()
    element2 = driver.find_element(By.TAG_NAME, 'div > p')
    for i in element2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()

    page = AuthPage(web_browser)
    page.rt_code.send_keys(my_code)
    new_pass = random
    page.new_pass.send_keys(new_pass)
    page.confirm.send_keys(new_pass)
    page.save.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=3011e2b2-06d5-47d4-94be-2571e7f6356d&client_id=account_b2c&theme=light#/'


# TC-RT-015 Восстановление пароля по логину.
def test_pass_recovery_login(web_browser):
    page = AuthPage(web_browser)

    page.recovery.click()
    page.login.send_keys(valid_login)
    symbols = page.captcha.get_text()
    page.symbol.send_keys(symbols)
    page.contin.click()

    page2 = pytest.driver.get('https://e.mail.ru/inbox/')
    element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span', 'Ваш код')
    )
    page2.element.click()
    element2 = driver.find_element(By.TAG_NAME, 'div > p')
    for i in element2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()

    page = AuthPage(web_browser)
    page.rt_code.send_keys(my_code)
    new_pass = random
    page.new_pass.send_keys(new_pass)
    page.confirm.send_keys(new_pass)
    page.save.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=3011e2b2-06d5-47d4-94be-2571e7f6356d&client_id=account_b2c&theme=light#/'
