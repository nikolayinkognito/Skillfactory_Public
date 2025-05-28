#   Часть 1: Импорты и fixture

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome('C:/Users/User/Desktop/Тестировщикккк/овая папка/chromedriver-win64 (1)/chromedriver.exe')
    driver.maximize_window()
    driver.get('http://petfriends.skillfactory.ru/login')
    yield driver
    driver.quit()
    
#   Часть 2: Первый тест - проверка отображения питомцев
    
def test_show_all_pets(driver):
    # Явное ожидание загрузки страницы
    WebDriverWait(driver, 10).until(EC.url_contains("/my_pets"))
    assert "PetFriends" in driver.title
    
    # Явные ожидания для полей ввода
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, 'email')))
    driver.find_element(By.ID, 'email').send_keys('vasya@mail.com')
    
    driver.find_element(By.ID, 'pass').send_keys('12345')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    
    # Проверка заголовка
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    
    # Неявное ожидание для карточек
    driver.implicitly_wait(10)
    images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')
    
    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i].text
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
        
        
#   Часть 3: Второй тест - проверка подсчета питомцев
        
def test_count_pets(driver):
    # Явное ожидание загрузки страницы
    WebDriverWait(driver, 10).until(EC.url_contains("/login"))
    
    # Явные ожидания для авторизации
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, 'email')))
    driver.find_element(By.ID, 'email').send_keys('aa@aaa.com')
    driver.find_element(By.ID, 'pass').send_keys('aaa')
    
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    
    # Явное ожидание перехода к списку питомцев
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/div[1]/ul/li[1]/a')))
    driver.find_element(By.XPATH, '/html/body/nav/div[1]/ul/li[1]/a').click()
    
    # Неявное ожидание для таблицы
    driver.implicitly_wait(10)
    
    # Получаем количество питомцев
    pets_number = driver.find_element(By.XPATH, '//div[@class="col-sm-4 left"]').text.split('\n')[1].split(': ')[1]
    print(f"Количество питомцев: {pets_number}")
    
    # Находим таблицу со всеми питомцами
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    
    # Проверяем соответствие количества
    assert int(pets_number) == len(pets_count)
    
    # Проверяем уникальность имен питомцев
    names = set()
    for row in pets_count:
        name = row.find_element(By.XPATH, './/td[2]').text
        assert name not in names
        names.add(name)
    
    # Проверяем уникальность видов питомцев
    kinds = set()
    for row in pets_count:
        kind = row.find_element(By.XPATH, './/td[3]').text
        assert kind not in kinds
        kinds.add(kind)
    
    # Проверяем наличие фотографий
    photos = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr/td[1]/img')
    photo_count = len([photo for photo in photos if photo.get_attribute('src') != ''])
    assert photo_count >= len(pets_count) // 2