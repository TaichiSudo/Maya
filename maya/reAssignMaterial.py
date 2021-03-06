// 使い方
// 元のアセットのネームスペースを nsMaya に書き込んでください
// 次にアサインし直したいいオブジェクトを選択して実行。それだけです


import pymel.core as pm
import maya.cmds as cmds

sel = pm.selected()

// ここにプレフィックスを入力
//nsAbc = "test"
nsMaya = "treeHero:"

for obj in sel:
    abcShapeNode = obj.getShapes()
    // プレフィックスが何文字かを手入力
    // 次のバージョンで自動化予定
    refShapeNode = nsMaya + abcShapeNode[0][15:]
    
    // デバッグ用出力
//    print( "abc:" + abcShapeNode[0] )
//    print( "refShapeNode:" + refShapeNode 
//    print( "SG:" + sg[0] )

    sg = cmds.listConnections( refShapeNode, s = False, d = True, type = 'shadingEngine')
    cmds.sets( str(abcShapeNode[0]),  fe = sg[0] )
