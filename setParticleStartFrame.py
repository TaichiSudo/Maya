// シーン内のparticleのスタートフレームを変更する

import maya.cmds as cmds

def setParticleStartFrame():
  startFrame = cmds.playbackOptions(q = True, min = True)
  pShapes = cmds.ls(type = "particle")
	
for obj in pShapes:
  pShapeStartAttr = obj + ".startFrame"
  cmds.setAttr(pShapeStartAttr, startFrame)

cmds.select( pShapes )
