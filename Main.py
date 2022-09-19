class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
    # Write your code here
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def pop(self) -> None:
    # Write your code here
    if(self.head != None): 
      temp = self.head
      self.head = temp.next
      temp.next = None

  def status(self):
    """
    It prints all the elements of stack.
    """
    # Write your code here 
    if(self.head != None):
      temp = self.head
      while(temp.next != None):
        print(temp.data, end = "=>")
        temp = temp.next
      else:
        print(temp.data,"None", sep="=>")
    else:
      print("None")


# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
 
