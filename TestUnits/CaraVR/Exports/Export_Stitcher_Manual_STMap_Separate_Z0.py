# import os
import basicCaraTestClass as BCTC

'''
    Written by Thomas Rice Research QA - Any Questions Please Ask - thomas.rice@thefoundry.co.uk 27/07/2016
'''

#CameraSolver creation and solve
node = BCTC.createNode('C_CameraSolver1_0')
BCTC.loadImages(node)
BCTC.CS_matchCameras(node)
BCTC.CS_solveCameras(node)
#ColourMatcher creation and solve
Snode = BCTC.createNode('C_Stitcher1_0')
BCTC.setExportOption(Snode, 3)
BCTC.exportSelection(Snode)

nodeConnectionSet = BCTC.checkNodeConnections("C_CameraSolver1", "JoinViews1")


originalNodes = set([
	('OneView9', 'STMap2', 'JoinViews1', 'ShuffleCopy1', 'C_Blender1'),
	('OneView3', 'STMap2', 'JoinViews1', 'ShuffleCopy1', 'C_Blender1'), 
	('C_Stitcher1', 'ShuffleCopy1', 'C_Blender1'), 
	('OneView2', 'STMap1', 'JoinViews1', 'ShuffleCopy1', 'C_Blender1'), 
	('OneView8', 'STMap1', 'JoinViews1', 'ShuffleCopy1', 'C_Blender1'),
	('OneView12', 'STMap5', 'JoinViews1', 'ShuffleCopy1', 'C_Blender1'),
	('OneView6', 'STMap5', 'JoinViews1', 'ShuffleCopy1', 'C_Blender1'), 
	('OneView7', 'STMap7', 'JoinViews1', 'ShuffleCopy1', 'C_Blender1'),
	('OneView4', 'STMap3', 'JoinViews1', 'ShuffleCopy1', 'C_Blender1'), 
	('BlackOutside1', 'Split', 'JoinViews1', 'ShuffleCopy1', 'C_Blender1'),
	('OneView5', 'STMap4', 'JoinViews1', 'ShuffleCopy1', 'C_Blender1'),
	('OneView10', 'STMap3', 'JoinViews1', 'ShuffleCopy1', 'C_Blender1'),
	('OneView1', 'STMap7', 'JoinViews1', 'ShuffleCopy1', 'C_Blender1'),
	('OneView11', 'STMap4', 'JoinViews1', 'ShuffleCopy1', 'C_Blender1')])


result = nodeConnectionSet.difference(originalNodes)

if result != set([]):
    nuke.tprint('Test failed as the there was a difference in the node connections, they were .. ' , result )
    sys.exit(1)
else:
    nuke.tprint('Test passed as there were no differences in the two sets')
    pass
    sys.exit(0) 






