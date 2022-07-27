#https://stackoverflow.com/questions/57224007/how-to-compute-the-delta-e-between-two-images-using-opencv
def deltaE(img1, img2,cv2,np):
    colorspace = cv2.COLOR_BGR2LAB
    # check the two images are of the same size, else resize the two images
    (h1, w1) = img1.shape[:2]
    (h2, w2) = img1.shape[:2]
    h, w = None, None
    # check the height
    if h1 > h2:
        h = h1
    else:
        h = h2
    #check the width
    if w1 > w2:
        w = w1
    else:
        w = w2
    
    img1 = cv2.resize(img1, (h,w))
    img2 = cv2.resize(img2, (h,w))
    # Convert BGR images to specified colorspace
    img1 = cv2.cvtColor(img1, colorspace)
    img2 = cv2.cvtColor(img2, colorspace)
    # compute the Euclidean distance with pixels of two images 
    return (np.sqrt(np.sum((img1 - img2) ** 2, axis=-1))/255.).mean()