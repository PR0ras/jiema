import cv2
import numpy as np
import zbar
from PIL import Image
import simple_get
# create a reader
scanner = zbar.ImageScanner()
# configure the reader
scanner.parse_config('enable')
# set the screen's word
font=cv2.FONT_HERSHEY_SIMPLEX
# open camera
camera=cv2.VideoCapture(1)
while True:
# grab the current frame
# get the video's everyone frame
    (grabbed, frame) = camera.read()

# check to see if we have reached the end of the video
    if not grabbed:
        break
# detect the simple_get  get the image by detect
    box = simple_get.detect(frame)
    #check
    if box != None:
        min=np.min(box,axis=0)
        max=np.max(box,axis=0)
    roi=frame[min[1]-10:max[1]+10,min[0]-10:max[0]+10]
    print roi.shape
    # make roi from hsv to rgb because grab only check rgb's image and pil image
    roi=cv2.cvtColor(roi,cv2.COLOR_BGR2RGB)
    pil= Image.fromarray(frame).convert('L')
    width, height = pil.size
    # change
    raw = pil.tostring()
    # wrap image data
    zarimage = zbar.Image(width, height, 'Y800', raw)
    # scan the image for barcodes
    scanner.scan(zarimage)
    # extract results
    for symbol in zarimage:
        # do something useful with results
        print 'decoded', symbol.type, 'symbol', '"%s"' %symbol.data
        cv2.drawContours(frame, [box], -1, (0, 255, 0), 2)
        cv2.putText(frame,symbol.data,(20,100),font,1,(0,255,0),4)
    # if a barcode was found, draw a bounding box on the frame
    # show the frame and record if the user presses a key
    cv2.imshow("Frame", frame)
    '''
    key = cv2.waitKey(1) & 0xFF
    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break
   '''
    # cleanup the camera and close any open windows
    camera.release()
    cv2.destroyAllWindows()
