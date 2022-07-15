SQDIFF_EDGE = 0.4
CCOEFF_CONFIDENT = 0.9
CCOEFF_EDGE = 0.5
SQDIFF_LIMIT = 1

#LOGO Upper
EXPECTED_MARGIN_X = 160
EXPECTED_MARGIN_Y = 70
SIZE_OF_EXPECTED_LOGO_X = 48
SIZE_OF_EXPECTED_LOGO_Y = 48

#LOGO Lower than usual
EXPECTED_LOWER_MARGIN_Y = 64

#LOGO Wider
EXPECTED_WIDER_LEFT_MARGIN_X = -23
EXPECTED_WIDER_LEFT_MARGIN_Y = 4
EXPECTED_WIDER_SIZE_MARGIN_X = 2
EXPECTED_WIDER_SIZE_MARGIN_Y = -8

#BORDEREDGES for Newstime
NEWSTIME_MARGIN_TOPLEFTX = 97
NEWSTIME_MARGIN_TOPLEFTY= 623
SIZE_OF_NEWSTIME_X = 20
SIZE_OF_NEWSTIME_Y = 20
NEWSTIME_MARGINS=[NEWSTIME_MARGIN_TOPLEFTX,NEWSTIME_MARGIN_TOPLEFTY,SIZE_OF_NEWSTIME_X,SIZE_OF_NEWSTIME_Y]

#BORDEREDGES for Picture without Appplication Borders
LEFT_BORDER_MARGIN = 9
TOP_BORDER_MARGIN = 33
RIGHT_BORDER_MARGIN = 10
BOTTOM_BORDER_MARGIN = 89

UPPER,LOWER,NEWSTIME,WIDER = 0,1,2,3
REGION_NAMES=["UPPER","LOWER","NEWSTIME","WIDER"]
CONFIDENCES = [0.3,0.3,0.7,0.3]

def getRegionNames():
    return REGION_NAMES

def getRegionIndexes():
    return UPPER,LOWER,NEWSTIME,WIDER

def debugMyRegions(regions,regionsPYAUTOGUI,imageApplicationVideoStream,pyautogui):
    for i in range(len(regions)):
        print("Taking Screenshot for Region: "+REGION_NAMES[i])
        selectedRegion = regions[i]
        selectedRegionPYAUTOGUI = regionsPYAUTOGUI[i]
        newimg = imageApplicationVideoStream.crop((selectedRegion))
        newimg.save("debugging/region"+REGION_NAMES[i]+".png")
        im1=pyautogui.screenshot(region=selectedRegionPYAUTOGUI)
        im1.save("debugging/regionPYAUTO"+REGION_NAMES[i]+".png")

def getLogoConfidence(currentSelectedExpectedRegion,imageApplicationVideoStream,PICTURE_TV_LOGO,cv,np,FOUND_LOGO_LOCATION):
        imageExpectedLogo = imageApplicationVideoStream.crop((currentSelectedExpectedRegion))
        imageExpectedLogoAsNumpy = cv.cvtColor(np.array(imageExpectedLogo), cv.COLOR_RGB2GRAY)
        resTM_SQDIFF_NORMED = cv.matchTemplate(imageExpectedLogoAsNumpy, PICTURE_TV_LOGO, cv.TM_SQDIFF_NORMED) #<0.4 quite represantive
        resTM_CCOEFF_NORMED = cv.matchTemplate(imageExpectedLogoAsNumpy, PICTURE_TV_LOGO, cv.TM_CCOEFF_NORMED) #>0.3 quite represantative
        logoIndicationBooleanSQDIFF = (resTM_SQDIFF_NORMED<=SQDIFF_EDGE) or (resTM_CCOEFF_NORMED>=CCOEFF_CONFIDENT)
        logoIndicationBooleanCCOEFF = (resTM_CCOEFF_NORMED>=CCOEFF_EDGE) and (resTM_SQDIFF_NORMED!=SQDIFF_LIMIT)
        if FOUND_LOGO_LOCATION!=None:
            imageExpectedLogo.save(FOUND_LOGO_LOCATION)
        # print(resTM_CCOEFF_NORMED)
        # print(resTM_SQDIFF_NORMED)
        return logoIndicationBooleanCCOEFF,logoIndicationBooleanSQDIFF,resTM_CCOEFF_NORMED,resTM_SQDIFF_NORMED,imageExpectedLogo


def getExpectedLogoRegion(regions,regionsPYAUTOGUI,imageApplicationVideoStream,LOGO_COLLECTION,cv,np):
    for i in range(len(regions)):
        print("Checking Logo in Other Region "+REGION_NAMES[i])
        selectedRegion = regions[i]
        currentSelectedExpectedRegion=regions[i]
        currentSelectedExpectedRegionPYAUTOGUI=regionsPYAUTOGUI[i]
        CURRENT_PICTURE_TV_LOGO=LOGO_COLLECTION[i]
        CONFIDENCE=CONFIDENCES[i]
        logoIndicationBooleanCCOEFF,logoIndicationBooleanSQDIFF,resTM_CCOEFF_NORMED,resTM_SQDIFF_NORMED,imageExpectedLogo\
         = getLogoConfidence(currentSelectedExpectedRegion,imageApplicationVideoStream,CURRENT_PICTURE_TV_LOGO,cv,np,None)
        if  (logoIndicationBooleanCCOEFF and logoIndicationBooleanSQDIFF):
            print("Stopping Logo Check")
            break
        else:
            #Use Upper as Default
            selectedRegion = regions[UPPER]
            currentSelectedExpectedRegion=regions[UPPER]
            currentSelectedExpectedRegionPYAUTOGUI=regionsPYAUTOGUI[UPPER]
            CURRENT_PICTURE_TV_LOGO=LOGO_COLLECTION[UPPER]
            CONFIDENCE=CONFIDENCES[UPPER]

    return currentSelectedExpectedRegion,currentSelectedExpectedRegionPYAUTOGUI,CURRENT_PICTURE_TV_LOGO,CONFIDENCE,(logoIndicationBooleanSQDIFF and logoIndicationBooleanCCOEFF) 

def getRegions(WIDTH):
    #Calculate Region of proposed Logo
    print("\ncalculating offset for region of tv logo")

    searchLogoX1 = WIDTH-EXPECTED_MARGIN_X-LEFT_BORDER_MARGIN
    searchLogoY1 = EXPECTED_MARGIN_Y-TOP_BORDER_MARGIN
    searchLogoX2 = SIZE_OF_EXPECTED_LOGO_X+searchLogoX1
    searchLogoY2 = SIZE_OF_EXPECTED_LOGO_Y+searchLogoY1

    #regions for Logos
    regionExpectedLogoUpper=(searchLogoX1,searchLogoY1,searchLogoX2,searchLogoY2)
    regionExpectedLogoLower=(searchLogoX1,searchLogoY1+EXPECTED_LOWER_MARGIN_Y,searchLogoX2,searchLogoY2+EXPECTED_LOWER_MARGIN_Y)
    regionExpectedLogoNewsTime=(NEWSTIME_MARGINS[0],NEWSTIME_MARGINS[1],NEWSTIME_MARGINS[0]+NEWSTIME_MARGINS[2],NEWSTIME_MARGINS[1]+NEWSTIME_MARGINS[3])
    regionExpectedLogoWide=(searchLogoX1+EXPECTED_WIDER_LEFT_MARGIN_X,searchLogoY1+EXPECTED_WIDER_LEFT_MARGIN_Y ,searchLogoX2+EXPECTED_WIDER_LEFT_MARGIN_X+EXPECTED_WIDER_SIZE_MARGIN_X,searchLogoY2+EXPECTED_WIDER_SIZE_MARGIN_Y+EXPECTED_WIDER_LEFT_MARGIN_Y)
    return [regionExpectedLogoUpper,regionExpectedLogoLower,regionExpectedLogoNewsTime,regionExpectedLogoWide]

def getRegionsPYAUTOGUI(APPLICATION_POSITION):
    #Calculate Region of proposed Logo 
    print("\ncalculating offset for region of tv logo pyautogui")
    TOP_LEFT_X = APPLICATION_POSITION[0]
    TOP_LEFT_Y = APPLICATION_POSITION[1]
    WIDTH = APPLICATION_POSITION[2]

    searchLogoX1=TOP_LEFT_X+WIDTH-EXPECTED_MARGIN_X
    searchLogoY1=TOP_LEFT_Y+EXPECTED_MARGIN_Y

    searchLogoX1NewsTime=TOP_LEFT_X+NEWSTIME_MARGINS[0]+LEFT_BORDER_MARGIN
    searchLogoY1NewsTime=TOP_LEFT_Y+NEWSTIME_MARGINS[1]+TOP_BORDER_MARGIN

    #regions for Logos
    regionExpectedLogoUpper=(searchLogoX1,searchLogoY1,SIZE_OF_EXPECTED_LOGO_X,SIZE_OF_EXPECTED_LOGO_Y)
    regionExpectedLogoLower=(searchLogoX1,searchLogoY1+EXPECTED_LOWER_MARGIN_Y,SIZE_OF_EXPECTED_LOGO_X,SIZE_OF_EXPECTED_LOGO_Y)
    regionExpectedLogoNewsTime=(searchLogoX1NewsTime,searchLogoY1NewsTime,NEWSTIME_MARGINS[2],NEWSTIME_MARGINS[3])
    regionExpectedLogoUpper=(searchLogoX1,searchLogoY1,SIZE_OF_EXPECTED_LOGO_X,SIZE_OF_EXPECTED_LOGO_Y)
    regionExpectedLogoWide=(searchLogoX1+EXPECTED_WIDER_LEFT_MARGIN_X,searchLogoY1+EXPECTED_WIDER_LEFT_MARGIN_Y,SIZE_OF_EXPECTED_LOGO_X+EXPECTED_WIDER_SIZE_MARGIN_X,SIZE_OF_EXPECTED_LOGO_Y+EXPECTED_WIDER_SIZE_MARGIN_Y)

    return [regionExpectedLogoUpper,regionExpectedLogoLower,regionExpectedLogoNewsTime,regionExpectedLogoWide]

def getRelativeWindowPosition(handleVariables,re):
    TOP_LEFT_X=int(''.join(str(x) for x in re.findall('[0-9]+', str(handleVariables[0].split(" ")[1]))))
    print("\nTOP_LEFT_X of tv application:: "+str(TOP_LEFT_X))
    TOP_LEFT_Y=int(''.join(str(x) for x in re.findall('[0-9]+', str(handleVariables[1]))))
    print("topleftY of tv application:: "+str(TOP_LEFT_Y))
    WIDTH=int(''.join(str(x) for x in re.findall('[0-9]+', str(handleVariables[2]))))
    print("WIDTH of tv application: "+str(WIDTH))
    HEIGHT=int(''.join(str(x) for x in re.findall('[0-9]+', str(handleVariables[3]))))
    print("HEIGHT of tv application: "+str(HEIGHT))
    return [TOP_LEFT_X,TOP_LEFT_Y,WIDTH,HEIGHT]

def getTVApplicationWithoutEdgesRegion(APPLICATION_POSITION):
    print("\ncalculating offset for region of video stream without borders")

    TOP_LEFT_X = APPLICATION_POSITION[0]
    TOP_LEFT_Y = APPLICATION_POSITION[1]
    WIDTH = APPLICATION_POSITION[2]
    HEIGHT = APPLICATION_POSITION[3]

    edgeTVAppX=TOP_LEFT_X+LEFT_BORDER_MARGIN
    edgeTVAppY=TOP_LEFT_Y+TOP_BORDER_MARGIN
    edgeTVAPPWIDTH=TOP_LEFT_X+WIDTH-RIGHT_BORDER_MARGIN
    edgeTVAPPHEIGHT=TOP_LEFT_Y+HEIGHT-BOTTOM_BORDER_MARGIN
    regionTVApplicationFullScreenshot=(edgeTVAppX,edgeTVAppY,edgeTVAPPWIDTH,edgeTVAPPHEIGHT)
    return regionTVApplicationFullScreenshot,edgeTVAPPWIDTH,edgeTVAPPHEIGHT

def getLogos(cv):
    #searchingForLogo
    PICTURE_TV_LOGO_UPPER = cv.imread("locators\pro7.png",cv.IMREAD_GRAYSCALE)
    #PICTURE_TV_LOGO_LOWER = cv.imread("locators\pro7_small.png",cv.IMREAD_GRAYSCALE)
    PICTURE_TV_LOGO_NEWSTIME = cv.imread("locators\pro7_newstime.png",cv.IMREAD_GRAYSCALE)
    PICTURE_TV_LOGO_WIDER = cv.imread("locators\pro7_gezerrt.png",cv.IMREAD_GRAYSCALE)
    PICTURE_TV_LOGO_LOWER = PICTURE_TV_LOGO_UPPER
    return [PICTURE_TV_LOGO_UPPER,PICTURE_TV_LOGO_LOWER,PICTURE_TV_LOGO_NEWSTIME,PICTURE_TV_LOGO_WIDER]