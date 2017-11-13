# Learn OpenCV Week 1 - Assignment
#
# Stick Figure Animation


import cv2
import numpy as np

image = np.zeros((400, 400, 3), dtype=np.uint8)
imgCentr = [50,350]

# Draw a circle
imageCircle = image.copy()
cv2.circle(imageCircle, (200, 200), 50, (0, 0, 255), thickness=2, lineType=cv2.LINE_AA)
cv2.imshow("circle", imageCircle)

# Create Video Writer Object
frame_width = 400
frame_height = 400
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 25, (frame_width,frame_height))


while True:

    if imgCentr[0] > 350:
        imgCentr[0] = 50
    else:
        imgCentr[0] = imgCentr[0]+10

    cv2.circle(imageCircle, (imgCentr[0], imgCentr[1]), 50, (0, 0, 255), thickness=2, lineType=cv2.LINE_AA)
    cv2.imshow("circle", imageCircle)

    # Write the frame into the file 'output.avi'
    out.write(imageCircle)
    imageCircle = image.copy()


    # Press ESC on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == 27:
        break

# When everything done, release the video write objects
out.release()

# Closes all frames
cv2.destroyAllWindows()