Итоговый проект по автоматизации тестирования skillfactory.ru.

conftest.py contains all the required code to catch failed test cases and make screenshot of the page in case any test case will fail.

pages/base.py contains PageObject pattern implementation for Python.

pages/elements.py contains helper class to define web elements on web pages.

tests/test_auth_page_rostelekom.py contains several tests for Rostelekom (https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=312322e5-94fa-41eb-880e-6e97327a1605&theme&auth_type)
