# UCB
通过UCB算法解决多臂老虎机【自写代码】

## 文件说明
- SlotMachine.py: 模拟单臂老虎机（正态分布和Beta分布）；
- DistributeView.py: 数据分布可视化（使用matplotlib，hist绘制直方图）；
- writecsv.py: 将SlotMachine.py产生的数据写入csv文件中，保存至ChooseFiles文件夹下；
- main_MAB.py: 利用UCB算法寻找最优的多臂老虎机；
- main_Choose.py: 利用UCB算法寻找最优选择，“选择”数据csv文件存放于ChooseFiles文件夹下；
- ChooseFiles: 存放“选择”的数据；
- UCBs: UCB算法库
  - UCB.py: UCB算法核心；
  - UCBView.py: UCB算法过程可视化（使用matplotlib实现）；
