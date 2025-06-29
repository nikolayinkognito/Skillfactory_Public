import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Тест-кейс 1

class TestAuthorization(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://samara.rt.ru/")

    def test_authorization(self):
        # Шаг 1: Нажать на кнопку "Войти"
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
        )
        login_button.click()

        # Ожидаемый результат: Отображается окно с вариантами входа
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'login-options')]"))
        ))

        # Шаг 2: Нажать на кнопку "Войти со своим паролем"
        password_login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти со своим паролем']"))
        )
        password_login_button.click()

        # Ожидаемый результат: Отображаются поля для ввода данных
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Логин']"))
        ))
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Пароль']"))
        ))

        # Шаг 3: Выбрать вкладку "Логин"
        # Предполагаем, что это уже сделано на предыдущем шаге

        # Шаг 4: Ввести логин и пароль и нажать на кнопку "Войти"
        username_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Логин']")
        password_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Пароль']")
        login_button = self.driver.find_element(By.XPATH, "//button[text()='Войти']")

        username_input.send_keys("ваш_логин")  # Замените на реальный логин
        password_input.send_keys("ваш_пароль")  # Замените на реальный пароль
        login_button.click()

        # Ожидаемый результат: Успешный вход
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'logged-in-user')]"))
        ))

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()

# Тест-кейс 2

class TestAuthorization(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://samara.rt.ru/")

    def test_authorization(self):
        # Шаг 1: Нажать на кнопку "Войти"
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
        )
        login_button.click()

        # Ожидаемый результат: Отображается окно с вариантами входа
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'login-options')]"))
        ))

        # Шаг 2: Нажать на кнопку "Войти со своим паролем"
        password_login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти со своим паролем']"))
        )
        password_login_button.click()

        # Ожидаемый результат: Отображаются поля для ввода данных
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Телефон']"))
        ))
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Пароль']"))
        ))

        # Шаг 3: Выбрать вкладку "Телефон"
        phone_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Телефон']"))
        )
        phone_tab.click()

        # Ожидаемый результат: Отображаются поля для ввода телефона и пароля
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Телефон']"))
        ))
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Пароль']"))
        ))

        # Шаг 4: Ввести телефон и пароль и нажать на кнопку "Войти"
        phone_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Телефон']")
        password_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Пароль']")
        login_button = self.driver.find_element(By.XPATH, "//button[text()='Войти']")

        phone_input.send_keys("ваш_телефон")  # Замените на реальный номер телефона
        password_input.send_keys("ваш_пароль")  # Замените на реальный пароль
        login_button.click()

        # Ожидаемый результат: Успешный вход
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'logged-in-user')]"))
        ))

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()

# Тест кейс 3

class TestAuthorization(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://samara.rt.ru/")

    def test_authorization(self):
        # Шаг 1: Нажать на кнопку "Войти"
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
        )
        login_button.click()

        # Ожидаемый результат: Отображается окно с вариантами входа
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'login-options')]"))
        ))

        # Шаг 2: Нажать на кнопку "Войти со своим паролем"
        password_login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти со своим паролем']"))
        )
        password_login_button.click()

        # Ожидаемый результат: Отображаются поля для ввода данных
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Почта']"))
        ))
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Пароль']"))
        ))

        # Шаг 3: Выбрать вкладку "Почта"
        email_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Почта']"))
        )
        email_tab.click()

        # Ожидаемый результат: Отображаются поля для ввода почты и пароля
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Почта']"))
        ))
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Пароль']"))
        ))

        # Шаг 4: Ввести почту и пароль и нажать на кнопку "Войти"
        email_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Почта']")
        password_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Пароль']")
        login_button = self.driver.find_element(By.XPATH, "//button[text()='Войти']")

        email_input.send_keys("ваш_email")  # Замените на реальный email
        password_input.send_keys("ваш_пароль")  # Замените на реальный пароль
        login_button.click()

        # Ожидаемый результат: Успешный вход
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'logged-in-user')]"))
        ))

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()

# Тест кейс 4

class TestAuthorization(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://samara.rt.ru/")

    def test_authorization(self):
        # Шаг 1: Нажать на кнопку "Войти"
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
        )
        login_button.click()

        # Ожидаемый результат: Отображается окно с вариантами входа
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'login-options')]"))
        ))

        # Шаг 2: Ввести СМС для входа и нажать кнопку "Получить код"
        phone_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Телефон']")
        get_code_button = self.driver.find_element(By.XPATH, "//button[text()='Получить код']")

        phone_input.send_keys("ваш_телефон")  # Замените на реальный номер телефона
        get_code_button.click()

        # Ожидаемый результат: Код для входа получен
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Код']"))
        ))

        # Шаг 3: Ввести полученный код в поле для ввода кода
        code_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Код']")
        login_button = self.driver.find_element(By.XPATH, "//button[text()='Войти']")

        code_input.send_keys("ваш_код")  # Замените на реальный код
        login_button.click()

        # Ожидаемый результат: Успешный вход
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'logged-in-user')]"))
        ))

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()

# Тест кейс 5

class TestAuthorization(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://samara.rt.ru/")

    def test_authorization(self):
        # Шаг 1: Нажать на кнопку "Войти"
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
        )
        login_button.click()

        # Ожидаемый результат: Отображается окно с вариантами входа
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'login-options')]"))
        ))

        # Шаг 2: Ввести E-mail для входа и нажать кнопку "Получить код"
        email_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Email']")
        get_code_button = self.driver.find_element(By.XPATH, "//button[text()='Получить код']")

        email_input.send_keys("ваш_email")  # Замените на реальный email
        get_code_button.click()

        # Ожидаемый результат: Код для входа получен
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Код']"))
        ))

        # Шаг 3: Ввести полученный код в поле для ввода кода
        code_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Код']")
        login_button = self.driver.find_element(By.XPATH, "//button[text()='Войти']")

        code_input.send_keys("ваш_код")  # Замените на реальный код
        login_button.click()

        # Ожидаемый результат: Успешный вход
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'logged-in-user')]"))
        ))

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()

# Тест кейс 6


class TestAuthorization(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://samara.rt.ru/")

    def test_authorization(self):
        # Шаг 1: Нажать на кнопку "Войти"
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
        )
        login_button.click()

        # Ожидаемый результат: Отображается окно с вариантами входа
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'login-options')]"))
        ))

        # Шаг 2: Нажать на кнопку "Войти со своим паролем"
        password_login_button = self.driver.find_element(By.XPATH, "//button[text()='Войти со своим паролем']")
        password_login_button.click()

        # Ожидаемый результат: Отображаются поля для ввода данных
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Логин']"))
        ))

        # Шаг 3: Выбрать вкладку "Лицевой счёт"
        account_tab = self.driver.find_element(By.XPATH, "//a[text()='Лицевой счёт']")
        account_tab.click()

        # Ожидаемый результат: Отображаются поля для ввода логина и пароля
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Лицевой счёт']"))
        ))

        # Шаг 4: Ввести лицевой счёт и пароль и нажать на кнопку "Войти"
        account_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Лицевой счёт']")
        password_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Пароль']")
        login_button = self.driver.find_element(By.XPATH, "//button[text()='Войти']")

        account_input.send_keys("ваш_лицевой_счёт")  # Замените на реальный лицевой счёт
        password_input.send_keys("ваш_пароль")  # Замените на реальный пароль
        login_button.click()

        # Ожидаемый результат: Успешный вход
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'logged-in-user')]"))
        ))

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()

# Тест кейс 7

class TestPasswordRecovery(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://samara.rt.ru/")

    def test_password_recovery(self):
        # Шаг 1: Нажать на кнопку "Войти"
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
        )
        login_button.click()

        # Ожидаемый результат: Отображается окно с вариантами входа
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'login-options')]"))
        ))

        # Шаг 2: Нажать на кнопку "Войти со своим паролем"
        password_login_button = self.driver.find_element(By.XPATH, "//button[text()='Войти со своим паролем']")
        password_login_button.click()

        # Ожидаемый результат: Отображаются поля для ввода данных
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Логин']"))
        ))

        # Шаг 3: Нажать на кнопку "Забыли пароль" и выбрать вкладку "логин"
        forgot_password_button = self.driver.find_element(By.XPATH, "//a[text()='Забыли пароль?']")
        forgot_password_button.click()
        login_tab = self.driver.find_element(By.XPATH, "//a[text()='Логин']")
        login_tab.click()

        # Ожидаемый результат: Отображаются поля для ввода логина и капчи
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Логин']"))
        ))

        # Шаг 4: Ввести свой логин и капчу и нажать на кнопку "продолжить"
        login_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Логин']")
        captcha_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Капча']")
        continue_button = self.driver.find_element(By.XPATH, "//button[text()='Продолжить']")

        login_input.send_keys("ваш_логин")  # Замените на реальный логин
        captcha_input.send_keys("ваша_капча")  # Замените на реальную капчу
        continue_button.click()

        # Ожидаемый результат: Отображается окно с выбором метода восстановления пароля
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'recovery-methods')]"))
        ))

        # Шаг 5: Выбрать метод восстановления по номеру телефона и нажать на кнопку "продолжить"
        phone_method = self.driver.find_element(By.XPATH, "//labelcontains(text(), 'Номер телефона')")
        phone_method.click()
        continue_button = self.driver.find_element(By.XPATH, "//buttontext()='Продолжить'")
        continue_button.click()

        # Ожидаемый результат: Открывается окно с возможностью ввода кода подтверждения
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input@placeholder='Код подтверждения'"))
        ))

        # Шаг 6: Ввести код подтверждения
        confirmation_code = self.driver.find_element(By.XPATH, "//input@placeholder='Код подтверждения'")
        confirmation_code.send_keys("ваш_код")  # Замените на реальный код

        # Ожидаемый результат: Открывается окно с вводом нового пароля
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input@placeholder='Новый пароль'"))
        ))

        # Шаг 7: Ввести новый пароль
        new_password = self.driver.find_element(By.XPATH, "//input@placeholder='Новый пароль'")
        confirm_password = self.driver.find_element(By.XPATH, "//input@placeholder='Подтверждение пароля'")
        submit_button = self.driver.find_element(By.XPATH, "//buttontext()='Сохранить'")

        new_password.send_keys("ваш_новый_пароль")  # Замените на новый пароль
        confirm_password.send_keys("ваш_новый_пароль")  # Повторите новый пароль
        submit_button.click()

        # Ожидаемый результат: Пароль восстановлен
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//divcontains(text(), 'Пароль успешно восстановлен')"))
        ))

        def tearDown(self):
            self.driver.quit()

    if __name__ == "__main__":
        unittest.main()

# Тест кейс 8

class TestPasswordRecovery(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://samara.rt.ru/")

    def test_password_recovery(self):
        # Шаг 1: Нажать на кнопку "Войти"
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
        )
        login_button.click()

        # Ожидаемый результат: Отображается окно с вариантами входа
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'login-options')]"))
        ))

        # Шаг 2: Нажать на кнопку "Войти со своим паролем"
        password_login_button = self.driver.find_element(By.XPATH, "//button[text()='Войти со своим паролем']")
        password_login_button.click()

        # Ожидаемый результат: Отображаются поля для ввода данных
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Логин']"))
        ))

        # Шаг 3: Нажать на кнопку "Забыли пароль" и выбрать вкладку "логин"
        forgot_password_button = self.driver.find_element(By.XPATH, "//a[text()='Забыли пароль?']")
        forgot_password_button.click()
        login_tab = self.driver.find_element(By.XPATH, "//a[text()='Логин']")
        login_tab.click()

        # Ожидаемый результат: Отображаются поля для ввода логина и капчи
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Логин']"))
        ))

        # Шаг 4: Ввести свой логин и капчу и нажать на кнопку "продолжить"
        login_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Логин']")
        captcha_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Капча']")
        continue_button = self.driver.find_element(By.XPATH, "//button[text()='Продолжить']")

        login_input.send_keys("ваш_логин")  # Замените на реальный логин
        captcha_input.send_keys("ваша_капча")  # Замените на реальную капчу
        continue_button.click()

        # Ожидаемый результат: Отображается окно с выбором метода восстановления пароля
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'recovery-methods')]"))
        ))

# Шаг 5: Выбрать метод восстановления по электронной почте и нажать на кнопку "продолжить"
email_method = self.driver.find_element(By.XPATH, "//label[contains(text(), 'Электронная почта')]")
email_method.click()
continue_button = self.driver.find_element(By.XPATH, "//button[text()='Продолжить']")
continue_button.click()

# Ожидаемый результат: Открывается окно с возможностью ввода кода подтверждения
self.assertTrue(WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Код подтверждения']"))
))

# Шаг 6: Ввести код подтверждения
confirmation_code = self.driver.find_element(By.XPATH, "//input[@placeholder='Код подтверждения']")
confirmation_code.send_keys("ваш_код")  # Замените на реальный код

# Ожидаемый результат: Открывается окно с вводом нового пароля
self.assertTrue(WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Новый пароль']"))
))

# Шаг 7: Ввести новый пароль
new_password = self.driver.find_element(By.XPATH, "//input[@placeholder='Новый пароль']")
confirm_password = self.driver.find_element(By.XPATH, "//input[@placeholder='Подтверждение пароля']")
submit_button = self.driver.find_element(By.XPATH, "//button[text()='Сохранить']")

new_password.send_keys("ваш_новый_пароль")  # Замените на новый пароль
confirm_password.send_keys("ваш_новый_пароль")  # Повторите новый пароль
submit_button.click()

# Ожидаемый результат: Пароль восстановлен
self.assertTrue(WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Пароль успешно восстановлен')]"))
))

#Тест кейс 9

class TestPasswordRecovery(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://samara.rt.ru/")

    def test_password_recovery(self):
        # Шаг 1: Нажать на кнопку "Войти"
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
        )
        login_button.click()

        # Ожидаемый результат: Отображается окно с вариантами входа
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'login-options')]"))
        ))

        # Шаг 2: Нажать на кнопку "Войти со своим паролем"
        password_login_button = self.driver.find_element(By.XPATH, "//button[text()='Войти со своим паролем']")
        password_login_button.click()

        # Ожидаемый результат: Отображаются поля для ввода данных
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Логин']"))
        ))

# Шаг 3: Нажать на кнопку "Забыли пароль" и выбрать вкладку "Телефон"
forgot_password_button = self.driver.find_element(By.XPATH, "//a[text()='Забыли пароль?']")
forgot_password_button.click()
phone_tab = self.driver.find_element(By.XPATH, "//a[text()='Телефон']")
phone_tab.click()

# Ожидаемый результат: Отображаются поля для ввода телефона и капчи
self.assertTrue(WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Телефон']"))
))

# Шаг 4: Ввести свой телефон и капчу и нажать на кнопку "продолжить"
phone_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Телефон']")
captcha_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Капча']")
continue_button = self.driver.find_element(By.XPATH, "//button[text()='Продолжить']")

phone_input.send_keys("ваш_номер_телефона")  # Замените на реальный номер
captcha_input.send_keys("ваша_капча")  # Замените на реальную капчу
continue_button.click()

# Ожидаемый результат: Открывается окно с возможностью ввода кода подтверждения
self.assertTrue(WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Код подтверждения']"))
))

# Шаг 5: Ввести код подтверждения
confirmation_code = self.driver.find_element(By.XPATH, "//input@placeholder='Код подтверждения'")
confirmation_code.send_keys("ваш_код")  # Замените на реальный код

# Ожидаемый результат: Открывается окно с вводом нового пароля
self.assertTrue(WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input@placeholder='Новый пароль'"))
))

# Шаг 6: Ввести новый пароль
new_password = self.driver.find_element(By.XPATH, "//input@placeholder='Новый пароль'")
confirm_password = self.driver.find_element(By.XPATH, "//input@placeholder='Подтверждение пароля'")
submit_button = self.driver.find_element(By.XPATH, "//button[text()='Сохранить']")

new_password.send_keys("ваш_новый_пароль")  # Замените на новый пароль
confirm_password.send_keys("ваш_новый_пароль")  # Повторите новый пароль
submit_button.click()

# Ожидаемый результат: Пароль восстановлен
self.assertTrue(WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Пароль успешно восстановлен')]"))
))

# Тест кейс 10

class TestAuthorization(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://samara.rt.ru/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_authorization(self):
        # Шаг 1: Нажать на кнопку "Войти"
        self.driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Варианты входа')]"))))

        # Шаг 2: Нажать на кнопку "Войти со своим паролем"
        self.driver.find_element(By.XPATH, "//button[text()='Войти со своим паролем']").click()
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Ваш логин']"))))

        # Шаг 3: Нажать на кнопку "Забыли пароль" и выбрать вкладку "Почта"
        self.driver.find_element(By.XPATH, "//a[text()='Забыли пароль?']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Почта']").click()
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Электронная почта']"))))

        # Шаг 4: Ввести email и капчу и нажать на кнопку "продолжить"
        email_input = self.driver.find_element(By.XPATH, "//input@placeholder='Электронная почта'")
        captcha_input = self.driver.find_element(By.XPATH, "//input@placeholder='Капча'")
        continue_button = self.driver.find_element(By.XPATH, "//buttontext()='Продолжить'")

        email_input.send_keys("ваш_email@example.com")  # Замените на реальный email
        captcha_input.send_keys("ваша_капча")  # Замените на реальную капчу
        continue_button.click()

        # Ожидаемый результат: Открывается окно с возможностью ввода кода подтверждения
        self.assertTrue(self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input@placeholder='Код подтверждения'"))
        ))

        # Шаг 5: Ввести код подтверждения
        confirmation_code = self.driver.find_element(By.XPATH, "//input@placeholder='Код подтверждения'")
        confirmation_code.send_keys("ваш_код")  # Замените на реальный код

        # Ожидаемый результат: Открывается окно с вводом нового пароля
        self.assertTrue(self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input@placeholder='Новый пароль'"))
        ))

        # Шаг 6: Ввести новый пароль
        new_password = self.driver.find_element(By.XPATH, "//input@placeholder='Новый пароль'")
        confirm_password = self.driver.find_element(By.XPATH, "//input@placeholder='Подтверждение пароля'")
        submit_button = self.driver.find_element(By.XPATH, "//buttontext()='Сохранить'")

        new_password.send_keys("ваш_новый_пароль")  # Замените на новый пароль
        confirm_password.send_keys("ваш_новый_пароль")  # Повторите новый пароль
        submit_button.click()

        # Ожидаемый результат: Пароль восстановлен
        self.assertTrue(self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//divcontains(text(), 'Пароль успешно восстановлен')"))
        ))

        def tearDown(self):
            self.driver.quit()

        if __name__ == "__main__":
            unittest.main()

# Тест кейс 11

class TestAuthorization(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://samara.rt.ru/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_authorization(self):
        # Шаг 1: Нажать на кнопку "Войти"
        self.driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Варианты входа')]"))))

        # Шаг 2: Нажать на кнопку "Войти со своим паролем"
        self.driver.find_element(By.XPATH, "//button[text()='Войти со своим паролем']").click()
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Ваш логин']"))))

        # Шаг 3: Нажать на кнопку "Забыли пароль" и выбрать вкладку "Лицевой счёт"
        self.driver.find_element(By.XPATH, "//a[text()='Забыли пароль?']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Лицевой счёт']").click()
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Лицевой счёт']"))))

        # Шаг 4: Ввести лицевой счёт и капчу, затем нажать на кнопку "продолжить"
        account_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Лицевой счёт']")
        captcha_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Капча']")
        continue_button = self.driver.find_element(By.XPATH, "//button[text()='Продолжить']")

        account_input.send_keys("ваш_лицевой_счёт")  # Замените на реальный лицевой счёт
        captcha_input.send_keys("ваша_капча")  # Замените на реальную капчу
        continue_button.click()

        # Ожидаемый результат: Открывается окно с возможностью ввода кода подтверждения
        self.assertTrue(self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Код подтверждения']"))
        ))

        # Шаг 5: Ввести код подтверждения
        confirmation_code = self.driver.find_element(By.XPATH, "//input[@placeholder='Код подтверждения']")
        confirmation_code.send_keys("ваш_код")  # Замените на реальный код

        # Ожидаемый результат: Открывается окно с вводом нового пароля
        self.assertTrue(self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Новый пароль']"))
        ))

        # Шаг 6: Ввести новый пароль
        new_password = self.driver.find_element(By.XPATH, "//input@placeholder='Новый пароль'")
        confirm_password = self.driver.find_element(By.XPATH, "//input@placeholder='Подтверждение пароля'")
        submit_button = self.driver.find_element(By.XPATH, "//buttontext()='Сохранить'")

        new_password.send_keys("ваш_новый_пароль")  # Замените на новый пароль
        confirm_password.send_keys("ваш_новый_пароль")  # Повторите новый пароль
        submit_button.click()

        # Ожидаемый результат: Пароль восстановлен
        self.assertTrue(self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Пароль успешно восстановлен')]"))
        ))

# Тест кейс 12

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://samara.rt.ru/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_registration(self):
        # Шаг 1: Нажать на кнопку "Войти"
        self.driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Варианты входа')]"))))

        # Шаг 2: Нажать на кнопку "Войти со своим паролем"
        self.driver.find_element(By.XPATH, "//button[text()='Войти со своим паролем']").click()
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Ваш логин']"))))

        # Шаг 3: Нажать на кнопку "Зарегистрироваться"
        self.driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Электронная почта']"))))

        # Шаг 4: Ввести личную информацию, электронную почту и пароль
        email_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Электронная почта']")
        password_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Пароль']")
        register_button = self.driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")

        email_input.send_keys("ваш_email@example.com")  # Замените на реальный email
        password_input.send_keys("ваш_пароль")  # Замените на реальный пароль
        register_button.click()

        # Ожидаемый результат: Открывается окно с возможностью ввода кода подтверждения
        self.assertTrue(self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Код подтверждения']"))
        ))

        # Шаг 5: Ввести код подтверждения
        confirmation_code = self.driver.find_element(By.XPATH, "//input[@placeholder='Код подтверждения']")
        confirmation_button = self.driver.find_element(By.XPATH, "//button[text()='Подтвердить']")

        confirmation_code.send_keys("ваш_код_подтверждения")  # Замените на реальный код
        confirmation_button.click()

        # Ожидаемый результат: Пользователь зарегистрирован
        self.assertTrue(self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Регистрация успешно завершена')]"))
        ))

# Тест кейс 13

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://samara.rt.ru/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_registration(self):
        # Шаг 1: Нажать на кнопку "Войти"
        self.driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Варианты входа')]"))))

        # Шаг 2: Нажать на кнопку "Войти со своим паролем"
        self.driver.find_element(By.XPATH, "//button[text()='Войти со своим паролем']").click()
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Ваш логин']"))))

        # Шаг 3: Нажать на кнопку "Зарегистрироваться"
        self.driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Номер телефона']"))))

        # Шаг 4: Ввести личную информацию, номер телефона и пароль
        phone_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Номер телефона']")
        password_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Пароль']")
        register_button = self.driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")

        phone_input.send_keys("ваш_номер_телефона")  # Замените на реальный номер телефона
        password_input.send_keys("ваш_пароль")  # Замените на реальный пароль
        register_button.click()

        # Ожидаемый результат: Открывается окно с возможностью ввода кода подтверждения
        self.assertTrue(self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Код подтверждения']"))
        ))

        # Шаг 5: Ввести код подтверждения
        confirmation_code = self.driver.find_element(By.XPATH, "//input[@placeholder='Код подтверждения']")
        confirmation_button = self.driver.find_element(By.XPATH, "//button[text()='Подтвердить']")

        confirmation_code.send_keys("ваш_код_подтверждения")  # Замените на реальный код
        confirmation_button.click()

        # Ожидаемый результат: Пользователь зарегистрирован
        self.assertTrue(self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Регистрация успешно завершена')]"))
        ))

# Тест кейс 14

class TestCookieAcceptance(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://samara.rt.ru/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_cookie_acceptance(self):
        # Шаг 1: Нажать на кнопку "Войти"
        self.driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        self.assertTrue(
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Варианты входа')]"))))

        # Ожидаемый результат: Открывается окно с предложением принять файлы cookie
        cookie_message = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//p[contains(text(), 'Файлы cookie используются для улучшения вашего опыта')]")))
        self.assertIsNotNone(cookie_message)

        # Шаг 2: Нажать на кнопку "принять файлы Cookie"
        cookie_accept_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Принять')]")
        cookie_accept_button.click()

        # Ожидаемый результат: Файлы Cookie приняты
        self.assertFalse(self.wait.until(EC.staleness_of(cookie_message)))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

# Тест кейс 15


class TestCookieRejection(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://samara.rt.ru/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_cookie_rejection(self):
        # Шаг 1: Нажать на кнопку "Войти"
        self.driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        self.assertTrue(
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Варианты входа')]"))))

        # Ожидаемый результат: Открывается окно с предложением принять файлы cookie
        cookie_message = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//p[contains(text(), 'Файлы cookie используются для улучшения вашего опыта')]")))
        self.assertIsNotNone(cookie_message)

        # Шаг 2: Нажать на кнопку "отклонить файлы Cookie"
        cookie_reject_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Отклонить')]")
        cookie_reject_button.click()

        # Ожидаемый результат: Файлы Cookie отклонены
        self.assertFalse(self.wait.until(EC.staleness_of(cookie_message)))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
