# import os
# os.chdir("/Users/Tom/Desktop/Python/nuketests/Tests/Apps/Nuke/TestUnits/CaraVR/Tests")
import basicCaraTestClass as BCTC

'''
    Written by Thomas Rice Research QA - Any Questions Please Ask - thomas.rice@thefoundry.co.uk 27/07/2016

    To Do:
    - Find a way to get into the group and list the nodes
'''

node = BCTC.createNode('C_CameraSolver1_0')
BCTC.loadImages(node)
BCTC.CS_matchCameras(node)
BCTC.CS_solveCameras(node)
BCTC.setExportOption(node, 3)
BCTC.exportSelection(node)


nodeConnectionSet = set()
#As we create groups of nodes with this operation we will need to go into it to check what's in there. 
goIntoGroup = nuke.toNode("RigWorkflow2D")
with goIntoGroup:
	#Get all of the inputs so we can check their connections
    inputGroup = nuke.allNodes('Input')
    for node in inputGroup:
        nodeConnectionSet.update(BCTC.checkNodeConnections(node.name(), "Output1"))



# The Format and connections that should be present
originalNodes = set([('AlphaMaskGenerator', 'C_SphericalTransform7', 'JoinViews1', 'C_Blender1', 'Output1'), ('AlphaMaskGenerator5', 'C_SphericalTransform5', 'JoinViews1', 'C_Blender1', 'Output1'), ('AlphaMaskGenerator4', 'C_SphericalTransform4', 'JoinViews1', 'C_Blender1', 'Output1'), ('AlphaMaskGenerator3', 'C_SphericalTransform3', 'JoinViews1', 'C_Blender1', 'Output1'), ('AlphaMaskGenerator2', 'C_SphericalTransform2', 'JoinViews1', 'C_Blender1', 'Output1'), ('AlphaMaskGenerator1', 'C_SphericalTransform1', 'JoinViews1', 'C_Blender1', 'Output1')])







result = nodeConnectionSet.difference(originalNodes)

if result != set([]):
    nuke.tprint('Test failed as the there was a difference in the node connections, they were .. ' , result )
    sys.exit(1)
else:
    pass
    sys.exit(0) 

