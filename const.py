#!/usr/bin/python
#coding: utf-8
"""
Module to deal with constant, much more easier and every sub module can access it
Easy to change model, parameters, learning_rate, cuda, experiments etc ...

Also path for loading, saving etc ...
"""
from os.path import expanduser

class DrunkProgrammer(Exception):pass

HOME = expanduser("~")+'/'

MODEL ='true'

MEMORY = 'prioritized' #choice between 'uniform' and 'prioritized'

NUM_RBF = 4
RBF = False
#rbf is just a way to represent the state,
#instead of being a single value, it is values taken from a mixture of gaussian distribution

TASK = 3
#first task => look at your left, don't look at the right, there is a monster
#second task => don't look at your left or right, look in front of you
#third task => 3D controlling hand with button

MAX_PAN = 1.2
MIDDLE_PAN = 0.1

LOADING = False
#Do you want to load the model (DQN) or learn from scratch ?

USE_CUDA = True
# To GPU or not GPU

DISPLAY = False #display image and representation associated at every timestep
NO_BRAIN = 25 # baxter does only this action

REWARD = False #show rewardbatch at every timestep

LEARNING_RATE = 0.05
GAMMA = 0.85
POWER = 0.5 #For prioritized memory, higher value => higher probability to replay 'surprising' reward. 0 => uniform random

NUM_EP = 75
BATCH_SIZE = 30 
PRINT_INFO = 50

if RBF:
    NUM_INPUT = NUM_RBF

N = 20 #number of hidden neuron

SIZE_MEMORY = 10000

EXPLO = 'boltzman' #explo can be 'boltzman' or 'eps'

#For epsilon greed
EPS_START = 0.9
EPS_END = 0.10
EPS_DECAY = 300

MAIN_PATH = HOME+'Documents/enstage/'

RL_PATH = MAIN_PATH+'rl/'
MODEL_PATH = RL_PATH+'model/'
LOG_RL = RL_PATH+'Log/'
TIM_PATH = MAIN_PATH+'learningRepresentation/Log/'

NUM_EXPE = 20
#1 : Do only one Rl for testing, the model is saved
#>1 : Do multiple experiences to get stats and plots, only last model is saved

if TASK==3:
    NUM_ACTION = 26
    RESET_TIME = 3 #Estimation of the time to reset robot
    ACTION_TIME = 0.1 #Estimation of the time to execute one action
    LIMIT = 399 #Timeout, the game is over, new game incomming
    NUM_INPUT = 3
    
else:
    RESET_TIME = 1 #Estimation of the time to reset robot
    ACTION_TIME = 0.40 #Estimation of the time to execute one action
    LIMIT = 199
    NUM_ACTION = 2
    NUM_INPUT = 1

    
