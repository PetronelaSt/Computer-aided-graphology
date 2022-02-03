import cv2
import numpy as np
import os, os.path

# my_absolute_dirpath = os.path.abspath(os.path.dirname(__file__))
# image path and valid extensions
# imgInputDir = "Input_img/"
# imgOutputDir = "Output_img/"
imgIn_path_list = []
valid_image_extensions = [".jpg", ".jpeg", ".png"]


def Crop_from_dir_to(imgInputDir, imgOutputDir):
    for file in os.listdir(imgInputDir):
        extension = os.path.splitext(file)[1]
        if extension.lower() not in valid_image_extensions:
            continue
        imgIn_path_list.append(os.path.join(imgInputDir, file))

    # loop through image_path_list to open each image
    for imagePath in imgIn_path_list:
        image = cv2.imread(imagePath, 1)
        imgPerson = str(imagePath).replace('.jpg', '').replace(str(imgInputDir), '')
        print(imagePath)
        image = np.asarray(image, dtype=np.uint8)

        # print(image)
        # cv2.imshow('orig',image)
        # cv2.waitKey(0)

        # grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('gray', gray)
        # cv2.waitKey(0)

        # binary
        ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
        # cv2.imshow('second', thresh)
        # cv2.waitKey(0)

        # dilation
        kernel = np.ones((5, 5), np.uint8)
        img_dilation = cv2.dilate(thresh, kernel, iterations=1)
        # cv2.imshow('dilated', img_dilation)
        # cv2.waitKey(0)

        # find contours
        ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # sort contours
        sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

        for i, ctr in enumerate(sorted_ctrs):
            # Get bounding box
            x, y, w, h = cv2.boundingRect(ctr)

            # Getting ROI
            roi = image[y:y + h, x:x + w]
            roi = cv2.resize(roi, (28, 28), cv2.INTER_AREA)

            if not os.path.exists(imgOutputDir):
                os.makedirs(imgOutputDir)
            if not os.path.exists(imgOutputDir + imgPerson + '/'):
                os.makedirs(imgOutputDir + imgPerson + '/')

            cv2.imwrite(os.path.join(imgOutputDir + imgPerson + '/' + imgPerson + '_segment_' + str(i) + '.jpg'), roi)
            # print(imgOutputDir + imgPerson + '/' + imgPerson + '_segment_' + str(i) + '.jpg')
            cv2.rectangle(image, (x, y), (x + w, y + h), (90, 0, 255), 2)
            # cv2.waitKey(0)

        # cv2.imshow('marked areas', image)
        # cv2.waitKey(0)
