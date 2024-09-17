import numpy as np
import pandas as pd

def one_arm_normal(mean = 0, std = 1, ranges = (0, 1)):
    '''
    【服从正态分布的单臂老虎机】
    -1 <= mean <= 1: 控制数据偏向小值还是偏向大值
    std > 0: 越小数据越集中于mean
    '''
    if not -1 <= mean <= 1:
        print('均值应在 [-1,1] 内。')
        return -1
    if std <= 0:
        print('方差应为正数。')
        return -1
    while True:
        r = np.random.normal(loc=mean, scale=std)
        if -3 <= r <= 3:
            break
    res = (r+3)*(ranges[1]-ranges[0])/6+ranges[0]
    return res

def one_arm_beta(a = 1, b = 1, ranges = (0, 1)):
    '''
    【服从Beta分布的单臂老虎机】
    b < 1 < a: 数据偏向大值
    a < 1 < b: 数据偏向小值
    a,b > 1: 数据集中在中间
    a,b < 1: 数据集中在两端
    a = b: 对称分布，越大越集中于中心
    a = b = 1: 均匀分布
    '''
    if a <= 0 or b <= 0:
        print('参数应为正数。')
        return -1
    r = np.random.beta(a=a, b=b)
    res = r*(ranges[1]-ranges[0])+ranges[0]
    return res

N = 5000
df = pd.DataFrame(columns = ['c1', 'c2', 'c3'])
for i in range(N):
    df.loc[i] = [one_arm_normal(0.7,0.5,(30,500)),one_arm_beta(5,3,(30,500)),one_arm_normal(0.3,1.5,(30,500))]
df.to_csv('.ChooseFiles/a.csv')