# import os
# os.chdir("/Users/macadmin/Desktop/nuketests/Tests/Apps/Nuke/TestUnits/CaraVR/Tests")
import basicCaraTestClass as BCTC

'''
	Check the amount of read nodes in the scene then add 2 to the number of the c_sphericalTransfrom to avoid any future errors

'''


node = BCTC.createNode('C_CameraSolver1_0')
BCTC.loadImages(node)
BCTC.CS_matchCameras(node)
BCTC.CS_solveCameras(node)
BCTC.setExportOption(node, 1)
BCTC.exportSelection(node)

#Note that the C_SphericaTransform is 2 number higher than the number of read nodes. 
amountOfReads = len(nuke.allNodes('Read')) + 2
lastNodeinSequence = "C_SphericalTransform{}".format(amountOfReads)
nodeConnectionSet = BCTC.checkNodeConnections("C_CameraSolver1", lastNodeinSequence)

#The Format and connections that should be present
originalNodes =  set([('C_SphericalTransform8',)])


result = nodeConnectionSet.difference(originalNodes)


if result != set([]):
    nuke.tprint('Test failed as the there was a difference in the node connections, they were .. ' , result )
    print 'Test failed as the there was a difference in the node connections, they were .. ' , result 
    # sys.exit(1)
else:
    nuke.tprint('Test passed as there were no differences in the two sets')
    print 'Test passed as there were no differences in the two sets'
    pass
    sys.exit(0) 





