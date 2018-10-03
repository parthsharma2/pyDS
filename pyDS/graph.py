from collections import defaultdict 
# defaultdict will make news keys if key does not exist

class Graph():
	"""An implementation of graph data structure."""
	def __init__(self):
		self._edges = []
		self._graph = defaultdict(list) 

	def __len__(self):
		return (len(self._edges))

	def __str__(self):
		"""Return the string representation of the Graph."""
		return str(self._items)

	def __repr__(self):
		return "pyDS.graph.Graph({})".format(self._graph)

	def addEdge(self,u,v):
		self._graph[u].append(v)
		return (self._graph) 

	def generateEdges(self):
		"""Returns all the edges in tuple inside a list. Ex - [(a,b),(c,d)]"""
		edges = []
		for node in self._graph:
			for neighbour in self._graph[node]:
				edges.append((node, neighbour))

		return (edges) 

