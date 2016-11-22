# import os
# os.chdir("/Users/Tom/Desktop/Python/nuketests/Tests/Apps/Nuke/TestUnits/CaraVR/Tests")
import basicCaraTestClass as BCTC
import time
'''
    Written by Thomas Rice Research QA - Any Questions Please Ask - thomas.rice@thefoundry.co.uk 27/07/2016
'''

node = BCTC.createNode('C_CameraSolver1_0')
BCTC.loadImages(node)
BCTC.CS_matchCameras(node)
BCTC.CS_setKeyNum(node, 200)
time.sleep(5)
numberOfFrames = BCTC.CS_returnNumFrames(node)


if numberOfFrames != 5:
    nuke.tprint('Test failed as the there was a difference in the number of key frames, we expected 5 and got ',  numberOfFrames)
    sys.exit(1)
else:
    pass
    sys.exit(0) 
