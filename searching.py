import hashlib
import json
import logging
import multiprocessing as mp
from functools import partial
from time import time
from tqdm import tqdm
from matplotlib import pyplot as plt


def checking_hash(bin: int, init_file: dict, number: int) -> int:
    """
    Сравнивает хэш полученной карты с уже существующим
    args:
        bin(int): первые 6 цифр
        init(dict): входные данные
        number(int): сгенерированные цифры карты
    return:
        (int): номер, если хэш совпал, иначе False
    """
    return int(f'{bin}{number:06d}{init_file["last_digits"]}') if hashlib.sha3_384(f'{bin}{number:06d}{init_file["last_digits"]}'.encode()).hexdigest() == f'{init_file["hash"]}' else False


def find_number(init: dict, processes: int):
    """
    Ищет карту с таким же хэшем
    args:
        init(dict): входные данные
        processes(int): количесто процессов
    """
    ok = 0
    with mp.Pool(processes) as p:
        for bin in init['first_digits']:
            logging.info(f'Подбор хэша для карт {bin}XXXXXX{init["last_digits"]}')
            for result in p.map(partial(checking_hash, int(bin), init), tqdm(range(1000000), colour='#D30000') ):
                    if result:
                        p.terminate()
                        ok = 1
                        logging.info(f'Найденная карта лежит по пути {init["found_card"]}')
                        data = {}
                        data["card_number"] = f"{result}"
                        data["luhn_check"] = "no result"
                        try:
                            with open(init["found_card"], 'w') as f:
                                    json.dump(data, f)
                        except FileNotFoundError:
                            logging.error(f"{init['found_card']} not found")
                        break
            if ok == 1:
                 break
    if ok == 0:
        logging.info('Карта не найдена')