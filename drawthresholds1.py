import matplotlib.pyplot as plt
import numpy as np


x = [1024,2048]
y=[27.33, 28.16]

x2 = [1024,2048]
y2 = [27.135, 28.69]

fig = plt.figure(figsize=(12,8))
plt.title("threshold 360p, 720p")
plt.xlabel("Bitrate(Kbps)") #xlabel、ylabel：分别设置X、Y轴的标题文字。
plt.ylabel("PSNR(db)")

plt.ylim(27.1, 29.1)
#plt.yticks(range(22, 24, 1))

x_ticks = np.linspace(1000, 2100,num=11)
plt.xticks(x_ticks)

plt.plot(x, y, marker='o',color="blue", ms=5,mfc="r", label='720p width diffrent bitrate ')
plt.plot(x2, y2, marker='o',color="green", ms=5,mfc="y", label='360p width diffrent bitrate ')

plt.legend(loc='lower right', bbox_to_anchor=(1, 0))
plt.grid(linestyle='--')
plt.show()