import numpy as np
import imutils
import cv2

class SingleMotionDetector:
    def __init__(self, accum_weight=0.5):
        # store the accumulated weight factor
        self.accum_weight = accum_weight
        
        # initialize the background mode
        self.bg = None
        
        def update(self, image):
            # if the background model is None, initialize it
            if self.bg is None:
                self.bg = image.copy().astype("float")
                return
            
            return cv2.accumulateWeighted(image, self.bg, self.accum_weight)
            
        def detect(self, image, tVal=25):
            # compute the absolute difference between the background model
            # and the image passed in, then threshold the delta image
            delta = cv2.absdiff(self.bg.astype("uint8"), image)
            thresh = cv2.threshold(delta, tVal, 255, cv2.THRESH_BINARY)[1]
            
            # perform series of erosion and dilation to remove noise
            thresh = cv2.erode(thresh, None, iterations=2)
            thresh = cv2.dilate(thresh, None, iterations=2)
            
            # fidning countours in the threshold images now
            # and initoialise the minimum and maximum bounding 
            # boxes
            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            (minX, minY) = (np.inf, np.inf)
            (maxX, maxY) = (-np.inf, -np.inf)
                
        