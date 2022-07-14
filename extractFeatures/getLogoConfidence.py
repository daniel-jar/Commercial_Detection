def getLogoConfidence(currentSelectedExpectedRegion,imageApplicationVideoStream,PICTURE_TV_LOGO,cv,np,FOUND_LOGO_LOCATION):
        imageExpectedLogo = imageApplicationVideoStream.crop((currentSelectedExpectedRegion))
        imageExpectedLogoAsNumpy = cv.cvtColor(np.array(imageExpectedLogo), cv.COLOR_RGB2GRAY)
        resTM_SQDIFF_NORMED = cv.matchTemplate(imageExpectedLogoAsNumpy, PICTURE_TV_LOGO, cv.TM_SQDIFF_NORMED) #<0.4 quite represantive
        resTM_CCOEFF_NORMED = cv.matchTemplate(imageExpectedLogoAsNumpy, PICTURE_TV_LOGO, cv.TM_CCOEFF_NORMED) #>0.3 quite represantative
        logoIndicationBooleanSQDIFF = (resTM_SQDIFF_NORMED<=0.4) or (resTM_CCOEFF_NORMED>=0.9)
        logoIndicationBooleanCCOEFF = (resTM_CCOEFF_NORMED>=0.3) #or (resTM_SQDIFF_NORMED<=0.05).any()
        if FOUND_LOGO_LOCATION!=None:
            imageExpectedLogo.save(FOUND_LOGO_LOCATION)
        return logoIndicationBooleanCCOEFF,logoIndicationBooleanSQDIFF,resTM_CCOEFF_NORMED,resTM_SQDIFF_NORMED,imageExpectedLogo


def getExpectedLogoRegion(currentSelectedExpectedRegion,regionExpectedLogoLower,regionExpectedLogoNewsTime,regionExpectedLogoUpper,imageApplicationVideoStream,PICTURE_TV_LOGO,cv,np):
    selectedRegionInteger=-1
    logoIndicationBooleanSQDIFF, logoIndicationBooleanCCOEFF,resTM_CCOEFF_NORMED,resTM_SQDIFF_NORMED,imageExpectedLogo\
    = getLogoConfidence(regionExpectedLogoLower,imageApplicationVideoStream,PICTURE_TV_LOGO,cv,np,None)

    if  not(logoIndicationBooleanCCOEFF and logoIndicationBooleanSQDIFF):
        logoIndicationBooleanSQDIFF, logoIndicationBooleanCCOEFF,resTM_CCOEFF_NORMED,resTM_SQDIFF_NORMED,imageExpectedLogo\
        = getLogoConfidence(regionExpectedLogoNewsTime,imageApplicationVideoStream,PICTURE_TV_LOGO,cv,np,None)
    else:
        currentSelectedExpectedRegion=regionExpectedLogoLower
        selectedRegionInteger=1

    if  not(logoIndicationBooleanCCOEFF and logoIndicationBooleanSQDIFF):
        logoIndicationBooleanSQDIFF, logoIndicationBooleanCCOEFF,resTM_CCOEFF_NORMED,resTM_SQDIFF_NORMED,imageExpectedLogo\
        = getLogoConfidence(regionExpectedLogoUpper,imageApplicationVideoStream,PICTURE_TV_LOGO,cv,np,None)   
    else:
        currentSelectedExpectedRegion=regionExpectedLogoNewsTime
        selectedRegionInteger=2

    if  not(logoIndicationBooleanCCOEFF and logoIndicationBooleanSQDIFF):
        currentSelectedExpectedRegion=currentSelectedExpectedRegion
    else:
        currentSelectedExpectedRegion=regionExpectedLogoUpper
        selectedRegionInteger=0

    return currentSelectedExpectedRegion,selectedRegionInteger,logoIndicationBooleanCCOEFF,logoIndicationBooleanSQDIFF

def getRegions(width,EXPECTED_MARGIN_X,EXPECTED_MARGIN_Y,LEFT_BORDER_MARGIN,TOP_BORDER_MARGIN,EXPECTED_LOWER_MARGIN,SIZE_OF_EXPECTED_LOGO_X,SIZE_OF_EXPECTED_LOGO_Y):
    #Calculate Region of proposed Logo
    print("\ncalculating offset for region of tv logo")
    searchLogoX1 = width-EXPECTED_MARGIN_X-LEFT_BORDER_MARGIN
    searchLogoY1 = EXPECTED_MARGIN_Y-TOP_BORDER_MARGIN
    searchLogoX2 = SIZE_OF_EXPECTED_LOGO_X+searchLogoX1
    searchLogoY2 = SIZE_OF_EXPECTED_LOGO_Y+searchLogoY1

    #regions for Logos
    regionExpectedLogoUpper=(searchLogoX1,searchLogoY1,searchLogoX2,searchLogoY2)
    regionExpectedLogoLower=(searchLogoX1,searchLogoY1+EXPECTED_LOWER_MARGIN,searchLogoX2,searchLogoY2+EXPECTED_LOWER_MARGIN)
    regionExpectedLogoNewsTime=(searchLogoX1,searchLogoY1,searchLogoX2,searchLogoY2)
    return regionExpectedLogoUpper,regionExpectedLogoLower,regionExpectedLogoNewsTime

def getRegionsPYAUTOGUI(topLeftX,topLeftY,width,SIZE_OF_EXPECTED_LOGO_X,SIZE_OF_EXPECTED_LOGO_Y,EXPECTED_MARGIN_X,EXPECTED_MARGIN_Y,EXPECTED_LOWER_MARGIN):
    #Calculate Region of proposed Logo
    print("\ncalculating offset for region of tv logo pyautogui")
    searchLogoX1=topLeftX+width-EXPECTED_MARGIN_X
    searchLogoY1=topLeftY+EXPECTED_MARGIN_Y
    searchLogoX2=SIZE_OF_EXPECTED_LOGO_X
    searchLogoY2=SIZE_OF_EXPECTED_LOGO_Y

    #regions for Logos
    regionExpectedLogoUpper=(searchLogoX1,searchLogoY1,searchLogoX2,searchLogoY2)
    regionExpectedLogoLower=(searchLogoX1,searchLogoY1+EXPECTED_LOWER_MARGIN,searchLogoX2,searchLogoY2+EXPECTED_LOWER_MARGIN)
    regionExpectedLogoNewsTime=(searchLogoX1,searchLogoY1,searchLogoX2,searchLogoY2)
    #import pyautogui
    #im1=pyautogui.screenshot(region=regionExpectedLogoUpperPYAUTOGUI)
    #im1.save("testingPyAutoGuiRegions.png")
    return regionExpectedLogoUpper,regionExpectedLogoLower,regionExpectedLogoNewsTime

def getRelativeWindowPosition(handleVariables,re):
    topLeftX=int(''.join(str(x) for x in re.findall('[0-9]+', str(handleVariables[0].split(" ")[1]))))
    print("\ntopleftX of tv application:: "+str(topLeftX))
    topLeftY=int(''.join(str(x) for x in re.findall('[0-9]+', str(handleVariables[1]))))
    print("topleftY of tv application:: "+str(topLeftY))
    width=int(''.join(str(x) for x in re.findall('[0-9]+', str(handleVariables[2]))))
    print("width of tv application: "+str(width))
    height=int(''.join(str(x) for x in re.findall('[0-9]+', str(handleVariables[3]))))
    print("height of tv application: "+str(height))
    return topLeftX,topLeftY,width,height

def getTVApplicationWithoutEdgesRegion(topLeftX,topLeftY,LEFT_BORDER_MARGIN,TOP_BORDER_MARGIN,width,height,RIGHT_BORDER_MARGIN,BOTTOM_BORDER_MARGIN):
    print("\ncalculating offset for region of video stream without borders")
    edgeTVAppX=topLeftX+LEFT_BORDER_MARGIN
    edgeTVAppY=topLeftY+TOP_BORDER_MARGIN
    edgeTVAPPwidth=topLeftX+width-RIGHT_BORDER_MARGIN
    edgeTVAPPheight=topLeftY+height-BOTTOM_BORDER_MARGIN
    regionTVApplicationFullScreenshot=(edgeTVAppX,edgeTVAppY,edgeTVAPPwidth,edgeTVAPPheight)
    return regionTVApplicationFullScreenshot,edgeTVAPPwidth,edgeTVAPPheight