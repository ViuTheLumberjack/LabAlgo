import ABR_Lista as lista
import ABR_Flag as flag
import ABR_Normale as abr 
from ABRTester import ABRTester 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import gc

sys.setrecursionlimit(100000)

def save_height_before_graph(df: pd.DataFrame, range: tuple):
    # crea un grafico con n sull'asse x e height_before sull'asse y
    plt.plot(df['n'], df['height_before'].where(df['abr_type'] == 'abr'), label='normale')
    plt.plot(df['n'], df['height_before'].where(df['abr_type'] == 'lista'), label='lista')
    plt.plot(df['n'], df['height_before'].where(df['abr_type'] == 'flag'), label='flag')
    plt.xlabel('n')
    plt.ylabel('altezza')
    plt.title('Altezza prima dell\'eliminazione')
    plt.legend()
    plt.savefig(f'out/height_before_graph_{range[1]}.png')
    plt.clf()

def save_height_after_graph(df: pd.DataFrame, range: tuple):
    # crea un grafico con n sull'asse x e height_after sull'asse y
    plt.plot(df['n'], df['height_after'].where(df['abr_type'] == 'abr'), label='normale')
    plt.plot(df['n'], df['height_after'].where(df['abr_type'] == 'lista'), label='lista')
    plt.plot(df['n'], df['height_after'].where(df['abr_type'] == 'flag'), label='flag')
    plt.xlabel('n')
    plt.ylabel('altezza')
    plt.title('Altezza dopo l\'eliminazione')
    plt.legend()
    plt.savefig(f'out/height_after_graph_{range[1]}.png')
    plt.clf()

def save_insert_graph(df: pd.DataFrame, range: tuple):
    # crea un grafico con n sull'asse x e height_after sull'asse y
    plt.plot(df['n'], df['insert_time'].where(df['abr_type'] == 'abr'), label='normale')
    plt.plot(df['n'], df['insert_time'].where(df['abr_type'] == 'lista'), label='lista')
    plt.plot(df['n'], df['insert_time'].where(df['abr_type'] == 'flag'), label='flag')
    plt.xlabel('n')
    plt.ylabel('tempo')
    plt.title('Tempo di inserimento')
    plt.legend()
    plt.savefig(f'out/insert_graph_{range[1]}.png')
    plt.clf()

def save_search_graph(df: pd.DataFrame, range: tuple):
    # crea un grafico con n sull'asse x e height_after sull'asse y
    plt.plot(df['n'], df['search_time'].where(df['abr_type'] == 'abr'), label='normale')
    plt.plot(df['n'], df['search_time'].where(df['abr_type'] == 'lista'), label='lista')
    plt.plot(df['n'], df['search_time'].where(df['abr_type'] == 'flag'), label='flag')
    plt.xlabel('n')
    plt.ylabel('tempo')
    plt.title('Tempo di ricerca')
    plt.legend()
    plt.savefig(f'out/search_graph_{range[1]}.png')
    plt.clf()

def save_delete_graph(df: pd.DataFrame, range: tuple):
    # crea un grafico con n sull'asse x e height_after sull'asse y
    plt.plot(df['n'], df['delete_time'].where(df['abr_type'] == 'abr'), label='normale')
    plt.plot(df['n'], df['delete_time'].where(df['abr_type'] == 'lista'), label='lista')
    plt.plot(df['n'], df['delete_time'].where(df['abr_type'] == 'flag'), label='flag')
    plt.xlabel('n')
    plt.ylabel('tempo')
    plt.title('Tempo di eliminazione')
    plt.legend()
    plt.savefig(f'out/delete_graph_{range[1]}.png') 
    plt.clf()

RANDOM_RANGES = [(0, 10), (0, 50)]
ITERATIONS = (10, 1000)
STEP = 5

for random_range in RANDOM_RANGES:
    ## Test 1 con range (0, 100)
    df_list: list = []

    for i in range(ITERATIONS[0], ITERATIONS[1], STEP):
        df_list.append(ABRTester(lista.ABR(), 'lista').test(i, random_range))
        gc.collect()
    for i in range(ITERATIONS[0], ITERATIONS[1], STEP):
        df_list.append(ABRTester(flag.ABR(), 'flag').test(i, random_range))
        gc.collect()
    for i in range(ITERATIONS[0], ITERATIONS[1], STEP):
        df_list.append(ABRTester(abr.ABR(), 'abr').test(i, random_range))
        gc.collect()

    df = pd.concat(df_list, ignore_index=True)

    save_height_before_graph(df, random_range)
    save_height_after_graph(df, random_range)
    save_insert_graph(df, random_range)
    save_search_graph(df, random_range)
    save_delete_graph(df, random_range)