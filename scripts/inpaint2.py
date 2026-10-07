import cv2, numpy as np
im=cv2.imread('data/ivory_flat.png'); H,W=im.shape[:2]
hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV); Hh,S,V=cv2.split(hsv)
x1,y1,x2,y2=int(W*0.10),int(H*0.30),int(W*0.90),int(H*0.775)
region=np.zeros((H,W),np.uint8); region[y1:y2,x1:x2]=255
# exclude stamp circles (safety)
cv2.circle(region,(int(W*0.10),int(H*0.86)),150,0,-1)
cv2.circle(region,(int(W*0.90),int(H*0.86)),150,0,-1)
ink=(((V<198)|(S>95))).astype(np.uint8)*255
ink=cv2.bitwise_and(ink,region)
ink=cv2.dilate(ink,np.ones((7,7),np.uint8),iterations=2)
clean=cv2.inpaint(im,ink,7,cv2.INPAINT_TELEA)
cv2.imwrite('data/ivory_clean.png',clean)
print('done')
