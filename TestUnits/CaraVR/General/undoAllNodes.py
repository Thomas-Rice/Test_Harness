# Tests the simple case of creating a node, then undo-ing the operation, then redo-ing the operation

def getNodes(menu):
  import nuke
  nodeList = []
  if isinstance(menu,nuke.Menu):
    for item in menu.items():
      name = item.name()
      if 'C_' in name:
        nuke.tprint(name)
        nodeList.append(name)
      getNodes(item)

  for node in nodeList:
    print 'testing', node
    undoRedoTest(node)


def undoRedoTest(node):
  import nuke
  # ANT: I'm unsure why we need this Undo.enable() call
  # The documentation gives no obvious clues,  "Undoes the previous disable()" !!!
  # PG: The undo system is only enable when Nuke start in GUI mode.
  # In terminal mode it's disabled.
  # It's very important to to call nuke.Undo.enable() only when is needed,
  # other wise undo/redo an operation could be not done properly
  if nuke.Undo.disabled() == True:
    nuke.Undo.enable()

  # Test Flow: Create a  Node > nuke.undo() > Assert No Node > nuke.redo() > Assert  Node comes back as expected
  nuke.tprint('Creating', node)
  nodeToCheck = "{}1_0".format(node)
  originalNode = nuke.createNode("{}1_0".format(node))


  numNodesBeforeUndo = len(nuke.allNodes(nodeToCheck))
  nuke.tprint("Number of %s's after creation, before Undo is %s" % (node , numNodesBeforeUndo))

  nuke.tprint("Calling nuke.undo()")
  nuke.undo()

  numNodesAfterUndo = len(nuke.allNodes(nodeToCheck))
  nuke.tprint("Number of %s's after nuke.undo() is %s" % (node ,numNodesAfterUndo))

  # First assert that the Undo has removed the  node we created
  if numNodesAfterUndo != 0:
    nuke.tprint("Undo failed to remove the %s node! There were %s %s nodes after calling nuke.undo()" %(node, numNodesAfterUndo, node))
    sys.exit(1)
  else:
    nuke.tprint("Asserted that Undo removed the node as expected.")

  nuke.tprint("Calling nuke.redo()")
  nuke.redo()

  NodesAfterRedo = nuke.allNodes(nodeToCheck)
  numNodesAfterRedo = len(NodesAfterRedo)

  nuke.tprint("Number of %s's after nuke.redo() is %s" % (node, numNodesAfterRedo))

  # Second assert that the Redo put the original  node back
  if numNodesAfterRedo != 1:
    nuke.tprint("Failed to Restore the %s node! There were %s %s nodes after calling nuke.undo()" % (node ,numNodesAfterUndo, node))
    sys.exit(1)
  else:
    restoredNode = NodesAfterRedo[0]
    nuke.tprint("Asserted that Redo restored a %s node.. now assert it's the same!..." % (node))

  # Third assert - the  Node after Redo is identical to the original  node
  if restoredNode != originalNode:
    nuke.tprint("Redo failed to restore the original %s node! (original %s, restored %s)" % (node, (str(originalNode), str(restoredNode))))
    sys.exit(1)
  else:
    nuke.tprint("Asserted the restored %s node is identical the original after Redo!..." % (node))
    # If we're here, we've passed all the asserts. Exit with zero exit status
    nuke.tprint("All tests for UndoRedoSingleNode passed. Exiting with zero exit status")
    # sys.exit(0)



getNodes(nuke.menu("Nodes"))
sys.exit(0)
