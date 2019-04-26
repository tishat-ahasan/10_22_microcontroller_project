import cv2
import pyautogui
import  time

import numpy as np
def imageCompare(original,image_to_compare,x):
    if original.shape == image_to_compare.shape:
        print("The images have same size and channels")
        difference = cv2.subtract(original, image_to_compare)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            #print("The images are completely Equal")
            return 100
        else:
            #print("The images are NOT equal")

            # 2) Check for similarities between the 2 images
            sift = cv2.xfeatures2d.SIFT_create()
            kp_1, desc_1 = sift.detectAndCompute(original, None)
            kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)

            index_params = dict(algorithm=0, trees=5)
            search_params = dict()
            flann = cv2.FlannBasedMatcher(index_params, search_params)
            matches = flann.knnMatch(desc_1, desc_2, k=2)
            good_points = []
            ratio = 0.9
            for m, n in matches:
                if m.distance < ratio * n.distance:
                    good_points.append(m)
            print(len(good_points))

            number_keypoints = 0
            if len(kp_1) <= len(kp_2):
                number_keypoints = len(kp_2)
            else:
                number_keypoints = len(kp_1)
            print("Keypoints 1ST Image: " + str(len(kp_1)))
            print("Keypoints 2ND Image: " + str(len(kp_2)))
            print("GOOD Matches:", len(good_points))
            percentage = len(good_points) / number_keypoints * 100
            print("How good it's the match: ", percentage)

            result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)
            #result.save(str(x)+".jpg")
            #cv2.save(str(x) + ".jpg")
            #cv2.imshow("result", cv2.resize(result, None, fx=0.6, fy=0.6))
            #cv2.imshow("Original", original)
            #cv2.imshow("Duplicate", image_to_compare)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            #while True:
             #   n=input("Enter 1:")
            #    if n=="1":
             #       break

            return  percentage

while True:
    f = open("C:\\Users\\tisha\\Documents\\Arduino\\MainProcesses\\data.txt", "r")
    contents = f.read()
    print(contents+"1")
    f.close()
    if contents=="0":
        time.sleep(1)
        #print(contents)
    elif contents=="1":
        #print(contents)
        time.sleep(1)
        pyautogui.screenshot('current.jpg', region=(0, 150, 500, 400))
        x=1
        percentage1=0
        percentage2=0
        while x<=5:
            original = cv2.imread("current.jpg")
            image_to_compare = cv2.imread(str(x)+".jpg")
            percentage1 = max(percentage1 , imageCompare(original,image_to_compare,x))
            x=x+1
        #percentage1 = percentage1/5

        x=6
        while x<=10:
            original = cv2.imread("current.jpg")
            image_to_compare = cv2.imread(str(x)+".jpg")
            percentage2 = max(percentage2 , imageCompare(original,image_to_compare,x))
            x=x+1
        #percentage2 = percentage2/5
        # 1) Check similarity between 2 images
        print("First image matching average percentage" + str(percentage1))
        print("Second image  matching average percentage" + str(percentage2))
        f = open("C:\\Users\\tisha\\Documents\\Arduino\\MainProcesses\\result.txt", "w")
        if percentage1<=10 and percentage2<=10:
            f.write("0")
        elif percentage1>percentage2:
            f.write("1")
        elif percentage2>percentage1:
            f.write("2")

        f.close()
        f = open("C:\\Users\\tisha\\Documents\\Arduino\\MainProcesses\\data.txt", "w")
        f.write("0")
        f.close()