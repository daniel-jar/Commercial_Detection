def SIFT_RATIO(img1,img2,np,cv2):
    # Initiate SURF detector
    #surf=cv2.xfeatures2d.SURF_create()
    surf=cv2.SIFT_create() 

    # find the keypoints and descriptors with SURF
    kp1, des1 = surf.detectAndCompute(img1,None)
    kp2, des2 = surf.detectAndCompute(img2,None)

    # BFMatcher with default params
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2, k=2)

    # Apply ratio test
    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])
            a=len(good)
            percent=(a*100)/len(kp2)
            return percent