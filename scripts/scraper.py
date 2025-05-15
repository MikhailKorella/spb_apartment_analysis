import os
import cianparser
import pandas as pd

def parse_cian_spb_min_records(min_records=150, deal_type='sale', rooms=(1, 2), save_dir='../data'):
    '''
    Функция для парсинга объявлений с Cian.ru
    '''
    # Инициализация парсера с нужным городом
    parser = cianparser.CianParser(location="Санкт-Петербург")
    all_data = []
    start_page = 1
    end_page = start_page
    
    # Цикл сбора данных, пока не достигнем нужного количества записей
    while len(all_data) < min_records:
        print(f"Парсим страницу {end_page}...")
        data = parser.get_flats(
            deal_type=deal_type,
            rooms=rooms,
            with_saving_csv=False,
            additional_settings={"start_page": end_page, "end_page": end_page}
        )
        if not data:
            print("Данных больше нет или возникла ошибка.")
            break
        all_data.extend(data)
        end_page += 1

    all_data = all_data[:min_records]

    # Сохранение в csv
    if all_data:
        df = pd.DataFrame(all_data)
        filename = 'cian_spb_data.csv'
        filepath = os.path.join(save_dir, filename)
        df.to_csv(filepath, index=False, encoding='utf-8-sig')
        print(f"Собрано {len(all_data)} записей. Данные сохранены в файл {filepath}")
    else:
        print("Не удалось получить данные.")

if __name__ == "__main__":
    parse_cian_spb_min_records(min_records=150, deal_type='sale', rooms=(1, 2), save_dir='../data')