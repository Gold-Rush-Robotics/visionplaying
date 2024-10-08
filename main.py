import cv2
import numpy as np

print("hello")
# Open the default camera
cam = cv2.VideoCapture(1)

print("2")

# Get the default frame width and height
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("3")

cv2.namedWindow('image')

cv2.createTrackbar('Lower - H','image',0,255, None)
cv2.createTrackbar('Lower - S','image',0,255, None)
cv2.createTrackbar('Lower - V','image',0,255, None)
cv2.createTrackbar('Upper - H','image',0,255, None)
cv2.createTrackbar('Upper - S','image',0,255, None)
cv2.createTrackbar('Upper - V','image',0,255, None)



while cam.isOpened():
    ret, frame = cam.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    
    lower_color = np.array([cv2.getTrackbarPos('Lower - H','image'), cv2.getTrackbarPos('Lower - S','image'), cv2.getTrackbarPos('Lower - V','image')]) 
    upper_color = np.array([cv2.getTrackbarPos('Upper - H','image'), cv2.getTrackbarPos('Upper - S','image'), cv2.getTrackbarPos('Upper - V','image')]) 

    mask = cv2.inRange(hsv, lower_color, upper_color) 
    
    result = cv2.bitwise_and(frame, frame, mask = mask) 
    
    # Display the captured frame
    cv2.imshow('Camera', result)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
cam.release()
cv2.destroyAllWindows()
