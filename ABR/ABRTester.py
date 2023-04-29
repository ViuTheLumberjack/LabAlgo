from time import perf_counter
import pandas as pd
import numpy as np

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
    
    def test(self, n: int, range: tuple) -> pd.DataFrame:
        # colonne: n, abr_type, height_before, height_after, insert_time, search_time, delete_time
        # righe: 1 riga per ogni test
        values = np.random.randint(range[0], range[1], n)
        # inserimento dei valori nell'albero
        insert_times = []
        for v in values:
            insert_times.append(self.test_insert(v, chr(v)))
        insert_df = pd.DataFrame(insert_times)
        height_before = self.test_height()
        # ricerca dei valori nell'albero
        search_times = []
        values2 = np.random.choice(values, int(np.floor(n / 4)))
        for v in values2:
            search_times.append(self.test_search(v))
        search_df = pd.DataFrame(search_times)
        # eliminazione dei valori dall'albero
        delete_times = []
        for v in values2:
            delete_times.append(self.test_delete(v))
        delete_df = pd.DataFrame(delete_times)
        height_after = self.test_height()
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