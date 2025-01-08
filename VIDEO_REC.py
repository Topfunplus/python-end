'''
  通过VideoCapture模型来导入视频文件
  创建专门用于体态检测的模型
  定义标志位，用来表示蹲下还是站起，用count来进行计数 time来进行分割时间
  不断进行：
    读取视频帧，以及拿到是否成功读取的标志
      睡眠一会
      如果成功读取的话：
        获取图像的高度宽度，以及通道数
        通过模型的findpose来找到帧的姿势
        通过模型的findposition来找到帧的位置 返回了一个三个元素的列表
        如果位置存在的话：
           找到角度
           画一个矩形
           
           如果角度小于75度，那么说明是蹲下的
              标志位如果为0 ，那么我们把count加一半，因为还没有站起，并且标志位1
           如果角度大于100度，那么说明是站起
              标志位如果为1 设置为0 并且count加一半
              
          屏幕中间显示文字 
        显示图像
      不成功 退出循环
'''

import cv2  # 导入OpenCV库，用于计算机视觉任务
import numpy as np  # 导入NumPy库，用于数值计算
import time  # 导入时间模块，用于控制循环时间

cap = cv2.VideoCapture("yangwo.mp4")  # 打开视频文件 "yangwo.mp4"
detector = PoseDetector()  # 创建PoseDetector实例
dir = 0  # 初始化方向标志位
count = 0  # 初始化计数器

while True:
    success, img = cap.read()  # 读取视频帧，success为读取是否成功，img为图像帧
    time.sleep(0.1)
    if success:
        h, w, c = img.shape
        img = detector.find_pose(img, draw=False)
        positions = detector.find_position(img)
        if positions:
            angle = detector.find_angle(img, positions[0], positions[1], positions[2])

            # 中间-100 和 中间 +100的位置
            bar = np.interp(angle, (50, 130), (w // 2 - 100, w // 2 + 100))
            cv2.rectangle(
                img,
                (w // 2 - 100, h - 150),
                (int(bar), h - 100),
                (0, 255, 0),
                cv2.FILLED,
            )

            # 完成一个周期
            if angle < 75:
                if dir == 0:
                    count += 0.5
                    dir = 1
            if angle > 100:
                if dir == 1:
                    count += 0.5
                    dir = 0

            cv2.putText(
                img,
                str(int(count)),  # 在图像上写入计数值
                (w // 2, h // 2),  # 文字的位置
                cv2.FONT_HERSHEY_SIMPLEX,  # 字体类型
                10,  # 字体大小
                (255, 255, 255),  # 字体颜色（白色）
                20,  # 字体厚度
                cv2.LINE_AA,  # 线条类型
            )
        cv2.imshow("Image", img)  # 显示图像窗口，窗口标题为"Image"
    else:
        break  # 如果读取视频帧失败，退出循环
    key = cv2.waitKey(1)  # 等待1毫秒，看是否有按键事件
    if key == ord("q"):  # 如果按下"q"键
        break  # 退出循环
cap.release()  # 释放视频捕获对象
cv2.destroyAllWindows()  # 关闭所有OpenCV窗口
