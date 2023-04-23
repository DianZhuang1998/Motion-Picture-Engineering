import cv2
import numpy as np

# Open videos
video1 = cv2.VideoCapture('dancing_org.mp4')
video2 = cv2.VideoCapture('360/test360_128k.mp4')

# Get video properties
fps = video1.get(cv2.CAP_PROP_FPS)
frame_count = int(video2.get(cv2.CAP_PROP_FRAME_COUNT))

width = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Calculate PSNR for each frame
psnr_list = []
for i in range(frame_count):
    # Read frames
    ret1, frame1 = video1.read()
    ret2, frametemp2 = video2.read()
    if not ret1 or not ret2:
        break
    
    # Convert frames to grayscale
    frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2_gray = cv2.cvtColor(frametemp2, cv2.COLOR_BGR2GRAY)

    # bicubic
    frame2 = cv2.resize(frame2_gray, (width, height), interpolation=cv2.INTER_CUBIC)
    
    # Calculate MSE and PSNR
    mse = np.mean((frame1_gray - frame2) ** 2)
    psnr = 10 * np.log10(255**2 / mse)
    psnr_list.append(psnr)

# Calculate average PSNR
avg_psnr = np.mean(psnr_list)

# Print result
print("Average PSNR:", avg_psnr)