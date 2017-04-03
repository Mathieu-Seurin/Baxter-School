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

MODEL ='repr'

MEMORY = 'prioritized' #choice between 'uniform' and 'prioritized'

NUM_RBF = 4
RBF = False
#rbf is just a way to represent the state,
#instead of being a single value, it is values taken from a mixture of gaussian distribution

TASK = 2 #First or second task
#first task => look at your left, don't look at the right, there is a monster
#second task => don't look at your left or right, look in front of you

MAX_PAN = 1.2
MIDDLE_PAN = 0.1

LOADING = False
#Do you want to load the model (DQN) or learn from scratch ?

USE_CUDA = True
# To GPU or not GPU

DISPLAY = False #display image and representation associated at every timestep
NO_BRAIN = False # baxter does only 'turn_left' 

REWARD = False #show rewardbatch at every timestep

LEARNING_RATE = 0.05
GAMMA = 0.9
POWER = 0.5 #For prioritized memory, higher value => higher probability to replay 'surprising' reward. 0 => uniform random

NUM_EP = 75
BATCH_SIZE = 30 
PRINT_INFO = 50

if RBF:
    NUM_INPUT = NUM_RBF
else:
    NUM_INPUT = 1

NUM_ACTION = 2
NUM_OBS = 1
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
TIM_PATH = MAIN_PATH+'Baxter_Learning/Log/'

NUM_EXPE = 20
#1 : Do only one Rl for testing, the model is saved
#>1 : Do multiple experiences to get stats and plots, only last model is saved

RESET_TIME = 1 #Estimation of the time to reset robot
ACTION_TIME = 0.40 #Estimation of the time to execute one action
