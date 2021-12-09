import cv2
# For Shape Detection, we are using a contour approximation algorithm for reducing the number of points in a curve with a reduced set of points.


class ShapeDetector:
    def detect(self, contour):
        #print(contour)
        shape = ''
        perimeter = cv2.arcLength(contour, True)
        approxContour = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
        #print(len(approxContour))

        if len(approxContour) == 3:
            shape = 'Triangle'
        elif len(approxContour) == 4:
            (x, y, w, h) = cv2.boundingRect(approxContour)
            ar = w / float(h)
            if 0.95 <= ar <= 1.05:
                shape = 'Square'
            else:
                shape = 'Rectangle'
        elif len(approxContour) == 5:
            shape = 'Pentagon'
        else:
            shape = 'Circle'

        return shape

