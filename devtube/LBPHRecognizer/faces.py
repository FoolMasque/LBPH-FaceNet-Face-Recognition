import numpy as np
import cv2
import pickle

face_cascade =cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
#创建LBPH识别器并开始训练，当然也可以选择Eigen或者Fisher识别器
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name": 1} # 构造对象 
with open("labels.pickle", 'rb') as file:
    new_labels = pickle.load(file) # 读取文件并建立对象
    labels = {v:k for k,v in new_labels.items()}

cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame逐帧捕获
    ret, frame = cap.read()
    #将测试图像转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #调用分类器进行检测#检测多尺度图像，返回值是一张脸部区域信息的列表（x坐标,y坐标,脸部宽,脸部高）
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)#minNeighbors：每个候选矩阵应包含的像素领域
    #画出矩形框
    for(x, y, w, h) in faces:
        #print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]#按q截取图片并保存ROI区域


# 根据给定的（x，y）坐标标识出人名
        id_, conf = recognizer.predict(roi_gray)
        if conf<=50:
            print(id_,conf)
            print(labels[id_])
            font = cv2.FONT_HERSHEY_DUPLEX
            name = labels[id_]
            color = (255,255,255)#矩形框颜色
            stroke = 2
            cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

        img_item = "my-image.png"
        cv2.imwrite(img_item, roi_gray)

        #根据给定的（x，y）坐标和宽度高度在图像上绘制矩形
        color = (98, 100, 60)
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x,end_cord_y), color, stroke)



    # Display the resulting frame
    cv2.imshow('recognizer',frame)#显示视频 第一个参数是视频播放窗口的名称，第二个参数是视频的当前帧
    if cv2.waitKey(20) & 0xFF == ord('q'):#在播放每一帧时，使用cv2.waitKey()适当持续时间，一般可以设置25ms。按q键退出
        break

# When everything done, release the capture释放对象和销毁窗口
cap.release()
cv2.destroyAllWindows()