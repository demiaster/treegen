import toolutils

def sculptStamenBase(scriptargs):
    sopnode = scriptargs['node']
    viewer = toolutils.sceneViewer()

    sculpt = sopnode.node("stamenbase_sculpt")

    sculpt.setCurrent(True, True)
    sculpt.setRenderFlag(True)
    sculpt.setDisplayFlag(True)
    viewer.enterCurrentNodeState()
    
#def sculptSBASE(scriptargs):
#    aborted = False
#    
#    with hou.InterruptableOperation(“doing stuff”, open_interrupt_dialog=True) as operation:
#        sopnode = scriptargs['node']
#        viewer = toolutils.sceneViewer()
#        sculpt = sopnode.node("stamenbase_sculpt")
#        sculpt.setCurrent(True, True)
#        sculpt.setRenderFlag(True)
#        sculpt.setDisplayFlag(True)
#        viewer.enterCurrentNodeState()
#        try:
#            operation.updateProgress()
#        except hou.OperationInterrupted:
#            aborted = True
#            
#        if aborted == True:
#            sopnode = scriptargs['node']
#            viewer = toolutils.sceneViewer()
#            node = sopnode.node("FLOWER")
#            node.setCurrent(True, True)
#            node.setRenderFlag(True)
#            node.setDisplayFlag(True)
#            viewer.enterCurrentNodeState()
