from ast import If
from time import sleep
import cv2
import numpy as np
import argparse
import mediapipe as mp
from Segmentations import * #AnimationSegmenter, AnimeSegmenter, HumanSegmentator, HumanSegmenter
from functions import *
mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation


ASCII_CHARS = ["@", "#", "&", "$", "X", "?", "!", "+", "-", "."]


image_direction = "D:/Visual_Studio_Project/Python/images/character2.jpg"

def People():
    img = cv2.imread(image_direction)
    segmented = HumanSegmenter.human_selection(img)
    resizedImage, dim = ASCII_Functions.resize_automatically2(segmented,200) #  => 1
    grayImage = ASCII_Functions.to_greyscale(resizedImage)
    gammaScaler = 1.0
    gammaScaler = 30/np.average(grayImage)
    gammaScaler = max(1, gammaScaler)
    
    return ASCII_Functions.for_loop(dim, gammaScaler, grayImage)

def Animation():
    img = cv2.imread(image_direction)
    segmenter = AnimationSegmenter()
    segmented = segmenter.run(img)
    resizedImage, dim = ASCII_Functions.resize_automatically2(segmented,400) #  => 1
    grayImage = ASCII_Functions.to_greyscale(resizedImage)
    gammaScaler = 1.0
    gammaScaler = 30/np.average(grayImage)
    gammaScaler = max(1, gammaScaler)
    
    return ASCII_Functions.for_loop(dim, gammaScaler, grayImage)

def with_everything():
    img = cv2.imread(image_direction)
    resizedImage, dim = ASCII_Functions.resize_automatically2(img,200) #  => 1
    grayImage = ASCII_Functions.to_greyscale(resizedImage)
    gammaScaler = 1.0
    gammaScaler = 30/np.average(grayImage)
    gammaScaler = max(1, gammaScaler)
    
    return ASCII_Functions.for_loop(dim, gammaScaler, grayImage)

def main():

    image = cv2.imread(image_direction)
    if image is None:
        print('Could not open or find the image.')
        exit(0)

    print("1 : People\n2 : Animation\n3 : Full Image")
    trans = int(input("Enter which transaction do you want to do :"))
    if trans == 1:
        image2 = HumanSegmenter.human_selection(image)
        cv2.imshow("final ",ASCII_Functions.to_greyscale(image2))
        cv2.waitKey(0)
        writeString = People()
        ASCII_Functions.file(writeString)
    elif trans == 2:
        segmenter = AnimationSegmenter()
        image3 = segmenter.run(image)
        cv2.imshow("final ",ASCII_Functions.to_greyscale(image3))
        cv2.waitKey(0)
        writeString = Animation()
        ASCII_Functions.file(writeString)
    elif trans == 3:
        cv2.imshow("final ",ASCII_Functions.to_greyscale(image))
        cv2.waitKey(0)
        writeString = with_everything()
        ASCII_Functions.file(writeString)
    else:
        print("press 1 or 2!!")


if __name__ == "__main__":
    main()
