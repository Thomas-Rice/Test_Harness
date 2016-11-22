# import os
import basicCaraTestClass as BCTC

'''
    Written by Thomas Rice Research QA - Any Questions Please Ask - thomas.rice@thefoundry.co.uk 27/07/2016
'''

node = BCTC.createNode('C_CameraSolver1_0')
BCTC.loadImages(node)
BCTC.CS_matchCameras(node)
BCTC.CS_solveCameras(node)
BCTC.setExportOption(node, 2)
BCTC.exportSelection(node)
nodeConnectionSet = BCTC.checkNodeConnections("C_CameraSolver1", "JoinViews1")



#The Format and connections that should be present
originalNodes = set([('Split', 'JoinViews1'), 
                    ('OneView1', 'C_SphericalTransform1', 'JoinViews1'),
                    ('OneView2', 'C_SphericalTransform2', 'JoinViews1'),
                    ('OneView3', 'C_SphericalTransform3', 'JoinViews1'),
                    ('OneView4', 'C_SphericalTransform4', 'JoinViews1'),
                    ('OneView5', 'C_SphericalTransform5', 'JoinViews1'),
                    ('OneView6', 'C_SphericalTransform6', 'JoinViews1')])


result = nodeConnectionSet.difference(originalNodes)

if result != set([]):
    nuke.tprint('Test failed as the there was a difference in the node connections, they were .. ' , result )
    sys.exit(1)
else:
    nuke.tprint('Test passed as there were no differences in the two sets')
    pass
    sys.exit(0) 






