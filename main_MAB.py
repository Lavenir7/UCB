'''利用UCB算法寻找最优的单臂老虎机'''

from SlotMachine import *
from DistributeView import *
from UCBs.UCB import UCB

N_min = 0
N_max = 10001

Multi_armed_slot_machines = [lambda:int(one_arm_normal(0.7, 0.5, (N_min, N_max))),
                             lambda:int(one_arm_beta(5, 3, (N_min, N_max))),
                             lambda:int(one_arm_normal(0.3, 1.5, (N_min, N_max)))]
slot_machine_list = ['normal(0.7, 0.5)',
                     'beta(5, 3)',
                     'normal(0.3, 1.5)',]
draw_distribute(Multi_armed_slot_machines, 2, 2, slot_machine_list)

best_index = UCB(Multi_armed_slot_machines, N_min, N_max, view = True)
print(best_index)