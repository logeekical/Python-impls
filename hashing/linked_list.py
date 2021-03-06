class LinkedListNode(object):
	def __init__(self, data):
		self.data = data
		self.next = None
		
class LinkedList(object):

	def __init__(self):
		self.first = LinkedListNode(None)
		self.last = self.first
		self.size = 0
	#Add any Element at a given position(None for the addition of new Node at the end)
	def add(self,data,pos=None):
		new_node = LinkedListNode(data)
		if pos is None:
			if self.size == 0:
				self.first.data = data
			else:

				self.last.next = new_node
				self.last = new_node
		else:
			current_node = self.first
			if pos == 1:
				new_node.next = self.first
				self.first = new_node
			else:
				for index in range(1,pos - 1):
					current_node = current_node.next
				new_node.next = current_node.next
				current_node.next = new_node

		self.size += 1

	#get Data on a particular index
	def getdata(self,index):
		if index > self.size :
			raise IndexError("Index cannot be greater than the maximum size : " + str(self.getSize()))
		current_node = self.first
		for indx in range(index - 1):
			current_node = current_node.next
		print current_node.data

	#Add multiple item by a list or tuple
	def addAll(self,lst):
		for item in lst:
			self.add(item)

	#Get the size of linkedList
	def getSize(self):
		return self.size

	#Print all the elements of LinkedList
	def prnt(self):
		current_node = self.first
		for i in range(self.size):
                       if current_node.data == None:
                               print "None" ,
                       else:
                               print current_node.data ,
                       current_node = current_node.next
	#Deleting a node from an index
	def delete(self,index):
		current = self.first
		if index == 0:
			self.first = self.first.next
			self.size -= 1
			return True
		for i in range(0,self.size-1):
			if i == index - 1:
				#print i,current.data
				if current.next.next is not None: #in case of last element
					current.next = current.next.next #skips the element to be deleted which is current.next
					self.size -= 1 #Reduce size by 1
					return True
				else:
					current.next = None
					self.last = current
					self.size -= 1
					return True
			current = current.next
			#print "New size is : ", self.size
		return False
	#
	#Method for deleting an element in the Linked List
	#
	def del_node(self,value,occurence=0):
		occur = 0
		i = 0
		k = 0 #Keeps track of number of deletions and thus will maintain the length of loop running.
		current_node = self.first
		for i in range(0, self.size - k):
                        #print "size : " , self.size
			if current_node.data == value:
				print "Deleting Node at index " , i , " in array " , self.prnt() ,"and size",self.getSize()
				self.delete(i-k)
				k += 1
				occur += 1
			current_node =  current_node.next
			if occurence != 0 and occur == occurence:
				break
	def lookup(self, value):
		""" Searches for a particular record and returns index in case it is found else False"""
		current =  self.first
		found = False
		for i in range(self.size):
			if  current.data == value:
				found = True
				return i
			else :
				current = current.next
		if not found:
			return -1
