#Use python3
import time

def timer(func):
	def newfunc(*args, **kws):
		t0 = time.time()
		result = func(*args, **kws)
		t1 = time.time()
		print(func.__name__,*args)
		print(t1 - t0)
		return result
	return newfunc

def find(node,nodeset):
	for x in nodeset:
		if node in x:
			return x
class Graph(object):
	def __init__(self, nodes, edges):
		self.nodes = nodes
		self.edges = edges

	@timer
	def Kruskal(self):
		mst = []
		index = 0
		nodeset = []
		for node in self.nodes:
			nodeset.append(set(node))
		edges = sorted(self.edges, key = lambda x:x[2])
		edgesnum = len(self.nodes)-1
		while index < len(self.nodes):
			node1,node2,weight = edges[index]
			node1superset = find(node1,nodeset)
			node2superset = find(node2,nodeset)
			print(node1superset)
			if node1superset != node2superset:
				mst.append(edges[index])
				nodeset.remove(node1superset)
				nodeset.remove(node2superset)
				newset = node1superset.union(node2superset)
				nodeset.append(newset)
			index += 1
		return mst

def main():
	nodes = list('ABCDEFGHI')
	edges = [["A", "B", 4], ["A", "H", 8],
             ["B", "C", 8], ["B", "H", 11],
             ["C", "D", 7], ["C", "F", 4],
             ["C", "I", 2], ["D", "E", 9],
             ["D", "F", 14], ["E", "F", 10],
             ["F", "G", 2], ["G", "H", 1],
             ["G", "I", 6], ["H", "I", 7]]

	graph = Graph(nodes,edges)
	print(graph.Kruskal())

if __name__ == '__main__':
	main()
			
