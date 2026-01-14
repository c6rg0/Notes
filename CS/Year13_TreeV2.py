#  This program uses trees in a pre, in and post order. Change the program to include user interaction and a meaningful closure.
#Implement a user -friendly menu where the user can type "in", "pre", or "post" and it will automatically run that traversal.

#import tkinter

class Node:
    def __init__(self, name):
        # Store the name of the node
        self.name = name
        # Left child (initially None)
        self.left = None
        # Right child (initially None)
        self.right = None


# Traversal functions

# In-Order Traversal 
def in_order(node):
    if node:  # 
        in_order(node.left)  # 
        print(node.name)     # 
        in_order(node.right) # 

# Pre-Order Traversal 
def pre_order(node):
    if node:
        print(node.name)      #
        pre_order(node.left)  # 
        pre_order(node.right) # 

# Post-Order Traversal 
def post_order(node):
    if node:
        post_order(node.left)   # 
        post_order(node.right)  # 
        print(node.name)        #


# start to build the tree

# node creation
gabriel = Node("Gabriel")
hadley = Node("Hadley")
ciara = Node("Ciara")
alfred = Node("Alfred")
javan = Node("Javan")
josephine = Node("Josephine")
ollie = Node("Ollie")
anh = Node("Anh")
oakley = Node("Oakley")
akasi = Node("Akasi")
lily = Node("Lily")
misha = Node("Misha")
abraham = Node("Abraham")

# Build the tree structure
gabriel.left = hadley
gabriel.right = ciara

hadley.left = alfred
hadley.right = javan
alfred.left = anh

ciara.left = josephine
ciara.right = ollie
josephine.right = oakley
oakley.left = akasi
oakley.right = lily
lily.left = misha
misha.left = abraham

while True:
    print("Which binary search do you want to perform:")
    print("- Press the according number")
    print("1. In order traversal")
    print("2. Pre order traversal")
    print("3. Post order traversal")
    print("4. Exit the program :( ")
    
    selection = int(input())
    print()
    
    print("please input a number, not anything else")
    
    if selection == 1:
        print("In-Order Traversal:")
        in_order(gabriel)              

    if selection == 2:
        print("\nPre-Order Traversal:")  
        pre_order(gabriel)                

    if selection == 3:
        print("\nPost-Order Traversal:") 
        post_order(gabriel)                

    if selection == 4:
        print("Goodbye")
        print()
        break
    
    print()
