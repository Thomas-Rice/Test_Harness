# import os
import basicCaraTestClass as BCTC

''' 
    This is a Hacky Method used to check this test - Will come back to this to check the node connections
'''


compareList = []
node = BCTC.createNode('C_CameraSolver1_0')
BCTC.loadImages(node)
BCTC.CS_matchCameras(node)
BCTC.CS_solveCameras(node)
BCTC.setExportOption(node, 6)
BCTC.exportSelection(node)


tmp = nuke.allNodes()

for item in tmp:
    compareList.append(item.name())


originalList = ['OneView6', 
                'OneView5', 
                'OneView4', 
                'OneView3', 
                'OneView2', 
                'OneView1', 
                'ShuffleViews6', 
                'ShuffleViews5', 
                'ShuffleViews4', 
                'ShuffleViews3', 
                'ShuffleViews2', 
                'ShuffleViews1', 
                'Read6', 
                'Read5', 
                'Read4', 
                'Read3', 
                'Read2', 
                'Read1', 
                'C_CameraSolver1']



if compareList != originalList:
    nuke.tprint('Test failed as the there was a difference in the node connections, they were .. ' , result )
    # sys.exit(1)
else:
    nuke.tprint('Test passed as there were no differences in the two sets')
    pass
    sys.exit(0) 






