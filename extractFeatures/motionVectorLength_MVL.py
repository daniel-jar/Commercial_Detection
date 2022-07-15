from logging import currentframe
from regex import R


def lucas_kanade_method_mvl(new_frame,prev_frame,cv2,np):
    # Parameters for ShiTomasi corner detection
    try:
        feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)

        # Parameters for Lucas Kanade optical flow
        lk_params = dict(
            winSize=(15, 15),
            maxLevel=2,
            criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03),
        )

        # Create random colors
        color = np.random.randint(0, 255, (100, 3))

        old_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
        p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

        frame_gray = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)

        # Calculate Optical Flow
        p1, st, err = cv2.calcOpticalFlowPyrLK(
            old_gray, frame_gray, p0, None, **lk_params
        )
        # Select good points
        good_new = p1[st == 1]
        good_old = p0[st == 1]

        diffs = good_new - good_old
        return [np.sum(diffs),np.sum(np.absolute(diffs)).max()]
    except Exception as e: # work on python 3.x:
        print("mvl error")
        f = open("logmvl.txt", "a")
        f.write(str(e)+"\n")
        f.write(str(prev_frame)+"\n")
        f.write(str(new_frame)+"\n")
        f.write(str(old_gray)+"\n")
        f.write(str(frame_gray)+"\n")
        f.close()
        return [0.0037703,0.0037703]
