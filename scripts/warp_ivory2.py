import cv2, numpy as np
im=cv2.imread('assets/ref_card.png')
pts=np.float32([[249,213],[797,139],[859,545],[319,654]])  # TL,TR,BR,BL
c=pts.mean(axis=0)
exp=1.065
pts2=c+(pts-c)*exp
W,Hh=1180,900
dst=np.float32([[0,0],[W,0],[W,Hh],[0,Hh]])
M=cv2.getPerspectiveTransform(pts2.astype(np.float32),dst)
out=cv2.warpPerspective(im,M,(W,Hh),flags=cv2.INTER_CUBIC)
cv2.imwrite('data/ivory_flat.png',out)
print('done')
