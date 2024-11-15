import cv2
img = cv2.imread('dog.png')
low_res_img = cv2.resize(img, (256, 256))  # Resize to low resolution
cv2.imwrite('dogout.png', low_res_img)
