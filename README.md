#Capturing Images and converting to video
 mkdir <trainingdatadir>
 cd <trainingdatadir>
 captureframe
 convertframe --dir=.
 frame2video

#Validating Mapping:
python verifyBundle.py

#Adjusting camera functions - Brightness, zoom, focus, etc, can be adjusted
#Good sample value for exposure
v4l2-ctl -c exposure_absolute=350

Display all controls: v4l2-ctl -L
Adjust Some Parameter:v4l2-ctl -c option=value