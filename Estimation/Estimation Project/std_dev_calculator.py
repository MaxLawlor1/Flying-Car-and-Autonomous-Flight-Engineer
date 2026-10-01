import numpy as np
import pandas as pd

graph1 = pd.read_csv('./FCND-Estimation-CPP/config/log/Graph1.txt', header=0)
graph2 = pd.read_csv('./FCND-Estimation-CPP/config/log/Graph2.txt', header=0)

if graph1.shape[0] == 2:
    print(f"{'='*10}GPS{'='*10}\n{graph1.describe()}")
    print(f"{'='*10}Accelerometer{'='*10}\n{graph2.describe()}")
else:
    print(f"{'='*10}XY Errors{'='*10}\n{graph1.describe()}")
    print(f"{'='*10}Z Errors{'='*10}\n{graph2.describe()}")
