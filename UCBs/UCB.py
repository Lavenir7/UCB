'''
Upper Confidence Bound [UCB]
信心上界算法
'''

from UCBs.UCBView import draw_dynamic_rectangles
import matplotlib.pyplot as plt

EXEC_time_least = 20 # 决定某个选择为最优之前，至少执行/尝试过的次数

def find_best(scores_min, scores_max) -> int:
    '''
    寻找UCB算法规则下的最优选择（最优选择的最低分要比非最优选择的最高分都高）：
    若存在最优选择，返回最优选择的索引
    否则，返回-1
    '''
    best_possible = scores_min.index(max(scores_min))
    best_score_min = max(scores_min)
    for i in range(len(scores_max)):
        if i == best_possible:
            continue
        if best_score_min < scores_max[i]:
            return -1
    return best_possible

def UCB(chooses: list, score_min, score_max, view = False):
    '''
    chooses: 存放多个函数名的列表，一个函数代表一种选择
    score_min, score_max: 所有选择中，能得到的最低分和最高分
    view: 是否可视化展示UCB算法的抉择过程
    '''
    if view:
        fig, ax = plt.subplots() # 绘图命令1
    choose_len = len(chooses)
    c = (score_max - score_min)/2
    choose_exec_n = [0 for _ in range(choose_len)]
    scores_min = [score_min for _ in range(choose_len)]
    scores_max = [score_max for _ in range(choose_len)]
    scores_history_average = []
    for i in range(choose_len):
        scorei = chooses[i]()
        choose_exec_n[i] += 1
        scores_history_average.append(scorei)
        scores_min[i] = scorei - c/(choose_exec_n[i])**0.5
        scores_max[i] = scorei + c/(choose_exec_n[i])**0.5
    # 
    while True:
        choose_exec_index = scores_max.index(max(scores_max)) # 面对未知乐观原则: 在乐观中选择最好的
        score = chooses[choose_exec_index]()
        choose_exec_n[choose_exec_index] += 1
        scores_history_average[choose_exec_index] = (scores_history_average[choose_exec_index]*(choose_exec_n[choose_exec_index]-1)+score)/choose_exec_n[choose_exec_index]
        # 原则2: 在交互中降低乐观
        scores_min[choose_exec_index] = scores_history_average[choose_exec_index] - c/(choose_exec_n[choose_exec_index])**0.5
        scores_max[choose_exec_index] = scores_history_average[choose_exec_index] + c/(choose_exec_n[choose_exec_index])**0.5
        if view:
            draw_dynamic_rectangles(fig, score_min, score_max, scores_min, scores_max, choose_exec_n) # 绘图命令2
        best_index = find_best(scores_min, scores_max)
        if best_index != -1: # 找到最优选择
            if choose_exec_n[best_index] >= EXEC_time_least: # 该最优选择尝试次数达到最低次数
                return best_index
    if view:
        plt.show() # 绘图命令3