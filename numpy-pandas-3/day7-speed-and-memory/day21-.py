import pandas as pd
import time
import psutil
import os
import numpy as np

def measure_memory():
    return psutil.Process(os.getpid()).memory_info().rss / (1024 ** 2)  # MB

def time_and_memory(func):
    def wrapper():
        start_mem = measure_memory()
        start_time = time.time()

        df = func()

        end_time = time.time()
        end_mem = measure_memory()

        return {
            'time(s)': round(end_time - start_time, 3),
            'mem used (MB)': round(end_mem - start_mem, 3),
            'rows': len(df)
        }
    return wrapper

path = "C:/Users/Umut/Desktop/ai-learning-path/numpy-pandas-matplot-3-4/raw/test_50mb.csv"
@time_and_memory
def read_standart():
    return pd.read_csv(path)

@time_and_memory
def read_chunksize():
    chunks = pd.read_csv(path, chunksize=500_000)
    return pd.concat(chunks)

@time_and_memory
def read_pyarrow():
    return pd.read_csv(path, engine='pyarrow')

results = {
    'standart': read_standart(),
    'chunksize': read_chunksize(),
    'pyarrow': read_pyarrow()
}

print("Process Completed.")
print(pd.DataFrame(results))
