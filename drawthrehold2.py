import matplotlib.pyplot as plt
import numpy as np


x = [96,128]
y=[22.67, 23.37]

x2 = [96, 128]
y2 = [22.72, 23.02]

fig = plt.figure(figsize=(12,8))
plt.title("threshold 360p, 180p")
plt.xlabel("Bitrate(Kbps)") #xlabel、ylabel：分别设置X、Y轴的标题文字。
plt.ylabel("PSNR(db)")

plt.ylim(22.1, 23.1)
#plt.yticks(range(22, 24, 1))

x_ticks = np.linspace(90, 130,num=11)
plt.xticks(x_ticks)

plt.plot(x, y, marker='o',color="blue", ms=5,mfc="r", label='360p width diffrent bitrate ')
plt.plot(x2, y2, marker='o',color="green", ms=5,mfc="y", label='180p width diffrent bitrate ')

plt.legend(loc='lower right', bbox_to_anchor=(1, 0))
plt.grid(linestyle='--')
plt.show()
