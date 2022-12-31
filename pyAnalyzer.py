#!/usr/bin/python3

_license    =   """
# LICENSE:
# -------
# This code is the property of Hemanth Haridas, and was written during his
# tenure at the Indian Institute of Technology Gandhinagar, to analyze the
# Molecular Dynamics Simulations in NAMD. The code is distributed under an 
# MIT License. You will recieve a copy of the license with the code and if
# not, can be downloaded from "https://opensource.org/licenses/MIT". 

# Upon using this code, you agree that this code is shared with others with 
# the hope that it may help them with  their projects, but the authors make 
# no guarantee for the accurateness of the code, or for the result obtained 
# running this code on any untested systems.

# FAIR WARNING:
# ------------
# Documentation for the modules used in the code are available online, and
# are easy to follow. If you need to modify the code, and has no basics in
# Python programming, please check "A Byte of Python" before attempting to
# modify the code.
"""

#import MDAnalysis   as mda
import  sys         as sys
import  numpy       as np
import  typing      as tp 

# global variables

inputFile:  str             =   sys.argv[1]
psfFile:    str             =   ""
trajfile:   tp.List[str]    =   []

"""
with open(inputFile) as inputObject:
    inputBuffer =   inputObject.readlines()
    psfFile     =   inputBuffer[0].strip("\n")
    ntraj       =   int(inputBuffer[1].split()[0])
    for line in inputBuffer[1:1+line]:
        trajFile.append(line.rstrip("\n"))
"""
print(_license)
