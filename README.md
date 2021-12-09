# Shape-Detector-using-openCV
Shape Detector using openCV

In this project I am trying to detect the shapes of the objects presented in an image.

For Shape Detection, I am using a contour approximation algorithm for reducing the number of points in a curve to a reduced set of points.

The below Image Shows some shapes we are trying to detect

![shapes_and_colors](https://user-images.githubusercontent.com/87881560/145394923-639d71a9-5ebb-4fd9-a62e-5bd7fc4fe55a.jpg)


The algorithm I am going to use in this project is known as the Ramer-Douglas-Peucker algorithm, or simply the split-and-merge algorithm.

Contour approximation is predicated on the assumption that a curve can be approximated by a series of short line segments. This leads to a resulting approximated curve that consists of a subset of points that were defined by the original curve.

The algorithm is built-in in OpenCV via the cv2.approxPolyDP method.

The Output of the Project will be something like this

![Screenshot from 2021-12-09 15-13-06](https://user-images.githubusercontent.com/87881560/145402980-efe2a695-12d5-41d3-b8fa-7527ab58dce2.png)
