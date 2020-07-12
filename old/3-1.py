import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Hiragino Sans GB']

name = ['姜作林', '尤丽', '姜钰鑫', '姜殿涛']
power = [200, 400, 100, 1000]

plt.grid()
plt.title('世界大战TOP10')
plt.xlabel('姓名')
plt.ylabel('战斗力')

plt.scatter(name, power,s= 60,marker='x',c='r')
plt.savefig('/Users/jiangdiantao/myfile/tj.png')