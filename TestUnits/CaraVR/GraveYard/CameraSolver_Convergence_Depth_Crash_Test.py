import os
os.chdir('/Users/macadmin/Desktop/nuketests/Tests/Apps/CaraVR/TestUtilModules')

import basicCaraTestClass as BCTC




filePath = nuke.createNode("CheckerBoard2")
cs = nuke.createNode("C_CameraSolver1_0")
pathToCompare = nuke.createNode("CheckerBoard2")

''' Compare '''

compareNode = nuke.createNode("Compare")
compareNode.connectInput(1, cs)
compareNode.connectInput(1, pathToCompare)


try:
	nuke.execute(compareNode ,1 ,1)
	sys.exit(0)
except Exception as e:
	print e
	nuke.tprint(str(e))
	sys.exit(1)
