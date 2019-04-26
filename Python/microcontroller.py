import cv2
import pyautogui
import  time

import numpy as np
x=1
while x<=2:
    time.sleep(1)
    pyautogui.screenshot(str(x)+'.jpg',region=(0,150, 300, 400))
    x=x+1
original = cv2.imread("1.jpg")
image_to_compare = cv2.imread("2.jpg")
# 1) Check if 2 images are equals
if original.shape == image_to_compare.shape:
    print("The images have same size and channels")
    difference = cv2.subtract(original, image_to_compare)
    b, g, r = cv2.split(difference)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("The images are completely Equal")
    else:
        print("The images are NOT equal")

        # 2) Check for similarities between the 2 images
        sift = cv2.xfeatures2d.SIFT_create()
        kp_1, desc_1 = sift.detectAndCompute(original, None)
        kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)

        index_params = dict(algorithm=0, trees=5)
        search_params = dict()
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(desc_1, desc_2, k=2)
        good_points = []
        ratio = 0.8
        for m, n in matches:
            if m.distance < ratio * n.distance:
                good_points.append(m)
        print(len(good_points))

        number_keypoints = 0
        if len(kp_1) <= len(kp_2):
            number_keypoints = len(kp_1)
        else:
            number_keypoints = len(kp_2)
        print("Keypoints 1ST Image: " + str(len(kp_1)))
        print("Keypoints 2ND Image: " + str(len(kp_2)))
        print("GOOD Matches:", len(good_points))
        print("How good it's the match: ", len(good_points) / number_keypoints * 100)

        result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)
        cv2.imshow("result",cv2.resize (result,None,fx=0.6,fy=0.6))
        cv2.imshow("Original", original)
        cv2.imshow("Duplicate", image_to_compare)
        cv2.waitKey(0)
        cv2.destroyAllWindows()