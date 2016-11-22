import nuke
import basicCaraTestClass as BCTC


fileName = BCTC.getFileName(__file__)
comparePath = ('/Volumes/netqa/netqa/Testing/TestHarness/Research/CaraVR/Stitcher/{}.%V.exr').format(fileName)

node = BCTC.createNode('C_CameraSolver1_0')
BCTC.loadImages(node)
BCTC.CS_matchCameras(node)
BCTC.CS_solveCameras(node)

stitcher = BCTC.createNode("C_Stitcher1_0")
stitcher['enableStereo'].setValue(1)
stitcher['vectorDetail'].setValue(0.6)


''' WRITE OUT '''

write = BCTC.createNode('Write')
write.connectInput(1, stitcher)
#Set the generic stuff
BCTC.setWriteNode(write)

filePath = ('[getenv TEST_TEMP]/{}.%V.exr').format(fileName)
write['file'].setValue(filePath)
nuke.execute(write, 1, 1)

compareNode = BCTC.createCompareNode(0.001, 0.001)
readNode = BCTC.createReadNode(comparePath)
readNode2 = BCTC.createReadNode(filePath)
compareNode.connectInput(1, readNode)
compareNode.connectInput(1, readNode2)
# BCTC.executeCompareNode(compareNode, 1, 1)