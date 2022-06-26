# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyautogui
import pygetwindow
import re #get numbers from string
import PIL #save images
import time



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('GITLAB')
    print_hi(__name__)

    windowHandle = pyautogui.getWindowsWithTitle("Hauppauge WinTV")[0]
    print(windowHandle)
    windowHandle.size = (1344,849)
    handleVariables=str(windowHandle).split(",")


    topLeftX=int(''.join(str(x) for x in re.findall('[0-9]+', str(handleVariables[0].split(" ")[1]))))
    print(topLeftX)
    topLeftY=int(''.join(str(x) for x in re.findall('[0-9]+', str(handleVariables[1]))))
    print(topLeftY)
    bottomRightX=int(''.join(str(x) for x in re.findall('[0-9]+', str(handleVariables[2]))))
    print(bottomRightX)
    bottomRightY=int(''.join(str(x) for x in re.findall('[0-9]+', str(handleVariables[3]))))
    print(bottomRightY)

    region=(topLeftX+900,topLeftY, bottomRightX, bottomRightY-700)

    #image for whole screen
    #im1=pyautogui.screenshot(region=(topLeftX,topLeftY, bottomRightX, bottomRightY))

    #image for logo detection
    #im1=pyautogui.screenshot(region=(topLeftX+900,topLeftY, bottomRightX, bottomRightY-700))

    #im1.save(r"C:\Users\Daniel\Documents\GitHub\masterthesispython\screenshots\test.png")
    searchLogoX=1223
    searchLogoY=115
    searchLogoX2=55
    searchLogoY2=55

    number=0


    while number < 100:
        time.sleep(1)
        im1=pyautogui.screenshot(region=(searchLogoX,searchLogoY, searchLogoX2, searchLogoY2))
        im1.save(r"C:\Users\Daniel\Documents\GitHub\masterthesispython\screenshots\searchLogo.png")

        #location=pyautogui.locateOnScreen('locators\pro7.png',grayscale=True,confidence=0.7, region=(topLeftX,topLeftY, bottomRightX, bottomRightY))
        location=pyautogui.locateOnScreen('locators\pro7.png',grayscale=True,confidence=0.3, region=(1223,115, 55, 55))
        print(location)
        print(location!="None")

        print(location!=None)

        #foundBox
        if location!=None:
            im1=pyautogui.screenshot(region=(location[0],location[1], location[2], location[3]))
            im1.save(r"C:\Users\Daniel\Documents\GitHub\masterthesispython\screenshots\foundLogo.png")
        number += 1



    #Box(left=1221, top=119, width=51, height=54)