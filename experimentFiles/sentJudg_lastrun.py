#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.03), Tue 26 Jan 16:02:28 2016
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'sentJudg'  # from the Builder filename that created this script
expInfo = {u'rechtshandig': u'', u'geslacht': u'', u'leeftijd': u'', u'list': u'A', u'deelnemer': u'1', u'opleiding': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.path.sep + expInfo['date']

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/bastienboutonnet/Dropbox/3.CurrentProjects/AThEME/LabWorkshop/psychoPyLabWorkshop/experimentFiles/sentJudg.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=[1240, 800], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor=u'MacBook', color=u'black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
instrText_2 = visual.TextStim(win=win, ori=0, name='instrText_2',
    text=u'Welkom bij dit experiment en alvast bedankt voor uw deelname.\r\n\r\nU gaat zinnen beoordelen op hun acceptabiliteit: er wordt \xe9\xe9n voor \xe9\xe9n een zin getoond en u bepaalt in hoeverre de getoonde zin acceptabel Nederlands is.',    font=u'Verdana',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
text = visual.TextStim(win=win, ori=0, name='text',
    text='Druk de spatiebalk om verder te gaan!',    font='Verdana',
    pos=[0, -0.77], height=0.07, wrapWidth=None,
    color=[-0.122,0.522,0.514], colorSpace='rgb', opacity=0.7,
    depth=-2.0)

# Initialize components for Routine "practice"
practiceClock = core.Clock()
word_6 = visual.TextStim(win=win, ori=0, name='word_6',
    text='default text',    font=u'Verdana',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
rating_6 = visual.RatingScale(win=win, name='rating_6', choices=[1,2,3,4,5,6,7],
mouseOnly=False, 
pos=(0,-0.7), 
marker='triangle', 
markerColor='blue', 
size=0.85,
singleClick=False, disappear=False


)
text_14 = visual.TextStim(win=win, ori=0, name='text_14',
    text='onacceptabel',    font='Verdana',
    pos=[-0.265, -0.6], height=0.05, wrapWidth=None,
    color='gray', colorSpace='rgb', opacity=1,
    depth=-2.0)
text_15 = visual.TextStim(win=win, ori=0, name='text_15',
    text='acceptabel',    font='Verdana',
    pos=[0.265,-0.6], height=0.05, wrapWidth=None,
    color='gray', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instruction"-------
t = 0
instructionClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
ready_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
ready_2.status = NOT_STARTED
# keep track of which components have finished
instructionComponents = []
instructionComponents.append(instrText_2)
instructionComponents.append(ready_2)
instructionComponents.append(text)
for thisComponent in instructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instruction"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText_2* updates
    if t >= 0.5 and instrText_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrText_2.tStart = t  # underestimates by a little under one frame
        instrText_2.frameNStart = frameN  # exact frame index
        instrText_2.setAutoDraw(True)
    
    # *ready_2* updates
    if t >= 0.5 and ready_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready_2.tStart = t  # underestimates by a little under one frame
        ready_2.frameNStart = frameN  # exact frame index
        ready_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if ready_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *text* updates
    if t >= 0.5 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
PracSent = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pract.csv'),
    seed=None, name='PracSent')
thisExp.addLoop(PracSent)  # add the loop to the experiment
thisPracSent = PracSent.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPracSent.rgb)
if thisPracSent != None:
    for paramName in thisPracSent.keys():
        exec(paramName + '= thisPracSent.' + paramName)

for thisPracSent in PracSent:
    currentLoop = PracSent
    # abbreviate parameter names if possible (e.g. rgb = thisPracSent.rgb)
    if thisPracSent != None:
        for paramName in thisPracSent.keys():
            exec(paramName + '= thisPracSent.' + paramName)
    
    #------Prepare to start Routine "practice"-------
    t = 0
    practiceClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    word_6.setColor(u'white', colorSpace='rgb')
    word_6.setText(sent)
    rating_6.reset()
    # keep track of which components have finished
    practiceComponents = []
    practiceComponents.append(word_6)
    practiceComponents.append(rating_6)
    practiceComponents.append(text_14)
    practiceComponents.append(text_15)
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "practice"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = practiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *word_6* updates
        if t >= 0.5 and word_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            word_6.tStart = t  # underestimates by a little under one frame
            word_6.frameNStart = frameN  # exact frame index
            word_6.setAutoDraw(True)
        # *rating_6* updates
        if t >= 0.5 and rating_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_6.tStart = t  # underestimates by a little under one frame
            rating_6.frameNStart = frameN  # exact frame index
            rating_6.setAutoDraw(True)
        continueRoutine &= rating_6.noResponse  # a response ends the trial
        
        # *text_14* updates
        if t >= 0.5 and text_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_14.tStart = t  # underestimates by a little under one frame
            text_14.frameNStart = frameN  # exact frame index
            text_14.setAutoDraw(True)
        
        # *text_15* updates
        if t >= 0.5 and text_15.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_15.tStart = t  # underestimates by a little under one frame
            text_15.frameNStart = frameN  # exact frame index
            text_15.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "practice"-------
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for PracSent (TrialHandler)
    PracSent.addData('rating_6.response', rating_6.getRating())
    PracSent.addData('rating_6.rt', rating_6.getRT())
    # the Routine "practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'PracSent'

# get names of stimulus parameters
if PracSent.trialList in ([], [None], None):  params = []
else:  params = PracSent.trialList[0].keys()
# save data for this loop
PracSent.saveAsExcel(filename + '.xlsx', sheetName='PracSent',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
win.close()
core.quit()
