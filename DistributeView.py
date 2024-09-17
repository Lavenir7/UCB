'''绘制老虎机所服从的分布的直方图'''

import matplotlib.pyplot as plt

def draw_distribute(chooses_list, h, w, labels):
    '''绘制各个选择所服从的分布的直方图'''
    N = len(chooses_list)
    if labels == None:
        labels = [i+1 for i in range(N)]
    fig, axs = plt.subplots(h, w)
    k = 0
    for i in range(w):
        for j in range(h):
            # 绘制子图
            axs[i, j].hist([chooses_list[k]() for _ in range(10000)], bins = 1000)
            axs[i, j].set_title(labels[k])
            k += 1
            if k >= N:
                break
        if k >= N:
            break    
    plt.tight_layout() # 自动调整子图布局
    plt.show() # 显示图形