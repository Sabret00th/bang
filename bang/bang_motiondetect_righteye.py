'''
Thanks to
http://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/


fixes 2/1/2016

needed to 
pip install imutils


also, as a result of using OpenCV3
had to add a third variable for the retu4rn of cv2.findContours

'''

# import the necessary packages
import argparse
import datetime
import imutils
import time
import cv2

# config frame and perceptual parameters


#natural log of 255 is 5.54
frame_w = 399
upper_thresh = 157.60 #is 255 divided by 1.618
lower_thresh = 97.40 #is upper_thresh divided by 1.618

min_obj_size = (frame_w *.0975)**2
max_obj_size = (frame_w *.36)**2

 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=min_obj_size, help="minimum area size")
args = vars(ap.parse_args())
 
# if the video argument is None, then we are reading from webcam
if args.get("video", None) is None:
    camera = cv2.VideoCapture(1)
    time.sleep(0.25)
 
# otherwise, we are reading from a video file
else:
    camera = cv2.VideoCapture(args["video"])
 
# initialize the first frame in the video stream
firstFrame = None

# loop over the frames of the video with the conditional logic rather than absolute True
while True:
    
    # grab the current frame and initialize the occupied/unoccupied
    # text
    (grabbed, frame) = camera.read()
    text = "Unoccupied"
    # if the frame could not be grabbed, then we have reached the end of the video
    if not grabbed:
        break
        
    # resize the frame, convert it to grayscale, and blur it
    frame = imutils.resize(frame, width=frame_w)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    
	# if the first frame is None, initialize it
    if firstFrame is None:
        firstFrame = gray
        continue

        
    # compute the absolute difference between the current frame and
	# first frame
    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, lower_thresh, upper_thresh, cv2.THRESH_BINARY)[1]
    
	# dilate the thresholded image to fill in holes, then find contours
	# on thresholded image
    thresh = cv2.dilate(thresh, None, iterations=2)
    (_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,\
    cv2.CHAIN_APPROX_SIMPLE)
 
 
	# loop over the contours
    for c in cnts:
        #if the contour is too small, ignore it
        if cv2.contourArea(c) < min_obj_size:
            continue
        if cv2.contourArea(c) > max_obj_size:
           continue
		# compute the bounding box for the contour, draw it on the frame,
		# and update the text
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Occupied"
        
        
    # draw the text and timestamp on the frame
    cv2.putText(frame, "Room Status: {}".format(text), (10, 20),\
    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),\
    (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
 
	# show the frame and record if the user presses a key
    cv2.imshow("Security Feed", frame)
    cv2.imshow("Thresh", thresh)
    cv2.imshow("Frame Delta", frameDelta)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key is pressed, break from the loop
    if key == ord("q"):
        break  
    
    
# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()