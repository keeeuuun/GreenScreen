import cv2  
import numpy as np


if __name__ == '__main__':
    def nothing(*arg):
        pass


cv2.namedWindow( "Color" ) 

cap = cv2.VideoCapture(0)

cv2.createTrackbar('R min', 'Color', 0, 255, nothing)
cv2.createTrackbar('G min', 'Color', 74, 255, nothing)
cv2.createTrackbar('B min', 'Color', 0, 255, nothing)
cv2.createTrackbar('R max', 'Color', 16, 255, nothing)
cv2.createTrackbar('G max', 'Color', 255, 255, nothing)
cv2.createTrackbar('B max', 'Color', 10, 255, nothing)

# Webcam Capture
#bgcap = cv2.VideoCapture(0)
# Existing Video Capture
bgcap = cv2.VideoCapture('bg.mp4')
#fgcap = cv2.VideoCapture('fg.mp4')
# Background pic
fgcap = cv2.imread('2.png')


success, bg_frame = bgcap.read()
# video
#ret, fg_frame = fgcap.read()
# pic
fg_frame = fgcap


while True:  
    try:
        flag, img = bgcap.read()
        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2BGR )
    except:
        bgcap = cv2.VideoCapture('bg.mp4')
        flag, img = bgcap.read()
        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2BGR )
    # try || except - video
    '''try:
        flag_1, im = fgcap.read()
    except:
        fgcap = cv2.VideoCapture('fg.mp4')
        flag_1, im = fgcap.read()'''
    # pic
    im = fgcap


    # считываем значения бегунков
    h1 = cv2.getTrackbarPos('R min', 'Color')
    s1 = cv2.getTrackbarPos('G min', 'Color')
    v1 = cv2.getTrackbarPos('B min', 'Color')
    h2 = cv2.getTrackbarPos('R max', 'Color')
    s2 = cv2.getTrackbarPos('G max', 'Color')
    v2 = cv2.getTrackbarPos('B max', 'Color')

    # формируем начальный и конечный цвет фильтра
    h_min = np.array((h1, s1, v1), np.uint8)
    h_max = np.array((h2, s2, v2), np.uint8)

    # накладываем фильтр на кадр в модели HSV
    thresh = cv2.inRange(hsv, h_min, h_max)
    hsv1 = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)

    output = np.where(hsv1 == (0, 0, 0), img, im)
    cv2.imshow('ChromaKey', output)
    
    ch = cv2.waitKey(5)
    if ch == 27:
        break

cap.release()
cv2.destroyAllWindows()