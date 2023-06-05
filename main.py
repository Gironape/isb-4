import multiprocessing as mp
import logging
import argparse
import json

from searching import search_number
from luhn_algorithm import luhn


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--init_path', default='file\\init_file.json', help='Путь к json файлу с данными, '
                                                                                  'default = file\\settings.json',
                                                                                                   action='store')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--find', help='Поиск номеров карт с заданным хэшем', action='store_true')
    group.add_argument('-c', '--check', help='Проверяет карту на достоверность', action='store_true')
    group.add_argument('-s', '--statistic', help='Вывод зависимости времени выполненя от кол-ва потоков',
                                                                                    action='store_true')
    args = parser.parse_args()
    init_path = args.init_path
    try:
        with open(init_path) as jf:
            init = json.load(jf)
    except FileNotFoundError:
        logging.error(f"{init_path} not found")
    if args.find:
        logging.info('Поиск номера карточки\n')
        search_number(init, args.find)
    elif args.check:
        logging.info('Проверка корректности карточки...')
        luhn(init)
