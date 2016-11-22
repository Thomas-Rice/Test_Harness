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
CMnode = BCTC.createNode('C_ColourMatcher1_0')
BCTC.CM_Analyse(CMnode)
BCTC.setExportOption(CMnode, 3)
BCTC.exportSelection(CMnode)

nodeConnectionSet = BCTC.checkNodeConnections("C_ColourMatcher1", "JoinViews1")



#The Format and connections that should be present
originalNodes = set([('OneView4', 'OCIOCDLTransform3', 'Exposure1', 'JoinViews1'), ('OneView2', 'OCIOCDLTransform1', 'Exposure1', 'JoinViews1'), ('OneView1', 'OCIOCDLTransform7', 'Exposure1', 'JoinViews1'), ('OneView3', 'OCIOCDLTransform2', 'Exposure1', 'JoinViews1'), ('OneView5', 'OCIOCDLTransform4', 'Exposure1', 'JoinViews1'), ('OneView6', 'OCIOCDLTransform5', 'Exposure1', 'JoinViews1')])


result = nodeConnectionSet.difference(originalNodes)

if result != set([]):
    nuke.tprint('Test failed as the there was a difference in the node connections, they were .. ' , result )
    sys.exit(1)
else:
    nuke.tprint('Test passed as there were no differences in the two sets')
    pass
    sys.exit(0) 






