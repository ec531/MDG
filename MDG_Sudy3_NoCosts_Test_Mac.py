#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.02), January 21, 2015, at 11:36
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import STARTED, NOT_STARTED, FINISHED  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import pandas as pd
from collections import Counter, defaultdict
import random  
from psychopy.visual.slider import Slider

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath('/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG/')) 
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'MDG_Study3_Test_NoCost' 
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

# Create a data list
trial_data = []

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation
    
# Setup the Window
win = visual.Window(size=(1500, 975), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='Laptop', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=False, units='pix'
    )

mouse = event.Mouse(visible=True, win=win)

# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate'] is not None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize global components for Experiment "Block Time"----------------------------------------------------------------------------------------------------------------------------------------------------------
phase=1
diagcond=1
block=0
score=0
#costs=''
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
np.random.shuffle(diseases)
np.random.shuffle(tests)
np.random.shuffle(locationsdummy)
np.random.shuffle(costsdummy)
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
GENpics=[('/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/fever.png'),('/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/rash.png'),('/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/migraine.png'),('/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/ache.png')]
np.random.shuffle(GENpics)
MRIpics=[('/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/MRI - POS.png'),('/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/MRI - NEUT.png'),('/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/MRI - NEG.png')]
LABpics=[('/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/LAB - POS.png'),('/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/LAB - NEUT.png'),('/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/LAB - NEG.png')]
XRAYpics=[('/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/RAY - POS.png'),('/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/RAY - NEUT.png'),('/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/RAY - NEG.png')]
CATpics=[('/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/CAT - POS.png'),('/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/CAT - NEUT.png'),('/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/CAT - NEG.png')]
symptoms=[('FEVER'), ('RASH'), ('MIGRAINE'),('ACHE')]

# Mapping shuffled test names to original test names
shuffled_to_original_tests = {original_test: shuffled_test for original_test, shuffled_test in zip(tests_copy, tests)}

# The probability structure for the presenting cue (GENImage)
gen_probabilities = np.array([[0.50, 0.10, 0.10, 0.30],
                              [0.30, 0.50, 0.10, 0.10],
                              [0.10, 0.30, 0.50, 0.10],
                              [0.10, 0.10, 0.30, 0.50]])

# The probability structure for the test outcomes
test_probabilities = pd.DataFrame({
    'Hypothesis': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],
    'Outcome': [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    'Test 1': [0.90, 0.05, 0.05, 0.05, 0.50, 0.45, 0.05, 0.50, 0.45, 0.05, 0.5, 0.45],
    'Test 2': [0.05, 0.50, 0.45, 0.90, 0.05, 0.05, 0.05, 0.50, 0.45, 0.05, 0.50, 0.45],
    'Test 3': [0.05, 0.50, 0.45, 0.05, 0.50, 0.45, 0.90, 0.05, 0.05, 0.05, 0.50, 0.45],
    'Test 4': [0.05, 0.50, 0.45, 0.05, 0.50, 0.45, 0.05, 0.50, 0.45, 0.90, 0.05, 0.05]
})

if locationsdummy[0]==1:
    imagelocation1=[-730,310]
    textlocation1=[-490,230]
    shape1delay=shapedelaytimes[0]
    text1delay=textdelaytimes[0]
elif locationsdummy[0]==2:
    imagelocation1=[730,310]
    textlocation1=[490,230]
    shape1delay=shapedelaytimes[1]
    text1delay=textdelaytimes[1]
elif locationsdummy[0]==3:
    imagelocation1=[-730,-310]
    textlocation1=[-490,-230]
    shape1delay=shapedelaytimes[2]
    text1delay=textdelaytimes[2]
else:
    imagelocation1=[730,-310]
    textlocation1=[490,-230]
    shape1delay=shapedelaytimes[3]
    text1delay=textdelaytimes[3]

if locationsdummy[1]==1:
    imagelocation2=[-730,310]
    textlocation2=[-490,230]
    shape2delay=shapedelaytimes[0]
    text2delay=textdelaytimes[0]
elif locationsdummy[1]==2:
    imagelocation2=[730,310]
    textlocation2=[490,230]
    shape2delay=shapedelaytimes[1]
    text2delay=textdelaytimes[1]
elif locationsdummy[1]==3:
    imagelocation2=[-730,-310]
    textlocation2=[-490,-230]
    shape2delay=shapedelaytimes[2]
    text2delay=textdelaytimes[2]
else:
    imagelocation2=[730,-310]
    textlocation2=[490,-230]
    shape2delay=shapedelaytimes[3]
    text2delay=textdelaytimes[3]

if locationsdummy[2]==1:
    imagelocation3=[-730,310]
    textlocation3=[-490,230]
    shape3delay=shapedelaytimes[0]
    text3delay=textdelaytimes[0]
elif locationsdummy[2]==2:
    imagelocation3=[730,310]
    textlocation3=[490,230]
    shape3delay=shapedelaytimes[1]
    text3delay=textdelaytimes[1]
elif locationsdummy[2]==3:
    imagelocation3=[-730,-310]
    textlocation3=[-490,-230]
    shape3delay=shapedelaytimes[2]
    text3delay=textdelaytimes[2]
else:
    imagelocation3=[730,-310]
    textlocation3=[490,-230]
    shape3delay=shapedelaytimes[3]
    text3delay=textdelaytimes[3]

if locationsdummy[3]==1:
    imagelocation4=[-730,310]
    textlocation4=[-490,230]
    shape4delay=shapedelaytimes[0]
    text4delay=textdelaytimes[0]
elif locationsdummy[3]==2:
    imagelocation4=[730,310]
    textlocation4=[490,230]
    shape4delay=shapedelaytimes[1]
    text4delay=textdelaytimes[1]
elif locationsdummy[3]==3:
    imagelocation4=[-730,-310]
    textlocation4=[-490,-230]
    shape4delay=shapedelaytimes[2]
    text4delay=textdelaytimes[2]
else:
    imagelocation4=[730,-310]
    textlocation4=[490,-230]
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
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructionsbackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True)

instructions1text = visual.TextStim(win=win, name='Instructions1Text',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=(0, 0),height=40, wrapWidth=1200, color=u'#FCC700', colorSpace=u'rgb', opacity=1)

# Initialize components for Routine "instructions2"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions2Clock = core.Clock()
backgroundinst2 = visual.ImageStim(win=win, name='backgroundinst2',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructionsbackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=1.0)

instructions2text = visual.TextStim(win=win, name='Instructions2Text',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=(0, 0),height=30, wrapWidth=1200, color=u'#FCC700', colorSpace=u'rgb', opacity=1)

#Initialize components for Routine "outcomes"
outcomesClock = core.Clock()
outcomesimage = visual.ImageStim(win=win, name='outcomesiamge',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/outcomes.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "instructions4.1"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions4Clock = core.Clock()
backgroundinst4 = visual.ImageStim(win=win, name='backgroundinst4',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructions4.1.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "instructions4.2"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions42Clock = core.Clock()
backgroundinst42 = visual.ImageStim(win=win, name='backgroundinst4',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructions4.2.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


# Initialize components for Routine "instructions4.3"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions43Clock = core.Clock()
backgroundinst43 = visual.ImageStim(win=win, name='backgroundinst4',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructions4.3.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "instructions5"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions5Clock = core.Clock()
backgroundinst5 = visual.ImageStim(win=win, name='backgroundinst5',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructionsbackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
dplinst5 = visual.ImageStim(win=win, name='dplinst5',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructions5.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
inst5pic = visual.ImageStim(win=win, name='inst5pic',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructions5.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "instructions6"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions6Clock = core.Clock()
backgroundinst6 = visual.ImageStim(win=win, name='backgroundinst6',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructions6.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "instructions7"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions7Clock = core.Clock()
instr7pic = visual.ImageStim(win=win, name='instr7pic',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructions7.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "instructions8"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions8Clock = core.Clock()
backgroundinst8 = visual.ImageStim(win=win, name='backgroundinst8',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructionsbackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
dplinst8 = visual.ImageStim(win=win, name='dplinst8',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructions8.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
inst8pic = visual.ImageStim(win=win, name='inst8pic',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructions8.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "start"----------------------------------------------------------------------------------------------------------------------------------------------------------
startClock = core.Clock()
startglow = visual.ImageStim(win=win, name='startglow',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/startglow.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
startpic = visual.ImageStim(win=win, name='startpic',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/start.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
startcountdown = visual.TextStim(win=win, ori=0, name='startcountdown',
    text=u'3',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[550, -50], height=500,wrapWidth=None,
    color=u'#01FFFD', colorSpace=u'rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "loading"----------------------------------------------------------------------------------------------------------------------------------------------------------
loadingClock = core.Clock()
background = visual.ImageStim(win=win, name='background',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/TrialBackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
loadingpic = visual.ImageStim(win=win, name='loadingpic',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/loading.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "trial"----------------------------------------------------------------------------------------------------------------------------------------------------------
mouse = event.Mouse(win=win)
ScoreText=visual.TextStim(win=win, ori=0, name='ScoreText',
    text=u'$%i' %(score),
    font=u'BatmanForeverAlternate',
    units='pix', pos=[0, -460], height=50,wrapWidth=None,
    color=u'#FCC700', colorSpace=u'rgb', opacity=1,
    depth=-6.0)
click1=0
click2=0
click3=0
click4=0
totalclick=0
trialClock = core.Clock()
learningbackground = visual.ImageStim(win=win, name='learningbackground',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/learningbackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
trialbackground = visual.ImageStim(win=win, name='trialbackground',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/TrialBackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

diagnosis = visual.Slider(
    win=win,
    units='pix',
    name='diagnosis',
    ticks=(1, 2, 3, 4),
    labels=[diseases[0], diseases[1], diseases[2], diseases[3]],
    granularity=1,
    labelHeight=25, 
    labelColor='#00B7B5', 
    style=['rating'],#styleTweaks=['triangleMarker'],
    markerColor='#FCC700',
    size=(550, 30),
    font='BatmanForeverAlternate',
    pos=(0, 10),
    flip=True,
    lineColor='white',
)

submit_button = visual.ButtonStim(
    win=win,
    name='submit',
    text='SUBMIT',
    font='BatmanForeverAlternate',
    pos=(0, -100),
    size=(200, 50),
    fillColor='white',
    borderColor='#00B7B5',
    color='#00B7B5',
    letterHeight=25
)

GenImage=visual.ImageStim(win=win, name='GenImage', units='pix', 
    image=GENpics[0],mask=None,
    ori=0, pos=[0,460], size = [288, 72],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=False, depth=-11.0)
Test1Image=visual.ImageStim(win=win, name='TLImage',units='pix', 
    image=Test1pics[0], mask=None,
    ori=0, pos=imagelocation1, size=[310, 310],
    color=[1,1,1], colorSpace=u'rgb', opacity=0,
    texRes=128, interpolate=False, depth=-10.0)
Test1Text=visual.TextStim(win=win, ori=0, name='TLText',
    text=tests[0],
    font=u'BatmanForeverAlternate',
    units='pix', pos=textlocation1, height=35,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-6.0)
Test2Image=visual.ImageStim(win=win, name='TLImage',units='pix', 
    image=Test2pics[0], mask=None,
    ori=0, pos=imagelocation2, size=[310, 310],
    color=[1,1,1], colorSpace=u'rgb', opacity=0,
    texRes=128, interpolate=False, depth=-10.0)
Test2Text=visual.TextStim(win=win, ori=0, name='TRText',
    text=tests[1],
    font=u'BatmanForeverAlternate',
    units='pix', pos=textlocation2, height=35,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-7.0)
Test3Image=visual.ImageStim(win=win, name='TLImage',units='pix', 
    image=Test3pics[0], mask=None,
    ori=0, pos=imagelocation3, size=[310, 310],
    color=[1,1,1], colorSpace=u'rgb', opacity=0,
    texRes=128, interpolate=False, depth=-10.0)
Test3Text=visual.TextStim(win=win, ori=0, name='BLText',
    text=tests[2],
    font=u'BatmanForeverAlternate',
    units='pix', pos=textlocation3, height=35,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
Test4Image=visual.ImageStim(win=win, name='TLImage',units='pix', 
    image=Test4pics[0], mask=None,
    ori=0, pos=imagelocation4, size=[310, 310],
    color=[1,1,1], colorSpace=u'rgb', opacity=0,
    texRes=128, interpolate=False, depth=-10.0)
Test4Text=visual.TextStim(win=win, ori=0, name='BRText',
    text=tests[3],
    font=u'BatmanForeverAlternate',
    units='pix', pos=textlocation4, height=35,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-9.0)
Test1Shape=visual.Circle(win, pos=imagelocation1, fillColor=u'#004646', lineColor=u'#004646',
    radius=150, units='pix')
Test2Shape=visual.Circle(win, pos=imagelocation2, fillColor=u'#004646', lineColor=u'#004646',
    radius=150, units='pix')
Test3Shape=visual.Circle(win, pos=imagelocation3, fillColor=u'#004646', lineColor=u'#004646',
    radius=150, units='pix')
Test4Shape=visual.Circle(win, pos=imagelocation4, fillColor=u'#004646', lineColor=u'#004646',
    radius=150, units='pix')
Random1Shape=visual.Circle(win, pos=imagelocation1, fillColor=u'#FCC700', lineColor=u'#FCC700',
    radius=150, units='pix')
Random2Shape=visual.Circle(win, pos=imagelocation2, fillColor=u'#FCC700', lineColor=u'#FCC700',
    radius=150, units='pix')
Random3Shape=visual.Circle(win, pos=imagelocation3, fillColor=u'#FCC700', lineColor=u'#FCC700',
    radius=150, units='pix')
Random4Shape=visual.Circle(win, pos=imagelocation4, fillColor=u'#FCC700', lineColor=u'#FCC700',
    radius=150, units='pix')
Cost1Text=visual.TextStim(win=win, ori=0, name='Cost1Text',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=textlocation1, height=30,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-6.0)
Cost2Text=visual.TextStim(win=win, ori=0, name='Cost2Text',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=textlocation2, height=30,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-6.0)
Cost3Text=visual.TextStim(win=win, ori=0, name='Cost3Text',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=textlocation3, height=30,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-6.0)
Cost4Text=visual.TextStim(win=win, ori=0, name='Cost4Text',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=textlocation4, height=30,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "AIinstructions"----------------------------------------------------------------------------------------------------------------------------------------------------------
AIinstructionsClock = core.Clock()
backgroundinst2 = visual.ImageStim(win=win, name='AIinstructions',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructionsbackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=1.0)

AIinstructionstext = visual.TextStim(win=win, name='AIinstructionsText',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=(0, 0),height=30, wrapWidth=1200, color=u'#FCC700', colorSpace=u'rgb', opacity=1)

# AI prompt to user
PromptTextAdvice = visual.TextStim(win=win, name='PromptTextAdvice',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=(0, 220),height=20,wrapWidth=700, color=u'#FCC700', colorSpace=u'rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "feedback"----------------------------------------------------------------------------------------------------------------------------------------------------------
feedbackClock = core.Clock()
Correct=''
DiseaseState=''
backgroundfeedback = visual.ImageStim(win=win, name='backgroundfeedback',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/TrialBackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Result=visual.TextStim(win=win, ori=0, name='Result',
    text=u'Result:',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[0, -50], height=25,wrapWidth=1280,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-1.0)
Correct_Incorrect=visual.TextStim(win=win, ori=0, name='Correct_Incorrect',
    text=u'Correct!',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[0, -90], height=70,wrapWidth=None,
    color=u'#01FFFD', colorSpace=u'rgb', opacity=1,
    depth=0.0)
YourResponseText=visual.TextStim(win=win, ori=0, name='YourResponseText',
    text=u'Your diagnosis:',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[-180, 80], height=25,wrapWidth=1280,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-1.0)
YourResponse=visual.TextStim(win=win, ori=0, name='YourResponse',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[-180, 50], height=40,wrapWidth=1280,
    color=u'#01FFFD', colorSpace=u'rgb', opacity=1,
    depth=-1.0)
AnswerWas=visual.TextStim(win=win, ori=0, name='AnswerWas',
    text=u'Patient:',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[180, 80], height=25,wrapWidth=1280,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-1.0)
State=visual.TextStim(win=win, ori=0, name='State',
    text=u'disease',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[180, 50], height=40,wrapWidth=1280,
    color=u'#01FFFD', colorSpace=u'rgb', opacity=1,
    depth=-1.0)
Press=visual.TextStim(win=win, ori=0, name='Press',
    text=u'Press the SPACEBAR to continue.',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[0, -240], height=30,wrapWidth=1280,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "timeup"----------------------------------------------------------------------------------------------------------------------------------------------------------
timeupClock = core.Clock()
timeupText = visual.TextStim(win=win, ori=0, name='Press',
    text=u'Time is up!',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[0, 0], height=70,wrapWidth=1280,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)

#Initialize componenets for Routine "learningphaseend"
learningendClock= core.Clock()
learningphaseend = visual.ImageStim(win=win, name='background1phase2',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/learningphaseend.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

#Initialize componenets for Routine "btwrounds"
instructionsbtwroundsClock = core.Clock()
instructionsbtwrounds = visual.ImageStim(win=win, name='instructionsbtwrounds',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructionsbtwrounds.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

#Initialize components for Routine "phase2instr1"
phase2instr1Clock = core.Clock()
background1phase2 = visual.ImageStim(win=win, name='background1phase2',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructions2phase2.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
pricetext1 = visual.TextStim(win=win, ori=0, name='BLText',
    text=u'\n\n\n$250',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[-490,-230], height=35,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
pricetext2 = visual.TextStim(win=win, ori=0, name='BLText',
    text=u'\n\n\n2.5 s',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[490,-230], height=35,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-8.0)

#Initialize component for Routine "phase2instr2"
phase2instr2Clock = core.Clock()
background2phase2 = visual.ImageStim(win=win, name='background1phase2',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructions2phase2.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

#Initialize component for Routine "phase2instr3"
phase2instr3Clock = core.Clock()
background3phase2 = visual.ImageStim(win=win, name='background1phase2',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructions3phase2.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

#Initialize component for Routine "phase2instr4"
phase2instr4Clock = core.Clock()
background4phase2 = visual.ImageStim(win=win, name='background4phase2',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructions3phase2.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

#Initialize components for Routine "results"
resultsClock = core.Clock()
resultsbackground = visual.ImageStim(win=win, name='resultsbackground',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/results.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
learning1scoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[-285,410], height=35,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
learning2scoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[-285,410], height=35,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
learning3scoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[-285,410], height=35,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
learningscoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[-285,410], height=35,wrapWidth=None,
    color=u'#004646', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
round1scoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[-285,285], height=35,wrapWidth=None,
    color=u'#FCC700', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
round2scoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[-285,170], height=35,wrapWidth=None,
    color=u'#FCC700', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
round3scoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[-285,55], height=35,wrapWidth=None,
    color=u'#FCC700', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
round4scoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[-285,-60], height=35,wrapWidth=None,
    color=u'#FCC700', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
round5scoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[-285,-175], height=35,wrapWidth=None,
    color=u'#FCC700', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
round6scoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[-285,-290], height=35,wrapWidth=None,
    color=u'#FCC700', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
topscoretext = visual.TextStim(win=win, ori=0, name='learningscoretext',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=[490,-180], height=70,wrapWidth=None,
    color=u'#FCC700', colorSpace=u'rgb', opacity=1,
    depth=-8.0)

#Initialize components for Routine "debrief"
debrief1Clock = core.Clock()
debrief2Clock = core.Clock()
goodbyeClock = core.Clock()
debrief1 = visual.ImageStim(win=win, name='debrief1',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructionsbackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

debrief1text = visual.TextStim(win=win, name='debrief1Text',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=(0, 0),height=20, wrapWidth=1200, color=u'#FCC700', colorSpace=u'rgb', opacity=1, depth=-10.0)

debrief2text = visual.TextStim(win=win, name='debrief2Text',
    text=u'',
    font=u'BatmanForeverAlternate',
    units='pix', pos=(0, 0),height=30, wrapWidth=1200, color=u'#FCC700', colorSpace=u'rgb', opacity=1, depth=-10.0)

goodbye = visual.ImageStim(win=win, name='goodbye',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/goodbye.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
goodbyeglow = visual.ImageStim(win=win, name='goodbyeglow',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/goodbyeglow.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)

#Initialize components for Routine "readyforphase2"
instructions9 = visual.ImageStim(win=win, name='instructions9',units='pix', 
    image=u'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/instructions9.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
blockClock = core.Clock()

#_#START EXP###########################################################################################################################################################START EXP##################################################

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
instructions6Components.append(submit_button)
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
    frameN += 1  # number of completed frames (so 0 is the first frame)

    # *backgroundinst6* updates
    if t >= 0.0 and backgroundinst6.status == NOT_STARTED:
        # keep track of start time/frame for later
        backgroundinst6.draw()
        backgroundinst6.tStart = t  # underestimates by a little under one frame
        backgroundinst6.frameNStart = frameN  # exact frame index
    
    # Update diagnosis slider
    if t >= 0.0 and diagnosis.status == NOT_STARTED:
        diagnosis.tStart = t
        diagnosis.frameNStart = frameN
        diagnosis.setAutoDraw(True)
    
    # Update submit button
    if t >= 0.0 and submit_button.status == NOT_STARTED:
        submit_button.tStart = t
        submit_button.frameNStart = frameN
        submit_button.setAutoDraw(True) 

    # *GenImage* updates
    if t >= 0.0 and GenImage.status == NOT_STARTED:
        GenImage.tStart = t
        GenImage.frameNStart = frameN
        GenImage.setOpacity(1)
        GenImage.setAutoDraw(True)

    # Update shapes and text components
    for idx, shape in enumerate([Test1Shape, Test2Shape, Test3Shape, Test4Shape], start=1):
        # Update each TestShape
        if t >= 0.0 and shape.status == NOT_STARTED:
            shape.tStart = t
            shape.frameNStart = frameN
            shape.setAutoDraw(True)
            shape.status = STARTED

        if shape.status == STARTED:
            if mouse.isPressedIn(shape) and locals()[f'click{idx}'] < 1:
                locals()[f'Test{idx}Image'].setAutoDraw(True)
                locals()[f'Test{idx}Text'].setColor(u'#FCC700')
                locals()[f'Cost{idx}Text'].setColor(u'#FCC700')
                shape.setAutoDraw(False)
                locals()[f'Test{idx}Image'].setOpacity(1)
                locals()[f'Random{idx}Shape'].setAutoDraw(True)

            if shape.contains(mouse):
                locals()[f'Random{idx}Shape'].setAutoDraw(True)
                shape.setOpacity(0)
            else:
                locals()[f'Random{idx}Shape'].setAutoDraw(False)
                shape.setOpacity(1)

    # Check for response and button click
    if diagnosis.getRating() is not None:  # If a rating has been made
        if mouse.isPressedIn(submit_button):  # And submit button is clicked
            # Record response and reaction time
            diagnosis.response = diagnosis.getRating()
            diagnosis.rt = diagnosis.getRT()
            continueRoutine = False  # End routine

    # Check if all components have finished
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

# Define a dictionary of symptoms for each genoutcome
symptoms_dict = {1: "FEVER", 2: "RASH", 3: "MIGRAINE", 4: "ACHE"}

# Define a dictionary where each click_order corresponds to a specific test
tests_dict = {1: 'MRI', 2: 'CAT', 3: 'XRAY', 4: 'LAB'}

# Define a dictionary to map image file paths to genoutcome 
genoutcome_map = {
'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/fever.png': 1,
'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/rash.png': 2,
'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/migraine.png': 3,
'/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG//Images/ache.png': 4,
}

# Create a list to store the extracted values of click_order for each trial
click_order_values = []
# Initialize advice_names as a list
advice_names = []

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method=u'random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG/conditionsTest.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
blockClock.reset()
phase=2
block=1
# Initialize costs
#costs1 = 0  # Initially, no cost has been incurred
#cost_per_click = 100  # Each click incurs a $100 cost
#costs=costs1

# Calculate number of trials and balance condition distribution
num_trials = len(trials.trialList)  # Total number of trials
conditions = [1, 2] * (num_trials // 2)  # Ensure equal distribution of conditions
random.shuffle(conditions)  # Shuffle the conditions

# Assign the shuffled conditions to each trial in a balanced random manner
for i, thisTrial in enumerate(trials.trialList):
    thisTrial['condition'] = conditions[i]  # Add a 'condition' field to the trial

# Trial loop
for thisTrial in trials:
    current_condition = thisTrial['condition']  # Retrieve the condition for the current trial
    
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
    Rand1=np.random.random()
    Rand2=np.random.random()
    Rand3=np.random.random()
    Rand4=np.random.random()
    CueRand=np.random.random()
    
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

    # Retrieve the condition assigned to this trial
    current_condition = thisTrial['condition']

    #------Prepare to start Routine "trial"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    t = 0
    trialClock.reset()  # reset the trial clock
    frameN = -1
    # update component parameters for each repeat
    diagnosis.reset()  # reset diagnosis component

    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(learningbackground)  # Always include the background
    trialComponents.append(mouse)  # Always include mouse
    trialComponents.append(ScoreText)  # Always include ScoreText
    trialComponents.append(GenImage)  # Always include GENImage
    trialComponents.append(diagnosis)  # Always include diagnosis
    trialComponents.append(submit_button) # Always include submit_button
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
        

    # Initialize the status of components
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial"-------
    continueRoutine = True
    click1, click2, click3, click4 = 0, 0, 0, 0
    click1order, click2order, click3order, click4order = 0, 0, 0, 0
    totalclick = 0
    testsRemaining = 4 

    # Initialize the most common and least common click orders
    most_common_click_order_for_genoutcome = None
    least_common_click_order_for_genoutcome = None

    # Calculate the most common and least common click orders
    if click_order_dict[genoutcome]:  # Check if the list is not empty
        most_common_click_order_for_genoutcome = Counter(click_order_dict[genoutcome]).most_common(1)[0][0]
        least_common_click_order_for_genoutcome = Counter(click_order_dict[genoutcome]).most_common()[-1][0]

    shuffled_test_most = tests_dict.get(most_common_click_order_for_genoutcome, "Test Not Found")

    shuffled_test_least = tests_dict.get(least_common_click_order_for_genoutcome, "Test Not Found")

    symptom_name = symptoms_dict[genoutcome_map[GENpics[genoutcome - 1]]]  # Use the shuffled genoutcome to get the user-friendly name    
    original_test = None
    advice_name = None

    while continueRoutine:

        # get current time
        t = trialClock.getTime()
        b = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        
        # Update mouse status
        if t >= 0.0 and mouse.status == NOT_STARTED:
            mouse.tStart = t
            mouse.frameNStart = frameN
        
        # *trialbackground* updates
        if t >= 0.0 and learningbackground.status == NOT_STARTED:
            learningbackground.draw()
            learningbackground.tStart = t
            learningbackground.frameNStart = frameN

        # Update backgroundinst4
        #if t >= 0.0 and backgroundinst4.status == NOT_STARTED:
            #backgroundinst4.tStart = t
            #backgroundinst4.frameNStart = frameN
            #backgroundinst4.setAutoDraw(True)
        
        # Update diagnosis slider
        if t >= 0.0 and diagnosis.status == NOT_STARTED:
            diagnosis.tStart = t
            diagnosis.frameNStart = frameN
            diagnosis.setAutoDraw(True)

        # Update submit button
        if t >= 0.0 and submit_button.status == NOT_STARTED:
            submit_button.tStart = t
            submit_button.frameNStart = frameN
            submit_button.setAutoDraw(True) 

        # *GenImage* updates
        if t >= 0.0 and GenImage.status == NOT_STARTED:
            GenImage.tStart = t
            GenImage.frameNStart = frameN
            GenImage.setAutoDraw(True)

        # *ScoreText* updates
        if t >= 0.0 and ScoreText.status == NOT_STARTED:
            ScoreText.tStart = t
            ScoreText.frameNStart = frameN
            ScoreText.setAutoDraw(True)

        # Updates for Test texts (Test1Text, Test2Text, etc.)
        for i, testText in enumerate([Test1Text, Test2Text, Test3Text, Test4Text]):
            if t >= 0.0 and testText.status == NOT_STARTED:
                testText.tStart = t
                testText.frameNStart = frameN
                testText.setAutoDraw(True)

        # Test and Random Shape updates based on condition
        if current_condition == 1:  # Only include Test and Random components in Condition 1

            # Handle Test Shape click and hover functionality
            for i, (testShape, randomShape, testImage, testText, clickVar, testOutcome, clickOrderIdx) in enumerate(
                    [(Test1Shape, Random1Shape, Test1Image, Test1Text, click1, test1outcome, 1),
                    (Test2Shape, Random2Shape, Test2Image, Test2Text, click2, test2outcome, 2),
                    (Test3Shape, Random3Shape, Test3Image, Test3Text, click3, test3outcome, 3),
                    (Test4Shape, Random4Shape, Test4Image, Test4Text, click4, test4outcome, 4)]):
                
                # Start drawing the test shape
                if t >= 0.0 and testShape.status == NOT_STARTED:
                    testShape.tStart = t
                    testShape.frameNStart = frameN
                    testShape.setAutoDraw(True)
                    testShape.status = STARTED

                # Process clicks only if the testShape is clicked and testsRemaining > 0
                if testShape.status == STARTED and testsRemaining > 0:
                    if mouse.isPressedIn(testShape) and eval(f'click{clickOrderIdx}') < 1:
                        testImage.setAutoDraw(True)
                        testText.setColor(u'#FCC700')
                        eval(f'Cost{clickOrderIdx}Text').setColor(u'#FCC700')
                        ScoreText.draw()
                        testShape.setAutoDraw(False)
                        testImage.setOpacity(1)
                        randomShape.setAutoDraw(True)

                        # Increment click counters and remaining tests
                        totalclick += 1
                        testsRemaining -= 1

                        # Update the respective click variable to indicate this test was clicked
                        exec(f'click{clickOrderIdx}order = totalclick')
                        exec(f'click{clickOrderIdx} += 1')  # Set click variable to 1 when clicked
                        exec(f'test{clickOrderIdx}viewoutcome = testOutcome')  # Assign the outcome

                        if eval(f'click{clickOrderIdx}order') == 1:
                            click_order.append(clickOrderIdx)
                            genoutcome_order.append(genoutcome)
                            click_order_dict[genoutcome].append(clickOrderIdx)

                        # Update the cost and deduct from score
                        #costs1 += 100 
                        #score -= 100
                        
                        # Update the score text in every frame
                        #ScoreText._pygletTextObj.text = f"Costs: ${costs1}"

                    # Handle hover functionality
                    if testShape.contains(mouse):
                        randomShape.setAutoDraw(True)
                        testShape.setOpacity(0)
                    else:
                        randomShape.setAutoDraw(False)
                        testShape.setOpacity(1)

        # Bayesian Logic: Update posterior based on viewed outcomes
        prior = np.array([0.25, 0.25, 0.25, 0.25])  # Equal prior probabilities

        # Ensure that gen_probabilities is a NumPy array
        gen_probabilities = np.array(gen_probabilities)

        # Update posterior with the GEN outcome
        gen_likelihood = gen_probabilities[:, genoutcome - 1]  # Adjust for 0-indexing in NumPy
        posterior = prior * gen_likelihood  # Update posterior based on gen outcome
        posterior = posterior / posterior.sum()  # Normalize to ensure the posterior sums to 1
        print('Posteriors after GEN outcome:', posterior)

        # List of clicked test outcomes based on trial code click variables
        clicked_tests = [click1, click2, click3, click4]  # 1 means clicked, 0 means not clicked

        # Iterate over the test outcomes and update posterior only for clicked tests
        for test_idx, (testoutcome, clicked) in enumerate(zip([test1outcome, test2outcome, test3outcome, test4outcome], clicked_tests), start=1):
            test_col = f'Test {test_idx}'
            
            if clicked:
                print(f"\nProcessing {test_col} for test outcome: {testoutcome} (clicked)")

                # Extract the relevant likelihoods for each hypothesis based on the current test outcome
                matching_rows = test_probabilities[test_probabilities['Outcome'] == testoutcome]

                if matching_rows.empty:
                    print(f"No matching rows for Outcome: {testoutcome} in {test_col}")
                else:
                    print(f"Matching rows for {test_col}:\n{matching_rows[['Hypothesis', 'Outcome', test_col]]}")

                # Extract the relevant likelihoods
                test_likelihoods = matching_rows[test_col].values
                print(f"Test likelihoods: {test_likelihoods}")

                if test_likelihoods.size == 0:
                    raise ValueError(f"No matching test likelihoods for outcome {testoutcome} in {test_col}")

                # Update the posterior with the test likelihoods
                posterior *= test_likelihoods
                posterior = posterior / posterior.sum()  # Normalize
                print(f"Updated posterior after {test_col}: {posterior}")
            else:
                print(f"{test_col} was not clicked, skipping update for this test outcome.")

        # If no test outcome was clicked, posterior remains updated only with the GEN outcome
        # Determine the most probable disease state (maximum a posteriori estimate)

        # Get the indices of the sorted probabilities (descending order)
        sorted_indices = np.argsort(posterior)[::-1]

        # Top two most probable disease states
        CorrResp = sorted_indices[0] + 1  # Add 1 to account for zero-indexing
        SecondResp = sorted_indices[1] + 1  # Second most probable disease state

        # Check if the probabilities are tied (same for the most probable and second most probable)
        if posterior[sorted_indices[0]] == posterior[sorted_indices[1]]:
            print(f"Tie between disease states: {CorrResp} and {SecondResp}")
        else:
            print(f"Most probable disease state: {CorrResp}")
            SecondResp = None  # No tie, so the second response is not valid

        # Check for response and button click
        if diagnosis.getRating() is not None:  # If a rating has been made
            if mouse.isPressedIn(submit_button):  # And submit button is clicked
                # Record response and reaction time
                diagnosis.response = diagnosis.getRating()
                diagnosis.rt = diagnosis.getRT()
                continueRoutine = False  # End routine

        # Check if all components have finished
        if not continueRoutine:
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component is still running
                
        # Check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # Refresh the screen
        if continueRoutine:
            win.flip()
        else:
            routineTimer.reset()

    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # Convert CorrResp and SecondResp (if applicable) to disease names
    correct_disease = diseases[CorrResp - 1] 
    if SecondResp:
        second_disease = diseases[SecondResp - 1]
    else:
        second_disease = None
        
    diagnosed_disease = diseases[diagnosis.response - 1]

    # Compare disease names (CorrResp or SecondResp) with participant's response
    if correct_disease == diagnosed_disease or (second_disease and second_disease == diagnosed_disease):
        Correct = 1
    else:
        Correct = 0

    # Update score
    if Correct==1:
        score = score + 1000
    else:
        score = score
    
    # store data for trials (TrialHandler)
    trials.addData('Phase', phase)
    #trials.addData('Costs', costs)
    trials.addData('Block', block)
    #trials.addData('Trial', learningtrials.thisTrialN+1)
    trials.addData('Condition', current_condition)
    trials.addData('Genoutcome', genoutcome)
    trials.addData('Symptom', symptom_name)
    trials.addData('Diagnosis', diagnosis.getRating())
    trials.addData('Diagnosis', diagnosed_disease)
    trials.addData('Diseasename', correct_disease)
    #trials.addData('diagnosis.rt', diagnosis.getRT())
    #trials.addData('blockdiagnosis.rt', globaldiagnosistime)
    trials.addData('Diseasenumber', CorrResp)
    trials.addData('Seconddiseasename', second_disease)
    trials.addData('Seconddiseasenumber', SecondResp)
    sorted_index = sorted_indices + 1
    trials.addData('Sortedindices', sorted_index)
    trials.addData('Accuracy', Correct)
    trials.addData('Totalclick', totalclick)
    trials.addData('Click1.order', click1order)
    trials.addData('Click2.order', click2order)
    trials.addData('Click3.order', click3order)
    trials.addData('Click4.order', click4order)
    trials.addData('Click1', click1)
    trials.addData('Click2', click2)
    trials.addData('Click3', click3)
    trials.addData('Click4', click4)
    trials.addData('Test1outcome', test1outcome)
    trials.addData('Test2outcome', test2outcome)
    trials.addData('Test3outcome', test3outcome)
    trials.addData('Test4outcome', test4outcome)
    trials.addData('Viewtest1outcome', test1viewoutcome)
    trials.addData('Viewtest2outcome', test2viewoutcome)
    trials.addData('Viewtest3outcome', test3viewoutcome)
    trials.addData('Viewtest4outcome', test4viewoutcome)
    #trials.addData('click1.rt', clicktime1)
    #trials.addData('click2.rt', clicktime2)
    #trials.addData('click3.rt', clicktime3)
    #trials.addData('click4.rt', clicktime4)
    trials.addData('Score', score)
    trials.addData('Learningscore', learningscore)
    trials.addData('Block1score', block1score)
    trials.addData('Block2score', block2score)
    trials.addData('Most_common_click_order_for_genoutcome',most_common_click_order_for_genoutcome) 
    trials.addData('Least_common_click_order_for_genoutcome',least_common_click_order_for_genoutcome) 
    trials.addData('First test selected', click_order_values)

    # Before accessing click_order, check if there are any clicks made
    if click_order: 
        click_order_values = shuffled_to_original_tests[tests_dict[click_order[-1]]]
    else:
        click_order_values = None 
        print("No clicks made yet.")

    rep_data = {'Symptom': symptom_name, 'First test selected': click_order_values,'Accuracy': Correct}  
    trial_data.append(rep_data)
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
    for thisComponent in btwroundsComponents:
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

#------Prepare to start Routine "AIinstructions"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
AIinstructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
inst_key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
inst_key_resp_2.status = NOT_STARTED
# keep track of which components have finished
AIinstructionsComponents = []
AIinstructionsComponents.append(backgroundinst1)
AIinstructionsComponents.append(inst_key_resp_2)
AIinstructionsComponents.append(AIinstructionstext)
for thisComponent in AIinstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "AIinstructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = AIinstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *backgroundinst2* updates
    if t >= 0.0 and backgroundinst1.status == NOT_STARTED:
        # keep track of start time/frame for later
        backgroundinst1.tStart = t  # underestimates by a little under one frame
        backgroundinst1.frameNStart = frameN  # exact frame index
        backgroundinst1.setAutoDraw(True)

    if t >= 0.0 and backgroundinst1.status == STARTED:
        AIinstructionstext.text = 'IN THIS NEXT ROUND YOU WILL RECEIVE ADVICE FROM AN AI ADVISOR IN MOST BUT NOT ALL OF THE TRIALS.\n\n THE ADVICE WILL BE PRESENTED TO YOU BEFORE YOU SELECT A TEST. \n\nPLEASE READ THE ADVICE CAREFULLY BEFORE PROCEEDING. IT IS IMPORTANT TO PAY ATTENTION TO THE DETAILS PROVIDED BY EACH ADVISOR. \n\n IF YOU HAVE ANY QUESTIONS PLEASE ASK THE EXPERIMENTER. '
        AIinstructionstext.setAutoDraw(True)

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
    for thisComponent in AIinstructionsComponents:
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
for thisComponent in AIinstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#++Block2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Block2+++++++++++++++++++++++++++++++++++++++++++++
# Create an empty list to collect selected advice
selected_advice_list = []

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method=u'random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('/Users/ec531/Library/CloudStorage/Dropbox/PhD/Study3/Medical_Diagnosis_Game/MDG/conditionsTest.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
blockClock.reset()
phase=2
block=2
# Initialize costs
#costs1 = 0  # Initially, no cost has been incurred
#cost_per_click = 100  # Each click incurs a $100 cost
#costs=costs1

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
    Rand1=np.random.random()
    Rand2=np.random.random()
    Rand3=np.random.random()
    Rand4=np.random.random()
    CueRand=np.random.random()
    
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

    # New Bayesian Logic: Update posterior based on outcomes
    prior = np.array([0.25, 0.25, 0.25, 0.25])  # Equal prior probabilities

    # Ensure that gen_probabilities is a NumPy array
    gen_probabilities = np.array(gen_probabilities)

    # Update posterior with the GEN outcome
    gen_likelihood = gen_probabilities[:, genoutcome - 1]  # Adjust for 0-indexing in NumPy
    posterior = prior * gen_likelihood  # Update posterior based on gen outcome
    posterior = posterior / posterior.sum()  # Normalize to ensure the posterior sums to 1

    # Update posterior based on each test outcome
    for test_idx, testoutcome in enumerate([test1outcome, test2outcome, test3outcome, test4outcome], start=1):
        test_col = f'Test {test_idx}'
        print(f"\nProcessing {test_col} for test outcome: {testoutcome}")
        
        # Extract the relevant likelihoods for each hypothesis based on the current test outcome
        matching_rows = test_probabilities[test_probabilities['Outcome'] == testoutcome]
        
        if matching_rows.empty:
            print(f"No matching rows for Outcome: {testoutcome} in {test_col}")
        else:
            print(f"Matching rows for {test_col}:\n{matching_rows[['Hypothesis', 'Outcome', test_col]]}")
        
        # Extract the relevant likelihoods
        test_likelihoods = matching_rows[test_col].values
        print(f"Test likelihoods: {test_likelihoods}")
        
        if test_likelihoods.size == 0:
            raise ValueError(f"No matching test likelihoods for outcome {testoutcome} in {test_col}")
        
        # Update the posterior with the test likelihoods
        posterior *= test_likelihoods
        posterior = posterior / posterior.sum()  # Normalize
        print(f"Updated posterior after {test_col}: {posterior}")

    # Determine the most probable disease state (maximum a posteriori estimate)
    CorrResp = np.argmax(posterior) + 1  # Add 1 to account for zero-indexing
    print(f"Most probable disease state: {CorrResp}")

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

    #------Prepare to start Routine "trial"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    t = 0
    trialClock.reset()  # reset the trial clock
    frameN = -1
    # update component parameters for each repeat
    diagnosis.reset()  # reset diagnosis component

    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(learningbackground)
    trialComponents.append(mouse)
    trialComponents.append(ScoreText)
    trialComponents.append(GenImage)
    trialComponents.append(diagnosis)
    trialComponents.append(submit_button)
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
    clickDiagnosis = 0
    # Initialize `adviceTriggered` at the start of the routine
    adviceTriggered = False
    adviceVisible = False

    # Initialize the most common and least common click orders
    most_common_click_order_for_genoutcome = None
    least_common_click_order_for_genoutcome = None

    # Calculate the most common and least common click orders
    if click_order_dict[genoutcome]:  # Check if the list is not empty
        most_common_click_order_for_genoutcome = Counter(click_order_dict[genoutcome]).most_common(1)[0][0]
        least_common_click_order_for_genoutcome = Counter(click_order_dict[genoutcome]).most_common()[-1][0]

    shuffled_test_most = tests_dict.get(most_common_click_order_for_genoutcome, "Test Not Found")

    shuffled_test_least = tests_dict.get(least_common_click_order_for_genoutcome, "Test Not Found")

    symptom_name = symptoms_dict[genoutcome_map[GENpics[genoutcome - 1]]]  # Use the shuffled genoutcome to get the user-friendly name    
    original_test = None
    advice_name = None

    # Initialize advice variables with default messages
    DA_advice = "THIS IS YOUR AI ADVISOR.\nIs there stronger evidence for any of the other diseases when the patient has had a symptom?"
    FAC_advice = "THIS IS YOUR AI ADVISOR.\nDo we have a majority opinion in the team for which disease it is, given the symptom?"
    MOD_advice = "THIS IS YOUR AI ADVISOR.\nBefore committing to a disease, are there team members that have anything more to say?"
    NO_advice = "No specific advice available."

    # Define your advice options and corresponding names
    advice_options = [DA_advice, FAC_advice, MOD_advice, NO_advice]
    advice_names = ['DA', 'FAC', 'MOD', 'No Advice']

    # Create a random generator and choose one of the advice options randomly
    rng = np.random.default_rng()
    selected_index = rng.choice(len(advice_options))  # Randomly choose an index
    random_advice = advice_options[selected_index]    # Select the advice based on the random index
    advice_name = advice_names[selected_index]        # Keep track of which advice was chosen

    print(f"Selected advice: {advice_name}")
    
    while continueRoutine:

        # Get current time
        t = trialClock.getTime()
        b = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

        # Update mouse status
        if t >= 0.0 and mouse.status == NOT_STARTED:
            mouse.tStart = t
            mouse.frameNStart = frameN

        # *learningbackground* updates
        if t >= 0.0 and learningbackground.status == NOT_STARTED:
            learningbackground.draw()
            learningbackground.tStart = t
            learningbackground.frameNStart = frameN

        # Update diagnosis slider
        if t >= 0.0 and diagnosis.status == NOT_STARTED:
            diagnosis.tStart = t
            diagnosis.frameNStart = frameN
            diagnosis.setAutoDraw(True)
        
        # Update submit button
        if t >= 0.0 and submit_button.status == NOT_STARTED:
            submit_button.tStart = t
            submit_button.frameNStart = frameN
            submit_button.setAutoDraw(True) 

        # *GenImage* updates
        if t >= 0.0 and GenImage.status == NOT_STARTED:
            GenImage.tStart = t
            GenImage.frameNStart = frameN
            GenImage.setAutoDraw(True)

        # *ScoreText* updates
        if t >= 0.0 and ScoreText.status == NOT_STARTED:
            ScoreText.tStart = t
            ScoreText.frameNStart = frameN
            ScoreText.setAutoDraw(True)

        # Update the score text in every frame
        #ScoreText._pygletTextObj.text = f"Costs: ${costs1}"
    
        # Check for trigger conditions specific to the chosen advice
        if not adviceTriggered:
            if advice_name == 'DA':
                print("Checking DA advice trigger condition...")
                if diagnosis.getRating() is not None and clickDiagnosis < 1:  # First click triggers DA advice
                    adviceTriggered = True
                    adviceVisible = True  # Show advice on screen
                    clickDiagnosis += 1
                    # Customize the DA advice text with specific symptom name
                    random_advice = f"THIS IS YOUR AI ADVISOR.\nIs there stronger evidence for any of the other diseases when the patient has had {symptom_name}?"
                    print("DA advice triggered")

            elif advice_name == 'FAC':
                print("Checking FAC advice trigger condition...")
                if any(mouse.isPressedIn(shape) for shape in [Test1Shape, Test2Shape, Test3Shape, Test4Shape]):
                    adviceTriggered = True
                    adviceVisible = True
                    # Customize FAC advice text with specific symptom name
                    random_advice = f"THIS IS YOUR AI ADVISOR.\nDo we have a majority opinion in the team for which disease it is, given the {symptom_name}?"
                    print("FAC advice triggered")

            elif advice_name == 'MOD':
                print("Checking MOD advice trigger condition...")
                if diagnosis.getRating() is not None and clickDiagnosis < 1:  # First click triggers MOD advice
                    adviceTriggered = True
                    adviceVisible = True
                    clickDiagnosis += 1
                    random_advice = "THIS IS YOUR AI ADVISOR.\nBefore committing to a disease, are there team members that have anything more to say?"
                    print("MOD advice triggered")

            elif advice_name == 'No Advice':
                adviceTriggered = True
                print("No Advice selected; no specific advice to trigger")

        # Updates for Test texts (Test1Text, Test2Text, etc.)
        for i, testText in enumerate([Test1Text, Test2Text, Test3Text, Test4Text]):
            if t >= 0.0 and testText.status == NOT_STARTED:
                testText.tStart = t
                testText.frameNStart = frameN
                testText.setAutoDraw(True)

        # Updates for Random shapes and Test shapes (Test1Shape, Test2Shape, etc.)
        for i, (testShape, randomShape, testImage, testText, clickVar, costText, testOutcome, clickOrderIdx) in enumerate(
                [(Test1Shape, Random1Shape, Test1Image, Test1Text, click1, Cost1Text, test1outcome, 1),
                (Test2Shape, Random2Shape, Test2Image, Test2Text, click2, Cost2Text, test2outcome, 2),
                (Test3Shape, Random3Shape, Test3Image, Test3Text, click3, Cost3Text, test3outcome, 3),
                (Test4Shape, Random4Shape, Test4Image, Test4Text, click4, Cost4Text, test4outcome, 4)]):

            # Start the test shape if not started
            if t >= 0.0 and testShape.status == NOT_STARTED:
                testShape.tStart = t
                testShape.frameNStart = frameN
                testShape.setAutoDraw(True)
                testShape.status = STARTED

            # Handle test shape interactions when it is started
            if testShape.status == STARTED and testsRemaining > 0:
                
                # Handle click event
                if mouse.isPressedIn(testShape) and eval(f'click{clickOrderIdx}') < 1:
                    testImage.setAutoDraw(True)
                    testText.setColor(u'#FCC700')
                    costText.setColor(u'#FCC700')
                    ScoreText.draw()
                    testShape.setAutoDraw(False)
                    testImage.setOpacity(1)
                    randomShape.setAutoDraw(True)

                    # Increment click counters and remaining tests
                    totalclick += 1
                    testsRemaining -= 1

                    # Update the cost and deduct from score
                    #costs1 += 100
                    #score -= 100

                    # Update the score display
                    #ScoreText._pygletTextObj.text = f"Costs: ${costs1}"

                    # Track the click order and outcome
                    exec(f'click{clickOrderIdx}order = totalclick')
                    exec(f'click{clickOrderIdx} += 1')
                    exec(f'test{clickOrderIdx}viewoutcome = testOutcome')

                    if eval(f'click{clickOrderIdx}order') == 1:
                        click_order.append(clickOrderIdx)
                        genoutcome_order.append(genoutcome)
                        click_order_dict[genoutcome].append(clickOrderIdx)

                # Handle hover functionality
                if testShape.contains(mouse):
                    randomShape.setAutoDraw(True)
                    testShape.setOpacity(0)
                else:
                    randomShape.setAutoDraw(False)
                    testShape.setOpacity(1)

        # Bayesian Logic: Update posterior based on viewed outcomes
        prior = np.array([0.25, 0.25, 0.25, 0.25])  # Equal prior probabilities

        # Ensure that gen_probabilities is a NumPy array
        gen_probabilities = np.array(gen_probabilities)

        # Update posterior with the GEN outcome
        gen_likelihood = gen_probabilities[:, genoutcome - 1]  # Adjust for 0-indexing in NumPy
        posterior = prior * gen_likelihood  # Update posterior based on gen outcome
        posterior = posterior / posterior.sum()  # Normalize to ensure the posterior sums to 1
        print('Posteriors after GEN outcome:', posterior)

        # List of clicked test outcomes based on trial code click variables
        clicked_tests = [click1, click2, click3, click4]  # 1 means clicked, 0 means not clicked

        # Iterate over the test outcomes and update posterior only for clicked tests
        for test_idx, (testoutcome, clicked) in enumerate(zip([test1outcome, test2outcome, test3outcome, test4outcome], clicked_tests), start=1):
            test_col = f'Test {test_idx}'
            
            if clicked:
                print(f"\nProcessing {test_col} for test outcome: {testoutcome} (clicked)")

                # Extract the relevant likelihoods for each hypothesis based on the current test outcome
                matching_rows = test_probabilities[test_probabilities['Outcome'] == testoutcome]

                if matching_rows.empty:
                    print(f"No matching rows for Outcome: {testoutcome} in {test_col}")
                else:
                    print(f"Matching rows for {test_col}:\n{matching_rows[['Hypothesis', 'Outcome', test_col]]}")

                # Extract the relevant likelihoods
                test_likelihoods = matching_rows[test_col].values
                print(f"Test likelihoods: {test_likelihoods}")

                if test_likelihoods.size == 0:
                    raise ValueError(f"No matching test likelihoods for outcome {testoutcome} in {test_col}")

                # Update the posterior with the test likelihoods
                posterior *= test_likelihoods
                posterior = posterior / posterior.sum()  # Normalize
                print(f"Updated posterior after {test_col}: {posterior}")
            else:
                print(f"{test_col} was not clicked, skipping update for this test outcome.")

        # If no test outcome was clicked, posterior remains updated only with the GEN outcome
        # Determine the most probable disease state (maximum a posteriori estimate)

        # Get the indices of the sorted probabilities (descending order)
        sorted_indices = np.argsort(posterior)[::-1]

        # Top two most probable disease states
        CorrResp = sorted_indices[0] + 1  # Add 1 to account for zero-indexing
        SecondResp = sorted_indices[1] + 1  # Second most probable disease state

        # Check if the probabilities are tied (same for the most probable and second most probable)
        if posterior[sorted_indices[0]] == posterior[sorted_indices[1]]:
            print(f"Tie between disease states: {CorrResp} and {SecondResp}")
        else:
            print(f"Most probable disease state: {CorrResp}")
            SecondResp = None  # No tie, so the second response is not valid

        # Toggle advice visibility based on clicks
        if adviceTriggered and adviceVisible and mouse.getPressed()[0]:  # Any subsequent click hides advice
            adviceVisible = False  # Hide advice on next click
            print("Advice hidden on subsequent click")

        # Display or hide advice based on visibility state
        if adviceVisible:
            PromptTextAdvice.text = random_advice  # Set the advice text
            PromptTextAdvice.setAutoDraw(True)     # Show advice text
        else:
            PromptTextAdvice.setAutoDraw(False)    # Hide advice text

        # Check for response and button click
        if diagnosis.getRating() is not None and mouse.isPressedIn(submit_button):
                diagnosis.response = diagnosis.getRating()
                diagnosis.rt = diagnosis.getRT()
                continueRoutine = False

        # Check if all components have finished
        if not continueRoutine:
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        
        continueRoutine = False  # will revert to True if at least one component is still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component is still running

        # Check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # Refresh the screen
        if continueRoutine:
            win.flip()
        else:
            routineTimer.reset()

    # -------Ending Routine "trial"-------

    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    print(f"Correct Response (CorrResp): {CorrResp}")
    print(f"Participant's Response (diagnosis.response): {diagnosis.response}")

    # Convert CorrResp (integer) to the corresponding disease name
    correct_disease = diseases[CorrResp - 1]  # CorrResp is 1-indexed, so adjust by -1

    print(f"Correct Disease (correct_disease): {correct_disease}")

    if correct_disease==diagnosis.response:
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
    trials.addData('Phase', phase)
    #trials.addData('Costs', costs)
    trials.addData('Block', block)
    #trials.addData('Trial', learningtrials.thisTrialN+1)
    trials.addData('Condition', current_condition)
    trials.addData('Genoutcome', genoutcome)
    trials.addData('Symptom', symptom_name)
    trials.addData('Diagnosis', diagnosis.getRating())
    trials.addData('Diseasename', correct_disease)
    #trials.addData('diagnosis.rt', diagnosis.getRT())
    #trials.addData('blockdiagnosis.rt', globaldiagnosistime)
    trials.addData('Diseasenumber', CorrResp)
    trials.addData('Seconddiseasename', second_disease)
    trials.addData('Seconddiseasenumber', SecondResp)
    sorted_index = sorted_indices + 1
    trials.addData('Sortedindices', sorted_index)
    trials.addData('Accuracy', Correct)
    trials.addData('Totalclick', totalclick)
    trials.addData('Click1.order', click1order)
    trials.addData('Click2.order', click2order)
    trials.addData('Click3.order', click3order)
    trials.addData('Click4.order', click4order)
    trials.addData('Click1', click1)
    trials.addData('Click2', click2)
    trials.addData('Click3', click3)
    trials.addData('Click4', click4)
    trials.addData('Test1outcome', test1outcome)
    trials.addData('Test2outcome', test2outcome)
    trials.addData('Test3outcome', test3outcome)
    trials.addData('Test4outcome', test4outcome)
    trials.addData('Viewtest1outcome', test1viewoutcome)
    trials.addData('Viewtest2outcome', test2viewoutcome)
    trials.addData('Viewtest3outcome', test3viewoutcome)
    trials.addData('Viewtest4outcome', test4viewoutcome)
    #trials.addData('click1.rt', clicktime1)
    #trials.addData('click2.rt', clicktime2)
    #trials.addData('click3.rt', clicktime3)
    #trials.addData('click4.rt', clicktime4)
    trials.addData('Score', score)
    trials.addData('Learningscore', learningscore)
    trials.addData('Block1score', block1score)
    trials.addData('Block2score', block2score)
    trials.addData('Most_common_click_order_for_genoutcome',most_common_click_order_for_genoutcome) 
    trials.addData('Least_common_click_order_for_genoutcome',least_common_click_order_for_genoutcome) 
        # Collect advice data 
    if random_advice == DA_advice:
        advice_name = 'DA'
    elif random_advice == FAC_advice:
        advice_name = 'FAC'
    elif random_advice == MOD_advice:
        advice_name = 'MOD'
    else:
        advice_name = 'NO Advice'
    click_order_values = shuffled_to_original_tests[tests_dict[click_order[-1]]]
    trials.addData('Advisor', advice_name) 
    trials.addData('Advice Text', random_advice) 
    trials.addData('Advice', original_test) 
    trials.addData('First test selected', click_order_values)

    rep_data = {'Symptom':symptom_name, 'Advisor': advice_name,'Advice': original_test, 'First test selected': click_order_values,  'Click_order': click_order, 'Genoutcome_order': genoutcome_order,'First test per symptom': click_order_dict} 
    trial_data.append(rep_data)
    thisExp.nextEntry()

    trial_data_df = pd.DataFrame(trial_data)
    trial_data_df.to_csv(filename + '_trial_data.csv', index=False)

# completed n repeats of 'trials'==========================================================================================================================================Block2============================================

block2score = score
score = block2score

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
    #if t >= 0.0 and learningscoretext.status == NOT_STARTED:
        #learningscoretext.tStart = t
        #learningscoretext.frameNStart = frameN
        #learningscoretext.setText('$%i' %(learningscore))
        #learningscoretext.setAutoDraw(True)
    
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
debrief1Components.append(debrief1)
debrief1Components.append(deb_key_resp_1)
debrief1Components.append(debrief1text)
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
    
    # *debrief1* updates
    if t >= 0.0 and debrief1.status == NOT_STARTED:
        # keep track of start time/frame for later
        debrief1.tStart = t  # underestimates by a little under one frame
        debrief1.frameNStart = frameN  # exact frame index
        debrief1.setAutoDraw(True)
    
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

    # debrief1 text
    if t >= 0.0 and debrief1text.status == NOT_STARTED:
        debrief1text.text = 'THE GOAL OF THIS STUDY WAS TO INVESTIGATE THE INFLUENCE OF AI ADVICE ON YOUR PERFORMANCE WITHIN THE MEDICAL DIAGNOSIS GAME. SPECIFICALLY, WE WERE EXAMINING HOW YOU SEARCHED FOR NEW INFORMATION WHEN FORMING THE DIAGNOSIS (ILLINGWORTH, 2020). \n\nIN THE FIRST PHASE WE WERE ALSO INTERESTED IN HOW YOU USED THE INFORMATION AVAILABLE WITHIN THE TRIAL, WHICH WE EXAMINED BY VARYING WHEN YOU WERE ABLE TO SEE TEST RESULTS. \n\nIN THE SECOND PHASE, THE NUMBER AND ORDER OF TESTS THAT YOU SELECTED, IN COMBINATION WITH THE SYMPTOM YOU WERE SHOWN AND FINAL DIAGNOSIS WERE ALL BEING ANALYZED. THE ANALYSIS COMPARED THE TRIALS THAT WERE PERFORMED WITH AND WITHOUT THE AI ADVICE. \n\nYOU WERE RANDOMLY ASSIGNED TO THE NO COSTS GROUP. THERE WAS ALSO A GROUP WHO PERFORMED THIS STUDY THAT INCURRED COSTS FOR EVERY TEST THEY CHOSE TO VIEW. WE WILL ANALYSE THE DIFFERENCE IN STRATEGIES BETWEEN THE COSTS AND NO COSTS GROUPS. \n\nIN ADDITION, THE AI ADVICE CAME IN ONE OF THREE ROLES. EACH ROLE PROVIDED A SUGGESTION BASED ON HOW YOU PREVIOUSLY SELECTED TESTS WHEN SHOWN A PARTICULAR SYMPTOM. ONE ROLE ENCOURAGED YOU TO REQUEST A DIFFERENT TEST TO THAT WHICH YOU PREVIOUSLY REQUESTED. A SECOND ROLE ENCOURAGED YOU TO CONSIDER REQUESTING THE TEST THAT YOU HAD LEAST REQUESTED. THE THIRD ROLE ENCOURAGED YOU TO SELECT THE TEST THAT YOU HAD REQUESTED MOST OFTEN. \n\nWE EXPECT THAT THE AI ADVICE WILL INFLUENCE HOW MANY TESTS YOU REQUESTED AND WHICH TESTS YOU REQUESTED (ILLINGWORTH, 2020). THE INFLUENCE IS ALSO EXPECTED TO DIFFER DEPENDING ON WHICH ROLE PROVIDED THE ADVICE (MATHIEU ET AL., 2008). THE RESULT FROM THIS STUDY WILL BE USED TO INSIGHT AS TO HOW AI MAY BE ABLE TO ASSIST HUMAN DECISION-MAKERS BY OFFERING ADVICE.'
        debrief1text.setAutoDraw(True)

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
debrief2Components.append(debrief1)
debrief2Components.append(deb_key_resp_2)
debrief2Components.append(debrief2text)
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
    
    # *debrief1* updates
    if t >= 0.0 and debrief1.status == NOT_STARTED:
        # keep track of start time/frame for later
        debrief1.tStart = t  # underestimates by a little under one frame
        debrief1.frameNStart = frameN  # exact frame index
        debrief1.setAutoDraw(True)
    
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

    # debrief2 text
    if t >= 0.0 and debrief2text.status == NOT_STARTED:
        debrief2text.text = 'DUE TO THE SENSITIVE NATURE OF THE RESEARCH PROCESS, PLEASE DO NOT DISCUSS THIS PROCEDURE WITH OTHER PEOPLE THAT MAY PARTICIPATE IN THIS EXPERIMENT. \n\nIF YOU HAVE ANY IMMEDIATE QUESTIONS YOU CAN ASK THE EXPERIMENTER OR IF YOU HAVE ANY QUESTIONS AT A LATER STAGE YOU CAN EMAIL EOIN CREMEN (EC531@BATH.AC.UK). \n\nIF YOU HAVE ANY ETHICAL CONCERNS RELATED TO YOUR PARTICIPATION IN THIS STUDY, PLEASE DIRECT THEM TO THE SOCIAL SCIENCES RESEARCH ETHICS COMMIITTEE (SOCIAL-SCIENCE-REC@BATH.AC.UK).'
        debrief2text.setAutoDraw(True)
    
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
