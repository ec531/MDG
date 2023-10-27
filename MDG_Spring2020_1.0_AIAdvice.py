 #!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.02), January 21, 2015, at 11:36
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import STARTED, NOT_STARTED, FINISHED  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import pandas as pd
from collections import Counter, defaultdict

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath('/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/'))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'MDG_Spring2020_1.0_AI_6'  # from the Builder filename that created this script
expInfo = {'participant':'','age':'','gender':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation
    
# Setup the Window
win = visual.Window(size=(1280, 800), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, units=u'pix'
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize global components for Experiment "Block Time"----------------------------------------------------------------------------------------------------------------------------------------------------------
phase=1
diagcond=1
block=0
score=0
costs=''


learningscore=''
learning1score=''
learning2score=''
learning3score=''
block1score=''
block2score=''
block3score=''
block4score=''
block5score=''
block6score=''

test1outcome=''
test2outcome=''
test3outcome=''
test4outcome=''
test1viewoutcome=''
test2viewoutcome=''
test3viewoutcome=''
test4viewoutcome=''
click1=''
click2=''
click3=''
click4=''
click1order=''
click2order=''
click3order=''
click4order=''
clicktime1=''
clicktime2=''
clicktime3=''
clicktime4=''
clicktime1global=''
clicktime2global=''
clicktime3global=''
clicktime4global=''
Totalclick=''
diseases=[('Metalytis'), ('Zymosis'), ('Gwaronia'),('Descolada')]
tests=[('MRI'), ('CAT'), ('XRAY'), ('LAB')]
tests_copy=[('MRI'), ('CAT'), ('XRAY'), ('LAB')]
locationsdummy=[1,2,3,4]
costsdummy=[1,2,3]
# EOIN
np.random.shuffle(diseases)
np.random.shuffle(tests)
np.random.shuffle(locationsdummy)
imagelocation1=''
imagelocation2=''
imagelocation3=''
imagelocation4=''
textlocation1=''
textlocation2=''
textlocation3=''
textlocation4=''
shape1delay=''
shape2delay=''
shape3delay=''
shape4delay=''
text1delay=''
text2delay=''
text3delay=''
text4delay=''
imagelocations=[(-730, 310),(730,310),(-730,-310),(730,-310)]
textlocations=[(-490,230),(490,230),(-490,-230),(490,-230)]
shapedelaytimes=[1.2,1.4,1.6,1.8]
textdelaytimes=[0.3,0.6,0.9,1.2]
Test1pics=''
Test2pics=''
Test3pics=''
Test4pics=''
GENpics=[('Images/fever.png'),('Images/rash.png'),('Images/migraine.png'),('Images/ache.png')]
GENpics_copy=[('Images/fever.png'),('Images/rash.png'),('Images/migraine.png'),('Images/ache.png')]
np.random.shuffle(GENpics)
MRIpics=[('Images/MRI - POS.png'),('Images/MRI - NEUT.png'),('Images/MRI - NEG.png')]
LABpics=[('Images/LAB - POS.png'),('Images/LAB - NEUT.png'),('Images/LAB - NEG.png')]
XRAYpics=[('Images/RAY - POS.png'),('Images/RAY - NEUT.png'),('Images/RAY - NEG.png')]
CATpics=[('Images/CAT - POS.png'),('Images/CAT - NEUT.png'),('Images/CAT - NEG.png')]
#EOIN
symptoms=[('fever'), ('rash'), ('migraine'),('ache')]

# Mapping shuffled test names to original test names
shuffled_to_original_tests = {original_test: shuffled_test for original_test, shuffled_test in zip(tests_copy, tests)}

# Scale factor
scale = 0.5

# Modify image locations
scaled_imagelocations = [(int(x * scale), int(y * scale)) for x, y in imagelocations]

# Modify text locations
scaled_textlocations = [(int(x * scale), int(y * scale)) for x, y in textlocations]

if locationsdummy[0]==1:
    imagelocation1=[-730,310]
    scaled_imagelocation1 = [int(x * scale) for x in imagelocation1]
    textlocation1=[-490,230]
    scaled_textlocation1 = [int(x * scale) for x in textlocation1]
    shape1delay=shapedelaytimes[0]
    text1delay=textdelaytimes[0]
elif locationsdummy[0]==2:
    imagelocation1=[730,310]
    scaled_imagelocation1 = [int(x * scale) for x in imagelocation1]
    textlocation1=[490,230]
    scaled_textlocation1 = [int(x * scale) for x in textlocation1]
    shape1delay=shapedelaytimes[1]
    text1delay=textdelaytimes[1]
elif locationsdummy[0]==3:
    imagelocation1=[-730,-310]
    scaled_imagelocation1 = [int(x * scale) for x in imagelocation1]
    textlocation1=[-490,-230]
    scaled_textlocation1 = [int(x * scale) for x in textlocation1]
    shape1delay=shapedelaytimes[2]
    text1delay=textdelaytimes[2]
else:
    imagelocation1=[730,-310]
    scaled_imagelocation1 = [int(x * scale) for x in imagelocation1]
    textlocation1=[490,-230]
    scaled_textlocation1 = [int(x * scale) for x in textlocation1]
    shape1delay=shapedelaytimes[3]
    text1delay=textdelaytimes[3]

if locationsdummy[1]==1:
    imagelocation2=[-730,310]
    scaled_imagelocation2 = [int(x * scale) for x in imagelocation2]
    textlocation2=[-490,230]
    scaled_textlocation2 = [int(x * scale) for x in textlocation2]
    shape2delay=shapedelaytimes[0]
    text2delay=textdelaytimes[0]
elif locationsdummy[1]==2:
    imagelocation2=[730,310]
    # Modify image location
    scaled_imagelocation2 = [int(x * scale) for x in imagelocation2]
    textlocation2=[490,230]
    # Modify text location
    scaled_textlocation2 = [int(x * scale) for x in textlocation2]
    shape2delay=shapedelaytimes[1]
    text2delay=textdelaytimes[1]
elif locationsdummy[1]==3:
    imagelocation2=[-730,-310]
    scaled_imagelocation2 = [int(x * scale) for x in imagelocation2]
    textlocation2=[-490,-230]
    scaled_textlocation2 = [int(x * scale) for x in textlocation2]
    shape2delay=shapedelaytimes[2]
    text2delay=textdelaytimes[2]
else:
    imagelocation2=[730,-310]
    scaled_imagelocation2 = [int(x * scale) for x in imagelocation2]
    textlocation2=[490,-230]
    scaled_textlocation2 = [int(x * scale) for x in textlocation2]
    shape2delay=shapedelaytimes[3]
    text2delay=textdelaytimes[3]

if locationsdummy[2]==1:
    imagelocation3=[-730,310]
    scaled_imagelocation3 = [int(x * scale) for x in imagelocation3]
    textlocation3=[-490,230]
    scaled_textlocation3 = [int(x * scale) for x in textlocation3]
    shape3delay=shapedelaytimes[0]
    text3delay=textdelaytimes[0]
elif locationsdummy[2]==2:
    imagelocation3=[730,310]
    scaled_imagelocation3 = [int(x * scale) for x in imagelocation3]
    textlocation3=[490,230]
    scaled_textlocation3 = [int(x * scale) for x in textlocation3]
    shape3delay=shapedelaytimes[1]
    text3delay=textdelaytimes[1]
elif locationsdummy[2]==3:
    imagelocation3=[-730,-310]
    scaled_imagelocation3 = [int(x * scale) for x in imagelocation3]
    textlocation3=[-490,-230]
    scaled_textlocation3 = [int(x * scale) for x in textlocation3]
    shape3delay=shapedelaytimes[2]
    text3delay=textdelaytimes[2]
else:
    imagelocation3=[730,-310]
    scaled_imagelocation3 = [int(x * scale) for x in imagelocation3]
    textlocation3=[490,-230]
    scaled_textlocation3 = [int(x * scale) for x in textlocation3]
    shape3delay=shapedelaytimes[3]
    text3delay=textdelaytimes[3]

if locationsdummy[3]==1:
    imagelocation4=[-730,310]
    scaled_imagelocation4 = [int(x * scale) for x in imagelocation4]
    textlocation4=[-490,230]
    scaled_textlocation4 = [int(x * scale) for x in textlocation4]
    shape4delay=shapedelaytimes[0]
    text4delay=textdelaytimes[0]
elif locationsdummy[3]==2:
    imagelocation4=[730,310]
    scaled_imagelocation3 = [int(x * scale) for x in imagelocation3]
    textlocation4=[490,230]
    scaled_textlocation4 = [int(x * scale) for x in textlocation4]
    shape4delay=shapedelaytimes[1]
    text4delay=textdelaytimes[1]
elif locationsdummy[3]==3:
    imagelocation4=[-730,-310]
    scaled_imagelocation3 = [int(x * scale) for x in imagelocation3]
    textlocation4=[-490,-230]
    scaled_textlocation4 = [int(x * scale) for x in textlocation4]
    shape4delay=shapedelaytimes[2]
    text4delay=textdelaytimes[2]
else:
    imagelocation4=[730,-310]
    scaled_imagelocation3 = [int(x * scale) for x in imagelocation3]
    textlocation4=[490,-230]
    scaled_textlocation4 = [int(x * scale) for x in textlocation4]
    shape4delay=shapedelaytimes[3]
    text4delay=textdelaytimes[3]

if tests[0]=='MRI':
    Test1pics=MRIpics
elif tests[0]=='LAB':
    Test1pics=LABpics
elif tests[0]=='XRAY': 
    Test1pics=XRAYpics
else:
    Test1pics=CATpics

if tests[1]=='MRI':
    Test2pics=MRIpics
elif tests[1]=='LAB':
    Test2pics=LABpics
elif tests[1]=='XRAY':
    Test2pics=XRAYpics
else:
    Test2pics=CATpics

if tests[2]=='MRI':
    Test3pics=MRIpics
elif tests[2]=='LAB':
    Test3pics=LABpics
elif tests[2]=='XRAY':
    Test3pics=XRAYpics
else:
    Test3pics=CATpics

if tests[3]=='MRI':
    Test4pics=MRIpics
elif tests[3]=='LAB':
    Test4pics=LABpics
elif tests[3]=='XRAY':
    Test4pics=XRAYpics
else:
    Test4pics=CATpics

# Initialize components for Routine "instructions1"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions1Clock = core.Clock()
backgroundinst1 = visual.ImageStim(win=win, name='backgroundinst1',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructions1.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)

# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
backgroundinst1.size = [new_width, new_height]

# Initialize components for Routine "instructions2"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions2Clock = core.Clock()
backgroundinst2 = visual.ImageStim(win=win, name='backgroundinst2',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructionsbackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1280, 800],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
dplinst2 = visual.ImageStim(win=win, name='dplinst2',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructions2.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
inst2pic = visual.ImageStim(win=win, name='inst2pic',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructions2.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
backgroundinst2.size = [new_width, new_height]
dplinst2.size = [new_width, new_height]
inst2pic.size = [new_width, new_height]

# Initialize components for Routine "instructions3"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions3Clock = core.Clock()
instbackground3 = visual.ImageStim(win=win, name='instbackground3',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructionsbackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
dplinst3 = visual.ImageStim(win=win, name='dplinst3',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructions3.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
inst3pic = visual.ImageStim(win=win, name='inst3pic',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructions3.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
instbackground3.size = [new_width, new_height]
dplinst3.size = [new_width, new_height]
inst3pic.size = [new_width, new_height]

#Initialize components for Routine "outcomes"
outcomesClock = core.Clock()
outcomesimage = visual.ImageStim(win=win, name='outcomesiamge',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/outcomes.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
outcomesimage.size = [new_width, new_height]

# Initialize components for Routine "instructions4.1"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions4Clock = core.Clock()
backgroundinst4 = visual.ImageStim(win=win, name='backgroundinst4',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructions4.1.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
backgroundinst4.size = [new_width, new_height]

# Initialize components for Routine "instructions4.2"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions42Clock = core.Clock()
backgroundinst42 = visual.ImageStim(win=win, name='backgroundinst4',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructions4.2.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
backgroundinst42.size = [new_width, new_height]

# Initialize components for Routine "instructions43"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions43Clock = core.Clock()
backgroundinst43 = visual.ImageStim(win=win, name='backgroundinst4',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructions4.3.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
backgroundinst43.size = [new_width, new_height]

# Initialize components for Routine "instructions5"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions5Clock = core.Clock()
backgroundinst5 = visual.ImageStim(win=win, name='backgroundinst5',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructionsbackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
dplinst5 = visual.ImageStim(win=win, name='dplinst5',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructions5.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
inst5pic = visual.ImageStim(win=win, name='inst5pic',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructions5.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
backgroundinst5.size = [new_width, new_height]
dplinst5.size = [new_width, new_height]
inst5pic.size = [new_width, new_height]

# Initialize components for Routine "instructions6"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions6Clock = core.Clock()
backgroundinst6 = visual.ImageStim(win=win, name='backgroundinst6',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructions6.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
backgroundinst6.size = [new_width, new_height]

# Initialize components for Routine "instructions7"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions7Clock = core.Clock()
instr7pic = visual.ImageStim(win=win, name='instr7pic',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructions7.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
instr7pic.size = [new_width, new_height]

# Initialize components for Routine "instructions8"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions8Clock = core.Clock()
backgroundinst8 = visual.ImageStim(win=win, name='backgroundinst8',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructionsbackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
dplinst8 = visual.ImageStim(win=win, name='dplinst8',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructions8.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
inst8pic = visual.ImageStim(win=win, name='inst8pic',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructions8.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
backgroundinst8.size = [new_width, new_height]
dplinst8.size = [new_width, new_height]
inst8pic.size = [new_width, new_height]

# Initialize components for Routine "start"----------------------------------------------------------------------------------------------------------------------------------------------------------
startClock = core.Clock()
startglow = visual.ImageStim(win=win, name='startglow',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/startglow.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
startpic = visual.ImageStim(win=win, name='startpic',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/start.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
# Original position and height
startcountdown_original_position = [550, -50]
startcountdown_original_height = 500
# Scale factor
scale_score = 0.5
# Modify position and height
startcountdown_scaled_position = [int(x * scale_score) for x in startcountdown_original_position]
startcountdown_scaled_height = int(startcountdown_original_height * scale_score)
startcountdown = visual.TextStim(win=win, ori=0, name='startcountdown',
    text=u'3',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=[550, -50], height=500,wrapWidth=None,
    color=u'#01FFFD', colorSpace=u'rgb', opacity=1,
    depth=-6.0)

# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
startglow.size = [new_width, new_height]
startpic.size = [new_width, new_height]
startcountdown.size = [new_width, new_height]

# Initialize components for Routine "loading"----------------------------------------------------------------------------------------------------------------------------------------------------------
loadingClock = core.Clock()
background = visual.ImageStim(win=win, name='background',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/TrialBackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
loadingpic = visual.ImageStim(win=win, name='loadingpic',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/loading.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
background.size = [new_width, new_height]
loadingpic.size = [new_width, new_height]

# Initialize components for Routine "trial"----------------------------------------------------------------------------------------------------------------------------------------------------------
mouse = event.Mouse(win=win)
# Original position and height
ScoreText_original_position = [0, -460]
ScoreText_original_height = 50
# Scale factor
scale_score = 0.67
# Modify position and height
ScoreText_scaled_position = [int(x * scale_score) for x in ScoreText_original_position]
ScoreText_scaled_height = int(ScoreText_original_height * scale_score)
ScoreText=visual.TextStim(win=win, ori=0, name='ScoreText',
    text=u'$%i' %(score),
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=ScoreText_scaled_position, height=ScoreText_scaled_height,wrapWidth=None,
    color=u'#FCC700', colorSpace=u'rgb', opacity=1,
    depth=-6.0)
click1=0
click2=0
click3=0
click4=0
totalclick=0
trialClock = core.Clock()
learningbackground = visual.ImageStim(win=win, name='learningbackground',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/learningbackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
trialbackground = visual.ImageStim(win=win, name='trialbackground',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/TrialBackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
diagnosis = visual.RatingScale(win=win, name='diagnosis', acceptPreText='SUBMIT', textSize=0.65,
    textColor='#00B7B5', marker=u'triangle', markerColor='#FCC700', markerExpansion=0, 
    size=0.87, textFont='BatmanForeverAlternate', pos=[0.0, 30.0], choices=[diseases[0], diseases[1], diseases[2],diseases[3]], 
    tickHeight=-1,depth=-1.0)
# Apply scaling to the original image position
scale_2 = 0.68
original_image_position = [0, 460]
scaled_image_position = [int(x * scale_2) for x in original_image_position]
# Create the GenImage object with the scaled position
GenImage=visual.ImageStim(win=win, name='GenImage', units=u'pix', 
    image=GENpics[0],mask=None,
    ori=0, pos=[scaled_image_position], size = [288, 72],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=False, depth=-11.0)
# Modify image location
scaled_imagelocation1 = [int(x * scale) for x in imagelocation1]
Test1Image=visual.ImageStim(win=win, name='TLImage',units=u'pix', 
    image=Test1pics[0], mask=None,
    ori=0, pos=scaled_imagelocation1, size=[310, 310],
    color=[1,1,1], colorSpace=u'rgb', opacity=0,
    texRes=128, interpolate=False, depth=-10.0)
Test1Text=visual.TextStim(win=win, ori=0, name='TLText',
    text=tests[0],
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=textlocation1, height=35,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-6.0)
# Modify image location
scaled_imagelocation2 = [int(x * scale) for x in imagelocation2]
Test2Image=visual.ImageStim(win=win, name='TLImage',units=u'pix', 
    image=Test2pics[0], mask=None,
    ori=0, pos=scaled_imagelocation2, size=[310, 310],
    color=[1,1,1], colorSpace=u'rgb', opacity=0,
    texRes=128, interpolate=False, depth=-10.0)
Test2Text=visual.TextStim(win=win, ori=0, name='TRText',
    text=tests[1],
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=textlocation2, height=35,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-7.0)
# Modify image location
scaled_imagelocation3 = [int(x * scale) for x in imagelocation3]
Test3Image=visual.ImageStim(win=win, name='TLImage',units=u'pix', 
    image=Test3pics[0], mask=None,
    ori=0, pos=scaled_imagelocation3, size=[310, 310],
    color=[1,1,1], colorSpace=u'rgb', opacity=0,
    texRes=128, interpolate=False, depth=-10.0)
Test3Text=visual.TextStim(win=win, ori=0, name='BLText',
    text=tests[2],
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=textlocation3, height=35,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
# Modify image location
scaled_imagelocation4 = [int(x * scale) for x in imagelocation4]
Test4Image=visual.ImageStim(win=win, name='TLImage',units=u'pix', 
    image=Test4pics[0], mask=None,
    ori=0, pos=scaled_imagelocation4, size=[310, 310],
    color=[1,1,1], colorSpace=u'rgb', opacity=0,
    texRes=128, interpolate=False, depth=-10.0)
Test4Text=visual.TextStim(win=win, ori=0, name='BRText',
    text=tests[3],
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=textlocation4, height=35,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-9.0)
Test1Shape=visual.Circle(win, pos=scaled_imagelocation1, fillColor=u'#004646', lineColor=u'#004646',
    radius=150, units='pix')
Test2Shape=visual.Circle(win, pos=scaled_imagelocation2, fillColor=u'#004646', lineColor=u'#004646',
    radius=150, units='pix')
Test3Shape=visual.Circle(win, pos=scaled_imagelocation3, fillColor=u'#004646', lineColor=u'#004646',
    radius=150, units='pix')
Test4Shape=visual.Circle(win, pos=scaled_imagelocation4, fillColor=u'#004646', lineColor=u'#004646',
    radius=150, units='pix')
Random1Shape=visual.Circle(win, pos=scaled_imagelocation1, fillColor=u'#FCC700', lineColor=u'#FCC700',
    radius=150, units='pix')
Random2Shape=visual.Circle(win, pos=scaled_imagelocation2, fillColor=u'#FCC700', lineColor=u'#FCC700',
    radius=150, units='pix')
Random3Shape=visual.Circle(win, pos=scaled_imagelocation3, fillColor=u'#FCC700', lineColor=u'#FCC700',
    radius=150, units='pix')
Random4Shape=visual.Circle(win, pos=scaled_imagelocation4, fillColor=u'#FCC700', lineColor=u'#FCC700',
    radius=150, units='pix')
Cost1Text=visual.TextStim(win=win, ori=0, name='Cost1Text',
    text=u'',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=textlocation1, height=30,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-6.0)
Cost2Text=visual.TextStim(win=win, ori=0, name='Cost2Text',
    text=u'',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=textlocation2, height=30,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-6.0)
Cost3Text=visual.TextStim(win=win, ori=0, name='Cost3Text',
    text=u'',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=textlocation3, height=30,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-6.0)
Cost4Text=visual.TextStim(win=win, ori=0, name='Cost4Text',
    text=u'',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=textlocation4, height=30,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-6.0)

# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
new_width_2 = 288 // 1.5
new_height_2 = 72 // 1.5
scaled_position_GenImage = [int(x * scale) for x in GenImage.pos]
new_width_3 = 310 // 1.5
new_height_3 = 310 // 1.5
new_radius = 150 // 1.5
learningbackground.size = [new_width, new_height]
trialbackground.size = [new_width, new_height]
GenImage.size = [new_width_2, new_height_2]
Test1Image.size = [new_width_3, new_height_3]
Test2Image.size = [new_width_3, new_height_3]
Test3Image.size = [new_width_3, new_height_3]
Test4Image.size = [new_width_3, new_height_3]
Test1Shape.radius = [new_radius]
Test2Shape.radius = [new_radius]
Test3Shape.radius = [new_radius]
Test4Shape.radius = [new_radius]
Random1Shape.radius = [new_radius]
Random2Shape.radius = [new_radius]
Random3Shape.radius = [new_radius]
Random4Shape.radius = [new_radius]

# Eoin
# AI prompt to user
PromptTextAI = visual.TextStim(win=win, name='PromptTextAI',
    text=u'',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=(0, 175),height=15,wrapWidth=None, color=u'#FCC700', colorSpace=u'rgb', opacity=1,
    depth=-6.0)

PromptTextAdvice = visual.TextStim(win=win, name='PromptTextAdvice',
    text=u'',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=(0, 150),height=15,wrapWidth=None, color=u'#FCC700', colorSpace=u'rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "feedback"----------------------------------------------------------------------------------------------------------------------------------------------------------
feedbackClock = core.Clock()
Correct=''
DiseaseState=''
backgroundfeedback = visual.ImageStim(win=win, name='backgroundfeedback',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/TrialBackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
# Original position and height
Result_original_position = [0, -50]
Result_original_height = 25
# Scale factor
scale = 0.5
# Modify position and height
Result_scaled_position = [int(x * scale) for x in Result_original_position]
Result_scaled_height = int(Result_original_height * scale)
Result=visual.TextStim(win=win, ori=0, name='Result',
    text=u'Result:',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=Result_scaled_position, height=Result_scaled_height, wrapWidth=1280,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-1.0)
# Original position and height
Correct_Incorrect_original_position = [0, -90]
Correct_Incorrect_original_height = 70
# Scale factor
scale = 0.5
# Modify position and height
Correct_Incorrect_scaled_position = [int(x * scale) for x in Correct_Incorrect_original_position]
Correct_Incorrect_scaled_height = int(Correct_Incorrect_original_height * scale)
Correct_Incorrect=visual.TextStim(win=win, ori=0, name='Correct_Incorrect',
    text=u'Correct!',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=Correct_Incorrect_scaled_position, height=Correct_Incorrect_scaled_height,wrapWidth=None,
    color=u'#01FFFD', colorSpace=u'rgb', opacity=1,
    depth=0.0)
# Original position and height
YourResponseText_original_position = [-180, 80]
YourResponseText_original_height = 25
# Scale factor
scale = 0.5
# Modify position and height
YourResponseText_scaled_position = [int(x * scale) for x in YourResponseText_original_position]
YourResponseText_scaled_height = int(YourResponseText_original_height * scale)
YourResponseText=visual.TextStim(win=win, ori=0, name='YourResponseText',
    text=u'Your diagnosis:',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=YourResponseText_scaled_position, height=YourResponseText_scaled_height,wrapWidth=1280,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-1.0)
# Original position and height
YourResponse_original_position = [-180, 50]
YourResponse_original_height = 40
# Scale factor
scale = 0.5
# Modify position and height
YourResponse_scaled_position = [int(x * scale) for x in YourResponse_original_position]
YourResponse_scaled_height = int(YourResponse_original_height * scale)
YourResponse=visual.TextStim(win=win, ori=0, name='YourResponse',
    text=u'',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=YourResponse_scaled_position, height=YourResponse_scaled_height, wrapWidth=1280,
    color=u'#01FFFD', colorSpace=u'rgb', opacity=1,
    depth=-1.0)
# Original position and height
AnswerWas_original_position = [180, 80]
AnswerWas_original_height = 25
# Scale factor
scale = 0.5
# Modify position and height
AnswerWas_scaled_position = [int(x * scale) for x in AnswerWas_original_position]
AnswerWas_scaled_height = int(AnswerWas_original_height * scale)
AnswerWas=visual.TextStim(win=win, ori=0, name='AnswerWas',
    text=u'Patient:',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=AnswerWas_scaled_position, height=AnswerWas_scaled_height, wrapWidth=1280,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-1.0)
# Original position and height
State_original_position = [180, 50]
State_original_height = 40
# Scale factor
scale = 0.5
# Modify position and height
State_scaled_position = [int(x * scale) for x in State_original_position]
State_scaled_height = int(State_original_height * scale)
State=visual.TextStim(win=win, ori=0, name='State',
    text=u'disease',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=State_scaled_position, height=State_scaled_height, wrapWidth=1280,
    color=u'#01FFFD', colorSpace=u'rgb', opacity=1,
    depth=-1.0)
# Original position and height
Press_original_position = [0, -360]
Press_original_height = 30
# Scale factor
scale = 0.5
# Modify position and height
Press_scaled_position = [int(x * scale) for x in Press_original_position]
Press_scaled_height = int(Press_original_height * scale)
Press=visual.TextStim(win=win, ori=0, name='Press',
    text=u'Press the SPACEBAR to continue.',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=Press_scaled_position, height=Press_scaled_height,wrapWidth=1280,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "timeup"----------------------------------------------------------------------------------------------------------------------------------------------------------
timeupClock = core.Clock()
timeupText = visual.TextStim(win=win, ori=0, name='Press',
    text=u'Time is up!',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=[0, 0], height=70,wrapWidth=1280,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)

#Initialize componenets for Routine "learningphaseend"
learningendClock= core.Clock()
learningphaseend = visual.ImageStim(win=win, name='background1phase2',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/learningphaseend.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
learningphaseend.size = [new_width, new_height]

#Initialize componenets for Routine "learningphasecompleted"
learningendClock= core.Clock()
learningphasecompleted = visual.ImageStim(win=win, name='background1phase2',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/learningphaseend.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
learningphasecompleted.size = [new_width, new_height]

#Initialize components for Routine "phase2instr1"
phase2instr1Clock = core.Clock()
background1phase2 = visual.ImageStim(win=win, name='background1phase2',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructions2phase2.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
background1phase2.size = [new_width, new_height]
# Original position and height
pricetext1_original_position = [-490,-230]
pricetext1_original_height = 35
# Scale factor
scale = 0.5
# Modify position and height
pricetext1_scaled_position = [int(x * scale) for x in pricetext1_original_position]
pricetext1_scaled_height = int(pricetext1_original_height * scale)
pricetext1 = visual.TextStim(win=win, ori=0, name='BLText',
    text=u'\n\n\n$250',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=pricetext1_scaled_position, height=pricetext1_scaled_height,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
# Original position and height
pricetext2_original_position = [-490,-230]
pricetext2_original_height = 35
# Scale factor
scale = 0.5
# Modify position and height
pricetext2_scaled_position = [int(x * scale) for x in pricetext2_original_position]
pricetext2_scaled_height = int(pricetext2_original_height * scale)
pricetext2 = visual.TextStim(win=win, ori=0, name='BLText',
    text=u'\n\n\n2.5 s',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=[490,-230], height=35,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
#Initialize component for Routine "phase2instr2"
phase2instr2Clock = core.Clock()
background2phase2 = visual.ImageStim(win=win, name='background1phase2',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructions2phase2.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
background2phase2.size = [new_width, new_height]
#Initialize component for Routine "phase2instr3"
phase2instr3Clock = core.Clock()
background3phase2 = visual.ImageStim(win=win, name='background1phase2',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructions3phase2.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
background3phase2.size = [new_width, new_height]
#Initialize component for Routine "phase2instr4"
phase2instr4Clock = core.Clock()
background4phase2 = visual.ImageStim(win=win, name='background4phase2',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructions3phase2.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
background4phase2.size = [new_width, new_height]
#Initialize componenets for Routine "btwrounds"
instructionsbtwroundsClock = core.Clock()
instructionsbtwrounds = visual.ImageStim(win=win, name='instructionsbtwrounds',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructionsbtwrounds.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
instructionsbtwrounds.size = [new_width, new_height]
#Initialize components for Routine "results"
resultsClock = core.Clock()
resultsbackground = visual.ImageStim(win=win, name='resultsbackground',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/results.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
resultsbackground.size = [new_width, new_height]
# Original position and height
learning1scoretext_original_position = [-285,410]
learning1scoretext_original_height = 35
# Scale factor
scale = 0.5
# Modify position and height
learning1scoretext_scaled_position = [int(x * scale) for x in learning1scoretext_original_position]
learning1scoretext_scaled_height = int(learning1scoretext_original_height * scale)
learning1scoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=learning1scoretext_scaled_position, height=learning1scoretext_scaled_height,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
# Original position and height
learning2scoretext_original_position = [-285,410]
learning2scoretext_original_height = 35
# Scale factor
scale = 0.5
# Modify position and height
learning2scoretext_scaled_position = [int(x * scale) for x in learning2scoretext_original_position]
learning2scoretext_scaled_height = int(learning2scoretext_original_height * scale)
learning2scoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=learning2scoretext_scaled_position, height=learning2scoretext_scaled_height,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
# Original position and height
learning3scoretext_original_position = [-285,410]
learning3scoretext_original_height = 35
# Scale factor
scale = 0.5
# Modify position and height
learning3scoretext_scaled_position = [int(x * scale) for x in learning3scoretext_original_position]
learning3scoretext_scaled_height = int(learning3scoretext_original_height * scale)
learning3scoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=learning3scoretext_scaled_position, height=learning3scoretext_scaled_height,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
# Original position and height
learningscoretext_original_position = [-285,420]
learningscoretext_original_height = 35
# Scale factor
scale = 0.65
# Modify position and height
learningscoretext_scaled_position = [int(x * scale) for x in learningscoretext_original_position]
learningscoretext_scaled_height = int(learningscoretext_original_height * scale)
learningscoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=learningscoretext_scaled_position, height=learningscoretext_original_height,wrapWidth=None,
    color=u'#FCC700', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
# Original position and height
round1scoretext_original_position = [-285,290]
round1scoretext_original_height = 35
# Scale factor
scale = 0.65
# Modify position and height
round1scoretext_scaled_position = [int(x * scale) for x in round1scoretext_original_position]
round1scoretext_scaled_height = int(round1scoretext_original_height * scale)
round1scoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=round1scoretext_scaled_position, height=round1scoretext_original_height,wrapWidth=None,
    color=u'#FCC700', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
# Original position and height
round2scoretext_original_position = [-285,175]
round2scoretext_original_height = 35
# Scale factor
scale = 0.65
# Modify position and height
round2scoretext_scaled_position = [int(x * scale) for x in round2scoretext_original_position]
round2scoretext_scaled_height = int(round2scoretext_original_height * scale)
round2scoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=round2scoretext_scaled_position, height=round2scoretext_original_height,wrapWidth=None,
    color=u'#FCC700', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
# Original position and height
round3scoretext_original_position = [-285,55]
round3scoretext_original_height = 35
# Scale factor
scale = 0.5
# Modify position and height
round3scoretext_scaled_position = [int(x * scale) for x in round3scoretext_original_position]
round3scoretext_scaled_height = int(round3scoretext_original_height * scale)
round3scoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=round3scoretext_scaled_position, height=round3scoretext_scaled_height,wrapWidth=None,
    color=u'#FCC700', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
# Original position and height
round4scoretext_original_position = [-285,60]
round4scoretext_original_height = 35
# Scale factor
scale = 0.5
# Modify position and height
round4scoretext_scaled_position = [int(x * scale) for x in round4scoretext_original_position]
round4scoretext_scaled_height = int(round4scoretext_original_height * scale)
round4scoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=round4scoretext_scaled_position, height=round4scoretext_scaled_height,wrapWidth=None,
    color=u'#FCC700', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
# Original position and height
round5scoretext_original_position = [-285,-175]
round5scoretext_original_height = 35
# Scale factor
scale = 0.5
# Modify position and height
round5scoretext_scaled_position = [int(x * scale) for x in round5scoretext_original_position]
round5scoretext_scaled_height = int(round5scoretext_original_height * scale)
round5scoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=round5scoretext_scaled_position, height=round5scoretext_scaled_height,wrapWidth=None,
    color=u'#FCC700', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
# Original position and height
round6scoretext_original_position = [-285,-290]
round6scoretext_original_height = 35
# Scale factor
scale = 0.5
# Modify position and height
round6scoretext_scaled_position = [int(x * scale) for x in round6scoretext_original_position]
round6scoretext_scaled_height = int(round6scoretext_original_height * scale)
round6scoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=round6scoretext_scaled_position, height=round6scoretext_scaled_height,wrapWidth=None,
    color=u'#FCC700', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
# Original position and height
topscoretext_original_position = [490,-180]
topscoretext_original_height = 35
# Scale factor
scale = 0.65
# Modify position and height
topscoretext_scaled_position = [int(x * scale) for x in topscoretext_original_position]
topscoretext_scaled_height = int(topscoretext_original_height * scale)
topscoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units=u'pix', pos=topscoretext_scaled_position, height=topscoretext_original_height,wrapWidth=None,
    color=u'#FCC700', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
#Initialize components for Routine "debrief"
debrief1Clock = core.Clock()
debrief2Clock = core.Clock()
goodbyeClock = core.Clock()
debriefimage1 = visual.ImageStim(win=win, name='debriefimage1',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/debrief1.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
debriefimage1.size = [new_width, new_height]
debriefimage2 = visual.ImageStim(win=win, name='debriefimage2',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/debrief2.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
debriefimage2.size = [new_width, new_height]
goodbye = visual.ImageStim(win=win, name='goodbye',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/goodbye.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
goodbye.size = [new_width, new_height]
goodbyeglow = visual.ImageStim(win=win, name='goodbyeglow',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/goodbyeglow.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
goodbyeglow.size = [new_width, new_height]
#Initialize components for Routine "readyforphase2"
instructions9 = visual.ImageStim(win=win, name='instructions9',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/Images/instructions9.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
# Rescale the image
new_width = 1920 // 1.5
new_height = 1080 // 1.5
instructions9.size = [new_width, new_height]

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
blockClock = core.Clock()

#_#START EXP###########################################################################################################################################################START EXP##################################################
#_#START EXP###########################################################################################################################################################START EXP##################################################
#_#START EXP###########################################################################################################################################################START EXP##################################################
#_#START EXP###########################################################################################################################################################START EXP##################################################
#_#START EXP###########################################################################################################################################################START EXP##################################################
#_#START EXP###########################################################################################################################################################START EXP##################################################
#_#START EXP###########################################################################################################################################################START EXP##################################################
#_#START EXP###########################################################################################################################################################START EXP##################################################
#_#START EXP###########################################################################################################################################################START EXP##################################################
#------Prepare to start Routine "instructions1"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
instructions1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
inst_key_resp_1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
inst_key_resp_1.status = NOT_STARTED
# keep track of which components have finished
instructions1Components = []
instructions1Components.append(backgroundinst1)
instructions1Components.append(inst_key_resp_1)
for thisComponent in instructions1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *backgroundinst1* updates
    if t >= 0.0 and backgroundinst1.status == NOT_STARTED:
        # keep track of start time/frame for later
        backgroundinst1.tStart = t  # underestimates by a little under one frame
        backgroundinst1.frameNStart = frameN  # exact frame index
        backgroundinst1.setAutoDraw(True)
    
    # *inst_key_resp_1* updates
    if t >= 0.0 and inst_key_resp_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_key_resp_1.tStart = t  # underestimates by a little under one frame
        inst_key_resp_1.frameNStart = frameN  # exact frame index
        inst_key_resp_1.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if inst_key_resp_1.status == STARTED:
        theseKeys = event.getKeys(keyList=['p'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instructions1"-------
for thisComponent in instructions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "instructions2"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
instructions2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
inst_key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
inst_key_resp_2.status = NOT_STARTED
# keep track of which components have finished
instructions2Components = []
instructions2Components.append(backgroundinst2)
instructions2Components.append(dplinst2)
instructions2Components.append(inst2pic)
instructions2Components.append(inst_key_resp_2)
for thisComponent in instructions2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *backgroundinst2* updates
    if t >= 0.0 and backgroundinst2.status == NOT_STARTED:
        # keep track of start time/frame for later
        backgroundinst2.tStart = t  # underestimates by a little under one frame
        backgroundinst2.frameNStart = frameN  # exact frame index
        backgroundinst2.setAutoDraw(True)
    
    # *dplinst2* updates
    if t >= 0.0 and dplinst2.status == NOT_STARTED:
        # keep track of start time/frame for later
        dplinst2.tStart = t  # underestimates by a little under one frame
        dplinst2.frameNStart = frameN  # exact frame index
        dplinst2.setAutoDraw(True)
    
    # *inst2pic* updates
    if t >= 0.0 and inst2pic.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst2pic.tStart = t  # underestimates by a little under one frame
        inst2pic.frameNStart = frameN  # exact frame index
        inst2pic.setAutoDraw(True)
    
    # *inst_key_resp_2* updates
    if t >= 0.0 and inst_key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_key_resp_2.tStart = t  # underestimates by a little under one frame
        inst_key_resp_2.frameNStart = frameN  # exact frame index
        inst_key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if inst_key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instructions2"-------
for thisComponent in instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "instructions3"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
instructions3Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
inst_key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
inst_key_resp_3.status = NOT_STARTED
# keep track of which components have finished
instructions3Components = []
instructions3Components.append(instbackground3)
instructions3Components.append(dplinst3)
instructions3Components.append(inst3pic)
instructions3Components.append(inst_key_resp_3)
for thisComponent in instructions3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions3"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instbackground3* updates
    if t >= 0.0 and instbackground3.status == NOT_STARTED:
        # keep track of start time/frame for later
        instbackground3.tStart = t  # underestimates by a little under one frame
        instbackground3.frameNStart = frameN  # exact frame index
        instbackground3.setAutoDraw(True)
    
    # *dplinst3* updates
    if t >= 0.0 and dplinst3.status == NOT_STARTED:
        # keep track of start time/frame for later
        dplinst3.tStart = t  # underestimates by a little under one frame
        dplinst3.frameNStart = frameN  # exact frame index
        dplinst3.setAutoDraw(True)
    
    # *inst3pic* updates
    if t >= 0.0 and inst3pic.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst3pic.tStart = t  # underestimates by a little under one frame
        inst3pic.frameNStart = frameN  # exact frame index
        inst3pic.setAutoDraw(True)
    
    # *inst_key_resp_3* updates
    if t >= 0.0 and inst_key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_key_resp_3.tStart = t  # underestimates by a little under one frame
        inst_key_resp_3.frameNStart = frameN  # exact frame index
        inst_key_resp_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if inst_key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instructions3"-------
for thisComponent in instructions3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "outcomes"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
outcomesClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
out_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
out_key_resp.status = NOT_STARTED
# keep track of which components have finished
outcomesComponents = []
outcomesComponents.append(outcomesimage)
outcomesComponents.append(out_key_resp)
for thisComponent in outcomesComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "outcomes"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = outcomesClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *outcomesimage* updates
    if t >= 0.0 and outcomesimage.status == NOT_STARTED:
        # keep track of start time/frame for later
        outcomesimage.tStart = t  # underestimates by a little under one frame
        outcomesimage.frameNStart = frameN  # exact frame index
        outcomesimage.setAutoDraw(True)
    
    # *out_key_resp* updates
    if t >= 0.0 and out_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        out_key_resp.tStart = t  # underestimates by a little under one frame
        out_key_resp.frameNStart = frameN  # exact frame index
        out_key_resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if out_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in outcomesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "outcomes"-------
for thisComponent in outcomesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "instructions4.1"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
instructions4Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
diagnosis.reset()
# keep track of which components have finished
instructions4Components = []
instructions4Components.append(backgroundinst4)
instructions4Components.append(diagnosis)
instructions4Components.append(GenImage)
for thisComponent in instructions4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions4"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *backgroundinst4* updates
    if t >= 0.0 and backgroundinst4.status == NOT_STARTED:
        # keep track of start time/frame for later
        backgroundinst4.draw()
        backgroundinst4.tStart = t  # underestimates by a little under one frame
        backgroundinst4.frameNStart = frameN  # exact frame index
    # *diagnosis* updates
    if t > 0.0:
        diagnosis.draw()
        continueRoutine = diagnosis.noResponse
        if diagnosis.noResponse == False:
            diagnosis.response = diagnosis.getRating()
            diagnosis.rt = diagnosis.getRT()
    # *GenImage* updates
    if t >= 0.0 and GenImage.status == NOT_STARTED:
        GenImage.tStart = t
        GenImage.frameNStart = frameN
        GenImage.setOpacity(1)
        GenImage.setAutoDraw(True)
        
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instructions4.1"-------
for thisComponent in instructions4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
Test1Image.setOpacity(0)
Test2Image.setOpacity(0)
Test3Image.setOpacity(0)
Test4Image.setOpacity(0)

#------Prepare to start Routine "instructions4.2"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
instructions42Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
diagnosis.reset()
# keep track of which components have finished
instructions42Components = []
instructions42Components.append(backgroundinst42)
instructions42Components.append(diagnosis)
instructions42Components.append(Test1Image)
instructions42Components.append(Test2Image)
instructions42Components.append(Test3Image)
instructions42Components.append(Test4Image)
instructions42Components.append(Test1Text)
instructions42Components.append(Test2Text)
instructions42Components.append(Test3Text)
instructions42Components.append(Test4Text)
for thisComponent in instructions42Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions4"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *backgroundinst42* updates
    if t >= 0.0 and backgroundinst42.status == NOT_STARTED:
        # keep track of start time/frame for later
        backgroundinst42.draw()
        backgroundinst42.tStart = t  # underestimates by a little under one frame
        backgroundinst42.frameNStart = frameN  # exact frame index
    # *diagnosis* updates
    if t > 0.0:
        diagnosis.draw()
        continueRoutine = diagnosis.noResponse
        if diagnosis.noResponse == False:
            diagnosis.response = diagnosis.getRating()
            diagnosis.rt = diagnosis.getRT()
    # *Test2Text* updates
    if t >= 0.0 and Test2Text.status == NOT_STARTED:
        Test2Text.tStart = t
        Test2Text.frameNStart = frameN
        Test2Text.setAutoDraw(True)
    # *Test3Text* updates
    if t >= 0.0 and Test3Text.status == NOT_STARTED:
        Test3Text.tStart = t
        Test3Text.frameNStart = frameN
        Test3Text.setAutoDraw(True)
    # *Test4Text* updates
    if t >= 0.0 and Test4Text.status == NOT_STARTED:
        Test4Text.tStart = t
        Test4Text.frameNStart = frameN
        Test4Text.setAutoDraw(True)
    # *Test1Text* updates
    if t >= 0.0 and Test1Text.status == NOT_STARTED:
        Test1Text.tStart = t
        Test1Text.frameNStart = frameN
        Test1Text.setAutoDraw(True)
    # *Test1Image* updates
    if t >= 1.0 and Test1Image.status == NOT_STARTED:
        Test1Image.tStart = t
        Test1Image.frameNStart = frameN
        Test1Image.setOpacity(1)
        Test1Image.setAutoDraw(True)
    # *Test2Image* updates
    if t >= 1.0 and Test2Image.status == NOT_STARTED:
        Test2Image.tStart = t
        Test2Image.frameNStart = frameN
        Test2Image.setOpacity(1)
        Test2Image.setAutoDraw(True)
    # *Test3Image* updates
    if t >= 1.0 and Test3Image.status == NOT_STARTED:
        Test3Image.tStart = t
        Test3Image.frameNStart = frameN
        Test3Image.setOpacity(1)
        Test3Image.setAutoDraw(True)
    # *Test4Image* updates
    if t >= 1.0 and Test4Image.status == NOT_STARTED:
        Test4Image.tStart = t
        Test4Image.frameNStart = frameN
        Test4Image.setOpacity(1)
        Test4Image.setAutoDraw(True)
        
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instructions4.2"-------
for thisComponent in instructions42Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
Test1Image.setOpacity(0)
Test2Image.setOpacity(0)
Test3Image.setOpacity(0)
Test4Image.setOpacity(0)

#------Prepare to start Routine "instructions4.3"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
instructions43Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
diagnosis.reset()
# keep track of which components have finished
instructions43Components = []
instructions43Components.append(backgroundinst4)
instructions43Components.append(diagnosis)
instructions43Components.append(Test1Image)
instructions43Components.append(Test2Image)
instructions43Components.append(Test3Image)
instructions43Components.append(Test4Image)
instructions43Components.append(Test1Text)
instructions43Components.append(Test2Text)
instructions43Components.append(Test3Text)
instructions43Components.append(Test4Text)
instructions43Components.append(GenImage)
for thisComponent in instructions43Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions4.3"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions43Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *backgroundinst4* updates
    if t >= 0.0 and backgroundinst43.status == NOT_STARTED:
        # keep track of start time/frame for later
        backgroundinst43.draw()
        backgroundinst43.tStart = t  # underestimates by a little under one frame
        backgroundinst43.frameNStart = frameN  # exact frame index
    # *diagnosis* updates
    if t > 0.0:
        diagnosis.draw()
        continueRoutine = diagnosis.noResponse
        if diagnosis.noResponse == False:
            diagnosis.response = diagnosis.getRating()
            diagnosis.rt = diagnosis.getRT()
    # *Test2Text* updates
    if t >= 0.0 and Test2Text.status == NOT_STARTED:
        Test2Text.tStart = t
        Test2Text.frameNStart = frameN
        Test2Text.setAutoDraw(True)
    # *Test3Text* updates
    if t >= 0.0 and Test3Text.status == NOT_STARTED:
        Test3Text.tStart = t
        Test3Text.frameNStart = frameN
        Test3Text.setAutoDraw(True)
    # *Test4Text* updates
    if t >= 0.0 and Test4Text.status == NOT_STARTED:
        Test4Text.tStart = t
        Test4Text.frameNStart = frameN
        Test4Text.setAutoDraw(True)
    # *Test1Text* updates
    if t >= 0.0 and Test1Text.status == NOT_STARTED:
        Test1Text.tStart = t
        Test1Text.frameNStart = frameN
        Test1Text.setAutoDraw(True)
    # *Test1Image* updates
    if t >= 1.0 and Test1Image.status == NOT_STARTED:
        Test1Image.tStart = t
        Test1Image.frameNStart = frameN
        Test1Image.setOpacity(1)
        Test1Image.setAutoDraw(True)
    # *Test2Image* updates
    if t >= 1.0 and Test2Image.status == NOT_STARTED:
        Test2Image.tStart = t
        Test2Image.frameNStart = frameN
        Test2Image.setOpacity(1)
        Test2Image.setAutoDraw(True)
    # *Test3Image* updates
    if t >= 1.0 and Test3Image.status == NOT_STARTED:
        Test3Image.tStart = t
        Test3Image.frameNStart = frameN
        Test3Image.setOpacity(1)
        Test3Image.setAutoDraw(True)
    # *Test4Image* updates
    if t >= 1.0 and Test4Image.status == NOT_STARTED:
        Test4Image.tStart = t
        Test4Image.frameNStart = frameN
        Test4Image.setOpacity(1)
        Test4Image.setAutoDraw(True)
    # *GenImage* updates
    if t >= 0.0 and GenImage.status == NOT_STARTED:
        GenImage.tStart = t
        GenImage.frameNStart = frameN
        GenImage.setOpacity(1)
        GenImage.setAutoDraw(True)
        
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions43Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instructions43"-------
for thisComponent in instructions43Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
Test1Image.setOpacity(0)
Test2Image.setOpacity(0)
Test3Image.setOpacity(0)
Test4Image.setOpacity(0)

#------Prepare to start Routine "instructions5"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
instructions5Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
inst_key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
inst_key_resp_5.status = NOT_STARTED
# keep track of which components have finished
instructions5Components = []
instructions5Components.append(backgroundinst5)
instructions5Components.append(dplinst5)
instructions5Components.append(inst5pic)
instructions5Components.append(inst_key_resp_5)
for thisComponent in instructions5Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions5"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *backgroundinst5* updates
    if t >= 0.0 and backgroundinst5.status == NOT_STARTED:
        # keep track of start time/frame for later
        backgroundinst5.tStart = t  # underestimates by a little under one frame
        backgroundinst5.frameNStart = frameN  # exact frame index
        backgroundinst5.setAutoDraw(True)
    
    # *dplinst5* updates
    if t >= 0.0 and dplinst5.status == NOT_STARTED:
        # keep track of start time/frame for later
        dplinst5.tStart = t  # underestimates by a little under one frame
        dplinst5.frameNStart = frameN  # exact frame index
        dplinst5.setAutoDraw(True)
    
    # *inst5pic* updates
    if t >= 0.0 and inst5pic.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst5pic.tStart = t  # underestimates by a little under one frame
        inst5pic.frameNStart = frameN  # exact frame index
        inst5pic.setAutoDraw(True)
    
    # *inst_key_resp_5* updates
    if t >= 0.0 and inst_key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_key_resp_5.tStart = t  # underestimates by a little under one frame
        inst_key_resp_5.frameNStart = frameN  # exact frame index
        inst_key_resp_5.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if inst_key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instructions5"-------
for thisComponent in instructions5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "instructions6"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
instructions6Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
diagnosis.reset()
# keep track of which components have finished
instructions6Components = []
instructions6Components.append(backgroundinst6)
instructions6Components.append(diagnosis)
instructions6Components.append(mouse)
instructions6Components.append(Test1Text)
instructions6Components.append(Test2Text)
instructions6Components.append(Test3Text)
instructions6Components.append(Test4Text)
instructions6Components.append(Test1Shape)
instructions6Components.append(Test2Shape)
instructions6Components.append(Test3Shape)
instructions6Components.append(Test4Shape)
instructions6Components.append(Random1Shape)
instructions6Components.append(Random2Shape)
instructions6Components.append(Random3Shape)
instructions6Components.append(Random4Shape)
instructions6Components.append(GenImage)
for thisComponent in instructions6Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions6"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *backgroundinst6* updates
    if t >= 0.0 and backgroundinst6.status == NOT_STARTED:
        # keep track of start time/frame for later
        backgroundinst6.draw()
        backgroundinst6.tStart = t  # underestimates by a little under one frame
        backgroundinst6.frameNStart = frameN  # exact frame index
    # *diagnosis* updates
    if t > 0.0:
        diagnosis.draw()
        continueRoutine = diagnosis.noResponse
        if diagnosis.noResponse == False:
            diagnosis.response = diagnosis.getRating()
            diagnosis.rt = diagnosis.getRT()
            
    # *GenImage* updates
    if t >= 0.0 and GenImage.status == NOT_STARTED:
        GenImage.tStart = t
        GenImage.frameNStart = frameN
        GenImage.setOpacity(1)
        GenImage.setAutoDraw(True)
        
    #*Test1Text* updates
    if t>=0.0 and Test1Text.status==NOT_STARTED:
        #keep track of start time/frame for later
        Test1Text.tStart=t#underestimates by a little under one frame
        Test1Text.frameNStart=frameN#exact frame index
        Test1Text.setAutoDraw(True)
    
    #*Test2Text* updates
    if t>=0.0 and Test2Text.status==NOT_STARTED:
        #keep track of start time/frame for later
        Test2Text.tStart=t#underestimates by a little under one frame
        Test2Text.frameNStart=frameN#exact frame index
        Test2Text.setAutoDraw(True)
    
    #*Test3Text* updates
    if t>=0.0 and Test3Text.status==NOT_STARTED:
        #keep track of start time/frame for later
        Test3Text.tStart=t#underestimates by a little under one frame
        Test3Text.frameNStart=frameN#exact frame index
        Test3Text.setAutoDraw(True)
    
    #*Test4Text* updates
    if t>=0.0 and Test4Text.status==NOT_STARTED:
        #keep track of start time/frame for later
        Test4Text.tStart=t#underestimates by a little under one frame
        Test4Text.frameNStart=frameN#exact frame index
        Test4Text.setAutoDraw(True)
    
    #*Random1Shape* updates
    if t>=0.0 and Random1Shape.status==NOT_STARTED:
        Random1Shape.tStart=t
        Random1Shape.frameNStart=frameN
        Random1Shape.setAutoDraw(False)
    
    #*Random2Shape* updates
    if t>=0.0 and Random2Shape.status==NOT_STARTED:
        Random2Shape.tStart=t
        Random2Shape.frameNStart=frameN
        Random2Shape.setAutoDraw(False)
    
    #*Random3Shape* updates
    if t>=0.0 and Random3Shape.status==NOT_STARTED:
        Random3Shape.tStart=t
        Random3Shape.frameNStart=frameN
        Random3Shape.setAutoDraw(False)
    
    #*Random4Shape* updates
    if t>=0.0 and Random4Shape.status==NOT_STARTED:
        Random4Shape.tStart=t
        Random4Shape.frameNStart=frameN
        Random4Shape.setAutoDraw(False)
    
    #*Test1Shape* updates
    if t>=0.0 and Test1Shape.status==NOT_STARTED:
        Test1Shape.tStart=t
        Test1Shape.frameNStart=frameN
        Test1Shape.setAutoDraw(True)
        Test1Shape.status=STARTED
    
    if Test1Shape.status==STARTED:
        if mouse.isPressedIn(Test1Shape) and click1<1:
            Test1Image.setAutoDraw(True)
            Test1Text.setColor(u'#FCC700')
            Cost1Text.setColor(u'#FCC700')
            Test1Shape.setAutoDraw(False)
            Test1Image.setOpacity(1)
            Random1Shape.setAutoDraw(True)
        
        if Test1Shape.contains(mouse):
            Random1Shape.setAutoDraw(True)
            Test1Shape.setOpacity(0)
        else:
            Random1Shape.setAutoDraw(False)
            Test1Shape.setOpacity(1)
    
    #*Test2Shape* updates
    if t>=0.0 and Test2Shape.status==NOT_STARTED:
        Test2Shape.tStart=t
        Test2Shape.frameNStart=frameN
        Test2Shape.setAutoDraw(True)
        Test2Shape.status=STARTED
    
    if Test2Shape.status==STARTED:
        if mouse.isPressedIn(Test2Shape) and click2<1:
            Test2Image.setAutoDraw(True)
            Test2Text.setColor(u'#FCC700')
            Cost2Text.setColor(u'#FCC700')
            Test2Shape.setAutoDraw(False)
            Test2Image.setOpacity(1)
            Random2Shape.setAutoDraw(True)

        if Test2Shape.contains(mouse):
            Random2Shape.setAutoDraw(True)
            Test2Shape.setOpacity(0)
        else:
            Random2Shape.setAutoDraw(False)
            Test2Shape.setOpacity(1)
    
    #*Test3Shape* updates
    if t>=0.0 and Test3Shape.status==NOT_STARTED:
        Test3Shape.tStart=t
        Test3Shape.frameNStart=frameN
        Test3Shape.setAutoDraw(True)
        Test3Shape.status=STARTED
    
    if Test3Shape.status==STARTED:
        if mouse.isPressedIn(Test3Shape) and click3<1:
            Test3Image.setAutoDraw(True)
            Test3Text.setColor(u'#FCC700')
            Cost3Text.setColor(u'#FCC700')
            Test3Shape.setAutoDraw(False)
            Test3Image.setOpacity(1)
            Random3Shape.setAutoDraw(True)

        if Test3Shape.contains(mouse):
            Random3Shape.setAutoDraw(True)
            Test3Shape.setOpacity(0)
        else:
            Random3Shape.setAutoDraw(False)
            Test3Shape.setOpacity(1)

    #*Test4Shape* updates
    if t>=0.0 and Test4Shape.status==NOT_STARTED:
        Test4Shape.tStart=t
        Test4Shape.frameNStart=frameN
        Test4Shape.setAutoDraw(True)
        Test4Shape.status=STARTED
    
    if Test4Shape.status==STARTED:
        if mouse.isPressedIn(Test4Shape) and click4<1:
            Test4Image.setAutoDraw(True)
            Test4Text.setColor(u'#FCC700')
            Cost4Text.setColor(u'#Fcc700')
            Test4Shape.setAutoDraw(False)
            Test4Image.setOpacity(1)
            Random4Shape.setAutoDraw(True)

        if Test4Shape.contains(mouse):
            Random4Shape.setAutoDraw(True)
            Test4Shape.setOpacity(0)
        else:
            Random4Shape.setAutoDraw(False)
            Test4Shape.setOpacity(1)
            
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instructions6"-------
for thisComponent in instructions6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
Test1Image.setOpacity(0)
Test2Image.setOpacity(0)
Test3Image.setOpacity(0)
Test4Image.setOpacity(0)
Test1Text.setColor(u'#004646')
Test2Text.setColor(u'#004646')
Test3Text.setColor(u'#004646')
Test4Text.setColor(u'#004646')
Cost1Text.setColor(u'#004646')
Cost2Text.setColor(u'#004646')
Cost3Text.setColor(u'#004646')
Cost4Text.setColor(u'#004646')
#------Prepare to start Routine "instructions7"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
instructions7Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
inst_key_resp_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
inst_key_resp_7.status = NOT_STARTED
# keep track of which components have finished
instructions7Components = []
instructions7Components.append(instr7pic)
instructions7Components.append(inst_key_resp_7)
for thisComponent in instructions7Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions7"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions7Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr7pic* updates
    if t >= 0.0 and instr7pic.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr7pic.tStart = t  # underestimates by a little under one frame
        instr7pic.frameNStart = frameN  # exact frame index
        instr7pic.setAutoDraw(True)
    
    # *inst_key_resp_7* updates
    if t >= 0.0 and inst_key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_key_resp_7.tStart = t  # underestimates by a little under one frame
        inst_key_resp_7.frameNStart = frameN  # exact frame index
        inst_key_resp_7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if inst_key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instructions7"-------
for thisComponent in instructions7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "instructions8"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
instructions8Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
inst_key_resp_8 = event.BuilderKeyResponse()  # create an object of type KeyResponse
inst_key_resp_8.status = NOT_STARTED
# keep track of which components have finished
instructions8Components = []
instructions8Components.append(backgroundinst8)
instructions8Components.append(dplinst8)
instructions8Components.append(inst8pic)
instructions8Components.append(inst_key_resp_8)
for thisComponent in instructions8Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions8"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions8Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *backgroundinst8* updates
    if t >= 0.0 and backgroundinst8.status == NOT_STARTED:
        # keep track of start time/frame for later
        backgroundinst8.tStart = t  # underestimates by a little under one frame
        backgroundinst8.frameNStart = frameN  # exact frame index
        backgroundinst8.setAutoDraw(True)
    
    # *dplinst8* updates
    if t >= 0.0 and dplinst8.status == NOT_STARTED:
        # keep track of start time/frame for later
        dplinst8.tStart = t  # underestimates by a little under one frame
        dplinst8.frameNStart = frameN  # exact frame index
        dplinst8.setAutoDraw(True)
    
    # *inst8pic* updates
    if t >= 0.0 and inst8pic.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst8pic.tStart = t  # underestimates by a little under one frame
        inst8pic.frameNStart = frameN  # exact frame index
        inst8pic.setAutoDraw(True)
    
    # *inst_key_resp_8* updates
    if t >= 0.0 and inst_key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_key_resp_8.tStart = t  # underestimates by a little under one frame
        inst_key_resp_8.frameNStart = frameN  # exact frame index
        inst_key_resp_8.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if inst_key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instructions8"-------
for thisComponent in instructions8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "start"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
startClock.reset()  # clock 
frameN = -1
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
startComponents = []
startComponents.append(startpic)
startComponents.append(startcountdown)
startComponents.append(startglow)
startComponents.append(backgroundinst8)
for thisComponent in startComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "start"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = startClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *background* updates
    if t >= 0.0 and backgroundinst8.status == NOT_STARTED:
        # keep track of start time/frame for later
        backgroundinst8.tStart = t  # underestimates by a little under one frame
        backgroundinst8.frameNStart = frameN  # exact frame index
        backgroundinst8.setAutoDraw(True)
    # *startglow* updates
    if t >= 0.0 and startglow.status == NOT_STARTED:
        startglow.tStart = t
        startglow.frameNStart = frameN
        startglow.setAutoDraw(True)
    elif startglow.status == STARTED and t >= (0.0 + (3.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        startglow.setAutoDraw(False)
    startglow.setOpacity(0.6+(0.3*(cos(4*t+1.5))))
    # *startpic* updates
    if t >= 0.0 and startpic.status == NOT_STARTED:
        # keep track of start time/frame for later
        startpic.tStart = t  # underestimates by a little under one frame
        startpic.frameNStart = frameN  # exact frame index
        startpic.setAutoDraw(True)
    elif startpic.status == STARTED and t >= (0.0 + (3.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        startpic.setAutoDraw(False)
    
    # startcountdown* updates
    if t >= 0.0 and startcountdown.status == NOT_STARTED:
        startcountdown.tStart = t
        startcountdown.frameNstart = frameN
        startcountdown.setText('3')
        startcountdown.setAutoDraw(True)
    elif startcountdown.status == STARTED and t >= (0.0 + (3.0-win.monitorFramePeriod*0.75)):
        startcountdown.setAutoDraw(False)
        
    if t > 1.0:
        startcountdown.setText('2')
    if t > 2.0:
        startcountdown.setText('1')
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
Test1Image.setOpacity(0)
Test2Image.setOpacity(0)
Test3Image.setOpacity(0)
Test4Image.setOpacity(0)

#++Learning++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Learning3+++++++++++++++++++++++++++++++++++++++++++++
#++Learning++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Learning3+++++++++++++++++++++++++++++++++++++++++++++
#++Learning++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Learning3+++++++++++++++++++++++++++++++++++++++++++++
#++Learning++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Learning3+++++++++++++++++++++++++++++++++++++++++++++
#++Learning++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Learning3+++++++++++++++++++++++++++++++++++++++++++++
#++Learning++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Learning3+++++++++++++++++++++++++++++++++++++++++++++
#++Learning++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Learning3+++++++++++++++++++++++++++++++++++++++++++++
#++Learning++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Learning3+++++++++++++++++++++++++++++++++++++++++++++
#++Learning++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Learning3+++++++++++++++++++++++++++++++++++++++++++++
# set up handler to look after randomisation of conditions etc
learningtrials = data.TrialHandler(nReps=1, method=u'random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/ConditionsTest.xlsx'),
    seed=None, name='learningtrials')
thisExp.addLoop(learningtrials)  # add the loop to the experiment
blockClock.reset()
phase=1
block=0
costs=''
score=0
thisTrial = learningtrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec('{}=thisTrial[paramName]'.format(paramName))

for thisTrial in learningtrials:
    currentLoop = learningtrials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec('{}=thisTrial[paramName]'.format(paramName))
    #------Prepare to start Routine "loading"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    TrialResp=0
    CorrResp=0
    Correct=0
    Rand1=random()
    Rand2=random()
    Rand3=random()
    Rand4=random()
    CueRand=random()
    
    if DiseaseState==1:
        CorrResp=diseases[0]
        if CueRand <= 0.50:
            GenImage.setImage(GENpics[0])
            genoutcome=1
        elif CueRand <= 0.60:
            GenImage.setImage(GENpics[1])
            genoutcome=2
        elif CueRand <= 0.70:
            GenImage.setImage(GENpics[2])
            genoutcome=3
        else:
            GenImage.setImage(GENpics[3])
            genoutcome=4
        if Rand1 <= 0.90:
            Test1Image.setImage(Test1pics[0])
            test1outcome=3
        elif Rand1 <= 0.95:
            Test1Image.setImage(Test1pics[1])
            test1outcome=2
        else:
            Test1Image.setImage(Test1pics[2])
            test1outcome=1
        if Rand2 <= 0.05:
            Test2Image.setImage(Test2pics[0])
            test2outcome=3
        elif Rand2 <= 0.55:
            Test2Image.setImage(Test2pics[1])
            test2outcome=2
        else:
            Test2Image.setImage(Test2pics[2])
            test2outcome=1
        if Rand3 <= 0.05:
            Test3Image.setImage(Test3pics[0])
            test3outcome=3
        elif Rand3 <= 0.55:
            Test3Image.setImage(Test3pics[1])
            test3outcome=2
        else:
            Test3Image.setImage(Test3pics[2])
            test3outcome=1
        if Rand4 <= 0.05:
            Test4Image.setImage(Test4pics[0])
            test4outcome=3
        elif Rand4 <= 0.55:
            Test4Image.setImage(Test4pics[1])
            test4oucome=2
        else:
            Test4Image.setImage(Test4pics[2])
            test4outcome=1
    elif DiseaseState==2:
        CorrResp=diseases[1]
        if CueRand <= 0.30:
            GenImage.setImage(GENpics[0])
            genoutcome=1
        elif CueRand <= 0.80:
            GenImage.setImage(GENpics[1])
            genoutcome=2
        elif CueRand <= 0.90:
            GenImage.setImage(GENpics[2])
            genoutcome=3
        else:
            GenImage.setImage(GENpics[3])
            genoutcome=4
        if Rand1 <= 0.05:
            Test1Image.setImage(Test1pics[0])
            test1outcome=3
        elif Rand1 <= 0.55:
            Test1Image.setImage(Test1pics[1])
            test1outcome=2
        else:
            Test1Image.setImage(Test1pics[2])
            test1outcome=1
        if Rand2 <= 0.90:
            Test2Image.setImage(Test2pics[0])
            test2outcome=3
        elif Rand2 <= 0.95:
            Test2Image.setImage(Test2pics[1])
            test2outcome=2
        else:
            Test2Image.setImage(Test2pics[2])
            test2outcome=1
        if Rand3 <= 0.05:
            Test3Image.setImage(Test3pics[0])
            test3outcome=3
        elif Rand3 <= 0.55:
            Test3Image.setImage(Test3pics[1])
            test3outcome=2
        else:
            Test3Image.setImage(Test3pics[2])
            test3outcome=1
        if Rand4 <= 0.05:
            Test4Image.setImage(Test4pics[0])
            test4outcome=3
        elif Rand4 <= 0.55:
            Test4Image.setImage(Test4pics[1])
            test4outcome=2
        else:
            Test4Image.setImage(Test4pics[2])
            test4outcome=1
    elif DiseaseState==3:
        CorrResp=diseases[2]
        if CueRand <= 0.10:
            GenImage.setImage(GENpics[0])
            genoutcome=1
        elif CueRand <= 0.40:
            GenImage.setImage(GENpics[1])
            genoutcome=2
        elif CueRand <= 0.90:
            GenImage.setImage(GENpics[2])
            genoutcome=3
        else:
            GenImage.setImage(GENpics[3])
            genoutcome=4
        if Rand1 <= 0.05:
            Test1Image.setImage(Test1pics[0])
            test1outcome=3
        elif Rand1 <= 0.55:
            Test1Image.setImage(Test1pics[1])
            test1outcome=2
        else:
            Test1Image.setImage(Test1pics[2])
            test1outcome=1
        if Rand2 <= 0.05:
            Test2Image.setImage(Test2pics[0])
            test2outcome=3
        elif Rand2 <= 0.55:
            Test2Image.setImage(Test2pics[1])
            test2outcome=2
        else:
            Test2Image.setImage(Test2pics[2])
            test2outcome=1
        if Rand3 <= 0.90:
            Test3Image.setImage(Test3pics[0])
            test3outcome=3
        elif Rand3 <= 0.95:
            Test3Image.setImage(Test3pics[1])
            test3outcome=2
        else:
            Test3Image.setImage(Test3pics[2])
            test3outcome=1
        if Rand4 <= 0.05:
            Test4Image.setImage(Test4pics[0])
            test4outcome=3
        elif Rand4 <= 0.55:
            Test4Image.setImage(Test4pics[1])
            test4outcome=2
        else:
            Test4Image.setImage(Test4pics[2])
            test4outcome=1
    else:
        CorrResp=diseases[3]
        if CueRand <= 0.10:
            GenImage.setImage(GENpics[0])
            genoutcome=1
        elif CueRand <= 0.20:
            GenImage.setImage(GENpics[1])
            genoutcome=2
        elif CueRand <= 0.50:
            GenImage.setImage(GENpics[2])
            genoutcome=3
        else:
            GenImage.setImage(GENpics[3])
            genoutcome=4
        if Rand1 <= 0.05:
            Test1Image.setImage(Test1pics[0])
            test1outcome=3
        elif Rand1 <= 0.55:
            Test1Image.setImage(Test1pics[1])
            test1outcome=2
        else:
            Test1Image.setImage(Test1pics[2])
            test1outcome=1
        if Rand2 <= 0.05:
            Test2Image.setImage(Test2pics[0])
            test2outcome=3
        elif Rand2 <= 0.55:
            Test2Image.setImage(Test2pics[1])
            test2outcome=2
        else:
            Test2Image.setImage(Test2pics[2])
            test2outcome=1
        if Rand3 <= 0.05:
            Test3Image.setImage(Test3pics[0])
            test3outcome=3
        elif Rand3 <= 0.55:
            Test3Image.setImage(Test3pics[1])
            test3outcome=2
        else:
            Test3Image.setImage(Test3pics[2])
            test3outcome=1
        if Rand4 <= 0.90:
            Test4Image.setImage(Test4pics[0])
            test4outcome=3
        elif Rand4 <= 0.95:
            Test4Image.setImage(Test4pics[1])
            test4outcome=2
        else:
            Test4Image.setImage(Test4pics[2])
            test4outcome=1
    
    t = 0
    loadingClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    loadingComponents = []
    loadingComponents.append(learningbackground)
    loadingComponents.append(loadingpic)
    loadingComponents.append(Test1Text)
    loadingComponents.append(Test2Text)
    loadingComponents.append(Test3Text)
    loadingComponents.append(Test4Text)
    
    for thisComponent in loadingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "loading"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = loadingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *learningbackground* updates
        if t >= 0.0 and learningbackground.status == NOT_STARTED:
            # keep track of start time/frame for later
            learningbackground.tStart = t  # underestimates by a little under one frame
            learningbackground.frameNStart = frameN  # exact frame index
            learningbackground.setAutoDraw(True)
        elif learningbackground.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            learningbackground.setAutoDraw(False)
        
        # *loadingpic* updates
        if t >= 0.0 and loadingpic.status == NOT_STARTED:
            # keep track of start time/frame for later
            loadingpic.tStart = t  # underestimates by a little under one frame
            loadingpic.frameNStart = frameN  # exact frame index
            loadingpic.setAutoDraw(True)
        elif loadingpic.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            loadingpic.setAutoDraw(False)
        loadingpic.setOpacity(0.6+(0.3*(cos(4*t+1.5))))
        
        # *Test1Text* updates
        if t>=text1delay and Test1Text.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test1Text.tStart = t
            Test1Text.frameNStart = frameN
            Test1Text.setAutoDraw(True)
        elif Test1Text.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)):
            Test1Text.setAutoDraw(False)
            
        # *Test2Text* updates
        if t>=text2delay and Test2Text.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test2Text.tStart = t
            Test2Text.frameNStart = frameN
            Test2Text.setAutoDraw(True)
        elif Test2Text.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)):
            Test2Text.setAutoDraw(False)
            
        # *Test3Text* updates
        if t>=text3delay and Test3Text.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test3Text.tStart = t
            Test3Text.frameNStart = frameN
            Test3Text.setAutoDraw(True)
        elif Test3Text.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)):
            Test3Text.setAutoDraw(False)
            
        # *Test4Text* updates
        if t>=text4delay and Test4Text.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test4Text.tStart = t
            Test4Text.frameNStart = frameN
            Test4Text.setAutoDraw(True)
        elif Test4Text.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)):
            Test4Text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in loadingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
            
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "loading"-------
    for thisComponent in loadingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "trial"-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    diagnosis.reset()
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(learningbackground)
    trialComponents.append(mouse)
    trialComponents.append(ScoreText)
    trialComponents.append(diagnosis)
    trialComponents.append(Test1Text)
    trialComponents.append(Test2Text)
    trialComponents.append(Test3Text)
    trialComponents.append(Test4Text)
    trialComponents.append(Test1Image)
    trialComponents.append(Test2Image)
    trialComponents.append(Test3Image)
    trialComponents.append(Test4Image)
    trialComponents.append(GenImage)
    
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------

    # Mapping shuffled genoutcomes to original genoutcomes
    shuffled_to_original_genoutcomes = {original_genoutcome: shuffled_genoutcome for original_genoutcome, shuffled_genoutcome in zip(symptoms, GENpics)}

    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #*Mouse* updates
        if t>=0.0 and mouse.status==NOT_STARTED:
            mouse.tStart=t
            mouse.frameNStart=frameN
            
        # *learningbackground* updates
        if t >= 0.0 and learningbackground.status == NOT_STARTED:
            # keep track of start time/frame for later
            learningbackground.draw()
            learningbackground.tStart = t  # underestimates by a little under one frame
            learningbackground.frameNStart = frameN  # exact frame index
        
        # *diagnosis* updates
        if t > 0.0:
            diagnosis.draw()
            continueRoutine = diagnosis.noResponse
            if diagnosis.noResponse == False:
                diagnosis.response = diagnosis.getRating()
                diagnosis.rt = diagnosis.getRT()
                globaldiagnosistime= round(blockClock.getTime(), 3)
        
        #*ScoreText* updates
        if t>=0.0 and ScoreText.status==NOT_STARTED:
            #keep track of start time/frame for later
            ScoreText.tStart=t#underestimates by a little under one frame
            ScoreText.frameNStart=frameN#exact frame index
            ScoreText.setAutoDraw(True)
        
        #*Test1Text* updates
        if t>=0.0 and Test1Text.status==NOT_STARTED:
            #keep track of start time/frame for later
            Test1Text.tStart=t#underestimates by a little under one frame
            Test1Text.frameNStart=frameN#exact frame index
            Test1Text.setAutoDraw(True)
        
        #*Test2Text* updates
        if t>=0.0 and Test2Text.status==NOT_STARTED:
            #keep track of start time/frame for later
            Test2Text.tStart=t#underestimates by a little under one frame
            Test2Text.frameNStart=frameN#exact frame index
            Test2Text.setAutoDraw(True)
        
        #*Test3Text* updates
        if t>=0.0 and Test3Text.status==NOT_STARTED:
            #keep track of start time/frame for later
            Test3Text.tStart=t#underestimates by a little under one frame
            Test3Text.frameNStart=frameN#exact frame index
            Test3Text.setAutoDraw(True)
        
        #*Test4Text* updates
        if t>=0.0 and Test4Text.status==NOT_STARTED:
            #keep track of start time/frame for later
            Test4Text.tStart=t#underestimates by a little under one frame
            Test4Text.frameNStart=frameN#exact frame index
            Test4Text.setAutoDraw(True)
        
        #*GenImage* updates
        if t>=0.0 and GenImage.status==NOT_STARTED:
            #keep track of start time/frame for later
            GenImage.tStart=t#underestimates by a little under one frame
            GenImage.frameNStart=frameN#exact frame index
            GenImage.setAutoDraw(True)
        
        #*Test1Image* updates
        if t>=0.2 and Test1Image.status==NOT_STARTED:
            Test1Image.tStart=t
            Test1Image.frameNStart=frameN
            Test1Image.setOpacity(1)
            Test1Image.setAutoDraw(True)
        
        #*Test2Image* updates
        if t>=0.2 and Test2Image.status==NOT_STARTED:
            Test2Image.tStart=t
            Test2Image.frameNStart=frameN
            Test2Image.setOpacity(1)
            Test2Image.setAutoDraw(True)
        
        #*Test3Image* updates
        if t>=0.2 and Test3Image.status==NOT_STARTED:
            Test3Image.tStart=t
            Test3Image.frameNStart=frameN
            Test3Image.setOpacity(1)
            Test3Image.setAutoDraw(True)
        
        #*Test4Image* updates
        if t>=0.2 and Test4Image.status==NOT_STARTED:
            Test4Image.tStart=t
            Test4Image.frameNStart=frameN
            Test4Image.setOpacity(1)
            Test4Image.setAutoDraw(True)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

       # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
        
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    #------Prepare to start Routine "feedback"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    if CorrResp==diagnosis.response:
        Correct=1
    else:
        Correct=0
    YourResponse.setText(diagnosis.getRating())
    if Correct==1:
        Correct_Incorrect.setText('Correct!')
        score = score + 1000
    else:
        Correct_Incorrect.setText('Incorrect')
        score = score
    if DiseaseState==1:
        State.setText(diseases[0])
    elif DiseaseState==2:
        State.setText(diseases[1])
    elif DiseaseState==3:
        State.setText(diseases[2])
    else:
        State.setText(diseases[3])
    t = 0
    feedbackClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_2.status = NOT_STARTED
    # keep track of which components have finished
    feedbackComponents = []
    feedbackComponents.append(learningbackground)
    feedbackComponents.append(key_resp_2)
    feedbackComponents.append(Correct_Incorrect)
    feedbackComponents.append(YourResponse)
    feedbackComponents.append(YourResponseText)
    feedbackComponents.append(Press)
    feedbackComponents.append(ScoreText)
    feedbackComponents.append(AnswerWas)
    feedbackComponents.append(State)
    feedbackComponents.append(ScoreText)
    feedbackComponents.append(Result)
    feedbackComponents.append(Test1Image)
    feedbackComponents.append(Test2Image)
    feedbackComponents.append(Test3Image)
    feedbackComponents.append(Test4Image)
    feedbackComponents.append(GenImage)
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "feedback"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *learningbackground* updates
        if t >= 0.0 and learningbackground.status == NOT_STARTED:
            # keep track of start time/frame for later
            learningbackground.tStart = t  # underestimates by a little under one frame
            learningbackground.frameNStart = frameN  # exact frame index
            learningbackground.setAutoDraw(True)
        
        #GenImage* updates
        if t>=0.0 and GenImage.status==NOT_STARTED:
            GenImage.tStart=t
            GenImage.frameNStart=frameN
            GenImage.setAutoDraw(True)
        
        #*Test1Image* updates
        if t>=0.0 and Test1Image.status==NOT_STARTED:
            Test1Image.tStart=t
            Test1Image.frameNStart=frameN
            Test1Image.setOpacity(1)
            Test1Image.setAutoDraw(True)
        
        #*Test2Image* updates
        if t>=0.0 and Test2Image.status==NOT_STARTED:
            Test2Image.tStart=t
            Test2Image.frameNStart=frameN
            Test2Image.setOpacity(1)
            Test2Image.setAutoDraw(True)
        
        #*Test3Image* updates
        if t>=0.0 and Test3Image.status==NOT_STARTED:
            Test3Image.tStart=t
            Test3Image.frameNStart=frameN
            Test3Image.setOpacity(1)
            Test3Image.setAutoDraw(True)
        
        #*Test4Image* updates
        if t>=0.0 and Test4Image.status==NOT_STARTED:
            Test4Image.tStart=t
            Test4Image.frameNStart=frameN
            Test4Image.setOpacity(1)
            Test4Image.setAutoDraw(True)
        
        #*ScoreText* updates
        if t>=0.0 and ScoreText.status==NOT_STARTED:
            #keep track of start time/frame for later
            ScoreText.tStart=t#underestimates by a little under one frame
            ScoreText.frameNStart=frameN#exact frame index
            ScoreText.setAutoDraw(True)
        if trialClock.getTime()>0:
            ScoreText.setText("$%i" %(score))
        
        #*Result* updates
        if t>=0.0 and Result.status==NOT_STARTED:
            #keep track of start time/frame for later
            Result.tStart=t#underestimates by a little under one frame
            Result.frameNStart=frameN#exact frame index
            Result.setAutoDraw(True)
        
        #*Correct_Incorrect* updates
        if t>=0.0 and Correct_Incorrect.status==NOT_STARTED:
            #keep track of start time/frame for later
            Correct_Incorrect.tStart=t#underestimates by a little under one frame
            Correct_Incorrect.frameNStart=frameN#exact frame index
            Correct_Incorrect.setAutoDraw(True)
        
        #*YourResponse* updates
        if t>=0.0 and YourResponse.status==NOT_STARTED:
            #keep track of start time/frame for later
            YourResponse.tStart=t#underestimates by a little under one frame
            YourResponse.frameNStart=frameN#exact frame index
            YourResponse.setAutoDraw(True)
        
        #*YourResponseText* updates
        if t>=0.0 and YourResponseText.status==NOT_STARTED:
            #keep track of start time/frame for later
            YourResponseText.tStart=t#underestimates by a little under one frame
            YourResponseText.frameNStart=frameN#exact frame index
            YourResponseText.setAutoDraw(True)
        
        #*AnswerWas* updates
        if t>=0.0 and AnswerWas.status==NOT_STARTED:
            AnswerWas.tStart=t
            AnswerWas.frameNStart=frameN
            AnswerWas.setAutoDraw(True)
        
        #*State* updates
        if t>=0.0 and State.status==NOT_STARTED:
            State.tStart=t
            State.frameNStart=frameN
            State.setAutoDraw(True)
        
        #*Press* updates
        if t>=0.0 and Press.status==NOT_STARTED:
            #keep track of start time/frame for later
            Press.tStart=t#underestimates by a little under one frame
            Press.frameNStart=frameN#exact frame index
            Press.setAutoDraw(True)
            
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t  # underestimates by a little under one frame
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space']) # Check for 'space' key
            
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()

    #-------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # store data for trials (TrialHandler)
    learningtrials.addData('phase', phase)
    learningtrials.addData('diagcond', diagcond)
    learningtrials.addData('costs', costs)
    learningtrials.addData('block', block)
    learningtrials.addData('trial', learningtrials.thisTrialN+1)
    learningtrials.addData('diagnosis', diagnosis.getRating())
    learningtrials.addData('diagnosis.rt', diagnosis.getRT())
    learningtrials.addData('blockdiagnosis.rt', globaldiagnosistime)
    learningtrials.addData('diseasestate', CorrResp)
    learningtrials.addData('accuracy', Correct)
    learningtrials.addData('totalclick', totalclick)
    learningtrials.addData('click1.order', click1order)
    learningtrials.addData('click2.order', click2order)
    learningtrials.addData('click3.order', click3order)
    learningtrials.addData('click4.order', click4order)
    learningtrials.addData('click1', click1)
    learningtrials.addData('click2', click2)
    learningtrials.addData('click3', click3)
    learningtrials.addData('click4', click4)
    learningtrials.addData('click1.rt', clicktime1)
    learningtrials.addData('click2.rt', clicktime2)
    learningtrials.addData('click3.rt', clicktime3)
    learningtrials.addData('click4.rt', clicktime4)
    learningtrials.addData('score', score)
    learningtrials.addData('learningscore', learningscore)
    learningtrials.addData('block1score', block1score)
    learningtrials.addData('block2score', block2score)
    learningtrials.addData('test1outcome', test1outcome)
    learningtrials.addData('test2outcome', test2outcome)
    learningtrials.addData('test3outcome', test3outcome)
    learningtrials.addData('test4outcome', test4outcome)
    learningtrials.addData('genoutcome', genoutcome)
    learningtrials.addData('viewtest1outcome', test1viewoutcome)
    learningtrials.addData('viewtest2outcome', test2viewoutcome)
    learningtrials.addData('viewtest3outcome', test3viewoutcome)
    learningtrials.addData('viewtest4outcome', test4viewoutcome)
    thisExp.nextEntry()
    
# completed n repeats of 'trials'=============================================================================================================================================Learning3============================================
#==Learning==================================================================================================================================================================Learning3============================================
#==Learning==================================================================================================================================================================Learning3============================================
#==Learning==================================================================================================================================================================Learning3============================================
#==Learning==================================================================================================================================================================Learning3============================================
#==Learning==================================================================================================================================================================Learning3============================================
#==Learning==================================================================================================================================================================Learning3============================================
Test1Image.setOpacity(0)
Test2Image.setOpacity(0)
Test3Image.setOpacity(0)
Test4Image.setOpacity(0)

#------Prepare to start Routine "learningphaseend"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
learningendClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
inst_key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
inst_key_resp_2.status = NOT_STARTED
# keep track of which components have finished
learningendComponents = []
learningendComponents.append(learningphaseend)
learningendComponents.append(ScoreText)
learningendComponents.append(inst_key_resp_2)
for thisComponent in learningendComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "learningend"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = learningendClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *backgroundinst2* updates
    if t >= 0.0 and learningphaseend.status == NOT_STARTED:
        # keep track of start time/frame for later
        learningphaseend.tStart = t  # underestimates by a little under one frame
        learningphaseend.frameNStart = frameN  # exact frame index
        learningphaseend.setAutoDraw(True)
    
    # *ScoreText* updates
    if t >= 0.0 and ScoreText.status == NOT_STARTED:
        # keep track of start time/frame for later
        ScoreText.tStart = t  # underestimates by a little under one frame
        ScoreText.frameNStart = frameN  # exact frame index
        ScoreText.setAutoDraw(True)
        ScoreText.setText('$%i'%(score))
    
    
    # *inst_key_resp_2* updates
    if t >= 0.0 and inst_key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_key_resp_2.tStart = t  # underestimates by a little under one frame
        inst_key_resp_2.frameNStart = frameN  # exact frame index
        inst_key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if inst_key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learningendComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "learningend"-------
for thisComponent in learningendComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#++Learning2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Learning3+++++++++++++++++++++++++++++++++++++++++++++
#++Learning2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Learning3+++++++++++++++++++++++++++++++++++++++++++++
#++Learning2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Learning3+++++++++++++++++++++++++++++++++++++++++++++
#++Learning2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Learning3+++++++++++++++++++++++++++++++++++++++++++++
#++Learning2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Learning3+++++++++++++++++++++++++++++++++++++++++++++
#++Learning2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Learning3+++++++++++++++++++++++++++++++++++++++++++++
#++Learning2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Learning3+++++++++++++++++++++++++++++++++++++++++++++
#++Learning2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Learning3+++++++++++++++++++++++++++++++++++++++++++++
#++Learning2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Learning3+++++++++++++++++++++++++++++++++++++++++++++
# set up handler to look after randomisation of conditions etc
learningtrials = data.TrialHandler(nReps=1, method=u'random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/ConditionsTest.xlsx'),
    seed=None, name='learningtrials')
thisExp.addLoop(learningtrials)  # add the loop to the experiment
blockClock.reset()
phase=1
block=0.2
costs=''
score=0
thisTrial = learningtrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec('{}=thisTrial[paramName]'.format(paramName))

for thisTrial in learningtrials:
    currentLoop = learningtrials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec('{}=thisTrial[paramName]'.format(paramName))
    #------Prepare to start Routine "loading"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    TrialResp=0
    CorrResp=0
    Correct=0
    Rand1=random()
    Rand2=random()
    Rand3=random()
    Rand4=random()
    CueRand=random()
    
    if DiseaseState==1:
        CorrResp=diseases[0]
        if CueRand <= 0.50:
            GenImage.setImage(GENpics[0])
            genoutcome=1
        elif CueRand <= 0.60:
            GenImage.setImage(GENpics[1])
            genoutcome=2
        elif CueRand <= 0.70:
            GenImage.setImage(GENpics[2])
            genoutcome=3
        else:
            GenImage.setImage(GENpics[3])
            genoutcome=4
        if Rand1 <= 0.90:
            Test1Image.setImage(Test1pics[0])
            test1outcome=3
        elif Rand1 <= 0.95:
            Test1Image.setImage(Test1pics[1])
            test1outcome=2
        else:
            Test1Image.setImage(Test1pics[2])
            test1outcome=1
        if Rand2 <= 0.05:
            Test2Image.setImage(Test2pics[0])
            test2outcome=3
        elif Rand2 <= 0.55:
            Test2Image.setImage(Test2pics[1])
            test2outcome=2
        else:
            Test2Image.setImage(Test2pics[2])
            test2outcome=1
        if Rand3 <= 0.05:
            Test3Image.setImage(Test3pics[0])
            test3outcome=3
        elif Rand3 <= 0.55:
            Test3Image.setImage(Test3pics[1])
            test3outcome=2
        else:
            Test3Image.setImage(Test3pics[2])
            test3outcome=1
        if Rand4 <= 0.05:
            Test4Image.setImage(Test4pics[0])
            test4outcome=3
        elif Rand4 <= 0.55:
            Test4Image.setImage(Test4pics[1])
            test4oucome=2
        else:
            Test4Image.setImage(Test4pics[2])
            test4outcome=1
    elif DiseaseState==2:
        CorrResp=diseases[1]
        if CueRand <= 0.30:
            GenImage.setImage(GENpics[0])
            genoutcome=1
        elif CueRand <= 0.80:
            GenImage.setImage(GENpics[1])
            genoutcome=2
        elif CueRand <= 0.90:
            GenImage.setImage(GENpics[2])
            genoutcome=3
        else:
            GenImage.setImage(GENpics[3])
            genoutcome=4
        if Rand1 <= 0.05:
            Test1Image.setImage(Test1pics[0])
            test1outcome=3
        elif Rand1 <= 0.55:
            Test1Image.setImage(Test1pics[1])
            test1outcome=2
        else:
            Test1Image.setImage(Test1pics[2])
            test1outcome=1
        if Rand2 <= 0.90:
            Test2Image.setImage(Test2pics[0])
            test2outcome=3
        elif Rand2 <= 0.95:
            Test2Image.setImage(Test2pics[1])
            test2outcome=2
        else:
            Test2Image.setImage(Test2pics[2])
            test2outcome=1
        if Rand3 <= 0.05:
            Test3Image.setImage(Test3pics[0])
            test3outcome=3
        elif Rand3 <= 0.55:
            Test3Image.setImage(Test3pics[1])
            test3outcome=2
        else:
            Test3Image.setImage(Test3pics[2])
            test3outcome=1
        if Rand4 <= 0.05:
            Test4Image.setImage(Test4pics[0])
            test4outcome=3
        elif Rand4 <= 0.55:
            Test4Image.setImage(Test4pics[1])
            test4outcome=2
        else:
            Test4Image.setImage(Test4pics[2])
            test4outcome=1
    elif DiseaseState==3:
        CorrResp=diseases[2]
        if CueRand <= 0.10:
            GenImage.setImage(GENpics[0])
            genoutcome=1
        elif CueRand <= 0.40:
            GenImage.setImage(GENpics[1])
            genoutcome=2
        elif CueRand <= 0.90:
            GenImage.setImage(GENpics[2])
            genoutcome=3
        else:
            GenImage.setImage(GENpics[3])
            genoutcome=4
        if Rand1 <= 0.05:
            Test1Image.setImage(Test1pics[0])
            test1outcome=3
        elif Rand1 <= 0.55:
            Test1Image.setImage(Test1pics[1])
            test1outcome=2
        else:
            Test1Image.setImage(Test1pics[2])
            test1outcome=1
        if Rand2 <= 0.05:
            Test2Image.setImage(Test2pics[0])
            test2outcome=3
        elif Rand2 <= 0.55:
            Test2Image.setImage(Test2pics[1])
            test2outcome=2
        else:
            Test2Image.setImage(Test2pics[2])
            test2outcome=1
        if Rand3 <= 0.90:
            Test3Image.setImage(Test3pics[0])
            test3outcome=3
        elif Rand3 <= 0.95:
            Test3Image.setImage(Test3pics[1])
            test3outcome=2
        else:
            Test3Image.setImage(Test3pics[2])
            test3outcome=1
        if Rand4 <= 0.05:
            Test4Image.setImage(Test4pics[0])
            test4outcome=3
        elif Rand4 <= 0.55:
            Test4Image.setImage(Test4pics[1])
            test4outcome=2
        else:
            Test4Image.setImage(Test4pics[2])
            test4outcome=1
    else:
        CorrResp=diseases[3]
        if CueRand <= 0.10:
            GenImage.setImage(GENpics[0])
            genoutcome=1
        elif CueRand <= 0.20:
            GenImage.setImage(GENpics[1])
            genoutcome=2
        elif CueRand <= 0.50:
            GenImage.setImage(GENpics[2])
            genoutcome=3
        else:
            GenImage.setImage(GENpics[3])
            genoutcome=4
        if Rand1 <= 0.05:
            Test1Image.setImage(Test1pics[0])
            test1outcome=3
        elif Rand1 <= 0.55:
            Test1Image.setImage(Test1pics[1])
            test1outcome=2
        else:
            Test1Image.setImage(Test1pics[2])
            test1outcome=1
        if Rand2 <= 0.05:
            Test2Image.setImage(Test2pics[0])
            test2outcome=3
        elif Rand2 <= 0.55:
            Test2Image.setImage(Test2pics[1])
            test2outcome=2
        else:
            Test2Image.setImage(Test2pics[2])
            test2outcome=1
        if Rand3 <= 0.05:
            Test3Image.setImage(Test3pics[0])
            test3outcome=3
        elif Rand3 <= 0.55:
            Test3Image.setImage(Test3pics[1])
            test3outcome=2
        else:
            Test3Image.setImage(Test3pics[2])
            test3outcome=1
        if Rand4 <= 0.90:
            Test4Image.setImage(Test4pics[0])
            test4outcome=3
        elif Rand4 <= 0.95:
            Test4Image.setImage(Test4pics[1])
            test4outcome=2
        else:
            Test4Image.setImage(Test4pics[2])
            test4outcome=1

    t = 0
    loadingClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    loadingComponents = []
    loadingComponents.append(learningbackground)
    loadingComponents.append(loadingpic)
    loadingComponents.append(Test1Text)
    loadingComponents.append(Test2Text)
    loadingComponents.append(Test3Text)
    loadingComponents.append(Test4Text)
    
    for thisComponent in loadingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "loading"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = loadingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *learningbackground* updates
        if t >= 0.0 and learningbackground.status == NOT_STARTED:
            # keep track of start time/frame for later
            learningbackground.tStart = t  # underestimates by a little under one frame
            learningbackground.frameNStart = frameN  # exact frame index
            learningbackground.setAutoDraw(True)
        elif learningbackground.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            learningbackground.setAutoDraw(False)
        
        # *loadingpic* updates
        if t >= 0.0 and loadingpic.status == NOT_STARTED:
            # keep track of start time/frame for later
            loadingpic.tStart = t  # underestimates by a little under one frame
            loadingpic.frameNStart = frameN  # exact frame index
            loadingpic.setAutoDraw(True)
        elif loadingpic.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            loadingpic.setAutoDraw(False)
        loadingpic.setOpacity(0.6+(0.3*(cos(4*t+1.5))))
        
        # *Test1Text* updates
        if t>=text1delay and Test1Text.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test1Text.tStart = t
            Test1Text.frameNStart = frameN
            Test1Text.setAutoDraw(True)
        elif Test1Text.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)):
            Test1Text.setAutoDraw(False)
            
        # *Test2Text* updates
        if t>=text2delay and Test2Text.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test2Text.tStart = t
            Test2Text.frameNStart = frameN
            Test2Text.setAutoDraw(True)
        elif Test2Text.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)):
            Test2Text.setAutoDraw(False)
            
        # *Test3Text* updates
        if t>=text3delay and Test3Text.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test3Text.tStart = t
            Test3Text.frameNStart = frameN
            Test3Text.setAutoDraw(True)
        elif Test3Text.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)):
            Test3Text.setAutoDraw(False)
            
        # *Test4Text* updates
        if t>=text4delay and Test4Text.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test4Text.tStart = t
            Test4Text.frameNStart = frameN
            Test4Text.setAutoDraw(True)
        elif Test4Text.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)):
            Test4Text.setAutoDraw(False)
        
            
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in loadingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
            
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "loading"-------
    for thisComponent in loadingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "trial"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    diagnosis.reset()
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(learningbackground)
    trialComponents.append(mouse)
    trialComponents.append(ScoreText)
    trialComponents.append(diagnosis)
    trialComponents.append(Test1Text)
    trialComponents.append(Test2Text)
    trialComponents.append(Test3Text)
    trialComponents.append(Test4Text)
    trialComponents.append(Test1Image)
    trialComponents.append(Test2Image)
    trialComponents.append(Test3Image)
    trialComponents.append(Test4Image)
    trialComponents.append(GenImage)
    
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #*Mouse* updates
        if t>=0.0 and mouse.status==NOT_STARTED:
            mouse.tStart=t
            mouse.frameNStart=frameN
            
        # *learningbackground* updates
        if t >= 0.0 and learningbackground.status == NOT_STARTED:
            # keep track of start time/frame for later
            learningbackground.draw()
            learningbackground.tStart = t  # underestimates by a little under one frame
            learningbackground.frameNStart = frameN  # exact frame index
        
        # *diagnosis* updates
        if t > 0.0:
            diagnosis.draw()
            continueRoutine = diagnosis.noResponse
            if diagnosis.noResponse == False:
                diagnosis.response = diagnosis.getRating()
                diagnosis.rt = diagnosis.getRT()
                globaldiagnosistime= round(blockClock.getTime(), 3)
        
        #*ScoreText* updates
        if t>=0.0 and ScoreText.status==NOT_STARTED:
            #keep track of start time/frame for later
            ScoreText.tStart=t#underestimates by a little under one frame
            ScoreText.frameNStart=frameN#exact frame index
            ScoreText.setAutoDraw(True)
        
        #*Test1Text* updates
        if t>=0.0 and Test1Text.status==NOT_STARTED:
            #keep track of start time/frame for later
            Test1Text.tStart=t#underestimates by a little under one frame
            Test1Text.frameNStart=frameN#exact frame index
            Test1Text.setAutoDraw(True)
        
        #*Test2Text* updates
        if t>=0.0 and Test2Text.status==NOT_STARTED:
            #keep track of start time/frame for later
            Test2Text.tStart=t#underestimates by a little under one frame
            Test2Text.frameNStart=frameN#exact frame index
            Test2Text.setAutoDraw(True)
        
        #*Test3Text* updates
        if t>=0.0 and Test3Text.status==NOT_STARTED:
            #keep track of start time/frame for later
            Test3Text.tStart=t#underestimates by a little under one frame
            Test3Text.frameNStart=frameN#exact frame index
            Test3Text.setAutoDraw(True)
        
        #*Test4Text* updates
        if t>=0.0 and Test4Text.status==NOT_STARTED:
            #keep track of start time/frame for later
            Test4Text.tStart=t#underestimates by a little under one frame
            Test4Text.frameNStart=frameN#exact frame index
            Test4Text.setAutoDraw(True)
        
        #*GenImage* updates
        if t>=0.0 and GenImage.status==NOT_STARTED:
            #keep track of start time/frame for later
            GenImage.tStart=t#underestimates by a little under one frame
            GenImage.frameNStart=frameN#exact frame index
            GenImage.setAutoDraw(True)
        
        #*Test1Image* updates
        if t>=0.2 and Test1Image.status==NOT_STARTED:
            Test1Image.tStart=t
            Test1Image.frameNStart=frameN
            Test1Image.setOpacity(1)
            Test1Image.setAutoDraw(True)
        
        #*Test2Image* updates
        if t>=0.2 and Test2Image.status==NOT_STARTED:
            Test2Image.tStart=t
            Test2Image.frameNStart=frameN
            Test2Image.setOpacity(1)
            Test2Image.setAutoDraw(True)
        
        #*Test3Image* updates
        if t>=0.2 and Test3Image.status==NOT_STARTED:
            Test3Image.tStart=t
            Test3Image.frameNStart=frameN
            Test3Image.setOpacity(1)
            Test3Image.setAutoDraw(True)
        
        #*Test4Image* updates
        if t>=0.2 and Test4Image.status==NOT_STARTED:
            Test4Image.tStart=t
            Test4Image.frameNStart=frameN
            Test4Image.setOpacity(1)
            Test4Image.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
            
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    #------Prepare to start Routine "feedback"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    if CorrResp==diagnosis.response:
        Correct=1
    else:
        Correct=0
    YourResponse.setText(diagnosis.getRating())
    if Correct==1:
        Correct_Incorrect.setText('Correct!')
        score = score + 1000
    else:
        Correct_Incorrect.setText('Incorrect')
        score = score
    if DiseaseState==1:
        State.setText(diseases[0])
    elif DiseaseState==2:
        State.setText(diseases[1])
    elif DiseaseState==3:
        State.setText(diseases[2])
    else:
        State.setText(diseases[3])
    t = 0
    feedbackClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_2.status = NOT_STARTED
    # keep track of which components have finished
    feedbackComponents = []
    feedbackComponents.append(learningbackground)
    feedbackComponents.append(key_resp_2)
    feedbackComponents.append(Correct_Incorrect)
    feedbackComponents.append(YourResponse)
    feedbackComponents.append(YourResponseText)
    feedbackComponents.append(Press)
    feedbackComponents.append(ScoreText)
    feedbackComponents.append(AnswerWas)
    feedbackComponents.append(State)
    feedbackComponents.append(ScoreText)
    feedbackComponents.append(Result)
    feedbackComponents.append(Test1Image)
    feedbackComponents.append(Test2Image)
    feedbackComponents.append(Test3Image)
    feedbackComponents.append(Test4Image)
    feedbackComponents.append(GenImage)
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "feedback"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *learningbackground* updates
        if t >= 0.0 and learningbackground.status == NOT_STARTED:
            # keep track of start time/frame for later
            learningbackground.tStart = t  # underestimates by a little under one frame
            learningbackground.frameNStart = frameN  # exact frame index
            learningbackground.setAutoDraw(True)
        
        #GenImage* updates
        if t>=0.0 and GenImage.status==NOT_STARTED:
            GenImage.tStart=t
            GenImage.frameNStart=frameN
            GenImage.setAutoDraw(True)
        
        #*Test1Image* updates
        if t>=0.0 and Test1Image.status==NOT_STARTED:
            Test1Image.tStart=t
            Test1Image.frameNStart=frameN
            Test1Image.setOpacity(1)
            Test1Image.setAutoDraw(True)
        
        #*Test2Image* updates
        if t>=0.0 and Test2Image.status==NOT_STARTED:
            Test2Image.tStart=t
            Test2Image.frameNStart=frameN
            Test2Image.setOpacity(1)
            Test2Image.setAutoDraw(True)
        
        #*Test3Image* updates
        if t>=0.0 and Test3Image.status==NOT_STARTED:
            Test3Image.tStart=t
            Test3Image.frameNStart=frameN
            Test3Image.setOpacity(1)
            Test3Image.setAutoDraw(True)
        
        #*Test4Image* updates
        if t>=0.0 and Test4Image.status==NOT_STARTED:
            Test4Image.tStart=t
            Test4Image.frameNStart=frameN
            Test4Image.setOpacity(1)
            Test4Image.setAutoDraw(True)
        
        #*ScoreText* updates
        if t>=0.0 and ScoreText.status==NOT_STARTED:
            #keep track of start time/frame for later
            ScoreText.tStart=t#underestimates by a little under one frame
            ScoreText.frameNStart=frameN#exact frame index
            ScoreText.setAutoDraw(True)
        if trialClock.getTime()>0:
            ScoreText.setText("$%i" %(score))
        
        #*Result* updates
        if t>=0.0 and Result.status==NOT_STARTED:
            #keep track of start time/frame for later
            Result.tStart=t#underestimates by a little under one frame
            Result.frameNStart=frameN#exact frame index
            Result.setAutoDraw(True)
        
        #*Correct_Incorrect* updates
        if t>=0.0 and Correct_Incorrect.status==NOT_STARTED:
            #keep track of start time/frame for later
            Correct_Incorrect.tStart=t#underestimates by a little under one frame
            Correct_Incorrect.frameNStart=frameN#exact frame index
            Correct_Incorrect.setAutoDraw(True)
        
        #*YourResponse* updates
        if t>=0.0 and YourResponse.status==NOT_STARTED:
            #keep track of start time/frame for later
            YourResponse.tStart=t#underestimates by a little under one frame
            YourResponse.frameNStart=frameN#exact frame index
            YourResponse.setAutoDraw(True)
        
        #*YourResponseText* updates
        if t>=0.0 and YourResponseText.status==NOT_STARTED:
            #keep track of start time/frame for later
            YourResponseText.tStart=t#underestimates by a little under one frame
            YourResponseText.frameNStart=frameN#exact frame index
            YourResponseText.setAutoDraw(True)
        
        #*AnswerWas* updates
        if t>=0.0 and AnswerWas.status==NOT_STARTED:
            AnswerWas.tStart=t
            AnswerWas.frameNStart=frameN
            AnswerWas.setAutoDraw(True)
        
        #*State* updates
        if t>=0.0 and State.status==NOT_STARTED:
            State.tStart=t
            State.frameNStart=frameN
            State.setAutoDraw(True)
        
        #*Press* updates
        if t>=0.0 and Press.status==NOT_STARTED:
            #keep track of start time/frame for later
            Press.tStart=t#underestimates by a little under one frame
            Press.frameNStart=frameN#exact frame index
            Press.setAutoDraw(True)
            
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t  # underestimates by a little under one frame
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # store data for trials (TrialHandler)
    learningtrials.addData('phase', phase)
    learningtrials.addData('diagcond', diagcond)
    learningtrials.addData('costs', costs)
    learningtrials.addData('block', block)
    learningtrials.addData('trial', learningtrials.thisTrialN+1)
    learningtrials.addData('diagnosis', diagnosis.getRating())
    learningtrials.addData('diagnosis.rt', diagnosis.getRT())
    learningtrials.addData('blockdiagnosis.rt', globaldiagnosistime)
    learningtrials.addData('diseasestate', CorrResp)
    learningtrials.addData('accuracy', Correct)
    learningtrials.addData('totalclick', totalclick)
    learningtrials.addData('click1.order', click1order)
    learningtrials.addData('click2.order', click2order)
    learningtrials.addData('click3.order', click3order)
    learningtrials.addData('click4.order', click4order)
    learningtrials.addData('click1', click1)
    learningtrials.addData('click2', click2)
    learningtrials.addData('click3', click3)
    learningtrials.addData('click4', click4)
    learningtrials.addData('click1.rt', clicktime1)
    learningtrials.addData('click2.rt', clicktime2)
    learningtrials.addData('click3.rt', clicktime3)
    learningtrials.addData('click4.rt', clicktime4)
    learningtrials.addData('score', score)
    learningtrials.addData('learningscore', learningscore)
    learningtrials.addData('block1score', block1score)
    learningtrials.addData('block2score', block2score)
    learningtrials.addData('test1outcome', test1outcome)
    learningtrials.addData('test2outcome', test2outcome)
    learningtrials.addData('test3outcome', test3outcome)
    learningtrials.addData('test4outcome', test4outcome)
    learningtrials.addData('genoutcome', genoutcome)
    learningtrials.addData('viewtest1outcome', test1viewoutcome)
    learningtrials.addData('viewtest2outcome', test2viewoutcome)
    learningtrials.addData('viewtest3outcome', test3viewoutcome)
    learningtrials.addData('viewtest4outcome', test4viewoutcome)
    thisExp.nextEntry()
    
# completed n repeats of 'trials'=============================================================================================================================================Learning3============================================
#==Learning2==================================================================================================================================================================Learning3============================================
#==Learning2==================================================================================================================================================================Learning3============================================
#==Learning2==================================================================================================================================================================Learning3============================================
#==Learning2==================================================================================================================================================================Learning3============================================
#==Learning2==================================================================================================================================================================Learning3============================================
#==Learning2==================================================================================================================================================================Learning3============================================
Test1Image.setOpacity(0)
Test2Image.setOpacity(0)
Test3Image.setOpacity(0)
Test4Image.setOpacity(0)
learningscore=score
score=learningscore

#------Prepare to start Routine "learningphaseend"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
learningendClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
inst_key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
inst_key_resp_2.status = NOT_STARTED
# keep track of which components have finished
learningendComponents = []
learningendComponents.append(learningphasecompleted)
learningendComponents.append(ScoreText)
learningendComponents.append(inst_key_resp_2)
for thisComponent in learningendComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "learningphaseend"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = learningendClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *backgroundinst2* updates
    if t >= 0.0 and learningphasecompleted.status == NOT_STARTED:
        # keep track of start time/frame for later
        learningphasecompleted.tStart = t  # underestimates by a little under one frame
        learningphasecompleted.frameNStart = frameN  # exact frame index
        learningphasecompleted.setAutoDraw(True)
    
    # *ScoreText* updates
    # *ScoreText* updates
    if t >= 0.0 and ScoreText.status == NOT_STARTED:
        # keep track of start time/frame for later
        ScoreText.tStart = t  # underestimates by a little under one frame
        ScoreText.frameNStart = frameN  # exact frame index
        ScoreText.setAutoDraw(True)
        ScoreText.setText('$%i'%(learningscore))
    
    
    # *inst_key_resp_2* updates
    if t >= 0.0 and inst_key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_key_resp_2.tStart = t  # underestimates by a little under one frame
        inst_key_resp_2.frameNStart = frameN  # exact frame index
        inst_key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if inst_key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learningendComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instructions2"-------
for thisComponent in learningendComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


#------Prepare to start Routine "phase2instr2"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
phase2instr2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
inst_key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
inst_key_resp_5.status = NOT_STARTED
# keep track of which components have finished
phase2instr2Components = []
phase2instr2Components.append(background2phase2)
phase2instr2Components.append(ScoreText)
phase2instr2Components.append(inst_key_resp_5)
for thisComponent in phase2instr2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
#-------Start Routine "phase2instr2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = phase2instr2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *background2phase2* updates
    if t >= 0.0 and background2phase2.status == NOT_STARTED:
        # keep track of start time/frame for later
        background2phase2.tStart = t  # underestimates by a little under one frame
        background2phase2.frameNStart = frameN  # exact frame index
        background2phase2.setAutoDraw(True)
    
    #*ScoreText* updates
    if t>=0.0 and ScoreText.status==NOT_STARTED:
        #keep track of start time/frame for later
        ScoreText.tStart=t#underestimates by a little under one frame
        ScoreText.frameNStart=frameN#exact frame index
        ScoreText.setAutoDraw(True)
    
    # *inst_key_resp_5* updates
    if t >= 0.0 and inst_key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_key_resp_5.tStart = t  # underestimates by a little under one frame
        inst_key_resp_5.frameNStart = frameN  # exact frame index
        inst_key_resp_5.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if inst_key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in phase2instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "phase2instr2"-------
for thisComponent in phase2instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "instructions6"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
instructions6Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
diagnosis.reset()
# keep track of which components have finished
instructions6Components = []
instructions6Components.append(backgroundinst6)
instructions6Components.append(diagnosis)
instructions6Components.append(mouse)
instructions6Components.append(Test1Text)
instructions6Components.append(Test2Text)
instructions6Components.append(Test3Text)
instructions6Components.append(Test4Text)
instructions6Components.append(Test1Shape)
instructions6Components.append(Test2Shape)
instructions6Components.append(Test3Shape)
instructions6Components.append(Test4Shape)
instructions6Components.append(Random1Shape)
instructions6Components.append(Random2Shape)
instructions6Components.append(Random3Shape)
instructions6Components.append(Random4Shape)
instructions6Components.append(GenImage)
for thisComponent in instructions6Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions6"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *backgroundinst6* updates
    if t >= 0.0 and backgroundinst6.status == NOT_STARTED:
        # keep track of start time/frame for later
        backgroundinst6.draw()
        backgroundinst6.tStart = t  # underestimates by a little under one frame
        backgroundinst6.frameNStart = frameN  # exact frame index
    # *diagnosis* updates
    if t > 0.0:
        diagnosis.draw()
        continueRoutine = diagnosis.noResponse
        if diagnosis.noResponse == False:
            diagnosis.response = diagnosis.getRating()
            diagnosis.rt = diagnosis.getRT()
            
    # *GenImage* updates
    if t >= 0.0 and GenImage.status == NOT_STARTED:
        GenImage.tStart = t
        GenImage.frameNStart = frameN
        GenImage.setOpacity(1)
        GenImage.setAutoDraw(True)
        
    #*Test1Text* updates
    if t>=0.0 and Test1Text.status==NOT_STARTED:
        #keep track of start time/frame for later
        Test1Text.tStart=t#underestimates by a little under one frame
        Test1Text.frameNStart=frameN#exact frame index
        Test1Text.setAutoDraw(True)
    
    #*Test2Text* updates
    if t>=0.0 and Test2Text.status==NOT_STARTED:
        #keep track of start time/frame for later
        Test2Text.tStart=t#underestimates by a little under one frame
        Test2Text.frameNStart=frameN#exact frame index
        Test2Text.setAutoDraw(True)
    
    #*Test3Text* updates
    if t>=0.0 and Test3Text.status==NOT_STARTED:
        #keep track of start time/frame for later
        Test3Text.tStart=t#underestimates by a little under one frame
        Test3Text.frameNStart=frameN#exact frame index
        Test3Text.setAutoDraw(True)
    
    #*Test4Text* updates
    if t>=0.0 and Test4Text.status==NOT_STARTED:
        #keep track of start time/frame for later
        Test4Text.tStart=t#underestimates by a little under one frame
        Test4Text.frameNStart=frameN#exact frame index
        Test4Text.setAutoDraw(True)
    
    #*Random1Shape* updates
    if t>=0.0 and Random1Shape.status==NOT_STARTED:
        Random1Shape.tStart=t
        Random1Shape.frameNStart=frameN
        Random1Shape.setAutoDraw(False)
    
    #*Random2Shape* updates
    if t>=0.0 and Random2Shape.status==NOT_STARTED:
        Random2Shape.tStart=t
        Random2Shape.frameNStart=frameN
        Random2Shape.setAutoDraw(False)
    
    #*Random3Shape* updates
    if t>=0.0 and Random3Shape.status==NOT_STARTED:
        Random3Shape.tStart=t
        Random3Shape.frameNStart=frameN
        Random3Shape.setAutoDraw(False)
    
    #*Random4Shape* updates
    if t>=0.0 and Random4Shape.status==NOT_STARTED:
        Random4Shape.tStart=t
        Random4Shape.frameNStart=frameN
        Random4Shape.setAutoDraw(False)
    
    #*Test1Shape* updates
    if t>=0.0 and Test1Shape.status==NOT_STARTED:
        Test1Shape.tStart=t
        Test1Shape.frameNStart=frameN
        Test1Shape.setAutoDraw(True)
        Test1Shape.status=STARTED
    
    if Test1Shape.status==STARTED:
        if mouse.isPressedIn(Test1Shape) and click1<1:
            Test1Image.setAutoDraw(True)
            Test1Text.setColor(u'#FCC700')
            Cost1Text.setColor(u'#FCC700')
            Test1Shape.setAutoDraw(False)
            Test1Image.setOpacity(1)
            Random1Shape.setAutoDraw(True)
        
        if Test1Shape.contains(mouse):
            Random1Shape.setAutoDraw(True)
            Test1Shape.setOpacity(0)
        else:
            Random1Shape.setAutoDraw(False)
            Test1Shape.setOpacity(1)
    
    #*Test2Shape* updates
    if t>=0.0 and Test2Shape.status==NOT_STARTED:
        Test2Shape.tStart=t
        Test2Shape.frameNStart=frameN
        Test2Shape.setAutoDraw(True)
        Test2Shape.status=STARTED
    
    if Test2Shape.status==STARTED:
        if mouse.isPressedIn(Test2Shape) and click2<1:
            Test2Image.setAutoDraw(True)
            Test2Text.setColor(u'#FCC700')
            Cost2Text.setColor(u'#FCC700')
            Test2Shape.setAutoDraw(False)
            Test2Image.setOpacity(1)
            Random2Shape.setAutoDraw(True)

        if Test2Shape.contains(mouse):
            Random2Shape.setAutoDraw(True)
            Test2Shape.setOpacity(0)
        else:
            Random2Shape.setAutoDraw(False)
            Test2Shape.setOpacity(1)
    
    #*Test3Shape* updates
    if t>=0.0 and Test3Shape.status==NOT_STARTED:
        Test3Shape.tStart=t
        Test3Shape.frameNStart=frameN
        Test3Shape.setAutoDraw(True)
        Test3Shape.status=STARTED
    
    if Test3Shape.status==STARTED:
        if mouse.isPressedIn(Test3Shape) and click3<1:
            Test3Image.setAutoDraw(True)
            Test3Text.setColor(u'#FCC700')
            Cost3Text.setColor(u'#FCC700')
            Test3Shape.setAutoDraw(False)
            Test3Image.setOpacity(1)
            Random3Shape.setAutoDraw(True)

        if Test3Shape.contains(mouse):
            Random3Shape.setAutoDraw(True)
            Test3Shape.setOpacity(0)
        else:
            Random3Shape.setAutoDraw(False)
            Test3Shape.setOpacity(1)

    #*Test4Shape* updates
    if t>=0.0 and Test4Shape.status==NOT_STARTED:
        Test4Shape.tStart=t
        Test4Shape.frameNStart=frameN
        Test4Shape.setAutoDraw(True)
        Test4Shape.status=STARTED
    
    if Test4Shape.status==STARTED:
        if mouse.isPressedIn(Test4Shape) and click4<1:
            Test4Image.setAutoDraw(True)
            Test4Text.setColor(u'#FCC700')
            Cost4Text.setColor(u'#Fcc700')
            Test4Shape.setAutoDraw(False)
            Test4Image.setOpacity(1)
            Random4Shape.setAutoDraw(True)

        if Test4Shape.contains(mouse):
            Random4Shape.setAutoDraw(True)
            Test4Shape.setOpacity(0)
        else:
            Random4Shape.setAutoDraw(False)
            Test4Shape.setOpacity(1)
            
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instructions6"-------
for thisComponent in instructions6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
Test1Image.setOpacity(0)
Test2Image.setOpacity(0)
Test3Image.setOpacity(0)
Test4Image.setOpacity(0)
Test1Text.setColor(u'#004646')
Test2Text.setColor(u'#004646')
Test3Text.setColor(u'#004646')
Test4Text.setColor(u'#004646')
Cost1Text.setColor(u'#004646')
Cost2Text.setColor(u'#004646')
Cost3Text.setColor(u'#004646')
Cost4Text.setColor(u'#004646')

#------Prepare to start Routine "phase2instr3"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
phase2instr3Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
inst_key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
inst_key_resp_6.status = NOT_STARTED
# keep track of which components have finished
phase2instr3Components = []
phase2instr3Components.append(background3phase2)
phase2instr3Components.append(inst_key_resp_6)
for thisComponent in phase2instr2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
#-------Start Routine "phase2instr2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = phase2instr2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *background3phase2* updates
    if t >= 0.0 and background3phase2.status == NOT_STARTED:
        # keep track of start time/frame for later
        background3phase2.tStart = t  # underestimates by a little under one frame
        background3phase2.frameNStart = frameN  # exact frame index
        background3phase2.setAutoDraw(True)
    
    # *inst_key_resp_6* updates
    if t >= 0.0 and inst_key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_key_resp_6.tStart = t  # underestimates by a little under one frame
        inst_key_resp_6.frameNStart = frameN  # exact frame index
        inst_key_resp_6.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if inst_key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in phase2instr3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "phase2instr3"-------
for thisComponent in phase2instr3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "phase2instr4"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
phase2instr4Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
inst_key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
inst_key_resp_6.status = NOT_STARTED
# keep track of which components have finished
phase2instr4Components = []
phase2instr4Components.append(instructions9)
phase2instr4Components.append(inst_key_resp_6)
for thisComponent in phase2instr4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
#-------Start Routine "phase2instr2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = phase2instr4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions9* updates
    if t >= 0.0 and instructions9.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions9.tStart = t  # underestimates by a little under one frame
        instructions9.frameNStart = frameN  # exact frame index
        instructions9.setAutoDraw(True)
    
    # *inst_key_resp_6* updates
    if t >= 0.0 and inst_key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_key_resp_6.tStart = t  # underestimates by a little under one frame
        inst_key_resp_6.frameNStart = frameN  # exact frame index
        inst_key_resp_6.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if inst_key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in phase2instr4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "phase2instr4"-------
for thisComponent in phase2instr4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "start"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
startClock.reset()  # clock 
frameN = -1
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
startComponents = []
startComponents.append(startpic)
startComponents.append(startcountdown)
startComponents.append(startglow)
startComponents.append(backgroundinst8)
for thisComponent in startComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "start"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = startClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *background* updates
    if t >= 0.0 and backgroundinst8.status == NOT_STARTED:
        # keep track of start time/frame for later
        backgroundinst8.tStart = t  # underestimates by a little under one frame
        backgroundinst8.frameNStart = frameN  # exact frame index
        backgroundinst8.setAutoDraw(True)
    # *startglow* updates
    if t >= 0.0 and startglow.status == NOT_STARTED:
        startglow.tStart = t
        startglow.frameNStart = frameN
        startglow.setAutoDraw(True)
    elif startglow.status == STARTED and t >= (0.0 + (3.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        startglow.setAutoDraw(False)
    startglow.setOpacity(0.6+(0.3*(cos(4*t+1.5))))
    # *startpic* updates
    if t >= 0.0 and startpic.status == NOT_STARTED:
        # keep track of start time/frame for later
        startpic.tStart = t  # underestimates by a little under one frame
        startpic.frameNStart = frameN  # exact frame index
        startpic.setAutoDraw(True)
    elif startpic.status == STARTED and t >= (0.0 + (3.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        startpic.setAutoDraw(False)
    
    # startcountdown* updates
    if t >= 0.0 and startcountdown.status == NOT_STARTED:
        startcountdown.tStart = t
        startcountdown.frameNstart = frameN
        startcountdown.setText('3')
        startcountdown.setAutoDraw(True)
    elif startcountdown.status == STARTED and t >= (0.0 + (3.0-win.monitorFramePeriod*0.75)):
        startcountdown.setAutoDraw(False)
        
    if t > 1.0:
        startcountdown.setText('2')
    if t > 2.0:
        startcountdown.setText('1')
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)




#++Block1++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Block1+++++++++++++++++++++++++++++++++++++++++++++
#++Block1++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Block1+++++++++++++++++++++++++++++++++++++++++++++
#++Block1++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Block1+++++++++++++++++++++++++++++++++++++++++++++
#++Block1++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Block1+++++++++++++++++++++++++++++++++++++++++++++
#++Block1++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Block1+++++++++++++++++++++++++++++++++++++++++++++
#++Block1++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Block1+++++++++++++++++++++++++++++++++++++++++++++
#++Block1++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Block1+++++++++++++++++++++++++++++++++++++++++++++
#++Block1++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Block1+++++++++++++++++++++++++++++++++++++++++++++
#++Block1++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Block1+++++++++++++++++++++++++++++++++++++++++++++

#EOIN
# Initialize click_order variable as an empty list
click_order = []  
# Initialize click_order variable as an empty list
genoutcome_order = []  
# Create a dictionary to keep track of click_order for each genoutcome
click_order_dict = defaultdict(list)  
for genoutcome in range(1, 5):
    click_order_dict[genoutcome] = click_order_dict.get(genoutcome, [])
most_common_click_order_dict = {}
least_common_click_order_dict = {}

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method=u'random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/ConditionsTest.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
blockClock.reset()
phase=2
block=1
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec('{}=thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec('{}=thisTrial[paramName]'.format(paramName))
    #------Prepare to start Routine "loading"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    globaldiagnosistime=''
    click1=0
    click2=0
    click3=0
    click4=0
    clicktime1=''
    clicktime2=''
    clicktime3=''
    clicktime4=''
    test1viewoutcome=''
    test2viewoutcome=''
    test3viewoutcome=''
    test4viewoutcome=''
    totalclick=0
    TrialResp=0
    CorrResp=0
    Correct=0
    Rand1=random()
    Rand2=random()
    Rand3=random()
    Rand4=random()
    CueRand=random()
    
    if DiseaseState==1:
        CorrResp=diseases[0]
        if CueRand <= 0.50:
            GenImage.setImage(GENpics[0])
            genoutcome=1
        elif CueRand <= 0.60:
            GenImage.setImage(GENpics[1])
            genoutcome=2
        elif CueRand <= 0.70:
            GenImage.setImage(GENpics[2])
            genoutcome=3
        else:
            GenImage.setImage(GENpics[3])
            genoutcome=4
        if Rand1 <= 0.90:
            Test1Image.setImage(Test1pics[0])
            test1outcome=3
        elif Rand1 <= 0.95:
            Test1Image.setImage(Test1pics[1])
            test1outcome=2
        else:
            Test1Image.setImage(Test1pics[2])
            test1outcome=1
        if Rand2 <= 0.05:
            Test2Image.setImage(Test2pics[0])
            test2outcome=3
        elif Rand2 <= 0.55:
            Test2Image.setImage(Test2pics[1])
            test2outcome=2
        else:
            Test2Image.setImage(Test2pics[2])
            test2outcome=1
        if Rand3 <= 0.05:
            Test3Image.setImage(Test3pics[0])
            test3outcome=3
        elif Rand3 <= 0.55:
            Test3Image.setImage(Test3pics[1])
            test3outcome=2
        else:
            Test3Image.setImage(Test3pics[2])
            test3outcome=1
        if Rand4 <= 0.05:
            Test4Image.setImage(Test4pics[0])
            test4outcome=3
        elif Rand4 <= 0.55:
            Test4Image.setImage(Test4pics[1])
            test4outcome=2
        else:
            Test4Image.setImage(Test4pics[2])
            test4outcome=1
    elif DiseaseState==2:
        CorrResp=diseases[1]
        if CueRand <= 0.30:
            GenImage.setImage(GENpics[0])
            genoutcome=1
        elif CueRand <= 0.80:
            GenImage.setImage(GENpics[1])
            genoutcome=2
        elif CueRand <= 0.90:
            GenImage.setImage(GENpics[2])
            genoutcome=3
        else:
            GenImage.setImage(GENpics[3])
            genoutcome=4
        if Rand1 <= 0.05:
            Test1Image.setImage(Test1pics[0])
            test1outcome=3
        elif Rand1 <= 0.55:
            Test1Image.setImage(Test1pics[1])
            test1outcome=2
        else:
            Test1Image.setImage(Test1pics[2])
            test1outcome=1
        if Rand2 <= 0.90:
            Test2Image.setImage(Test2pics[0])
            test2outcome=3
        elif Rand2 <= 0.95:
            Test2Image.setImage(Test2pics[1])
            test2outcome=2
        else:
            Test2Image.setImage(Test2pics[2])
            test2outcome=1
        if Rand3 <= 0.05:
            Test3Image.setImage(Test3pics[0])
            test3outcome=3
        elif Rand3 <= 0.55:
            Test3Image.setImage(Test3pics[1])
            test3outcome=2
        else:
            Test3Image.setImage(Test3pics[2])
            test3outcome=1
        if Rand4 <= 0.05:
            Test4Image.setImage(Test4pics[0])
            test4outcome=3
        elif Rand4 <= 0.55:
            Test4Image.setImage(Test4pics[1])
            test4outcome=2
        else:
            Test4Image.setImage(Test4pics[2])
            test4outcome=1
    elif DiseaseState==3:
        CorrResp=diseases[2]
        if CueRand <= 0.10:
            GenImage.setImage(GENpics[0])
            genoutcome=1
        elif CueRand <= 0.40:
            GenImage.setImage(GENpics[1])
            genoutcome=2
        elif CueRand <= 0.90:
            GenImage.setImage(GENpics[2])
            genoutcome=3
        else:
            GenImage.setImage(GENpics[3])
            genoutcome=4
        if Rand1 <= 0.05:
            Test1Image.setImage(Test1pics[0])
            test1outcome=3
        elif Rand1 <= 0.55:
            Test1Image.setImage(Test1pics[1])
            test1outcome=2
        else:
            Test1Image.setImage(Test1pics[2])
            test1outcome=1
        if Rand2 <= 0.05:
            Test2Image.setImage(Test2pics[0])
            test2outcome=3
        elif Rand2 <= 0.55:
            Test2Image.setImage(Test2pics[1])
            test2outcome=2
        else:
            Test2Image.setImage(Test2pics[2])
            test2outcome=1
        if Rand3 <= 0.90:
            Test3Image.setImage(Test3pics[0])
            test3outcome=3
        elif Rand3 <= 0.95:
            Test3Image.setImage(Test3pics[1])
            test3outcome=2
        else:
            Test3Image.setImage(Test3pics[2])
            test3outcome=1
        if Rand4 <= 0.05:
            Test4Image.setImage(Test4pics[0])
            test4outcome=3
        elif Rand4 <= 0.55:
            Test4Image.setImage(Test4pics[1])
            test4outcome=2
        else:
            Test4Image.setImage(Test4pics[2])
            test4outcome=1
    else:
        CorrResp=diseases[3]
        if CueRand <= 0.10:
            GenImage.setImage(GENpics[0])
            genoutcome=1
        elif CueRand <= 0.20:
            GenImage.setImage(GENpics[1])
            genoutcome=2
        elif CueRand <= 0.50:
            GenImage.setImage(GENpics[2])
            genoutcome=3
        else:
            GenImage.setImage(GENpics[3])
            genoutcome=4
        if Rand1 <= 0.05:
            Test1Image.setImage(Test1pics[0])
            test1outcome=3
        elif Rand1 <= 0.55:
            Test1Image.setImage(Test1pics[1])
            test1outcome=2
        else:
            Test1Image.setImage(Test1pics[2])
            test1outcome=1
        if Rand2 <= 0.05:
            Test2Image.setImage(Test2pics[0])
            test2outcome=3
        elif Rand2 <= 0.55:
            Test2Image.setImage(Test2pics[1])
            test2outcome=2
        else:
            Test2Image.setImage(Test2pics[2])
            test2outcome=1
        if Rand3 <= 0.05:
            Test3Image.setImage(Test3pics[0])
            test3outcome=3
        elif Rand3 <= 0.55:
            Test3Image.setImage(Test3pics[1])
            test3outcome=2
        else:
            Test3Image.setImage(Test3pics[2])
            test3outcome=1
        if Rand4 <= 0.90:
            Test4Image.setImage(Test4pics[0])
            test4outcome=3
        elif Rand4 <= 0.95:
            Test4Image.setImage(Test4pics[1])
            test4outcome=2
        else:
            Test4Image.setImage(Test4pics[2])
            test4outcome=1

    t = 0
    loadingClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    loadingComponents = []
    loadingComponents.append(learningbackground)
    loadingComponents.append(loadingpic)
    loadingComponents.append(Test1Shape)
    loadingComponents.append(Test2Shape)
    loadingComponents.append(Test3Shape)
    loadingComponents.append(Test4Shape)
    loadingComponents.append(Test1Text)
    loadingComponents.append(Test2Text)
    loadingComponents.append(Test3Text)
    loadingComponents.append(Test4Text)
    
    for thisComponent in loadingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    Test1Shape.setOpacity(1)
    Test2Shape.setOpacity(1)
    Test3Shape.setOpacity(1)
    Test4Shape.setOpacity(1)

    #-------Start Routine "loading"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = loadingClock.getTime()
        b = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *learningbackground* updates
        if t >= 0.0 and learningbackground.status == NOT_STARTED:
            # keep track of start time/frame for later
            learningbackground.tStart = t  # underestimates by a little under one frame
            learningbackground.frameNStart = frameN  # exact frame index
            learningbackground.setAutoDraw(True)
        
        # *loadingpic* updates
        if t >= 0.0 and loadingpic.status == NOT_STARTED:
            # keep track of start time/frame for later
            loadingpic.tStart = t  # underestimates by a little under one frame
            loadingpic.frameNStart = frameN  # exact frame index
            loadingpic.setAutoDraw(True)
        elif loadingpic.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            loadingpic.setAutoDraw(False)
        loadingpic.setOpacity(0.6+(0.3*(cos(4*t+1.5))))
        
        # *Test1Shape* updates
        if t >=shape1delay and Test1Shape.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test1Shape.tStart = t
            Test1Shape.frameNStart = frameN
            Test1Shape.setAutoDraw(True)
        elif Test1Shape.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)):
            Test1Shape.setAutoDraw(False)
            
        # *Test2Shape* updates
        if t >=shape2delay and Test2Shape.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test2Shape.tStart = t
            Test2Shape.frameNStart = frameN
            Test2Shape.setAutoDraw(True)
        elif Test2Shape.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)):
            Test2Shape.setAutoDraw(False)
            
        # *Test3Shape* updates
        if t >=shape3delay and Test3Shape.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test3Shape.tStart = t
            Test3Shape.frameNStart = frameN
            Test3Shape.setAutoDraw(True)
        elif Test3Shape.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)):
            Test3Shape.setAutoDraw(False)
       
        # *Test4Shape* updates
        if t >=shape4delay and Test4Shape.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test4Shape.tStart = t
            Test4Shape.frameNStart = frameN
            Test4Shape.setAutoDraw(True)
        elif Test4Shape.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)):
            Test4Shape.setAutoDraw(False)
        
        # *Test1Text* updates
        if t>=text1delay and Test1Text.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test1Text.tStart = t
            Test1Text.frameNStart = frameN
            Test1Text.setAutoDraw(True)
        elif Test1Text.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)):
            Test1Text.setAutoDraw(False)
            
        # *Test2Text* updates
        if t>=text2delay and Test2Text.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test2Text.tStart = t
            Test2Text.frameNStart = frameN
            Test2Text.setAutoDraw(True)
        elif Test2Text.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)):
            Test2Text.setAutoDraw(False)
            
        # *Test3Text* updates
        if t>=text3delay and Test3Text.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test3Text.tStart = t
            Test3Text.frameNStart = frameN
            Test3Text.setAutoDraw(True)
        elif Test3Text.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)):
            Test3Text.setAutoDraw(False)
            
        # *Test4Text* updates
        if t>=text4delay and Test4Text.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test4Text.tStart = t
            Test4Text.frameNStart = frameN
            Test4Text.setAutoDraw(True)
        elif Test4Text.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)):
            Test4Text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in loadingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "loading"-------
    for thisComponent in loadingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    #------Prepare to start Routine "trial"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    diagnosis.reset()
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(learningbackground)
    trialComponents.append(mouse)
    trialComponents.append(ScoreText)
    trialComponents.append(diagnosis)
    trialComponents.append(Test1Text)
    trialComponents.append(Test2Text)
    trialComponents.append(Test3Text)
    trialComponents.append(Test4Text)
    trialComponents.append(Test1Shape)
    trialComponents.append(Test2Shape)
    trialComponents.append(Test3Shape)
    trialComponents.append(Test4Shape)
    trialComponents.append(Random1Shape)
    trialComponents.append(Random2Shape)
    trialComponents.append(Random3Shape)
    trialComponents.append(Random4Shape)
    trialComponents.append(Test1Image)
    trialComponents.append(Cost1Text)
    trialComponents.append(Cost2Text)
    trialComponents.append(Cost3Text)
    trialComponents.append(Cost4Text)
    trialComponents.append(GenImage)

    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "trial"-------
    continueRoutine = True
    click1=0
    click2=0
    click3=0
    click4=0
    click1order=0
    click2order=0
    click3order=0
    click4order=0
    totalclick=0
    testsRemaining = 4
    while continueRoutine: 

        # get current time
        t = trialClock.getTime()
        b = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #*Mouse* updates
        if t>=0.0 and mouse.status==NOT_STARTED:
            mouse.tStart=t
            mouse.frameNStart=frameN
            
        # *trialbackground* updates
        if t >= 0.0 and learningbackground.status == NOT_STARTED:
            # keep track of start time/frame for later
            learningbackground.draw()
            learningbackground.tStart = t  # underestimates by a little under one frame
            learningbackground.frameNStart = frameN  # exact frame index
        
        # *diagnosis* updates
        if t > 0.0:
            diagnosis.draw()
            continueRoutine = diagnosis.noResponse
            if diagnosis.noResponse == False:
                diagnosis.response = diagnosis.getRating()
                diagnosis.rt = diagnosis.getRT()
        
        #*ScoreText* updates
        if t>=0.0 and ScoreText.status==NOT_STARTED:
            #keep track of start time/frame for later
            ScoreText.tStart=t#underestimates by a little under one frame
            ScoreText.frameNStart=frameN#exact frame index
            ScoreText.setAutoDraw(True)
        if trialClock.getTime()>0:
            ScoreText._pygletTextObj.text=str("$----")
        
        #*Test1Text* updates
        if t>=0.0 and Test1Text.status==NOT_STARTED:
            #keep track of start time/frame for later
            Test1Text.tStart=t#underestimates by a little under one frame
            Test1Text.frameNStart=frameN#exact frame index
            Test1Text.setAutoDraw(True)
        
        #*Test2Text* updates
        if t>=0.0 and Test2Text.status==NOT_STARTED:
            #keep track of start time/frame for later
            Test2Text.tStart=t#underestimates by a little under one frame
            Test2Text.frameNStart=frameN#exact frame index
            Test2Text.setAutoDraw(True)
        
        #*Test3Text* updates
        if t>=0.0 and Test3Text.status==NOT_STARTED:
            #keep track of start time/frame for later
            Test3Text.tStart=t#underestimates by a little under one frame
            Test3Text.frameNStart=frameN#exact frame index
            Test3Text.setAutoDraw(True)
        
        #*Test4Text* updates
        if t>=0.0 and Test4Text.status==NOT_STARTED:
            #keep track of start time/frame for later
            Test4Text.tStart=t#underestimates by a little under one frame
            Test4Text.frameNStart=frameN#exact frame index
            Test4Text.setAutoDraw(True)
        
        #*Random1Shape* updates
        if t>=0.0 and Random1Shape.status==NOT_STARTED:
            Random1Shape.tStart=t
            Random1Shape.frameNStart=frameN
            Random1Shape.setAutoDraw(False)
        
        #*Random2Shape* updates
        if t>=0.0 and Random2Shape.status==NOT_STARTED:
            Random2Shape.tStart=t
            Random2Shape.frameNStart=frameN
            Random2Shape.setAutoDraw(False)
        
        #*Random3Shape* updates
        if t>=0.0 and Random3Shape.status==NOT_STARTED:
            Random3Shape.tStart=t
            Random3Shape.frameNStart=frameN
            Random3Shape.setAutoDraw(False)
        
        #*Random4Shape* updates
        if t>=0.0 and Random4Shape.status==NOT_STARTED:
            Random4Shape.tStart=t
            Random4Shape.frameNStart=frameN
            Random4Shape.setAutoDraw(False)
        
        #*GenImage* updates
        if t>=0.0 and GenImage.status==NOT_STARTED:
            GenImage.tStart=t
            GenImage.frameNStart=frameN
            GenImage.setAutoDraw(True)
        
        #*Test1Shape* updates
        if t>=0.0 and Test1Shape.status==NOT_STARTED:
            Test1Shape.tStart=t
            Test1Shape.frameNStart=frameN
            Test1Shape.setAutoDraw(True)
            Test1Shape.status=STARTED
        
        if Test1Shape.status==STARTED and testsRemaining>0:
            if mouse.isPressedIn(Test1Shape) and click1<1:
                Test1Image.setAutoDraw(True)
                Test1Text.setColor(u'#FCC700')
                Cost1Text.setColor(u'#FCC700')
                ScoreText.draw()
                Test1Shape.setAutoDraw(False)
                Test1Image.setOpacity(1)
                Random1Shape.setAutoDraw(True)
                totalclick=totalclick+1
                click1order=totalclick
                click1=click1+1
                testsRemaining=testsRemaining-1
                test1viewoutcome=test1outcome
                #EOIN
                if click1order == 1:
                    click_order.append(1)
                    genoutcome_order.append(genoutcome)
                    click_order_dict[genoutcome].append(1)
        
            if Test1Shape.contains(mouse):
                Random1Shape.setAutoDraw(True)
                Test1Shape.setOpacity(0)
            else:
                Random1Shape.setAutoDraw(False)
                Test1Shape.setOpacity(1)
        
        #*Test2Shape* updates
        if t>=0.0 and Test2Shape.status==NOT_STARTED:
            Test2Shape.tStart=t
            Test2Shape.frameNStart=frameN
            Test2Shape.setAutoDraw(True)
            Test2Shape.status=STARTED
        
        if Test2Shape.status==STARTED and testsRemaining>0:
            if mouse.isPressedIn(Test2Shape) and click2<1:
                Test2Image.setAutoDraw(True)
                Test2Text.setColor(u'#FCC700')
                Cost2Text.setColor(u'#FCC700')
                ScoreText.draw()
                Test2Shape.setAutoDraw(False)
                Test2Image.setOpacity(1)
                Random2Shape.setAutoDraw(True)
                totalclick=totalclick+1
                click2order=totalclick
                click2=click2+1
                testsRemaining=testsRemaining-1
                test2viewoutcome=test2outcome
                if click2order == 1: 
                    click_order.append(2)
                    genoutcome_order.append(genoutcome)
                    click_order_dict[genoutcome].append(2)

            if Test2Shape.contains(mouse):
                Random2Shape.setAutoDraw(True)
                Test2Shape.setOpacity(0)
            else:
                Random2Shape.setAutoDraw(False)
                Test2Shape.setOpacity(1)
        
        #*Test3Shape* updates
        if t>=0.0 and Test3Shape.status==NOT_STARTED:
            Test3Shape.tStart=t
            Test3Shape.frameNStart=frameN
            Test3Shape.setAutoDraw(True)
            Test3Shape.status=STARTED
        
        if Test3Shape.status==STARTED and testsRemaining>0:
            if mouse.isPressedIn(Test3Shape) and click3<1:
                Test3Image.setAutoDraw(True)
                Test3Text.setColor(u'#FCC700')
                Cost3Text.setColor(u'#FCC700')
                ScoreText.draw()
                Test3Shape.setAutoDraw(False)
                Test3Image.setOpacity(1)
                Random3Shape.setAutoDraw(True)
                totalclick=totalclick+1
                click3order=totalclick
                click3=click3+1
                testsRemaining=testsRemaining-1
                test3viewoutcome=test3outcome
                if click3order == 1: 
                    click_order.append(3)
                    genoutcome_order.append(genoutcome)
                    click_order_dict[genoutcome].append(3)

            if Test3Shape.contains(mouse):
                Random3Shape.setAutoDraw(True)
                Test3Shape.setOpacity(0)
            else:
                Random3Shape.setAutoDraw(False)
                Test3Shape.setOpacity(1)
    
        #*Test4Shape* updates
        if t>=0.0 and Test4Shape.status==NOT_STARTED:
            Test4Shape.tStart=t
            Test4Shape.frameNStart=frameN
            Test4Shape.setAutoDraw(True)
            Test4Shape.status=STARTED
        
        if Test4Shape.status==STARTED and testsRemaining>0:
            if mouse.isPressedIn(Test4Shape) and click4<1:
                Test4Image.setAutoDraw(True)
                Test4Text.setColor(u'#FCC700')
                Cost4Text.setColor(u'#Fcc700')
                ScoreText.draw()
                Test4Shape.setAutoDraw(False)
                Test4Image.setOpacity(1)
                Random4Shape.setAutoDraw(True)
                totalclick=totalclick+1
                click4order=totalclick
                click4=click4+1
                testsRemaining=testsRemaining-1
                test4viewoutcome=test4outcome
                if click4order == 1:
                    click_order.append(4)
                    genoutcome_order.append(genoutcome)
                    click_order_dict[genoutcome].append(4)

            if Test4Shape.contains(mouse):
                Random4Shape.setAutoDraw(True)
                Test4Shape.setOpacity(0)
            else:
                Random4Shape.setAutoDraw(False)
                Test4Shape.setOpacity(1)

        # EOIN
        # Define a dictionary of symptoms for each genoutcome
        symptoms_dict = {1: "fever", 2: "rash", 3: "migraine", 4: "ache"}

        # Define a dictionary where each click_order corresponds to a specific test
        tests_dict = {1: 'MRI', 2: 'CAT', 3: 'XRAY', 4: 'LAB'}
            
        print('genoutcome_order', genoutcome_order)
        print('click_order', click_order)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
            
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if CorrResp==diagnosis.response:
        Correct=1
    else:
        Correct=0
    if Correct==1:
        score = score + 1000
    else:
        score = score
    
    # store data for trials (TrialHandler)
    trials.addData('phase', phase)
    trials.addData('diagcond', diagcond)
    trials.addData('costs', costs)
    trials.addData('block', block)
    trials.addData('trial', learningtrials.thisTrialN+1)
    trials.addData('diagnosis', diagnosis.getRating())
    trials.addData('diagnosis.rt', diagnosis.getRT())
    trials.addData('blockdiagnosis.rt', globaldiagnosistime)
    trials.addData('diseasestate', CorrResp)
    trials.addData('accuracy', Correct)
    trials.addData('totalclick', totalclick)
    trials.addData('click1.order', click1order)
    trials.addData('click2.order', click2order)
    trials.addData('click3.order', click3order)
    trials.addData('click4.order', click4order)
    trials.addData('click1', click1)
    trials.addData('click2', click2)
    trials.addData('click3', click3)
    trials.addData('click4', click4)
    trials.addData('click1.rt', clicktime1)
    trials.addData('click2.rt', clicktime2)
    trials.addData('click3.rt', clicktime3)
    trials.addData('click4.rt', clicktime4)
    trials.addData('score', score)
    trials.addData('learningscore', learningscore)
    trials.addData('block1score', block1score)
    trials.addData('block2score', block2score)
    trials.addData('test1outcome', test1outcome)
    trials.addData('test2outcome', test2outcome)
    trials.addData('test3outcome', test3outcome)
    trials.addData('test4outcome', test4outcome)
    trials.addData('genoutcome', genoutcome)
    trials.addData('viewtest1outcome', test1viewoutcome)
    trials.addData('viewtest2outcome', test2viewoutcome)
    trials.addData('viewtest3outcome', test3viewoutcome)
    trials.addData('viewtest4outcome', test4viewoutcome)
    #EOIN
    trials.addData('click_order', click_order)
    trials.addData('genoutcome_order', genoutcome_order)
    thisExp.nextEntry()
    
    Test1Image.setOpacity(0)
    Test2Image.setOpacity(0)
    Test3Image.setOpacity(0)
    Test4Image.setOpacity(0)
    Test1Text.setColor(u'#004646')
    Test2Text.setColor(u'#004646')
    Test3Text.setColor(u'#004646')
    Test4Text.setColor(u'#004646')
    Cost1Text.setColor(u'#004646')
    Cost2Text.setColor(u'#004646')
    Cost3Text.setColor(u'#004646')
    Cost4Text.setColor(u'#004646')


# completed n repeats of 'trials'==========================================================================================================================================Block1============================================
#==Block1==================================================================================================================================================================Block1============================================
#==Block1==================================================================================================================================================================Block1============================================
#==Block1==================================================================================================================================================================Block1============================================
#==Block1==================================================================================================================================================================Block1============================================
#==Block1==================================================================================================================================================================Block1============================================
#==Block1==================================================================================================================================================================Block1============================================


block1score = score
score = block1score
#------Prepare to start Routine "btwrounds"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
instructionsbtwroundsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
inst_key_resp_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
inst_key_resp_7.status = NOT_STARTED
# keep track of which components have finished
btwroundsComponents = []
btwroundsComponents.append(instructionsbtwrounds)
btwroundsComponents.append(inst_key_resp_7)
btwroundsComponents.append(ScoreText)
for thisComponent in btwroundsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
#-------Start Routine "btwrounds"-------

continueRoutine = True
while continueRoutine:
    # get current time
    t = instructionsbtwroundsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructionsbtwrounds* updates
    if t >= 0.0 and instructionsbtwrounds.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructionsbtwrounds.tStart = t  # underestimates by a little under one frame
        instructionsbtwrounds.frameNStart = frameN  # exact frame index
        instructionsbtwrounds.setAutoDraw(True)
    
    # *ScoreText* updates
    if t >= 0.0 and ScoreText.status == NOT_STARTED:
        ScoreText.tStart = t
        ScoreText.frameNStart = frameN
        ScoreText.setText("$%i" %(score))
        ScoreText.setAutoDraw(True)
    
    
    # *inst_key_resp_7* updates
    if t >= 0.0 and inst_key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_key_resp_7.tStart = t  # underestimates by a little under one frame
        inst_key_resp_7.frameNStart = frameN  # exact frame index
        inst_key_resp_7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if inst_key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in phase2instr3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "btwrounds"-------
for thisComponent in btwroundsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#++Block2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Block2+++++++++++++++++++++++++++++++++++++++++++++
#++Block2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Block2+++++++++++++++++++++++++++++++++++++++++++++
#++Block2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Block2+++++++++++++++++++++++++++++++++++++++++++++
#++Block2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Block2+++++++++++++++++++++++++++++++++++++++++++++
#++Block2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Block2+++++++++++++++++++++++++++++++++++++++++++++
#++Block2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Block2+++++++++++++++++++++++++++++++++++++++++++++
#++Block2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Block2+++++++++++++++++++++++++++++++++++++++++++++
#++Block2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Block2+++++++++++++++++++++++++++++++++++++++++++++
#++Block2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Block2+++++++++++++++++++++++++++++++++++++++++++++

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method=u'random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('/Users/ec531/Library/CloudStorage/Dropbox/ART-AI/Coding/Medical_Diagnosis_Game/MDGSpring20Task/ConditionsTest.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
blockClock.reset()
phase=2
block=2
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec('{}=thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec('{}=thisTrial[paramName]'.format(paramName))
    #------Prepare to start Routine "loading"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    globaldiagnosistime=''
    click1=0
    click2=0
    click3=0
    click4=0
    clicktime1=''
    clicktime2=''
    clicktime3=''
    clicktime4=''
    test1viewoutcome=''
    test2viewoutcome=''
    test3viewoutcome=''
    test4viewoutcome=''
    totalclick=0
    TrialResp=0
    CorrResp=0
    Correct=0
    Rand1=random()
    Rand2=random()
    Rand3=random()
    Rand4=random()
    CueRand=random()
    
    if DiseaseState==1:
        CorrResp=diseases[0]
        if CueRand <= 0.50:
            GenImage.setImage(GENpics[0])
            genoutcome=1
        elif CueRand <= 0.60:
            GenImage.setImage(GENpics[1])
            genoutcome=2
        elif CueRand <= 0.70:
            GenImage.setImage(GENpics[2])
            genoutcome=3
        else:
            GenImage.setImage(GENpics[3])
            genoutcome=4
        if Rand1 <= 0.90:
            Test1Image.setImage(Test1pics[0])
            test1outcome=3
        elif Rand1 <= 0.95:
            Test1Image.setImage(Test1pics[1])
            test1outcome=2
        else:
            Test1Image.setImage(Test1pics[2])
            test1outcome=1
        if Rand2 <= 0.05:
            Test2Image.setImage(Test2pics[0])
            test2outcome=3
        elif Rand2 <= 0.55:
            Test2Image.setImage(Test2pics[1])
            test2outcome=2
        else:
            Test2Image.setImage(Test2pics[2])
            test2outcome=1
        if Rand3 <= 0.05:
            Test3Image.setImage(Test3pics[0])
            test3outcome=3
        elif Rand3 <= 0.55:
            Test3Image.setImage(Test3pics[1])
            test3outcome=2
        else:
            Test3Image.setImage(Test3pics[2])
            test3outcome=1
        if Rand4 <= 0.05:
            Test4Image.setImage(Test4pics[0])
            test4outcome=3
        elif Rand4 <= 0.55:
            Test4Image.setImage(Test4pics[1])
            test4outcome=2
        else:
            Test4Image.setImage(Test4pics[2])
            test4outcome=1
    elif DiseaseState==2:
        CorrResp=diseases[1]
        if CueRand <= 0.30:
            GenImage.setImage(GENpics[0])
            genoutcome=1
        elif CueRand <= 0.80:
            GenImage.setImage(GENpics[1])
            genoutcome=2
        elif CueRand <= 0.90:
            GenImage.setImage(GENpics[2])
            genoutcome=3
        else:
            GenImage.setImage(GENpics[3])
            genoutcome=4
        if Rand1 <= 0.05:
            Test1Image.setImage(Test1pics[0])
            test1outcome=3
        elif Rand1 <= 0.55:
            Test1Image.setImage(Test1pics[1])
            test1outcome=2
        else:
            Test1Image.setImage(Test1pics[2])
            test1outcome=1
        if Rand2 <= 0.90:
            Test2Image.setImage(Test2pics[0])
            test2outcome=3
        elif Rand2 <= 0.95:
            Test2Image.setImage(Test2pics[1])
            test2outcome=2
        else:
            Test2Image.setImage(Test2pics[2])
            test2outcome=1
        if Rand3 <= 0.05:
            Test3Image.setImage(Test3pics[0])
            test3outcome=3
        elif Rand3 <= 0.55:
            Test3Image.setImage(Test3pics[1])
            test3outcome=2
        else:
            Test3Image.setImage(Test3pics[2])
            test3outcome=1
        if Rand4 <= 0.05:
            Test4Image.setImage(Test4pics[0])
            test4outcome=3
        elif Rand4 <= 0.55:
            Test4Image.setImage(Test4pics[1])
            test4outcome=2
        else:
            Test4Image.setImage(Test4pics[2])
            test4outcome=1
    elif DiseaseState==3:
        CorrResp=diseases[2]
        if CueRand <= 0.10:
            GenImage.setImage(GENpics[0])
            genoutcome=1
        elif CueRand <= 0.40:
            GenImage.setImage(GENpics[1])
            genoutcome=2
        elif CueRand <= 0.90:
            GenImage.setImage(GENpics[2])
            genoutcome=3
        else:
            GenImage.setImage(GENpics[3])
            genoutcome=4
        if Rand1 <= 0.05:
            Test1Image.setImage(Test1pics[0])
            test1outcome=3
        elif Rand1 <= 0.55:
            Test1Image.setImage(Test1pics[1])
            test1outcome=2
        else:
            Test1Image.setImage(Test1pics[2])
            test1outcome=1
        if Rand2 <= 0.05:
            Test2Image.setImage(Test2pics[0])
            test2outcome=3
        elif Rand2 <= 0.55:
            Test2Image.setImage(Test2pics[1])
            test2outcome=2
        else:
            Test2Image.setImage(Test2pics[2])
            test2outcome=1
        if Rand3 <= 0.90:
            Test3Image.setImage(Test3pics[0])
            test3outcome=3
        elif Rand3 <= 0.95:
            Test3Image.setImage(Test3pics[1])
            test3outcome=2
        else:
            Test3Image.setImage(Test3pics[2])
            test3outcome=1
        if Rand4 <= 0.05:
            Test4Image.setImage(Test4pics[0])
            test4outcome=3
        elif Rand4 <= 0.55:
            Test4Image.setImage(Test4pics[1])
            test4outcome=2
        else:
            Test4Image.setImage(Test4pics[2])
            test4outcome=1
    else:
        CorrResp=diseases[3]
        if CueRand <= 0.10:
            GenImage.setImage(GENpics[0])
            genoutcome=1
        elif CueRand <= 0.20:
            GenImage.setImage(GENpics[1])
            genoutcome=2
        elif CueRand <= 0.50:
            GenImage.setImage(GENpics[2])
            genoutcome=3
        else:
            GenImage.setImage(GENpics[3])
            genoutcome=4
        if Rand1 <= 0.05:
            Test1Image.setImage(Test1pics[0])
            test1outcome=3
        elif Rand1 <= 0.55:
            Test1Image.setImage(Test1pics[1])
            test1outcome=2
        else:
            Test1Image.setImage(Test1pics[2])
            test1outcome=1
        if Rand2 <= 0.05:
            Test2Image.setImage(Test2pics[0])
            test2outcome=3
        elif Rand2 <= 0.55:
            Test2Image.setImage(Test2pics[1])
            test2outcome=2
        else:
            Test2Image.setImage(Test2pics[2])
            test2outcome=1
        if Rand3 <= 0.05:
            Test3Image.setImage(Test3pics[0])
            test3outcome=3
        elif Rand3 <= 0.55:
            Test3Image.setImage(Test3pics[1])
            test3outcome=2
        else:
            Test3Image.setImage(Test3pics[2])
            test3outcome=1
        if Rand4 <= 0.90:
            Test4Image.setImage(Test4pics[0])
            test4outcome=3
        elif Rand4 <= 0.95:
            Test4Image.setImage(Test4pics[1])
            test4outcome=2
        else:
            Test4Image.setImage(Test4pics[2])
            test4outcome=1

    t = 0
    loadingClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    loadingComponents = []
    loadingComponents.append(learningbackground)
    loadingComponents.append(loadingpic)
    loadingComponents.append(Test1Shape)
    loadingComponents.append(Test2Shape)
    loadingComponents.append(Test3Shape)
    loadingComponents.append(Test4Shape)
    loadingComponents.append(Test1Text)
    loadingComponents.append(Test2Text)
    loadingComponents.append(Test3Text)
    loadingComponents.append(Test4Text)
    
    for thisComponent in loadingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    Test1Shape.setOpacity(1)
    Test2Shape.setOpacity(1)
    Test3Shape.setOpacity(1)
    Test4Shape.setOpacity(1)
    #-------Start Routine "loading"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = loadingClock.getTime()
        b = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *learningbackground* updates
        if t >= 0.0 and learningbackground.status == NOT_STARTED:
            # keep track of start time/frame for later
            learningbackground.tStart = t  # underestimates by a little under one frame
            learningbackground.frameNStart = frameN  # exact frame index
            learningbackground.setAutoDraw(True)
        
        # *loadingpic* updates
        if t >= 0.0 and loadingpic.status == NOT_STARTED:
            # keep track of start time/frame for later
            loadingpic.tStart = t  # underestimates by a little under one frame
            loadingpic.frameNStart = frameN  # exact frame index
            loadingpic.setAutoDraw(True)
        elif loadingpic.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            loadingpic.setAutoDraw(False)
        loadingpic.setOpacity(0.6+(0.3*(cos(4*t+1.5))))
        
        # *Test1Shape* updates
        if t >=shape1delay and Test1Shape.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test1Shape.tStart = t
            Test1Shape.frameNStart = frameN
            Test1Shape.setAutoDraw(True)
        elif Test1Shape.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)):
            Test1Shape.setAutoDraw(False)
            
        # *Test2Shape* updates
        if t >=shape2delay and Test2Shape.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test2Shape.tStart = t
            Test2Shape.frameNStart = frameN
            Test2Shape.setAutoDraw(True)
        elif Test2Shape.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)):
            Test2Shape.setAutoDraw(False)
            
        # *Test3Shape* updates
        if t >=shape3delay and Test3Shape.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test3Shape.tStart = t
            Test3Shape.frameNStart = frameN
            Test3Shape.setAutoDraw(True)
        elif Test3Shape.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)):
            Test3Shape.setAutoDraw(False)
       
        # *Test4Shape* updates
        if t >=shape4delay and Test4Shape.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test4Shape.tStart = t
            Test4Shape.frameNStart = frameN
            Test4Shape.setAutoDraw(True)
        elif Test4Shape.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)):
            Test4Shape.setAutoDraw(False)
        
        # *Test1Text* updates
        if t>=text1delay and Test1Text.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test1Text.tStart = t
            Test1Text.frameNStart = frameN
            Test1Text.setAutoDraw(True)
        elif Test1Text.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)):
            Test1Text.setAutoDraw(False)
            
        # *Test2Text* updates
        if t>=text2delay and Test2Text.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test2Text.tStart = t
            Test2Text.frameNStart = frameN
            Test2Text.setAutoDraw(True)
        elif Test2Text.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)):
            Test2Text.setAutoDraw(False)
            
        # *Test3Text* updates
        if t>=text3delay and Test3Text.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test3Text.tStart = t
            Test3Text.frameNStart = frameN
            Test3Text.setAutoDraw(True)
        elif Test3Text.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)):
            Test3Text.setAutoDraw(False)
            
        # *Test4Text* updates
        if t>=text4delay and Test4Text.status ==NOT_STARTED:
            #keep track of start time/frame for later
            Test4Text.tStart = t
            Test4Text.frameNStart = frameN
            Test4Text.setAutoDraw(True)
        elif Test4Text.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)):
            Test4Text.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in loadingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "loading"-------
    for thisComponent in loadingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)


    #------Prepare to start Routine "trial"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    diagnosis.reset()
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(learningbackground)
    trialComponents.append(mouse)
    trialComponents.append(ScoreText)
    trialComponents.append(diagnosis)
    trialComponents.append(Test1Text)
    trialComponents.append(Test2Text)
    trialComponents.append(Test3Text)
    trialComponents.append(Test4Text)
    trialComponents.append(Test1Shape)
    trialComponents.append(Test2Shape)
    trialComponents.append(Test3Shape)
    trialComponents.append(Test4Shape)
    trialComponents.append(Random1Shape)
    trialComponents.append(Random2Shape)
    trialComponents.append(Random3Shape)
    trialComponents.append(Random4Shape)
    trialComponents.append(Test1Image)
    trialComponents.append(Cost1Text)
    trialComponents.append(Cost2Text)
    trialComponents.append(Cost3Text)
    trialComponents.append(Cost4Text)
    trialComponents.append(GenImage)
    # EOIN
    trialComponents.append(PromptTextAI)
    trialComponents.append(PromptTextAdvice)
    
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    click1=0
    click2=0
    click3=0
    click4=0
    click1order=0
    click2order=0
    click3order=0
    click4order=0
    totalclick=0
    testsRemaining = 4
    
    # Define a dictionary of symptoms for each genoutcome
    symptoms_dict = {1: "fever", 2: "rash", 3: "migraine", 4: "ache"}

    # Define a dictionary where each click_order corresponds to a specific test
    tests_dict = {1: 'MRI', 2: 'CAT', 3: 'XRAY', 4: 'LAB'}    

    # Define a dictionary to map image file paths to genoutcome 
    genoutcome_map = {
    'Images/fever.png': 1,
    'Images/rash.png': 2,
    'Images/migraine.png': 3,
    'Images/ache.png': 4,
    }

    # Initialize the most common and least common click orders
    most_common_click_order_for_genoutcome = None
    least_common_click_order_for_genoutcome = None

    # Calculate the most common and least common click orders
    if click_order_dict[genoutcome]:  # Check if the list is not empty
        most_common_click_order_for_genoutcome = Counter(click_order_dict[genoutcome]).most_common(1)[0][0]
        least_common_click_order_for_genoutcome = Counter(click_order_dict[genoutcome]).most_common()[-1][0]

    shuffled_test_most = tests_dict.get(most_common_click_order_for_genoutcome, "Test Not Found")

    shuffled_test_least = tests_dict.get(least_common_click_order_for_genoutcome, "Test Not Found")

    # Generate advice based on these values
    DA_advice = "This is your AI Advisor\n"
    if genoutcome in symptoms_dict and most_common_click_order_for_genoutcome in tests_dict:
        #original_genoutcome = shuffled_to_original_genoutcomes[symptoms_dict[genoutcome]]
        original_test = shuffled_to_original_tests[tests_dict[most_common_click_order_for_genoutcome]]
        user_friendly_name = symptoms_dict[genoutcome_map[GENpics[genoutcome - 1]]]  # Use the shuffled genoutcome to get the user-friendly name
        DA_advice += f"When the patient has had {user_friendly_name}, you have most frequently requested {original_test}, consider requesting a different test this time."
    else:
        DA_advice += "Unable to provide advice due to missing data."

    FAC_advice = "This is your AI Advisor\n"
    if genoutcome in symptoms_dict and most_common_click_order_for_genoutcome in tests_dict:
       # original_genoutcome = shuffled_to_original_genoutcomes[symptoms_dict[genoutcome]]
        original_test = shuffled_to_original_tests[tests_dict[most_common_click_order_for_genoutcome]]
        user_friendly_name = symptoms_dict[genoutcome_map[GENpics[genoutcome - 1]]]  # Use the shuffled genoutcome to get the user-friendly name
        FAC_advice += f"When the patient has had {user_friendly_name}, you have most frequently requested {original_test}, consider requesting this test again."
    else:
        FAC_advice += "Unable to provide advice due to missing data."

    MOD_advice = "This is your AI Advisor\n"
    if genoutcome in symptoms_dict and most_common_click_order_for_genoutcome in tests_dict:
        #original_genoutcome = shuffled_to_original_genoutcomes[symptoms_dict[genoutcome]]
        original_test = shuffled_to_original_tests[tests_dict[least_common_click_order_for_genoutcome]]
        user_friendly_name = symptoms_dict[genoutcome_map[GENpics[genoutcome - 1]]]  # Use the shuffled genoutcome to get the user-friendly name
        MOD_advice += f"When the patient has had {user_friendly_name}, you have least frequently requested {original_test}, consider requesting this test this time."
    else:
        MOD_advice += "Unable to provide advice due to missing data."  

    NO_advice = ""

    # Create a random generator
    rng = np.random.default_rng()      

    # Define your advice options
    advice_options = [DA_advice, FAC_advice, MOD_advice, NO_advice]

    # Randomly choose advice
    random_advice = rng.choice(advice_options)

    print('DA_advice:', DA_advice)
    print('FAC_advice:', FAC_advice)
    print('MOD_advice:', MOD_advice)

    while continueRoutine:

        # get current time
        t = trialClock.getTime()
        b = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

        # update/draw components on each frame
        #*Mouse* updates
        if t>=0.0 and mouse.status==NOT_STARTED:
            mouse.tStart=t
            mouse.frameNStart=frameN
            
        # *learningbackground* updates
        if t >= 0.0 and learningbackground.status == NOT_STARTED:
            # keep track of start time/frame for later
            learningbackground.draw()
            learningbackground.tStart = t  # underestimates by a little under one frame
            learningbackground.frameNStart = frameN  # exact frame index
        
        # *diagnosis* updates
        if t > 0.0:
            diagnosis.draw()
            continueRoutine = diagnosis.noResponse
            if diagnosis.noResponse == False:
                diagnosis.response = diagnosis.getRating()
                diagnosis.rt = diagnosis.getRT()
        
        #*ScoreText* updates
        if t>=0.0 and ScoreText.status==NOT_STARTED:
            #keep track of start time/frame for later
            ScoreText.tStart=t#underestimates by a little under one frame
            ScoreText.frameNStart=frameN#exact frame index
            ScoreText.setAutoDraw(True)
        if trialClock.getTime()>0:
            ScoreText._pygletTextObj.text=str("$----")
        
        #*Test1Text* updates
        if t>=0.0 and Test1Text.status==NOT_STARTED:
            #keep track of start time/frame for later
            Test1Text.tStart=t#underestimates by a little under one frame
            Test1Text.frameNStart=frameN#exact frame index
            Test1Text.setAutoDraw(True)
        
        #*Test2Text* updates
        if t>=0.0 and Test2Text.status==NOT_STARTED:
            #keep track of start time/frame for later
            Test2Text.tStart=t#underestimates by a little under one frame
            Test2Text.frameNStart=frameN#exact frame index
            Test2Text.setAutoDraw(True)
        
        #*Test3Text* updates
        if t>=0.0 and Test3Text.status==NOT_STARTED:
            #keep track of start time/frame for later
            Test3Text.tStart=t#underestimates by a little under one frame
            Test3Text.frameNStart=frameN#exact frame index
            Test3Text.setAutoDraw(True)
        
        #*Test4Text* updates
        if t>=0.0 and Test4Text.status==NOT_STARTED:
            #keep track of start time/frame for later
            Test4Text.tStart=t#underestimates by a little under one frame
            Test4Text.frameNStart=frameN#exact frame index
            Test4Text.setAutoDraw(True)
        
        #*Random1Shape* updates
        if t>=0.0 and Random1Shape.status==NOT_STARTED:
            Random1Shape.tStart=t
            Random1Shape.frameNStart=frameN
            Random1Shape.setAutoDraw(False)
        
        #*Random2Shape* updates
        if t>=0.0 and Random2Shape.status==NOT_STARTED:
            Random2Shape.tStart=t
            Random2Shape.frameNStart=frameN
            Random2Shape.setAutoDraw(False)
        
        #*Random3Shape* updates
        if t>=0.0 and Random3Shape.status==NOT_STARTED:
            Random3Shape.tStart=t
            Random3Shape.frameNStart=frameN
            Random3Shape.setAutoDraw(False)
        
        #*Random4Shape* updates
        if t>=0.0 and Random4Shape.status==NOT_STARTED:
            Random4Shape.tStart=t
            Random4Shape.frameNStart=frameN
            Random4Shape.setAutoDraw(False)
        #*GenImage* updates
        if t>=0.0 and GenImage.status==NOT_STARTED:
            GenImage.tStart=t
            GenImage.frameNStart=frameN
            GenImage.setAutoDraw(True)

                #*Test1Shape* updates
        if t>=0.0 and Test1Shape.status==NOT_STARTED:
            Test1Shape.tStart=t
            Test1Shape.frameNStart=frameN
            Test1Shape.setAutoDraw(True)
            Test1Shape.status=STARTED
        
        if Test1Shape.status==STARTED and testsRemaining>0:
            if mouse.isPressedIn(Test1Shape) and click1<1:
                Test1Image.setAutoDraw(True)
                Test1Text.setColor(u'#FCC700')
                Cost1Text.setColor(u'#FCC700')
                ScoreText.draw()
                Test1Shape.setAutoDraw(False)
                Test1Image.setOpacity(1)
                Random1Shape.setAutoDraw(True)
                totalclick=totalclick+1
                click1order=totalclick
                click1=click1+1
                testsRemaining=testsRemaining-1
                test1viewoutcome=test1outcome
                #EOIN
                if click1order == 1:
                    click_order.append(1)
                    genoutcome_order.append(genoutcome)
                    click_order_dict[genoutcome].append(1)
        
            if Test1Shape.contains(mouse):
                Random1Shape.setAutoDraw(True)
                Test1Shape.setOpacity(0)
            else:
                Random1Shape.setAutoDraw(False)
                Test1Shape.setOpacity(1)
        
        #*Test2Shape* updates
        if t>=0.0 and Test2Shape.status==NOT_STARTED:
            Test2Shape.tStart=t
            Test2Shape.frameNStart=frameN
            Test2Shape.setAutoDraw(True)
            Test2Shape.status=STARTED
        
        if Test2Shape.status==STARTED and testsRemaining>0:
            if mouse.isPressedIn(Test2Shape) and click2<1:
                Test2Image.setAutoDraw(True)
                Test2Text.setColor(u'#FCC700')
                Cost2Text.setColor(u'#FCC700')
                ScoreText.draw()
                Test2Shape.setAutoDraw(False)
                Test2Image.setOpacity(1)
                Random2Shape.setAutoDraw(True)
                totalclick=totalclick+1
                click2order=totalclick
                click2=click2+1
                testsRemaining=testsRemaining-1
                test2viewoutcome=test2outcome
                if click2order == 1:
                    click_order.append(2)
                    genoutcome_order.append(genoutcome)
                    click_order_dict[genoutcome].append(2)

            if Test2Shape.contains(mouse):
                Random2Shape.setAutoDraw(True)
                Test2Shape.setOpacity(0)
            else:
                Random2Shape.setAutoDraw(False)
                Test2Shape.setOpacity(1)
        
        #*Test3Shape* updates
        if t>=0.0 and Test3Shape.status==NOT_STARTED:
            Test3Shape.tStart=t
            Test3Shape.frameNStart=frameN
            Test3Shape.setAutoDraw(True)
            Test3Shape.status=STARTED
        
        if Test3Shape.status==STARTED and testsRemaining>0:
            if mouse.isPressedIn(Test3Shape) and click3<1:
                Test3Image.setAutoDraw(True)
                Test3Text.setColor(u'#FCC700')
                Cost3Text.setColor(u'#FCC700')
                ScoreText.draw()
                Test3Shape.setAutoDraw(False)
                Test3Image.setOpacity(1)
                Random3Shape.setAutoDraw(True)
                totalclick=totalclick+1
                click3order=totalclick
                click3=click3+1
                testsRemaining=testsRemaining-1
                test3viewoutcome=test3outcome
                if click3order == 1:
                    click_order.append(3)
                    genoutcome_order.append(genoutcome)
                    click_order_dict[genoutcome].append(3)

            if Test3Shape.contains(mouse):
                Random3Shape.setAutoDraw(True)
                Test3Shape.setOpacity(0)
            else:
                Random3Shape.setAutoDraw(False)
                Test3Shape.setOpacity(1)
    
        #*Test4Shape* updates
        if t>=0.0 and Test4Shape.status==NOT_STARTED:
            Test4Shape.tStart=t
            Test4Shape.frameNStart=frameN
            Test4Shape.setAutoDraw(True)
            Test4Shape.status=STARTED
        
        if Test4Shape.status==STARTED and testsRemaining>0:
            if mouse.isPressedIn(Test4Shape) and click4<1:
                Test4Image.setAutoDraw(True)
                Test4Text.setColor(u'#FCC700')
                Cost4Text.setColor(u'#Fcc700')
                ScoreText.draw()
                Test4Shape.setAutoDraw(False)
                Test4Image.setOpacity(1)
                Random4Shape.setAutoDraw(True)
                totalclick=totalclick+1
                click4order=totalclick
                click4=click4+1
                testsRemaining=testsRemaining-1
                test4viewoutcome=test4outcome
                if click4order == 1:
                    click_order.append(4)
                    genoutcome_order.append(genoutcome)
                    click_order_dict[genoutcome].append(4)

            if Test4Shape.contains(mouse):
                Random4Shape.setAutoDraw(True)
                Test4Shape.setOpacity(0)
            else:
                Random4Shape.setAutoDraw(False)
                Test4Shape.setOpacity(1)
        
        # EOIN
        print('genoutcome_order', genoutcome_order)
        print('click_order', click_order)
        print('click_order_dict', click_order_dict)

        # Display the most common click order
        print(f"The most common click order for genoutcome {genoutcome} is {most_common_click_order_dict.get(genoutcome, 'N/A')}")
        print(f"The least common click order for genoutcome {genoutcome} is {least_common_click_order_dict.get(genoutcome, 'N/A')}")

        print('shuffled_to_original_genoutcomes:', shuffled_to_original_genoutcomes)
        print('shuffled_to_original_tests:', shuffled_to_original_tests)

        # AI prompt text
        if t >= 0.0 and GenImage.status == STARTED:
            # Randomise AI advice 
            PromptTextAdvice.text = random_advice 
            PromptTextAdvice.draw()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
            
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()

    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if CorrResp==diagnosis.response:
        Correct=1
    else:
        Correct=0
    if Correct==1:
        score = score + 1000
    else:
        score = score
    Test1Image.setOpacity(0)
    Test2Image.setOpacity(0)
    Test3Image.setOpacity(0)
    Test4Image.setOpacity(0)
    Test1Text.setColor(u'#004646')
    Test2Text.setColor(u'#004646')
    Test3Text.setColor(u'#004646')
    Test4Text.setColor(u'#004646')
    Cost1Text.setColor(u'#004646')
    Cost2Text.setColor(u'#004646')
    Cost3Text.setColor(u'#004646')
    Cost4Text.setColor(u'#004646')
    core.wait(.25)

    # store data for trials (TrialHandler)
    trials.addData('phase', phase)
    trials.addData('diagcond', diagcond)
    trials.addData('costs', costs)
    trials.addData('block', block)
    trials.addData('trial', learningtrials.thisTrialN+1)
    trials.addData('diagnosis', diagnosis.getRating())
    trials.addData('diagnosis.rt', diagnosis.getRT())
    trials.addData('blockdiagnosis.rt', globaldiagnosistime)
    trials.addData('diseasestate', CorrResp)
    trials.addData('accuracy', Correct)
    trials.addData('totalclick', totalclick)
    trials.addData('click1.order', click1order)
    trials.addData('click2.order', click2order)
    trials.addData('click3.order', click3order)
    trials.addData('click4.order', click4order)
    trials.addData('click1', click1)
    trials.addData('click2', click2)
    trials.addData('click3', click3)
    trials.addData('click4', click4)
    trials.addData('click1.rt', clicktime1)
    trials.addData('click2.rt', clicktime2)
    trials.addData('click3.rt', clicktime3)
    trials.addData('click4.rt', clicktime4)
    trials.addData('score', score)
    trials.addData('learningscore', learningscore)
    trials.addData('block1score', block1score)
    trials.addData('block2score', block2score)
    trials.addData('test1outcome', test1outcome)
    trials.addData('test2outcome', test2outcome)
    trials.addData('test3outcome', test3outcome)
    trials.addData('test4outcome', test4outcome)
    trials.addData('genoutcome', genoutcome)
    trials.addData('viewtest1outcome', test1viewoutcome)
    trials.addData('viewtest2outcome', test2viewoutcome)
    trials.addData('viewtest3outcome', test3viewoutcome)
    trials.addData('viewtest4outcome', test4viewoutcome)
    # EOIN
    trials.addData('click_order', click_order)
    trials.addData('genoutcome_order', genoutcome_order)
    trials.addData('most_common_click_order_for_genoutcome',most_common_click_order_for_genoutcome) 
    trials.addData('least_common_click_order_for_genoutcome',least_common_click_order_for_genoutcome) 
    trials.addData('Advice', random_advice)
    thisExp.nextEntry()

# completed n repeats of 'trials'==========================================================================================================================================Block2============================================
#==Block2==================================================================================================================================================================Block2============================================
#==Block2==================================================================================================================================================================Block2============================================
#==Block2==================================================================================================================================================================Block2============================================
#==Block2==================================================================================================================================================================Block2============================================
#==Block2==================================================================================================================================================================Block2============================================
#==Block2==================================================================================================================================================================Block2============================================


block2score = score
score = block2score


#_#END EXP###########################################################################################################################################################END EXP##################################################
#_#END EXP###########################################################################################################################################################END EXP##################################################
#_#END EXP###########################################################################################################################################################END EXP##################################################
#_#END EXP###########################################################################################################################################################END EXP##################################################
#_#END EXP###########################################################################################################################################################END EXP##################################################
#_#END EXP###########################################################################################################################################################END EXP##################################################
#_#END EXP###########################################################################################################################################################END EXP##################################################
#_#END EXP###########################################################################################################################################################END EXP##################################################
#_#END EXP###########################################################################################################################################################END EXP##################################################

#------Prepare to start Routine "results"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
resultsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
inst_key_resp_9 = event.BuilderKeyResponse()  # create an object of type KeyResponse
inst_key_resp_9.status = NOT_STARTED
# keep track of which components have finished
resultsComponents = []
resultsComponents.append(resultsbackground)
resultsComponents.append(learningscoretext)
resultsComponents.append(round1scoretext)
resultsComponents.append(round2scoretext)
resultsComponents.append(topscoretext)
resultsComponents.append(inst_key_resp_9)
for thisComponent in btwroundsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
#-------Start Routine "results"-------
topscore=max(block1score,block2score)
#topfirst3=np.amax(block1score,block2score,block3score)
#topsecond3=np.amax(block4score,block5score,block6score)
#topscore=np.amax(topfirst3,topsecond3)
continueRoutine = True
while continueRoutine:
    # get current time
    t = resultsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *resultsbackground* updates
    if t >= 0.0 and resultsbackground.status == NOT_STARTED:
        # keep track of start time/frame for later
        resultsbackground.tStart = t  # underestimates by a little under one frame
        resultsbackground.frameNStart = frameN  # exact frame index
        resultsbackground.setAutoDraw(True)
    
    # *learningscoretext* updates
    if t >= 0.0 and learningscoretext.status == NOT_STARTED:
        learningscoretext.tStart = t
        learningscoretext.frameNStart = frameN
        learningscoretext.setText('$%i' %(learningscore))
        learningscoretext.setAutoDraw(True)
    
    # *round1scoretext* updates
    if t >= 0.0 and round1scoretext.status == NOT_STARTED:
        round1scoretext.tStart = t
        round1scoretext.frameNStart = frameN
        round1scoretext.setText('$%i' %(block1score))
        round1scoretext.setAutoDraw(True)
    
    # *round2scoretext* updates
    if t >= 0.0 and round2scoretext.status == NOT_STARTED:
        round2scoretext.tStart = t
        round2scoretext.frameNStart = frameN
        round2scoretext.setText('$%i' %(block2score))
        round2scoretext.setAutoDraw(True)
    
    # *topscoretext* updates
    if t >= 0.0 and topscoretext.status == NOT_STARTED:
        topscoretext.tStart = t
        topscoretext.frameNStart = frameN
        topscoretext.setText('$%i' %(topscore))
        topscoretext.setAutoDraw(True)
    
    # *inst_key_resp_9* updates
    if t >= 0.0 and inst_key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_key_resp_9.tStart = t  # underestimates by a little under one frame
        inst_key_resp_9.frameNStart = frameN  # exact frame index
        inst_key_resp_9.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if inst_key_resp_9.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in resultsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "results"-------
for thisComponent in resultsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
block=7
trials.addData('block', block)
trials.addData('learningscore', learningscore)
trials.addData('block1score', block1score)
trials.addData('block2score', block2score)
thisExp.nextEntry()

#------Prepare to start Routine "debrief1"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
debrief1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
deb_key_resp_1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
deb_key_resp_1.status = NOT_STARTED
# keep track of which components have finished
debrief1Components = []
debrief1Components.append(debriefimage1)
debrief1Components.append(deb_key_resp_1)
for thisComponent in debrief1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
#-------Start Routine "debrief1"-------

continueRoutine = True
while continueRoutine:
    # get current time
    t = debrief1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *debriefimage1* updates
    if t >= 0.0 and debriefimage1.status == NOT_STARTED:
        # keep track of start time/frame for later
        debriefimage1.tStart = t  # underestimates by a little under one frame
        debriefimage1.frameNStart = frameN  # exact frame index
        debriefimage1.setAutoDraw(True)
    
    # *deb_key_resp_1* updates
    if t >= 0.0 and deb_key_resp_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        deb_key_resp_1.tStart = t  # underestimates by a little under one frame
        deb_key_resp_1.frameNStart = frameN  # exact frame index
        deb_key_resp_1.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if deb_key_resp_1.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in debrief1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "debrief1"-------
for thisComponent in debrief1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "debrief2"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
debrief2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
deb_key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
deb_key_resp_2.status = NOT_STARTED
# keep track of which components have finished
debrief2Components = []
debrief2Components.append(debriefimage1)
debrief2Components.append(deb_key_resp_2)
for thisComponent in debrief2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
#-------Start Routine "debrief2"-------

continueRoutine = True
while continueRoutine:
    # get current time
    t = debrief2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *debriefimage2* updates
    if t >= 0.0 and debriefimage2.status == NOT_STARTED:
        # keep track of start time/frame for later
        debriefimage2.tStart = t  # underestimates by a little under one frame
        debriefimage2.frameNStart = frameN  # exact frame index
        debriefimage2.setAutoDraw(True)
    
    # *deb_key_resp_2* updates
    if t >= 0.0 and deb_key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        deb_key_resp_2.tStart = t  # underestimates by a little under one frame
        deb_key_resp_2.frameNStart = frameN  # exact frame index
        deb_key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if deb_key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in debrief2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "debrief2"-------
for thisComponent in debrief2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "goodbye"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
goodbyeClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
bye_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
bye_key_resp.status = NOT_STARTED
# keep track of which components have finished
goodbyeComponents = []
goodbyeComponents.append(dplinst2)
goodbyeComponents.append(backgroundinst8)
goodbyeComponents.append(goodbye)
goodbyeComponents.append(goodbyeglow)
goodbyeComponents.append(bye_key_resp)
for thisComponent in goodbyeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
#-------Start Routine "goodbye"-------

continueRoutine = True
while continueRoutine:
    # get current time
    t = goodbyeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *dplinst2* updates
    if t >= 0.0 and dplinst2.status == NOT_STARTED:
        # keep track of start time/frame for later
        dplinst2.tStart = t  # underestimates by a little under one frame
        dplinst2.frameNStart = frameN  # exact frame index
        dplinst2.setAutoDraw(True)
    
    # *background* updates
    if t >= 0.0 and backgroundinst8.status == NOT_STARTED:
        # keep track of start time/frame for later
        backgroundinst8.tStart = t  # underestimates by a little under one frame
        backgroundinst8.frameNStart = frameN  # exact frame index
        backgroundinst8.setAutoDraw(True)
    
    # *goodbye* updates
    if t >= 0.0 and goodbye.status == NOT_STARTED:
        goodbye.tStart = t
        goodbye.frameNStart = frameN
        goodbye.setAutoDraw(True)
    
    # *goodbyeglow* updates
    if t >= 0.0 and goodbyeglow.status == NOT_STARTED:
        goodbyeglow.tStart = t
        goodbyeglow.frameNStart = frameN
        goodbyeglow.setAutoDraw(True)
    goodbyeglow.setOpacity(0.6+(0.3*(cos(4*t+1.5))))
    
    # *bye_key_resp* updates
    if t >= 0.0 and bye_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        bye_key_resp.tStart = t  # underestimates by a little under one frame
        bye_key_resp.frameNStart = frameN  # exact frame index
        bye_key_resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if bye_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['escape'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in goodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "goodbye"-------
for thisComponent in goodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

win.close()
core.quit()
