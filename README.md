#Capturing Images and converting to video

mkdir trainingdatadir

cd trainingdatadir

captureframe

convertframe --dir=.

frame2video

#Validating Mapping:

python verifyBundle.py

#Camera brightness, zoom, focus, etc, can be adjusted. Example for exposure

v4l2-ctl -c exposure_absolute=350

#General Camera Controls

Display all controls: v4l2-ctl -L

Adjust Some Parameter:v4l2-ctl -c option=value
 