'''对UCB算法中的抉择过程可视化'''

import matplotlib.pyplot as plt
import matplotlib.patches as patches

sleep_time = 0.1 # UCB算法可视化时，每步停留的时间

# 实时演化的绘图函数
def draw_dynamic_rectangles(fig, N_min, N_max, scores_min, scores_max, choose_exec_n, labels = None):
    '''
    fig: 绘图窗口
    N_min, N_max: 分数总上下限
    scores_min, scores_max: 各选择所得分数的上下限
    choose_exec_n: 各选择的执行次数
    labels: 各选择的名称/标签
    '''
    plt.pause(sleep_time/2)
    N = len(choose_exec_n)
    if labels == None:
        labels = [i+1 for i in range(N)]
    width = 2.5 # 大矩形宽度
    height = 10 # 大矩形高度
    spacing = 1.5 # 定义间距
    positions = [i*(width + spacing) for i in range(N)] # 定义大矩形横坐标
    plt.clf() # 清除当前图形内容

    # 设置画布背景颜色为黑色
    fig.patch.set_facecolor('black')
    ax = plt.gca() # 获取当前坐标轴
    ax.set_facecolor('black') # 设置背景颜色

    # 绘制每个大矩形和对应的小矩形
    for i, pos in enumerate(positions):
        # 大矩形
        rect = patches.Rectangle(
            (pos, 0), # 左下角位置
            width, # 宽度
            height, # 高度
            linewidth=2, # 边框宽度
            edgecolor='white', # 边框颜色
            facecolor='none', # 矩形内部透明
            zorder=1
        )
        ax.add_patch(rect)

        # 计算小矩形参数
        small_height = (scores_max[i] - scores_min[i]) / (N_max - N_min) * height # 计算小矩形的高度
        small_bottom = (scores_min[i] - N_min) / (N_max - N_min) * height # 计算小矩形的纵坐标

        # 小矩形
        small_rect = patches.Rectangle(
            (pos, small_bottom), # 左下角位置
            width, # 宽度
            small_height, # 高度
            linewidth=0, # 边框宽度
            edgecolor='none', # 边框颜色
            facecolor='blue', # 填充颜色
            alpha=0.7, # 半透明
            zorder=2
        )
        ax.add_patch(small_rect)

        # 绘制小矩形中心的黄色横线
        plt.plot(
            [pos, pos + width], # 横线起点和终点
            [small_bottom + small_height / 2] * 2, # 横线的 y 坐标（小矩形中心）
            color='yellow', # 横线颜色
            linewidth=1, # 横线宽度
            zorder=3
        )

        # 标注执行次数
        plt.text(
            pos + width / 2, # x 坐标（大矩形中心）
            height+2.5, # y 坐标（大矩形上方）
            str(choose_exec_n[i]), # 执行次数
            color='yellow', # 文字颜色
            ha='center', # 水平对齐方式
            va='center', # 垂直对齐方式
            fontsize=12 # 字体大小
        )

        # 添加标签
        plt.text(
            pos + width / 2, # x 坐标（大矩形中心）
            -2.5, # y 坐标（大矩形下方）
            str(labels[i]), # 标签内容
            color='white', # 文字颜色
            ha='center', # 水平对齐方式
            va='center', # 垂直对齐方式
            fontsize=12 # 字体大小
        )

    # 设置坐标轴范围
    yn = 10
    ax.set_xlim(-spacing, N*width+N*spacing)
    ax.set_ylim(-yn, height+yn) # 适当扩展 y 轴范围以便查看标签
    ax.set_aspect('equal') # 保持纵横比
    ax.axis('off') # 去除坐标轴

    # 更新显示
    plt.pause(sleep_time/2)