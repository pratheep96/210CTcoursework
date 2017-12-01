class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
 
 
def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print (tree.value)
    if(tree.right!=None):
        in_order(tree.right)
 
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)

#Function to delete node 
def delete_node(self, node):
    if node==None:
        print ("Node to be deleted is not found in BST")
        return None
    if node.parent==None:
            self.tree=None
            return None

    tree_parent=tree.parent

#CASE 1 - There are no children in the node
    if tree_children==0:
        if tree_parent.left_child==node:
               tree_parent.left_child=None
    else:
        tree_parent.right_child=None
                    

#CASE 2 - Node has 1 child
    if tree_children==1: 
        if tree.left_child!=None:
                child=tree.left_child
    else:
	        child=tree.right_child
    if tree_parent.left_child==tree:
	        tree_parent.left_child=child
    else:
                tree_parent.right_child=child
                child.parent=tree_parent

#CASE 3 - Node has 2 children
    if tree_children==2:
        if tree.left_child>tree.right_child        
                tree_parent=tree.left_child
        else:
            tree.right_>tree.left_child
                tree_parent=tree.right_child

#Title: Binary Tree Search in Python
#Author: Hintea, D.
#Date: 2017
#Availability: http://cumoodle.coventry.ac.uk 
