# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyautogui
import pygetwindow
import re #get numbers from string
import PIL #save images
import time


if __name__ == '__main__':

    #define Variables
    prefferedWindowSize=(1301,849)
    applicationName="Hauppauge WinTV"
    
    #debugging
    foundLogo=r"screenshots\foundLogo.png"
    searchedRegion=r"screenshots\searchLogo.png"
    locatorPro7Logo='locators\pro7.png'

    #logovariables
    expectedMarginX=167
    exptecedMarginY=133
    squareSize=55

    #
    print(("Preffered Window Size: "+''.join(str(prefferedWindowSize))))

    #get Window Handle and Resize
    windowHandle = pyautogui.getWindowsWithTitle(applicationName)[0]
    windowHandle.size = prefferedWindowSize

    #print(windowHandle)


    #get Relative Window Position

    handleVariables=str(windowHandle).split(",")
    topLeftX=int(''.join(str(x) for x in re.findall('[0-9]+', str(handleVariables[0].split(" ")[1]))))
    print("left: "+str(topLeftX))
    topLeftY=int(''.join(str(x) for x in re.findall('[0-9]+', str(handleVariables[1]))))
    print("top: "+str(topLeftY))
    width=int(''.join(str(x) for x in re.findall('[0-9]+', str(handleVariables[2]))))
    print("width: "+str(width))
    height=int(''.join(str(x) for x in re.findall('[0-9]+', str(handleVariables[3]))))
    print("height: "+str(height))

    #regionWholeScreen=region=(topLeftX,topLeftY, bottomRightX, bottomRightY)

    #image for whole screen
    #im1=pyautogui.screenshot(region=(topLeftX,topLeftY, bottomRightX, bottomRightY))

    #image for logo detection
    #im1=pyautogui.screenshot(region=(topLeftX+900,topLeftY, bottomRightX, bottomRightY-700))

    #im1.save(r"C:\Users\Daniel\Documents\GitHub\masterthesispython\screenshots\test.png")



    searchLogoX1=topLeftX+width-expectedMarginX
    searchLogoY1=topLeftY+exptecedMarginY
    searchLogoX2=squareSize
    searchLogoY2=squareSize


    regionExpectedLogo=(searchLogoX1,searchLogoY1,searchLogoX2,searchLogoY2)
    print( regionExpectedLogo)

    #print(regionExpectedLogo)

    #regionExpectedLogo=(0,0,2000,2000)

    #number=0


    while 1:
        time.sleep(1)
        im1=pyautogui.screenshot(region=regionExpectedLogo)
        im1.save(searchedRegion)

        #location=pyautogui.locateOnScreen('locators\pro7.png',grayscale=True,confidence=0.7, region=(topLeftX,topLeftY, bottomRightX, bottomRightY))
        #location=pyautogui.locateOnScreen('locators\pro7.png',grayscale=True,confidence=0.3, region=(1223,115, 55, 55))
        location=pyautogui.locateOnScreen(locatorPro7Logo,grayscale=True,confidence=0.3, region=regionExpectedLogo)
        #print(location)

        #foundBox
        if location!=None:
            print("Programm!")
            im1=pyautogui.screenshot(region=(location[0],location[1], location[2], location[3]))
            im1.save(foundLogo)
            #extract metadata and add to csv
        else:
            print("Werbung!")
            #extract metadata and add to csv
        #number += 1



    #Box(left=1221, top=119, width=51, height=54)