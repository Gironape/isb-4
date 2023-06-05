import hashlib
import multiprocessing as mp
from tqdm import tqdm
from typing import Union
import logging
import json


def search_number(init: dict, core_number: int = mp.cpu_count()):
    """
 Подбор номера карты c помощью хэша.
 :param  init: входные данные
 :param core_number: Количество ядер.
    """
    args = []
    ok = 0
    for i in range(1000000):
        args.append((init['hash'], f"{init['first_digits']}{i:06d}{init['last_digits']}"))
    with mp.Pool(processes=core_number) as p:
        for result in p.starmap(find_number, tqdm(args, desc="Процесс нахождения номера карты: ", ncols=120)):
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


def find_number(hash_card: str, bin_card: str) -> Union[str, bool]:
    """
 Проверка соответствия номера с хэшем.
 :param hash_card: Хэш карты.
 :param bin_card: Номер карты.
    """
    if hash_card == hashlib.sha3_384(bin_card.encode()).hexdigest():
        return bin_card
    return False