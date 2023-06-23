import ABR_Lista as lista
import ABR_Flag as flag
import ABR_Normale as abr 
from ABRTester import ABRTester 

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(100000)

def save_graph(df: pd.DataFrame, title: str, x: str, y: str, x_title: str, y_title: str, filename: str):
    # crea un grafico
    plt.figure(figsize=(15, 5))
    plt.plot(df[x].where(df['abr_type'] == 'abr'), df[y].where(df['abr_type'] == 'abr'), label='normale')
    plt.plot(df[x], df[y].where(df['abr_type'] == 'lista'), label='lista')
    plt.plot(df[x], df[y].where(df['abr_type'] == 'flag'), label='flag')
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.title(title)
    plt.legend()
    plt.savefig(f'{filename}_linear.png')
    plt.yscale('log')
    plt.savefig(f'{filename}_log.png')
    plt.clf()

RANDOM_RANGES = [(0, 100), (0, 500)]
DATA_MEAN = 100
ITERATIONS = (10, 10000)
STEP = 100

for random_range in RANDOM_RANGES:
    df_list: list = []
    for d in range(DATA_MEAN):
        df_app: list = []
        value_list: list = []

        for i in range(ITERATIONS[0], ITERATIONS[1], STEP):
            value_list.append(np.random.randint(random_range[0], random_range[1], i))
        for i in range(ITERATIONS[0], ITERATIONS[1], STEP):
            df_app.append(ABRTester(lista.ABR(), 'lista').test(value_list[(i - ITERATIONS[0]) // STEP]))
        for i in range(ITERATIONS[0], ITERATIONS[1], STEP):
            df_app.append(ABRTester(flag.ABR(), 'flag').test(value_list[(i - ITERATIONS[0]) // STEP]))
        for i in range(ITERATIONS[0], ITERATIONS[1], STEP):
            df_app.append(ABRTester(abr.ABR(), 'abr').test(value_list[(i - ITERATIONS[0]) // STEP]))

        print(f'{d} - {random_range[1]}')
        df_list.append(pd.concat(df_app, ignore_index=True))

    df_concat = pd.concat(df_list)
    by_row_index = df_concat.groupby([df_concat.index, 'n', 'abr_type'])
    df = by_row_index.mean(numeric_only=True).reset_index()

    save_graph(df, 'Altezza prima dell\'eliminazione', 'n', 'height_before', 'n', 'altezza', f'out/height_before_graph_{random_range[1]}')
    save_graph(df, 'Altezza dopo l\'eliminazione', 'n', 'height_after', 'n', 'altezza', f'out/height_after_graph_{random_range[1]}')
    save_graph(df, 'Tempo di inserimento', 'n', 'insert_time', 'n', 'altezza', f'out/insert_graph_{random_range[1]}')
    save_graph(df, 'Tempo di ricerca', 'n', 'search_time', 'n', 'altezza', f'out/search_graph_{random_range[1]}')
    save_graph(df, 'Tempo di eliminazione', 'n', 'delete_time', 'n', 'altezza', f'out/delete_graph_{random_range[1]}')
    df.to_csv(f'out/df_{random_range[1]}.csv', index=False)
    print(f'Finito {random_range}')