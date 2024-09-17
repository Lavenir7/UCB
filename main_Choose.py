'''利用UCB算法寻找最优的选择'''

import numpy as np
import pandas as pd
from UCBs.UCB import UCB

N_min = 30
N_max = 500
csv_file = r'./ChooseFiles/a.csv' # 选择数据表文件路径


df = pd.read_csv(csv_file)
Multi_armed_slot_machines = [lambda:np.random.choice(df['c1']),
                             lambda:np.random.choice(df['c2']),
                             lambda:np.random.choice(df['c3'])]

best_index = UCB(Multi_armed_slot_machines, N_min, N_max, view = True)
print(best_index)