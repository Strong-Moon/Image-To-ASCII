from typing import ClassVar
import cv2
import mediapipe as mp
import numpy as np
import imutils
ASCII_CHARS = ["@", "#", "&", "$", "X", "?", "!", "+", "-", "."]

class ASCII_Functions:
    
    def to_greyscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def gammaCorrection_by_hand(image, gamma):
        invGamma = 1.0 / gamma
        table = [((i / 255) ** invGamma) * 255 for i in range(256)]
        table = np.array(table, np.uint8)
        return cv2.LUT(image, table)

    def resize_image(image, scale_percent):
        width = int(image.shape[1] * scale_percent / 100)
        height = int(int(image.shape[0] * scale_percent / 100)/2.3)
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        return resized, dim

    def convert_pixel_to_character(pixel):
        (r, g, b) = pixel
        pixel_brightness = r + g + b
        max_brightness = 255 * 3
        brightness_weight = len(ASCII_CHARS) / max_brightness
        index = int(pixel_brightness * brightness_weight) - 1
        return ASCII_CHARS[index]
    
    def Downscale_with_resize(image):
        scale_percent = 50 # percent of original size
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        return resized, dim
    
    def Upscale_with_resize(image):
        scale_percent = 200 # percent of original size
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        return resized, dim
    
    def Resize_only_width(image, width):
        height = image.shape[0] # keep original height
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        return resized, dim
    
    def resize_by_hand(image, width, height):
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        return resized, dim
    
    def resize_automatically(image,width):
        resized = imutils.resize(image, width)
        height1 = int(resized.shape[0])
        width1 = int(resized.shape[1])
        dim = (width1, height1)
        return resized, dim

    def resize_automatically2(image,T_Width):
        Height, Width = image.shape[0], image.shape[1]
        scale_Number = T_Width / Width
        targetHeight = int(scale_Number * Height / 2.4) 
        dim = (T_Width, targetHeight)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        return resized, dim
 
    def edge_detection(image, width, height):
        edges = cv2.Canny(image,width,height)
        cv2.imshow("Edge Detected Image", edges)   

    def file(writeString):
        print("Do you want to save image in a file : ")
        answer = input("Yes or No :")   
        if answer == "Yes" or "yes":
            try:
                with open('C:/Users/Berkay Pehlivan/Desktop/newASCII.txt', 'w+') as f:
                    f.write(writeString)
            except FileNotFoundError:
                print("The directory does not exist.")
        elif answer == "No" or "no":
            print("Finished...")
        else:
            print("Wrong choice!!!")


    def for_loop(dim, gammaScaler, grayImage):

        one_255 = "@"
        two_225 = "#"
        three_200 = "&"
        four_175 = "$"
        five_150 = "X"
        six_125 = "?"
        seven_100 = "!"
        eight_75 = "+"
        nine_50 = "-"
        ten_25 = "."

        returnString = ""
        for y in range(0,dim[1]):  # for resize_automatically(segmented, [give iny value]) function, do like this range(0,dim[1],2)  => 1
            for x in range(dim[0]):
                value = grayImage[y][x] * gammaScaler
                if value < 25:
                    print(ten_25, end="")
                    returnString+=ten_25
                elif value < 50:
                    print(nine_50, end="")
                    returnString+=nine_50
                elif value < 75:
                    print(eight_75, end="")
                    returnString+=eight_75
                elif value < 100:
                    print(seven_100, end="")
                    returnString+=seven_100
                elif value < 125:
                    print(six_125, end="")
                    returnString+=six_125
                elif value < 150:
                    print(five_150, end="")
                    returnString+=five_150
                elif value < 175:
                    print(four_175, end="")
                    returnString+=four_175
                elif value < 200:
                    print(three_200, end="")
                    returnString+=three_200
                elif value < 225:
                    print(two_225, end="")
                    returnString+=two_225
                else:
                    print(one_255, end="")
                    returnString+=one_255
            print()
            returnString+="\n"
        return returnString
