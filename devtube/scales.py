import cv2

img = cv2.imread('./images/1.jpg')


##----计算原始图片每次缩放的比例----##

#def calculateScales(img):
	#复制传入的图片
copy_img = img.copy()
    #比例初始化
pr_scale = 1.0
h,w,_ = copy_img.shape
    #对原始图片resize预处理
if min(w,h)>500:
    pr_scale = 500.0/min(h,w)
    w = int(w*pr_scale)
    h = int(h*pr_scale)
elif max(w,h)<500:
    pr_scale = 500.0/max(h,w)
    w = int(w*pr_scale)
    h = int(h*pr_scale)
#存放比例系数
scales = []
#resize比例因子
factor = 0.709
factor_count = 0
minsize = min(h,w)
#缩放至最小边≥12
while minsize >= 12:
    scales.append(pr_scale*pow(factor, factor_count))
    minsize *= factor
    factor_count += 1
#    return scales



#a_img=calculateScales(copy_img)

print(scales)
cv2.imshow('Face Detector',copy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()