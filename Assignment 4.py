#ex.1
def is_palindrome(string):
  stack = []
  for char in string:
    stack.append(char)
  reversed_string = ""
  while stack:
    reversed_string += stack.pop()
  return string == reversed_string
string1 = "mom"
string2 = "Neveroddoreven"
string3 = "hello"
print(is_palindrome(string1))
print(is_palindrome(string2))
print(is_palindrome(string3))
#EX2
def is_balanced(expression):
  stack1 = []
  opening_brackets = "([{"
  closing_brackets = ")]}"

  for char in expression:
    if char in opening_brackets:
      stack1.append(char)
    elif char in closing_brackets:
      if not stack1:
        return False
      top_element = stack1.pop()
      if opening_brackets.index(top_element) != closing_brackets.index(char):
        return False

  return not stack1
expressions = ["(1+2)-3*[41+6]", "(1+2)-3*[41+6}", "(1+2)-3*[41+6", "(1+2)-3*]41+6[", "(1+[2-3]*4{41+6})"]

for expression in expressions:
  print(expression, ":", is_balanced(expression))

#ex3:
  def decode_mib_message(message):

    stack2 = []
    decoded_message = ""

    for char in message:
      if char.isalpha() or char.isspace():
        stack2.append(char)
      elif char == '*':
        if stack2:
          stack2.pop()
    while stack2:
      decoded_message += stack2.pop()

    # Reverse the decoded message to get the correct order
    return decoded_message[::-1]

  message = "SIVLE ****** DAED TNSI ***"
  decoded_message = decode_mib_message(message)
  print(decoded_message)
#EX 4:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def deleteAtLocation(self,position):
        if self.head is None:
            print("Linked list is empty")
            return

        if position < 0:
            print("Invalid position")
            return

        if position == 0:
            self.head = self.head.next
            return

        current = self.head
        previous = None
        count = 0

        while current and count < position:
            previous = current
            current = current.next
            count += 1

        if current is None:
            print("Position out of bounds")
            return

        previous.next = current.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Example usage:
llist = LinkedList()
llist.head = Node(12)
second = Node(56)
third = Node(76)
fourth = Node(11)
fifth = Node(0)

llist.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

print("Original Linked List:")
llist.printList()

llist.deleteAtLocation(0)
print("Linked List after deleting node at position 0:")
llist.printList()

llist.deleteAtLocation(3)
print("Linked List after deleting node at position 3:")
llist.printList()