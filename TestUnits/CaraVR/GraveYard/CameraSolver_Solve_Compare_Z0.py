# import os
# os.chdir("/Users/macadmin/Desktop/nuketests/Tests/Apps/Nuke/TestUnits/CaraVR/Tests")

import basicCaraTestClass as BCTC
import sys
import nuke, json

'''
    Written by Thomas Rice Research QA - Any Questions Please Ask - thomas.rice@thefoundry.co.uk 

    To Do:

'''
returnValue = 0
with open('/Users/macadmin/Desktop/data.txt', 'w') as outfile:
    json.dump(returnValue, outfile)

filePath = '/Volumes/netqa/netqa/Testing/TestHarness/Research/CaraVR/CameraSolver/CameraSolver_Solve_Compare_Z0.exr'
readPath = '/Volumes/netqa/netqa/Testing/TestHarness/Research/CaraVR/CameraSolver/CameraSolver_Solve_Compare_Z0.%V.exr'
iterations = 5

for i in range(0, iterations):
    # CameraSolver creation and solve
    node = BCTC.createNode('C_CameraSolver1_0')
    BCTC.loadImages(node)
    nuke.tprint("Asserted that Images Loaded SUCCESSFULLY.")
    BCTC.CS_matchCameras(node)
    nuke.tprint("Asserted that MAtched SUCCESSFULLY.")
    BCTC.CS_solveCameras(node)
    nuke.tprint("Asserted that Solved SUCCESSFULLY.")


    path = BCTC.getFileName(__file__)
    write, pathToCompare = BCTC.createWriteNode(path)
    write.connectInput(1, node)
    nuke.execute(write, 1, 1)
    nuke.tprint("Asserted that WRITE EXECUTED SUCCESSFULLY.")


    compareNode = BCTC.createCompareNode(0.001, 0.001)
    readNode = BCTC.createReadNode(readPath)
    compareNode.connectInput(1, readNode)
    newValue = BCTC.executeMultipleCompares(compareNode, 1, 1)

    if (newValue == 0):
        break
    else:
        with open('/Users/macadmin/Desktop/data.txt', 'w') as outfile:
            json.dump(i + 1, outfile)

    nuke.tprint('LOLOLOLOLOLOLOLOLOLOLOLOLOL ', i)


    for item in nuke.allNodes():
        nuke.delete(item)

nuke.tprint('OUT OF LOOP')

if returnValue >= (iterations -1):
    nuke.tprint(returnValue)
    nuke.tprint('success')
    sys.exit(0)
elif returnValue < (iterations -1):
    nuke.tprint(returnValue)
    nuke.tprint('fail')
    sys.exit(1)