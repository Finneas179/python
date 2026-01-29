from matplotlib import pyplot as plt

# x=range(1,13)
# y=[1,4,32,4,6,3,2,4,6,32,3,5]
# plt.plot(x,y)
# plt.ylabel('1')

# plt.figure()
# plt.plot([1,2,3],[4,5,6])
#
# plt.subplots()
# fig,ax = plt.subplots()
plt.rcParams['font.sans-serif'] = ['SimHei']
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(["北京","上海","杭州"],[1,2,3])
plt.show()


fig=plt.figure()
ax=plt.axes()
ax.plot(["北京","上海","杭州"],[1,2,3])
plt.show()