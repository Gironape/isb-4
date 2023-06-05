import json
import os
import logging

logger = logging.getLogger()
logger.setLevel('INFO')

SETTINGS = {
    "hash": "78495810cec383f3f82049d03a522f5141583d1d6577235c74084c1d21f7a1df4612c05c0d6b5eb15edd1270ab5069f0",
    "last_digits": "9920",
    "found_card": "file/found_card.json",
    "stat_path": "file/picture_of_time.png",
    "first_digits": "220070"
}

if __name__ == '__main__':
    try:
        with open(os.path.join('file', 'init_file.json'), 'w') as fp:
            json.dump(SETTINGS, fp)
        logging.info("Настройки записаны")
    except OSError as err:
        logging.warning(f'{err} ошибка при записи в файл')