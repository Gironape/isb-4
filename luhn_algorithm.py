import logging
import json


def luhn(init: dict) -> bool:
    """
    Проверяет номер на корректность алгоритмом Луна
    args:
        init(dict): входные данные
    return:
        (bool): True, если все сошлось, иначе - False
    """
    res = 0
    try:
        with open(init["found_card"]) as f:
            data = json.load(f)
    except FileNotFoundError:
          logging.error(f"{init['found_card']} not found")
    number = str(data["card_number"])
    number = list(map(int, number))
    if len(number) != 16:
         logging.info("Номер не корректен")
         data["luhn_check"] = "no result"
    else:
        last = number[15]
        number.pop()
        for n in number[0:16:2]:
            i = n * 2
            if i > 9:
                res += i % 10 + i // 10
            else:
                res += i
        res = 10 - res % 10
        if res == last:
            logging.info("Карточка корректна")
            data["luhn_check"] = "true"
        else:
            logging.info("Карточка не корректна")
            data["luhn_check"] = "false"
    logging.info(f"Результат сохранен по пути {init['found_card']}")
    try:
        with open(init["found_card"], 'w') as f:
            json.dump(data, f)
    except FileNotFoundError:
          logging.error(f"{init['found_card']} not found")