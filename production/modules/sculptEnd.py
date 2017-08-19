import toolutils

def sculptEnd(scriptargs):
    sopnode = scriptargs['node']
    viewer = toolutils.sceneViewer()
    node = sopnode.node("FLOWER")
    node.setCurrent(True, True)
    node.setRenderFlag(True)
    node.setDisplayFlag(True)
    viewer.enterCurrentNodeState()