import cv2
import numpy as np 
import matplotlib.pyplot as plt
# Đọc ảnh
img = cv2.imread('cat.jpg')
if img is None:
    print("Không thể tải file!")
else:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Các kernel (bộ lọc)
    kernel_identity = np.array([[0,0,0],
                                [0,1,0],
                                [0,0,0]], np.float32)
    kernel_3x3 = np.ones((3,3), np.float32) / 9.0
    kernel_5x5 = np.ones((5,5), np.float32) / 25.0
    # Áp dụng bộ lọc
    output_identity = cv2.filter2D(img_rgb, -1, kernel_identity)
    output_3x3 = cv2.filter2D(img_rgb, -1, kernel_3x3)
    output_5x5 = cv2.filter2D(img_rgb, -1, kernel_5x5)

    # Hiển thị ảnh
    titles = ['Original', 'Identity Filter', '3x3 Blur', '5x5 Blur']
    images = [img_rgb, output_identity, output_3x3, output_5x5]

    plt.figure(figsize=(12, 6))
    for i in range(4):
        plt.subplot(1, 4, i + 1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.axis('off')
    plt.show()
