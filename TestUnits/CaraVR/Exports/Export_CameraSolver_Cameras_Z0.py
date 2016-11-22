# import os
import basicCaraTestClass as BCTC

'''
    Written by Thomas Rice Research QA - Any Questions Please Ask - thomas.rice@thefoundry.co.uk 27/07/2016
'''
node = BCTC.createNode('C_CameraSolver1_0')
BCTC.loadImages(node)
BCTC.CS_matchCameras(node)
BCTC.CS_solveCameras(node)
BCTC.setExportOption(node, 0)
BCTC.exportSelection(node)
nodeConnectionSet = BCTC.checkNodeConnections("Axis1", "Scene1")

#The Format and connections that should be present
originalNodes = set([
					('Camera1', 'Scene1'), 
					('Camera2', 'Scene1'), 
					('Camera3', 'Scene1'),
					('Camera4', 'Scene1'), 
					('Camera5', 'Scene1'), 
					('Camera6', 'Scene1')])


result = nodeConnectionSet.difference(originalNodes)

if result != set([]):
    nuke.tprint('Test failed as the there was a difference in the node connections, they were .. ' , result )
    sys.exit(1)
else:
    nuke.tprint('Test passed as there were no differences in the two sets')
    pass
    sys.exit(0) 






