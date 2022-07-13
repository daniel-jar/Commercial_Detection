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


def getExpectedLogoRegion(currentSelectedExpectedRegion,regionExpectedLogoLower,regionExpectedLogoNewsTime,regionExpectedLogoUpper,imageApplicationVideoStream,PICTURE_TV_LOGO,cv,np,FOUND_LOGO_LOCATION):

    logoIndicationBooleanSQDIFF, logoIndicationBooleanCCOEFF,resTM_CCOEFF_NORMED,resTM_SQDIFF_NORMED,imageExpectedLogo\
    = getLogoConfidence(regionExpectedLogoLower,imageApplicationVideoStream,PICTURE_TV_LOGO,cv,np,None)

    if  not(logoIndicationBooleanCCOEFF and logoIndicationBooleanSQDIFF):
        logoIndicationBooleanSQDIFF, logoIndicationBooleanCCOEFF,resTM_CCOEFF_NORMED,resTM_SQDIFF_NORMED,imageExpectedLogo\
        = getLogoConfidence(regionExpectedLogoNewsTime,imageApplicationVideoStream,PICTURE_TV_LOGO,cv,np,None)
    else:
        currentSelectedExpectedRegion=regionExpectedLogoLower

    if  not(logoIndicationBooleanCCOEFF and logoIndicationBooleanSQDIFF):
        logoIndicationBooleanSQDIFF, logoIndicationBooleanCCOEFF,resTM_CCOEFF_NORMED,resTM_SQDIFF_NORMED,imageExpectedLogo\
        = getLogoConfidence(regionExpectedLogoUpper,imageApplicationVideoStream,PICTURE_TV_LOGO,cv,np,None)   
    else:
        currentSelectedExpectedRegion=regionExpectedLogoNewsTime

    if  not(logoIndicationBooleanCCOEFF and logoIndicationBooleanSQDIFF):
        currentSelectedExpectedRegion=currentSelectedExpectedRegion
    else:
        currentSelectedExpectedRegion=regionExpectedLogoUpper

    return currentSelectedExpectedRegion,logoIndicationBooleanCCOEFF,logoIndicationBooleanSQDIFF