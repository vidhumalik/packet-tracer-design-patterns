class pathNode:
	def __init__(self, currNode, parent):
		self.currNode = currNode
		self.childrenList = []
		self.parent = parent #Backward reference from child node to parent node
	def addChild(self, newChild):
		self.childrenList.append(newChild)
	def getCurrNode(self):
		return self.currNode
	def getChildren(self):
		return self.childrenList