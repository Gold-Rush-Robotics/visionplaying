import sys
import cv2 as cv
import numpy as np


def main():
    
    filename = 'testphoto-1-20.jpg'
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        return -1
    
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)
    rows = gray.shape[0]
    

    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1.5, 250,
                            param1=40, param2=55,
                            minRadius=200, maxRadius=290)
    
    if circles is not None:
        print(len(circles[0, :]))

        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv.circle(src, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv.circle(src, center, radius, (255, 0, 255), 3)
    else:
        print("no circles found")
    
    
    cv.imshow("detected circles", src)
    cv.waitKey(0)
    
    return 0

if __name__ == "__main__":
    main()
