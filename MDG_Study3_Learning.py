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
_thisDir = os.path.dirname(os.path.abspath('X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG/')) 
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'MDG_Study3_Learning'
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
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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
GENpics=[('X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/fever.png'),('X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/rash.png'),('X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/migraine.png'),('X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/ache.png')]
np.random.shuffle(GENpics)
MRIpics=[('X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/MRI - POS.png'),('X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/MRI - NEUT.png'),('X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/MRI - NEG.png')]
LABpics=[('X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/LAB - POS.png'),('X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/LAB - NEUT.png'),('X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/LAB - NEG.png')]
XRAYpics=[('X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/RAY - POS.png'),('X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/RAY - NEUT.png'),('X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/RAY - NEG.png')]
CATpics=[('X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/CAT - POS.png'),('X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/CAT - NEUT.png'),('X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/CAT - NEG.png')]
symptoms=[('FEVER'), ('RASH'), ('MIGRAINE'),('ACHE')]

# Mapping shuffled test names to original test names
shuffled_to_original_tests = {original_test: shuffled_test for original_test, shuffled_test in zip(tests_copy, tests)}

# The probability structure for the presenting cue (GENImage)
gen_probabilities = np.array([[0.70, 0.10, 0.10, 0.10],
                              [0.10, 0.70, 0.10, 0.10],
                              [0.10, 0.10, 0.70, 0.10],
                              [0.10, 0.10, 0.10, 0.70]])

# The probability structure for the test outcomes
test_probabilities = pd.DataFrame({
    'Hypothesis': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],
    'Outcome': [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    'Test 1': [0.95, 0.03, 0.02, 0.02, 0.49, 0.49, 0.02, 0.49, 0.49, 0.02, 0.49, 0.49],
    'Test 2': [0.02, 0.49, 0.49, 0.95, 0.03, 0.02, 0.02, 0.49, 0.49, 0.02, 0.49, 0.49],
    'Test 3': [0.02, 0.49, 0.49, 0.02, 0.49, 0.49, 0.95, 0.03, 0.02, 0.02, 0.49, 0.49],
    'Test 4': [0.02, 0.49, 0.49, 0.02, 0.49, 0.49, 0.02, 0.49, 0.49, 0.95, 0.03, 0.02]
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
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructionsbackground.png', mask=None,
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
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructionsbackground.png', mask=None,
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
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/outcomes.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "instructions4.1"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions4Clock = core.Clock()
backgroundinst4 = visual.ImageStim(win=win, name='backgroundinst4',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructions4.1.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "instructions4.2"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions42Clock = core.Clock()
backgroundinst42 = visual.ImageStim(win=win, name='backgroundinst4',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructions4.2.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


# Initialize components for Routine "instructions4.3"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions43Clock = core.Clock()
backgroundinst43 = visual.ImageStim(win=win, name='backgroundinst4',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructions4.3.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "instructions5"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions5Clock = core.Clock()
backgroundinst5 = visual.ImageStim(win=win, name='backgroundinst5',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructionsbackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
dplinst5 = visual.ImageStim(win=win, name='dplinst5',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructions5.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
inst5pic = visual.ImageStim(win=win, name='inst5pic',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructions5.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "instructions6"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions6Clock = core.Clock()
backgroundinst6 = visual.ImageStim(win=win, name='backgroundinst6',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructions6.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "instructions7"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions7Clock = core.Clock()
instr7pic = visual.ImageStim(win=win, name='instr7pic',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructions7.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "instructions8"----------------------------------------------------------------------------------------------------------------------------------------------------------
instructions8Clock = core.Clock()
backgroundinst8 = visual.ImageStim(win=win, name='backgroundinst8',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructionsbackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
dplinst8 = visual.ImageStim(win=win, name='dplinst8',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructions8.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
inst8pic = visual.ImageStim(win=win, name='inst8pic',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructions8.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "start"----------------------------------------------------------------------------------------------------------------------------------------------------------
startClock = core.Clock()
startglow = visual.ImageStim(win=win, name='startglow',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/startglow.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
startpic = visual.ImageStim(win=win, name='startpic',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/start.png', mask=None,
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
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/TrialBackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
loadingpic = visual.ImageStim(win=win, name='loadingpic',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/loading.png', mask=None,
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
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/learningbackground.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
trialbackground = visual.ImageStim(win=win, name='trialbackground',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/TrialBackground.png', mask=None,
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
    pos=(0, -100),  # Positioned below the slider
    size=(200, 50),
    fillColor='white',  # Transparent fill
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
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructionsbackground.png', mask=None,
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
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/TrialBackground.png', mask=None,
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
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/learningphaseend.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

#Initialize componenets for Routine "btwrounds"
instructionsbtwroundsClock = core.Clock()
instructionsbtwrounds = visual.ImageStim(win=win, name='instructionsbtwrounds',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructionsbtwrounds.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

#Initialize components for Routine "phase2instr1"
phase2instr1Clock = core.Clock()
background1phase2 = visual.ImageStim(win=win, name='background1phase2',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructions2phase2.png', mask=None,
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
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructions2phase2.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

#Initialize component for Routine "phase2instr3"
phase2instr3Clock = core.Clock()
background3phase2 = visual.ImageStim(win=win, name='background1phase2',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructions3phase2.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

#Initialize component for Routine "phase2instr4"
phase2instr4Clock = core.Clock()
background4phase2 = visual.ImageStim(win=win, name='background4phase2',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructions3phase2.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

#Initialize components for Routine "results"
resultsClock = core.Clock()
resultsbackground = visual.ImageStim(win=win, name='resultsbackground',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/results.png', mask=None,
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
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructionsbackground.png', mask=None,
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
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/goodbye.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
goodbyeglow = visual.ImageStim(win=win, name='goodbyeglow',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/goodbyeglow.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)

#Initialize components for Routine "readyforphase2"
instructions9 = visual.ImageStim(win=win, name='instructions9',units='pix', 
    image=u'X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG//Images/instructions9.png', mask=None,
    ori=0, pos=[0, 0], size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
blockClock = core.Clock()

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
instructions1Components.append(instructions1text)
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
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False

    # instructions1 text
    if t >= 0.0 and instructions1text.status == NOT_STARTED:
        instructions1text.text = 'THANK YOU FOR AGREEING TO PARTICIPATE IN THIS STUDY. \nTO BEGIN, YOU WILL FIRST LEARN TO PLAY THE MEDICAL DIAGNOSIS GAME.\n\nIT IS IMPORTANT THAT YOU READ THESE INSTRUCTIONS CAREFULLY TO UNDERSTAND WHAT YOU WILL BE DOING DURING THE GAME.\n\nPLEASE DO NOT TAKE ANY NOTES DURING THE GAME.\n\nPRESS THE SPACE BAR TO CONTINUE.'
        instructions1text.setAutoDraw(True)
    
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
instructions2Components.append(inst_key_resp_2)
instructions2Components.append(instructions2text)
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

    if t >= 0.0 and backgroundinst2.status == STARTED:
        # instructions2 text
        instructions2text.text = 'THE GAME HAS TWO PARTS, EACH PART WITH THE SAME GOAL: TO EARN AS MANY POINTS ($) AS YOU POSSIBLE CAN.\n\nTO ACHIEVE THIS GOAL, YOU WILL BE TAKING ON THE ROLE OF A MEDICAL DOCTOR DIAGNOSING PATIENTS. FOR EACH PATIENT THAT YOU CORRECTLY DIAGNOSE, $1,000 WILL BE ADDED TO YOUR SCORE. \n\nALL THE PATIENTS WILL HAVE ONE OF FOUR FICTITIOUS DISEASES: METALYTIS, ZYMOSIS, GWARONIA, OR DESCOLADA.\n\nYOU WILL FIRST BE SHOWN THE SYMPTOM OR SIGN THAT PATIENT HAS. THESE CAN BE EITHER: MIGRAINE, FEVER, ACHE, OR RASH.\n\nTO HELP YOU MAKE THE DIAGNOSIS YOU CAN VIEW UP TO FOUR TESTS: MRI SCAN, CAT SCAN, XRAY, AND LAB TEST.\nTHESE TESTS WILL BE AVAILABLE IN SOME, BUT NOT ALL, CASES.'
        instructions2text.setAutoDraw(True)

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

#------Prepare to start Routine "instructions4"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
t = 0
instructions4Clock.reset()  # clock
frameN = -1
# update component parameters for each repeat
diagnosis.reset()

# Create mouse object once at the start of the routine
mouse = event.Mouse(win=win)

# keep track of which components have finished
instructions4Components = []
instructions4Components.append(backgroundinst4)
instructions4Components.append(diagnosis)
instructions4Components.append(submit_button)
instructions4Components.append(GenImage)
for thisComponent in instructions4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions4"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions4Clock.getTime()
    frameN += 1  # number of completed frames (so 0 is the first frame)
    
    # Update backgroundinst4
    if t >= 0.0 and backgroundinst4.status == NOT_STARTED:
        backgroundinst4.tStart = t
        backgroundinst4.frameNStart = frameN
        backgroundinst4.setAutoDraw(True)
    
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
    
    # Update GenImage
    if t >= 0.0 and GenImage.status == NOT_STARTED:
        GenImage.tStart = t
        GenImage.frameNStart = frameN
        GenImage.setOpacity(1)
        GenImage.setAutoDraw(True)
    
    # Check for response and button click
    if diagnosis.getRating() is not None:  # If a rating has been made
        if mouse.isPressedIn(submit_button):  # And submit button is clicked
            # Record response and reaction time
            diagnosis.response = diagnosis.getRating()
            diagnosis.rt = diagnosis.getRT()
            continueRoutine = False  # End routine
    
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

#-------End Routine "instructions4"-------

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
instructions42Components.append(submit_button)
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

    # *backgroundinst42* updates
    if t >= 0.0 and backgroundinst42.status == NOT_STARTED:
        # keep track of start time/frame for later
        backgroundinst42.draw()
        backgroundinst42.tStart = t  # underestimates by a little under one frame
        backgroundinst42.frameNStart = frameN  # exact frame index

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

    # Check for response and button click
    if diagnosis.getRating() is not None:  # If a rating has been made
        if mouse.isPressedIn(submit_button):  # And submit button is clicked
            # Record response and reaction time
            diagnosis.response = diagnosis.getRating()
            diagnosis.rt = diagnosis.getRT()
            continueRoutine = False  # End routine

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
instructions43Components.append(submit_button)
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
    
    # Update backgroundinst4
    if t >= 0.0 and backgroundinst4.status == NOT_STARTED:
        backgroundinst4.tStart = t
        backgroundinst4.frameNStart = frameN
        backgroundinst4.setAutoDraw(True)

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
        
    # Check for response and button click
    if diagnosis.getRating() is not None:  # If a rating has been made
        if mouse.isPressedIn(submit_button):  # And submit button is clicked
            # Record response and reaction time
            diagnosis.response = diagnosis.getRating()
            diagnosis.rt = diagnosis.getRT()
            continueRoutine = False  # End routine
    
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
startComponents.append(backgroundinst1)
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
    if t >= 0.0 and backgroundinst1.status == NOT_STARTED:
        # keep track of start time/frame for later
        backgroundinst1.tStart = t  # underestimates by a little under one frame
        backgroundinst1.frameNStart = frameN  # exact frame index
        backgroundinst1.setAutoDraw(True)
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
# set up handler to look after randomisation of conditions etc
learningtrials = data.TrialHandler(nReps=1, method=u'random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG/conditionsTest1.xlsx'),
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
    print('Posteriors after GEN outcome:', posterior)

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
        print(f"Updated posterior after {test_col}: {posterior}")\

    # Determine the most probable disease state (maximum a posteriori estimate)
    #CorrResp = np.argmax(posterior) + 1  # Add 1 to account for zero-indexing
    #print(f"Most probable disease state: {CorrResp}")
    
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
    
    #------Prepare to start Routine "trial"-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    diagnosis.reset()
    submit_button.reset()
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(learningbackground)
    trialComponents.append(mouse)
    trialComponents.append(ScoreText)
    trialComponents.append(diagnosis)
    trialComponents.append(submit_button)
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
    
        # Check for response and button click
        if diagnosis.getRating() is not None:  # If a rating has been made
            if mouse.isPressedIn(submit_button):  # And submit button is clicked
                # Record response and reaction time
                diagnosis.response = diagnosis.getRating()
                diagnosis.rt = diagnosis.getRT()
                continueRoutine = False  # End routine

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
    print(f"Correct Response (CorrResp): {CorrResp}")
    print(f"Participant's Response (diagnosis.response): {diagnosis.response}")

    # Convert CorrResp (integer) to the corresponding disease name
    correct_disease = diseases[CorrResp - 1]  # CorrResp is 1-indexed, so adjust by -1
    diagnosed_disease = diseases[diagnosis.response - 1]

    print(f"Correct Disease (correct_disease): {correct_disease}")
    print(f"Participant diagnosed (diagnosed_disease): {diagnosed_disease}")

    # Compare disease names instead of comparing an integer to a string
    if correct_disease == diagnosed_disease:
        Correct = 1
    else:
        Correct = 0

    YourResponse.setText(f"{diagnosed_disease}")  # Display the participant's diagnosis

    # Feedback to participant
    if Correct == 1:
        Correct_Incorrect.setText('Correct!')
        score = score + 1000  # Award points for correct response
    else:
        Correct_Incorrect.setText('Incorrect')
        score = score  # No score change for incorrect response

    # Display the correct disease state
    State.setText(correct_disease)  # Now correctly shows the disease name

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
    learningtrials.addData('Phase', phase)
    learningtrials.addData('Costs', costs)
    learningtrials.addData('Block', block)
    learningtrials.addData('Trial', learningtrials.thisTrialN+1)
    learningtrials.addData('Genoutcome', genoutcome)
    learningtrials.addData('Diagnosis', diagnosis.getRating())
    learningtrials.addData('Diagnosis', diagnosed_disease)
    learningtrials.addData('Diseasename', correct_disease)
    #learningtrials.addData('diagnosis.rt', diagnosis.getRT())
    #learningtrials.addData('blockdiagnosis.rt', globaldiagnosistime)
    learningtrials.addData('Diseasenumber', CorrResp)
    learningtrials.addData('Accuracy', Correct)
    #learningtrials.addData('totalclick', totalclick)
    #learningtrials.addData('click1.order', click1order)
    #learningtrials.addData('click2.order', click2order)
    #learningtrials.addData('click3.order', click3order)
    #learningtrials.addData('click4.order', click4order)
    #learningtrials.addData('click1', click1)
    #learningtrials.addData('click2', click2)
    #learningtrials.addData('click3', click3)
    #learningtrials.addData('click4', click4)
    #learningtrials.addData('test1outcome', test1outcome)
    #learningtrials.addData('test2outcome', test2outcome)
    #learningtrials.addData('test3outcome', test3outcome)
    #learningtrials.addData('test4outcome', test4outcome)
    #learningtrials.addData('viewtest1outcome', test1viewoutcome)
    #learningtrials.addData('viewtest2outcome', test2viewoutcome)
    #learningtrials.addData('viewtest3outcome', test3viewoutcome)
    #learningtrials.addData('viewtest4outcome', test4viewoutcome)
    #learningtrials.addData('click1.rt', clicktime1)
    #learningtrials.addData('click2.rt', clicktime2)
    #learningtrials.addData('click3.rt', clicktime3)
    #learningtrials.addData('click4.rt', clicktime4)
    #learningtrials.addData('score', score)
    learningtrials.addData('Learningscore', learningscore)
    learningtrials.addData('Block1score', block1score)
    learningtrials.addData('Block2score', block2score)
    thisExp.nextEntry()
    
# completed n repeats of 'trials'=============================================================================================================================================Learning3============================================
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
# set up handler to look after randomisation of conditions etc
learningtrials = data.TrialHandler(nReps=1, method=u'random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('X:/Psychology/ResearchProjects/JAHoffmann/PhDCremenAITeams/Projects/Study3/Medical_Diagnosis_Game/MDG/conditionsTest1.xlsx'),
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

    # New Bayesian Logic: Update posterior based on outcomes
    prior = np.array([0.25, 0.25, 0.25, 0.25])  # Equal prior probabilities

    # Ensure that gen_probabilities is a NumPy array
    gen_probabilities = np.array(gen_probabilities)

    # Update posterior with the GEN outcome
    gen_likelihood = gen_probabilities[:, genoutcome - 1]  # Adjust for 0-indexing in NumPy
    posterior = prior * gen_likelihood  # Update posterior based on gen outcome
    posterior = posterior / posterior.sum()  # Normalize to ensure the posterior sums to 1
    print('Posteriors after GEN outcome:', posterior)

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
    #CorrResp = np.argmax(posterior) + 1  # Add 1 to account for zero-indexing
    #print(f"Most probable disease state: {CorrResp}")
    
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
    trialComponents.append(submit_button)
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

        # Check for response and button click
        if diagnosis.getRating() is not None:  # If a rating has been made
            if mouse.isPressedIn(submit_button):  # And submit button is clicked
                # Record response and reaction time
                diagnosis.response = diagnosis.getRating()
                diagnosis.rt = diagnosis.getRT()
                continueRoutine = False  # End routine

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
    print(f"Correct Response (CorrResp): {CorrResp}")
    print(f"Participant's Response (diagnosis.response): {diagnosis.response}")

    # Convert CorrResp (integer) to the corresponding disease name
    correct_disease = diseases[CorrResp - 1]  # CorrResp is 1-indexed, so adjust by -1
    diagnosed_disease = diseases[diagnosis.response - 1]

    print(f"Correct Disease (correct_disease): {correct_disease}")
    print(f"Participant diagnosed (diagnosed_disease): {diagnosed_disease}")

    # Compare disease names instead of comparing an integer to a string
    if correct_disease == diagnosed_disease:
        Correct = 1
    else:
        Correct = 0

    YourResponse.setText(f"{diagnosed_disease}")  # Display the participant's diagnosis

    # Feedback to participant
    if Correct == 1:
        Correct_Incorrect.setText('Correct!')
        score = score + 1000  # Award points for correct response
    else:
        Correct_Incorrect.setText('Incorrect')
        score = score  # No score change for incorrect response

    # Display the correct disease state
    State.setText(correct_disease)  # Now correctly shows the disease name
    
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
    learningtrials.addData('Phase', phase)
    learningtrials.addData('Costs', costs)
    learningtrials.addData('Block', block)
    learningtrials.addData('Trial', learningtrials.thisTrialN+1)
    learningtrials.addData('Genoutcome', genoutcome)
    learningtrials.addData('Diagnosis', diagnosis.getRating())
    learningtrials.addData('Diagnosis', diagnosed_disease)
    learningtrials.addData('Diseasename', correct_disease)
    #learningtrials.addData('diagnosis.rt', diagnosis.getRT())
    #learningtrials.addData('blockdiagnosis.rt', globaldiagnosistime)
    learningtrials.addData('Diseasenumber', CorrResp)
    learningtrials.addData('Accuracy', Correct)
    #learningtrials.addData('totalclick', totalclick)
    #learningtrials.addData('click1.order', click1order)
    #learningtrials.addData('click2.order', click2order)
    #learningtrials.addData('click3.order', click3order)
    #learningtrials.addData('click4.order', click4order)
    #learningtrials.addData('click1', click1)
    #learningtrials.addData('click2', click2)
    #learningtrials.addData('click3', click3)
    #learningtrials.addData('click4', click4)
    #learningtrials.addData('test1outcome', test1outcome)
    #learningtrials.addData('test2outcome', test2outcome)
    #learningtrials.addData('test3outcome', test3outcome)
    #learningtrials.addData('test4outcome', test4outcome)
    #learningtrials.addData('viewtest1outcome', test1viewoutcome)
    #learningtrials.addData('viewtest2outcome', test2viewoutcome)
    #learningtrials.addData('viewtest3outcome', test3viewoutcome)
    #learningtrials.addData('viewtest4outcome', test4viewoutcome)
    #learningtrials.addData('click1.rt', clicktime1)
    #learningtrials.addData('click2.rt', clicktime2)
    #learningtrials.addData('click3.rt', clicktime3)
    #learningtrials.addData('click4.rt', clicktime4)
    #learningtrials.addData('score', score)
    learningtrials.addData('Learningscore', learningscore)
    learningtrials.addData('Block1score', block1score)
    learningtrials.addData('Block2score', block2score)
    thisExp.nextEntry()
    
# completed n repeats of 'trials'=============================================================================================================================================Learning3============================================
Test1Image.setOpacity(0)
Test2Image.setOpacity(0)
Test3Image.setOpacity(0)
Test4Image.setOpacity(0)
learningscore=score
score=learningscore

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
        debrief1text.text = 'YOU HAVE NOW FINISHED THE LEARNING PHASE. PLEASE TAKE A BREAK. \n\nPLEASE DO NOT DISTURB YOUR TEAM MATES IF THEY ARE STILL COMPLETING THEIR LEARNING PHASES.'
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

win.close()
core.quit()
