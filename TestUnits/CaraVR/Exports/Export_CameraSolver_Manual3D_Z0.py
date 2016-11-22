# import os
# os.chdir("/Users/macadmin/Desktop/nuketests/Tests/Apps/Nuke/TestUnits/CaraVR/Tests")
import basicCaraTestClass as BCTC

'''
    Written by Thomas Rice Research QA - Any Questions Please Ask - thomas.rice@thefoundry.co.uk 27/07/2016
'''


node = BCTC.createNode('C_CameraSolver1_0')
BCTC.loadImages(node)
BCTC.CS_matchCameras(node)
BCTC.CS_solveCameras(node)
BCTC.setExportOption(node, 4)
BCTC.exportSelection(node)


nodeConnectionSet = set()
#As we create groups of nodes with this operation we will need to go into it to check what's in there. 
goIntoGroup = nuke.toNode("RigWorkflow3D")
with goIntoGroup:
	#Get all of the inputs so we can check their connections
    inputGroup = nuke.allNodes('Input')
    for node in inputGroup:
        nodeConnectionSet.update(BCTC.checkNodeConnections(node.name(), "Output1"))



# The Format and connections that should be present
originalNodes = set([('AlphaMaskGenerator3', 'C_SphericalTransform3', 'Project3D3', 'MergeMat2', 'MergeMat3', 'MergeMat4', 'MergeMat5', 'Sphere1', 'C_RayRender1_0_1', 'Output1'), ('AlphaMaskGenerator5', 'C_SphericalTransform5', 'Project3D1', 'MergeMat1', 'MergeMat2', 'MergeMat3', 'MergeMat4', 'MergeMat5', 'Sphere1', 'C_RayRender1_0_1', 'Output1'), ('AlphaMaskGenerator', 'C_SphericalTransform7', 'Project3D6', 'MergeMat5', 'Sphere1', 'C_RayRender1_0_1', 'Output1'), ('AlphaMaskGenerator2', 'C_SphericalTransform2', 'Project3D4', 'MergeMat3', 'MergeMat4', 'MergeMat5', 'Sphere1', 'C_RayRender1_0_1', 'Output1'), ('AlphaMaskGenerator4', 'C_SphericalTransform4', 'Project3D2', 'MergeMat1', 'MergeMat2', 'MergeMat3', 'MergeMat4', 'MergeMat5', 'Sphere1', 'C_RayRender1_0_1', 'Output1'), ('AlphaMaskGenerator1', 'C_SphericalTransform1', 'Project3D5', 'MergeMat4', 'MergeMat5', 'Sphere1', 'C_RayRender1_0_1', 'Output1')])







result = nodeConnectionSet.difference(originalNodes)

if result != set([]):
    nuke.tprint('Test failed as the there was a difference in the node connections, they were .. ' , result )
    sys.exit(1)
else:
    pass
    sys.exit(0) 













