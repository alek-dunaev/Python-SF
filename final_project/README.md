Итоговый проект по автоматизации тестирования skillfactory.ru.

Для запуска:
python -m pytest -v --driver Chrome --driver-path C:/project/chromedriver.exe tests/test_auth_page_rostelekom.py**

TC-RT-001 Регистрацию по электронной почте. Позитивный тест.

TC-RT-002 Регистрация по номеру телефона. Позитивный тест.

TC-RT-003 Регистрация по номеру телефона. Негативный тест.

TC-RT-004 Авторизация по логину. Позитивный тест.

TC-RT-005 Авторизация по логину. Негативный тест.

TC-RT-006 Авторизация по электронной почте.

TC-RT-007 Авторизация по номеру телефона.

TC-RT-008 Авторизация по номеру лицевого счёта.

TC-RT-009 Авторизация по электронной почте с кодом подтверждения.

TC-RT-010 Авторизация по номеру телефона с кодом подтверждения.

TC-RT-011 Восстановление пароля по номеру телефона.

TC-RT-012 Восстановление пароля по адресу электронной почты. Позитивный тест

TC-RT-013 Восстановление пароля по адресу электронной почты. Негативный тест

TC-RT-014 Восстановление пароля проверка.

TC-RT-015 Восстановление пароля по логину.

conftest.py contains all the required code to catch failed test cases and make screenshot of the page in case any test case will fail.
pages/base.py contains PageObject pattern implementation for Python.
pages/elements.py contains helper class to define web elements on web pages.
tests/test_auth_page_rostelekom.py contains several tests for Rostelekom (https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=312322e5-94fa-41eb-880e-6e97327a1605&theme&auth_type)
