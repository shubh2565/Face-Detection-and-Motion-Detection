# Face-Detection-and-Motion-Detection

This project contains codes for basic face detection and motion detection with the help of OpenCV (Open Source Computer Vision), a BSD licensed library with stong focus on real time applications.
It takes advantage of multi-core processing.

Haar cascade clssifier is used for face detection which calculates Haar like features.
A Haar-like feature considers adjacent rectangular regions at a specific location in a detection window, sums up the pixel intensities in each region and calculates the difference between these sums and calculates the difference to categorize subsections of an image.
Due to use of integral images, A Haar like feature of any size can be calculated in constant time, making it much faster than other classifiers.

In motion detection, we utilize several image processing methods like Gaussian Blur, thresholding, finding contours, dilation ,etc .
A csv file is also created to record the start and end time of motion detection.
