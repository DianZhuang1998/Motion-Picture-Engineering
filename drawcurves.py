import matplotlib.pyplot as plt
import numpy as np


x720 = [512,1024,2048,3072]
y720=[25.46,27.135,28.69,29.83]

x360 = [96,128,256,384, 512, 1024,2048]
y360 = [22.67, 23.37, 24.86, 25.68, 26.20, 27.33,28.16]

x180 = [64, 96, 128, 256,512, 1024]
y180 = [22.19, 22.72, 23.02, 23.54, 23.82, 23.96]
fig = plt.figure(figsize=(12,8))
plt.title("RD curves")
plt.xlabel("Bitrate(Kbps)") #xlabel、ylabel：分别设置X、Y轴的标题文字。
plt.ylabel("PSNR(db)")

plt.ylim(20, 30)
plt.yticks(range(20, 31, 1))
x_ticks = np.linspace(64, 3072, num=11)
plt.xticks(x_ticks)
# 然后绘制图像
# 绘制折线图，并指定点标记类型和颜色
#plt.plot(x720, y720, 'o-', color='red')

# 设置线的颜色
#plt.plot(x720, y720, color='blue', label="sin(x)")
#plt.plot(x720, y720, marker='o',color="blue", ms=8,mfc="r",mec="c", label='720p width diffrent bitrate ')
plt.plot(x720, y720, marker='o',color="blue", ms=5,mfc="r", label='720p width diffrent bitrate ')
plt.plot(x360, y360, marker='o',color="green", ms=5,mfc="y", label='360p width diffrent bitrate ')
plt.plot(x180, y180, marker='o',color="m", ms=5,mfc="k", label='180p width diffrent bitrate ')
plt.legend(loc='lower right', bbox_to_anchor=(1, 0))
plt.grid(linestyle='--')
plt.show()
