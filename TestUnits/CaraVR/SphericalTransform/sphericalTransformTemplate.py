import basicCaraTestClass as BCTC

class sphericalTransformTemplate():
	def __init__(self, scriptName):
		self.scriptName = scriptName
		# Create CameraSolver and Read nodes
		self.SphericalTransformInstance = BCTC.sphericalTransformOps(scriptName)

	def returnNode(self):
		# Do Specific Test Setup and get variables
		self.node, self.filePath = self.SphericalTransformInstance.setup()
		return self.node

	def writeOut(self):
		''' WRITE OUT '''
		#Get the path to the images so we can compare
		pathToCompare = self.SphericalTransformInstance.writeOut(self.node)
		return pathToCompare

	def compare(self):
		self.writeOut()
		''' Compare '''
		#Create the compare node etc
		CompareObj = BCTC.compareImages(0.001, self.filePath, 1, 1)
		#Compare the reult to the ref image
		CompareObj.compare()

