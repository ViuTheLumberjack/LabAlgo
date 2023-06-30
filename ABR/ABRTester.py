from time import perf_counter
import pandas as pd
import numpy as np
import pdb

class ABRTester:
    def __init__(self, ABR, type: str):
        self.ABR = ABR
        self.type = type

    def test_insert(self, key: int, item: object) -> float:
        start = perf_counter()
        self.ABR.tree_insert(key, item)
        end = perf_counter()
        return end - start

    def test_search(self, key: int) -> float:
        start = perf_counter()
        self.ABR.search(key)
        end = perf_counter()

        return end - start

    def test_delete(self, key: int) -> float:
        start = perf_counter()
        self.ABR.tree_delete_key(key)
        end = perf_counter()

        return end - start
    
    def test_height(self) -> int:
        return self.ABR.getHeight(self.ABR.root)
    
    def test(self, values: list) -> pd.DataFrame:
        # colonne: n, abr_type, height_before, height_after, insert_time, search_time, delete_time
        # righe: 1 riga per ogni test
        n = len(values)
        # inserimento dei valori nell'albero
        insert_times = []
        for v in values:
            insert_times.append(self.test_insert(v, chr(v)))
        insert_df = pd.DataFrame(insert_times)
        insert_df = insert_df[(insert_df.iloc[:, 0] > insert_df.iloc[:, 0].quantile(0.1)) & (insert_df.iloc[:, 0] < insert_df.iloc[:, 0].quantile(0.9))] 
        height_before = self.test_height()
        # ricerca dei valori nell'albero
        search_times = []
        values2 = np.random.choice(values, int(np.floor(n / 4)))
        for v in values2:
            search_times.append(self.test_search(v))
        search_df = pd.DataFrame(search_times)
        search_df = search_df[(search_df.iloc[:, 0] > search_df.iloc[:, 0].quantile(0.1)) & (search_df.iloc[:, 0] < search_df.iloc[:, 0].quantile(0.9))] 
        # eliminazione dei valori dall'albero
        delete_times = []
        for v in values2:
            delete_times.append(self.test_delete(v))
        delete_df = pd.DataFrame(delete_times)
        delete_df = delete_df[(delete_df.iloc[:, 0] > delete_df.iloc[:, 0].quantile(0.1)) & (delete_df.iloc[:, 0] < delete_df.iloc[:, 0].quantile(0.9))] 
        height_after = self.test_height()
        # riporto l'albero alle condizioni iniziali
        self.ABR.root = None
        self.ABR.length = 0
        # creazione del dataframe
        return pd.DataFrame({
            'n': n,
            'abr_type': self.type,
            'height_before': height_before,
            'height_after': height_after,
            'insert_time': insert_df.mean(),
            'search_time': search_df.mean(),
            'delete_time': delete_df.mean()
        })