import time
import glob 
import os
import nuke
import sys
import platform

'''
    Use this to store all of the Nuke / Cara commands then call on these commands in your test script

'''

''' ************************************************************* Generic Operations ************************************************************* ''' \

def createNode(nodeToCreate):
	#Create node
	nuke.tprint('Creating %s' %(nodeToCreate))
	node = nuke.createNode(nodeToCreate)

	#Check node creation is successful
	numNodes = len(nuke.allNodes(nodeToCreate))
	if numNodes != 1:
	    nuke.tprint("Creation of %s node failed" %(node))
	    sys.exit(1)
	else:
	    nuke.tprint("Asserted that Creation of %s worked as expected." %(nodeToCreate))
	    return node

def createReadNode(filePath, start = None, end = None):
  imageReader = nuke.createNode("Read", inpanel=False)
  imageReader.knob("file").setValue(filePath)

  if start != None:
  	imageReader.knob("first").setValue(int(start))
  if end != None:
  	imageReader.knob("last").setValue(int(end))
  return imageReader

def setExportOption(node, value):
	#Set the Export option
	'''
		0 - Cameras
		1 - Transforms Split 
		2 - Transforms Separate
		3 - Manual 2D
		4 - Manual 3D
	'''
	try:
	    node['exportMenu'].setValue(value) #This is currently the Split Option
	except Exception as e:
	    nuke.tprint('Error Setting the Export Type - ', e)
	    sys.exit(1)
	#Wait a short time otherwise the export button seems to fire too quickly and is not connected properly
	time.sleep(5)

def exportSelection(node):
	#Export the chosen option
	try:
	    node['exportButton'].execute()   
	except Exception as e:
	    nuke.tprint('Error Exporting - ', e)
	    sys.exit(1)


''' ************************************************************* CameraSolver ************************************************************* ''' 
def CS_matchCameras(node):
	#Match Cameras
	try:
	    node['matchCameras'].execute()
	except Exception as e:
	    nuke.tprint('Error Matching - ', e)
	    sys.exit(1)

def CS_solveCameras(node):
	#Solve Cameras
	try:
	    node['solveCameras'].execute()
	except Exception as e:
	    nuke.tprint('Error Solving - ', e)
	    sys.exit(1)

def CS_returnNumFrames(node):
	try:
		string = str(node)
		string2 = string.splitlines()
		#We cannot get the value of frames set straight up so we need to conver the node details into a string the hack at it to return this number
		#Get the index number of the frames setion of the list
		for i, j in enumerate(string2): 
		    if 'frames' in j:
		        print i
		        break

		#The string is in a format 'frames 1' so we only need the last number 
		name, number = string2[i].split(" ")
		return str(node)
	except Exception as e:
	    nuke.tprint('Error getting number of frames in string conversion - ', e)
	    sys.exit(1)

def CS_setKeyNum(node, num):
	try:
		node['keyStep'].setValue(num)
		node['addAllAnalysisKeys'].execute()
	except Exception as e:
	    nuke.tprint('Error setting number of frames - ', e)
	    sys.exit(1)

def CS_chooseRigPreset(node, preset):
	try:
		node['rigPreset'].setValue(preset)
	except Exception as e:
	    nuke.tprint('Error choosing the rig preset - ', e)
	    sys.exit(1)
	try:
		node['setupRig'].execute()
	except Exception as e:
	    nuke.tprint('Error setting the rig preset - ', e)
	    sys.exit(1)

''' ************************************************************* ColourMatcher Operations ************************************************************* ''' 
def CM_Analyse(node):
	#Activate the analyse button
	try:
	    node['solveGainCompensation'].execute()   
	except Exception as e:
	    nuke.tprint('Error Analysing - ', e)
	    sys.exit(1)

''' ************************************************************* CameraTracker Operations ************************************************************* ''' 

def CT_trackAndSolve(node):
	try:
		node['trackRange'].setValue(2)
	except Exception as e:
		nuke.tprint('Error Setting the track range to custom - ', e)
		sys.exit(1)
	try:
		node['trackStop'].setValue(30)
	except Exception as e:
		nuke.tprint('Error Setting the track end range to 5 - ', e)
		sys.exit(1)
	try:
		node['trackFeatures'].execute()
		time.sleep(5)
	except Exception as e:
		nuke.tprint('Error tracking features - ', e)
		sys.exit(1)
	try:
		node['solveCamera'].execute() 
		time.sleep(5)
	except Exception as e:
		nuke.tprint('Error solving cameras - ', e)
		sys.exit(1)


''' ************************************************************* Nuke Operations ************************************************************* ''' 

def loadImages(node):
	#Change to image folder directory and load in a read node for each image/sequence then connect that to the cameraSolver
	os.chdir("/Volumes/netpics/Clients/ErikWinquist/ewinquist_360video/plates/")
	for index, video in enumerate(glob.glob("*.MP4")):
	    try:
	        # i = nuke.nodes.Read(file = video)
	        i = nuke.createNode('Read')
	        i['file'].setValue(video)
	        # i = nuke.createNode('CheckerBoard2')
	    except Exception as e:
	        nuke.tprint ('Error creating read node', e)
	        sys.exit(1)
	    try:
	        node.setInput(index, i)
	    except Exception as e:
	        nuke.tprint ('Error connecting input of %s to %s' % (index, i))
	        sys.exit(1)


def loadSolvedImage():
	try:
		img = nuke.nodes.Read(file = '/Users/macadmin/Desktop/Solve_Test.%V.exr')
		img['noprefix'].setValue(1)
		return img
	except Exception as e:
		nuke.tprint ('Error creating read node', e)
		sys.exit(1)



def loadJumpImages(node):
	#Change to image folder directory and load in a read node for each image/sequence then connect that to the cameraSolver
	os.chdir("/Volumes/netpics/Clients/Google/test_stills/") 
	for index, video in enumerate(glob.glob("*.jpg")):
	    try:
	    	if ('camera' in video):
	        	i = nuke.nodes.Read(file = video)
	    except Exception as e:
	        nuke.tprint ('Error creating read node', e)
	        sys.exit(1)
	    try:
	        node.setInput(index, i)
	    except Exception as e:
	        nuke.tprint ('Error connecting input of %s to %s' % (index, i))
	        sys.exit(1)




''' ************************************************************* Util Operations ************************************************************* ''' 

nodeConnectionSet = set()
tmp = []
tupleTmp = ()
print 'initialised'

def checkNodeConnections(originalNode, lastNodeInSequence):
	global nodeConnectionSet
	global tmp 
	global tupleTmp

	#Make sure that the node you are searching to exists otherwise the test will pass incorrectly
	if nuke.exists(lastNodeInSequence):
		node = nuke.toNode(originalNode)
		#Check downstream node of the current selected node
		for downStreamNode in node.dependent():
		    if lastNodeInSequence in downStreamNode.name():
		        tmp.append(downStreamNode.name())
		        tupleTmp = tuple(tmp)
		        nodeConnectionSet.add(tupleTmp)
		        tmp = []
		    else:
		        tmp.append(downStreamNode.name())
		    #Recurse through nodes 
		    checkNodeConnections(downStreamNode.name(), lastNodeInSequence)
		return nodeConnectionSet
	else:
		nuke.tprint('The %s node does not exist, there is either a problem with the code or something is wrong with the build' % (lastNodeInSequence))
		sys.exit(1)
		print 'node error'

def createCompareNode(warnThr = None, errThr = None, continueAft = None):
	try:
		#Create the node
		comparer = nuke.createNode("Compare", inpanel=False)

		if warnThr != None:
			comparer.knob("warnThres").setValue(float(warnThr))
		if errThr != None:
			comparer.knob("errorThres").setValue(float(errThr))
		if continueAft != None:
			comparer['continueAfterFailure'].setValue(1)
		nuke.tprint("Asserted that Creation of Compare worked as expected.")
		return comparer
	except Exception as e:
		print 'Failed at creating Compare Node!', e

def executeCompareNode(node, start, end):
	try:
		nuke.execute(node ,start ,end)
		nuke.tprint("Asserted that Compare worked as expected.")
		# nuke.scriptSaveAndClear(filename=None, ignoreUnsavedChanges=True)
		sys.exit(0)
	except Exception as e:
		# print e
		nuke.tprint(str(e))
		nuke.tprint("Asserted that Compare FAILED.")
		# nuke.scriptSaveAndClear(filename=None, ignoreUnsavedChanges=True)
		sys.exit(1)

def executeMultipleCompares(node, start, end):
	try:
		nuke.execute(node ,start ,end , inpanel = False)
		nuke.tprint('Compared and Succeeded')
		return 1
	except RuntimeError as e:
		nuke.tprint('Compare failed badly')
		nuke.tprint(str(e))
		return 0

def createWriteNode(name):
	try:
		write = nuke.createNode("Write")
	except Exception as e:
		nuke.tprint('Failed to create write node')
	try:
		# testVar =("/Users/macadmin/Desktop/1.%V.exr")
		testVar =("[getenv TEST_TEMP]/{}.%V.exr").format(name)
		write['file'].setValue(testVar)
		write['file_type'].setValue('exr')
		write['datatype'].setValue(1)
		write['compression'].setValue('none')
		write['channels'].setValue('all')
		nuke.tprint("Asserted that Creation of Write worked as expected.")
	except Exception as e:
		print e
		nuke.tprint('Failed to add the correct settings to the write node')

	return write, testVar

def executeRender(node, start, end):
	try:
		nuke.execute(node, start, end)
		sys.exit(0)
	except Exception as e:
		nuke.tprint('Failed to render range')
		sys.exit(1)


def getFileName(inputFile):
	try:
		if platform.system() == 'Darwin':
			iF = inputFile.rsplit("/", 1)
		elif platform.system() == 'Windows':
			iF = inputFile.rsplit("\\", 1)
		else:
			nuke.tprint('Broken on platform recognition')

		filename = iF[1].split('.py')
		return filename[0]
	except Exception as e:
		nuke.tprint('Error getting the file name from BCTC' , e)



def addViews():
	for i in range(1,6):
		nuke.addView('cam{}'.format(i))



''' JoinViews Operations '''
def getViews(C_node) :
  # Best way: from metadata
  numCameras = C_node.metadata("vr/rig/numberOfCameras")
  if numCameras is not None :
    return numCameras
  # Otherwise from the view management knobs
  if C_node.knob("rigViews") is not None :
    return len(C_node['rigViews'].toScript().strip().split(' '))
  if C_node.knob("multiView") is not None :
    multiView = C_node['multiView'].toScript()
    mLines = StringIO.StringIO( multiView ).readlines()
    return mLines[2].strip().split(' ')

def createAndConnectJoinViews(node):
	joinViews = createNode('JoinViews')
	views =["cam"+str(x+1) for x in range(0, getViews(node))]
	views.extend('right')
	for i, view in enumerate(views):
		joinViews.connectInput(i, node)
	return joinViews

def deselectAllViews():
	for each in nuke.allNodes():
		each.knob("selected").setValue(False)



''' ************************************************************* Test Classes ************************************************************* ''' 
''' ************************************************************* Base Class *************************************************************** ''' 
class baseOpsClass(object):
	def __init__(self, file, testName):
		self.fileName = getFileName(file)
		self.filePath = ('/Volumes/netqa/netqa/Testing/TestHarness/Research/CaraVR/{}/{}.%V.exr').format(testName,self.fileName)

	def setup(self):
		node = createNode('C_CameraSolver1_0')
		loadImages(node)
		CS_matchCameras(node)
		CS_solveCameras(node)
		return node, self.filePath

	def addNode(self, nodeName):
		newNode = createNode(nodeName)
		return newNode

	def export(self, node):
		CS_matchCameras(node)
		CS_solveCameras(node)
		setExportOption(node, 2)
		exportSelection(node)

	def createReformat(self, node):
		reformatNode = nuke.createNode("Reformat")
		reformatNode.connectInput(1, node)
		reformatNode['format'].setValue('PC_Video')
		nuke.tprint("Asserted that Creation of Reformat worked as expected.")
		return reformatNode

	def writeOut(self, node):
		deselectAllViews()
		reformatNode = self.createReformat(node)
		reformatNode.connectInput(1, node)
		write, pathToCompare = createWriteNode(self.fileName)
		write.connectInput(1, reformatNode)
		nuke.execute(write, 1, 1)
		nuke.tprint("Asserted that WRITE EXECUTED SUCCESSFULLY.")
		return pathToCompare
''' ************************************************************* Overriden Classes ************************************************************* ''' 

class cameraSolverOps(baseOpsClass):
	# Inherits the baseClass
	def __init__(self, file, testName = 'CameraSolver'):
		super(cameraSolverOps, self).__init__(file, testName) 

class colourMatcherOps(baseOpsClass):
	# Inherits the baseClass
	def __init__(self, file, testName = 'ColourMatcher'):
		super(colourMatcherOps, self).__init__(file, testName) 

	def setup(self):
		# Overrides the function setup to add a colour matcher to the end of the operation list then return that. 
		# Need to use Return Super to return a value via the super method.
		super(colourMatcherOps, self).setup()
		colourMatcher = self.addNode("C_ColourMatcher1_0")
		return colourMatcher, self.filePath


class sphericalTransformOps(baseOpsClass):
	# Inherits the baseClass
	def __init__(self, file, testName = 'SphericalTransform'):
		super(sphericalTransformOps, self).__init__(file, testName)

	def setup(self):
		#We only need a checkerboard in this case so ovveride the function to be differnet.
		createNode('CheckerBoard2')
		node = createNode('C_SphericalTransform1_0')
		return node, self.filePath

	def createReformat(self, node):
		reformatNode = nuke.createNode("Reformat")
		reformatNode.connectInput(1, node)
		reformatNode['format'].setValue('PC_Video')
		#The black outside option is needed here because when written out the autofilled areas seen in Nuke are black. 
		#This therefore ensures that the autofilled areas are black and the same as the write.
		reformatNode['black_outside'].setValue(1)
		return reformatNode


class stitcherOps(baseOpsClass):
	# Inherits the baseClass
	def __init__(self, file, testName = 'Stitcher'):
		super(stitcherOps, self).__init__(file, testName)

	def setup(self):
		# Overrides the function setup to add a colour matcher to the end of the operation list then return that. 
		# Need to use Return Super to return a value via the super method.
		super(stitcherOps, self).setup()
		stitcher = self.addNode("C_Stitcher1_0")
		return stitcher, self.filePath

	def jumpSetup(self):
		node = createNode('C_CameraSolver1_0')
		loadJumpImages(node)
		CS_matchCameras(node)
		CS_solveCameras(node)
		stitcher = self.addNode("C_Stitcher1_0")
		return stitcher, self.filePath

	
	# def metaDataSetup(self):
	# 	# Overrides the function setup to add a colour matcher to the end of the operation list then return that. 
	# 	# Need to use Return Super to return a value via the super method.
	# 	super(stitcherOps, self).setup()
	# 	metaDataNode = self.addNode("C_MetaDataTransform1_0")
	# 	return metaDataNode, self.filePath

	# def blenderWriteOut(self, blender):
	# 	write, pathToCompare = createWriteNode(self.fileName)
	# 	write.connectInput(1, blender)
	# 	nuke.execute(write, 1, 1)
	# 	return pathToCompare



class compareImages(object):
	def __init__(self, tolerance, readPath, start = None, stop = None ):
		self.tolerance = tolerance
		self.readPath = readPath
		self.start = start
		self.stop = stop

	def compare(self):
		compareNode = createCompareNode(self.tolerance, self.tolerance)
		readNode = createReadNode(self.readPath)
		compareNode.connectInput(1, readNode)
		executeCompareNode(compareNode, self.start, self.stop)

	def compareTwoInputs(self, filePath):
		compareNode = createCompareNode(self.tolerance, self.tolerance)
		readNode = createReadNode(self.readPath)
		readNode2 = createReadNode(filePath)
		compareNode.connectInput(1, readNode)
		compareNode.connectInput(1, readNode2)
		executeCompareNode(compareNode, self.start, self.stop)


