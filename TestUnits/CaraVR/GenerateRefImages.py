import nuke
import os
import basicCaraTestClass as BCTC
os.chdir("/Users/macadmin/Desktop/nuketests/Tests/Apps/Nuke/TestUnits/CaraVR/Tests")

def setWriteNode(node):
    node['channels'].setValue('rgba')
    node['file_type'].setValue('exr')
    node['datatype'].setValue('32 bit float')
    node['compression'].setValue('none')



filesToMake = set()


path = '/Volumes/netqa/Testing/TestHarness/Research/CaraVR/Import_Presets/'
# Get all directories in this directory [1] is the directory part of the tuple [0] is the root and [2] is files
files = os.walk(path).next()[2]

#Get a list of all the images that are currently created
for file in files:
    #remove the .py
    result = file.rsplit('.',2)
    filesToMake.add(result[0])

#CameraSolver creation and solve
node = BCTC.createNode('C_CameraSolver1_0')
BCTC.loadImages(node)
#Create a write node
write = BCTC.createNode('Write')
#Set the generic stuff
setWriteNode(write)

#Get all the presets in the cameraSolver node
rigPresetList = []
for i in node['rigPreset'].values():
     rigPresetList.append(i)



for preset in rigPresetList:
    print preset
    #Ignore all the presets that need inputs
    if 'Custom' in preset:
        pass
    elif 'PTGui (.pts)' in preset:
        pass 
    elif 'Nokia' in preset: 
        pass
    else:
        BCTC.CS_chooseRigPreset(node, preset)
        modPreset = preset.split(" ")
        for item in filesToMake:
            if modPreset[0] in item:
                # filePath = ('/Users/macadmin/Desktop/tmp/{}.%V.exr').format(item)
                # filePath = ('/Volumes/netqa/Testing/TestHarness/Research/CaraVR/Import_Presets/{}.%V.exr').format(item)
                filePath = ('/Users/Tom/Desktop/{}.%V.exr').format(item)
                write['file'].setValue(filePath)
                nuke.execute(write, 1, 1)




