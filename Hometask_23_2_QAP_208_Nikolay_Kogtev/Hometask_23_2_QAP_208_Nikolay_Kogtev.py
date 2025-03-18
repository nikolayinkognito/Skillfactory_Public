import requests
from bs4 import BeautifulSoup
import pandas as pd # библиотека для Excel файлов

def page_counter():
    page_num = 1
    sofa_data = []  # Создаем список для хранения всех данных
    check_sofa_name = set()  # Используем set для хранения уникальных названий

    while True:
        url = f'https://batamebel.ru/product/krovati/?display=price&PAGEN_1={page_num}'
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, 'lxml')

        entries = soup.find_all('div', class_='catalog-table__wrapper grid-list__item grid-list-border-outer')

        if not entries:  # Проверяем, есть ли записи на странице
            break  # Если нет, заканчиваем цикл

        for entry in entries:
            # Находим название кровати
            div_sofa_name = entry.find('div', class_='catalog-table__info flex-1 flexbox flexbox--direction-row1')
            sofa_name = div_sofa_name.find('span').text

            # Проверяем, встречалось ли такое название раньше
            if sofa_name in check_sofa_name:
                return sofa_data  # Возвращаем собранные данные, если нашли дубликат

            check_sofa_name.add(sofa_name)  # Добавляем название в набор

            # Ищем все размеры кровати
            div_sofa_sizes = entry.find('div', class_='line-block line-block--align-normal flexbox--wrap js-offers-prop')
            sizes = []
            for size_block in div_sofa_sizes.find_all('div', class_='properties__value color_333 font_14 font_short js-prop-value'):
                size = size_block.text.strip()
                sizes.append(size)

            # Ищем цену
            div_sofa_cost = entry.find('div', class_='price__new')
            sofa_cost = div_sofa_cost.find('span').text.strip()

            # Добавляем данные в список
            sofa_data.append({
                'Название': sofa_name,
                'Длина, мм': sizes[0],
                'Ширина, мм': sizes[1],
                'Высота, мм': sizes[2],
                'Цена': sofa_cost
            })

            # Выводим результаты
            print(f"Название: {sofa_name}")
            print(f"Длина, мм: {sizes[0]}")
            print(f"Ширина, мм: {sizes[1]}")
            print(f"Высота, мм: {sizes[2]}")
            print(f"Цена: {sofa_cost}")
            print("-" * 40)

        page_num += 1 # Переходим на следующую страницу

    return sofa_data  # Возвращаем собранные данные

# Запускаем функцию
sofa_data = page_counter()

# Создаем DataFrame из собранных данных
df = pd.DataFrame(sofa_data)

# Сохраняем в Excel
df.to_excel('sofa_data.xlsx', index=False)

print("Данные успешно сохранены в файл sofa_data.xlsx")
