// ファイルパスのリネーム

import pymel.core as pm

class replaceFilePath:

	def __init__( self ):
		oldPath = None
		replacePath = None

		with pm.window( title = 'Replace File Path', resizeToFitChildren = True ) as rfpWindow:
			with pm.columnLayout( adjustableColumn = True ):
				with pm.rowColumnLayout( numberOfColumns = 2, columnAttach = [(1, 'right', 5), (2, 'both', 5)], backgroundColor = [0.5, 0.5, 0.5], adjustableColumn = True ):
					pm.text( 'Old Path' )
					txtOldPath = pm.textField()

					pm.text( 'Replace Path' )
					txtreplacePath = pm.textField()

				with pm.columnLayout( adjustableColumn = True ):
					btnReplace = pm.button( 'Replace' )
					
	def replaceAll( self ):
		fileNodes = pm.ls( type = 'file' )

		for fileNode in fileNodes:
			beforePath = fileNode.getAttr( 'fileTextureName' )
			newPath = beforePath.replace( oldPath, replacePath )

			fileNode.setAttr( 'fileTextureName', newPath )
