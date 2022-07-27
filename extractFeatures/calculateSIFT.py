def SIFT_RATIO(img1,img2,np,cv2):
    try:
        # Initiate SURF detector
        #surf=cv2.xfeatures2d.SURF_create()
        surf=cv2.SIFT_create() 

        # find the keypoints and descriptors with SURF
        kp1, des1 = surf.detectAndCompute(img1,None)
        kp2, des2 = surf.detectAndCompute(img2,None)
        if des2 is not None and des1 is not None and len(kp1)!=0 and len(kp2)!=0:
            if np.array_equal(des1,des2):
                return 1
            else:
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
        else:
            "SIFT Returning 0"
            return 0
    except Exception as e: # work on python 3.x:
            print("Sift detected Error")
            f = open("logsift.txt", "a")
            f.write(str(e)+"\n")
            f.write(str(img1)+"\n")
            f.write(str(img2)+"\n")
            f.write(str(des1)+"\n")
            f.write(str(des2)+"\n")
            f.close()
            return 0.0037703

            