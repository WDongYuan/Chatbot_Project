from __future__ import print_function
from Wit_Project2 import Gateway

class Node:
	def __init__(self,depth,featurename,branchclass):
		self.name = featurename
		self.questionSet = []
		self.depth = depth
		self.child = []
		self.joke = []
		self.vector = []
		self.infervector = []
		self.branchclass = branchclass

	def ShowNode(self):
		print("question"+str(self.questionSet)+": "+self.name+", vector: "\
			+str(self.vector)+" "+str(self.joke)+" "\
			+str(self.questionSet)+" infervector: "+str(self.infervector))
	def LeafGetJoke(self,moviename):
		print(self.vector,moviename)
		tmpv = Gateway(self.vector,moviename)
		# tmpv = ["1","1","1","1","1"]
		error = 0
		for i in range(len(tmpv)):
			print(i)
			if tmpv[i]!=self.infervector[i]:
				error += 1
		if float(error)/len(tmpv)>0.5:
			return self.joke[0]
		else:
			return self.joke[1]

class Feature:
	def __init__(self,vector,feature):
		self.vector = vector
		self.feature = feature
		self.inferencevector = []
class Tree:


	def BuildTree(self,depth,question):
		if depth>self.depth:
			return None
		if depth!=self.depth:
			node = Node(depth,self.featureSet[depth-1],self.branchclass)
			node.questionSet = question[node.name]
		else:
			node = Node(depth,"joke",self.branchclass)
		for i in range(len(self.branchclass)):
			node.child.append(self.BuildTree(depth+1,question))
		return node
	def Initialize(self):
		self.pointer = self.root

	def __init__(self,featureSet,question,branchclass):
		self.featureSet = featureSet
		self.depth = len(featureSet)+1
		self.branchnum = len(branchclass)
		self.branchclass = [br for br in branchclass]
		self.root = self.BuildTree(1,question)
		self.pointer = self.root

	def ShowTree(self,node):
		if node==None:
			return
		node.ShowNode()
		for ch in node.child:
			self.ShowTree(ch)

	def AddSample(self,vector,infervector,joke):
		node = self.root
		while node.depth<=len(vector):
			node = node.child[int(vector[node.depth-1])]
		node.joke=joke
		node.vector = vector
		node.infervector = infervector

	def AskQuestion(self):
		print("Question: "+str(self.pointer.questionSet[0]))

	def Answer(self,ans):
		for i in range(len(self.pointer.branchclass)):
			if ans == self.pointer.branchclass[i]:
				self.pointer = self.pointer.child[i]
		if self.pointer.name=="joke":
			print(self.pointer.LeafGetJoke("Avatar"))
			self.Initialize()
			


file = open("scripts.csv.rtf")
file.readline()
ss = file.readline().strip()
data = []
while ss!=None and ss!="":
	arr = ss.split(",")
	treevector = []
	for i in range(len(arr[1])):
		treevector.append(arr[1][i])
	infervector = []
	for i in range(len(arr[2])):
		infervector.append(arr[2][i])
	data.append([treevector,infervector,[arr[0],arr[3]]])
	ss = file.readline().strip()

questionMap = {"seen_movie":["Have you seen the movie XXX"],\
"like_movie": ["Do you like the movie XXX?"],\
"like_actor": ["Do you like the actor XXX in this movie"],\
"like_director": ["Do you like the director XXX?"],\
"like_story": ["Do you like the story"],\
"like_genre":["Do you like the genre of the movie"]}

feature = ["seen_movie","like_movie","like_actor","like_director", "like_story","like_genre"]
tree = Tree(feature,questionMap,["yes","no","don't know"])

for sample in data:
	print(sample)
	tree.AddSample(sample[0],sample[1],sample[2])
# tree.ShowTree(tree.root)

tree.AskQuestion()
tree.Answer(raw_input(""))
tree.AskQuestion()
tree.Answer(raw_input(""))
tree.AskQuestion()
tree.Answer(raw_input(""))
tree.AskQuestion()
tree.Answer(raw_input(""))
tree.AskQuestion()
tree.Answer(raw_input(""))
tree.AskQuestion()
tree.Answer(raw_input(""))
#Question Map:






	
