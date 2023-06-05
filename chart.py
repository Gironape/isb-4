import matplotlib.pyplot as plt
from searching import search_number
import time


def visualize(init: dict) -> None:
    """
    Создание гистограммы статистики для 4 ядер.
    :param init: Входные данные.
    """
    cores = []
    enumerate_time = []
    for i in range(4):
        t1 = time.perf_counter()
        search_number(init, i+1)
        t2 = time.perf_counter()
        cores.append(i+1)
        enumerate_time.append(t2-t1)
    plt.figure(figsize=(18, 9))
    plt.xlabel('Processes')
    plt.ylabel('Time')
    plt.title('Statistics')
    plt.bar(cores, enumerate_time, color='red', width=0.5)
    plt.savefig(init['stat_path'])