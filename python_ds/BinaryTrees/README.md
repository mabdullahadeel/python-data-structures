# Binary Tree Data Structure

A **_binary tree_** is a data structure in which each node at most two
children, which are referred to as the left child and the right child.
```
       Parend Node (root node)
             /    \
            /      \
           /        \
       left child   right child
```
<hr>

### Depth of Node

The length of the path from a node to the root node. Keeping this in mind,
the length of the parent/root node is always `0`.
```
            root node
               2
             /    \
            /      \
           /        \
          7          5  -----------> Depth = 1
       /    \          /   \
     /        \       /     \
    6          9     2       6   -----------Depth = 2
```
In the above tree, the depth of the nodes with data `7` and `5` is `1`

<hr>

### Height Of a Tree
The length of the path from n to its deepest descendant. The height of the 
tree itself is the height of the root node, and the height of leaf nodes is 
always `0`.
```
    Height of a Tree = Height of a Root Node
```

<hr>

### Types of Binary Tree
There are following main types of Binary Trees

#### Complete Binary Tree
In a complete binary tree, every level except possibly the last, is completely filled and all nodes in the last level 
are as far left as possible.

![Complete Binary Tree](imgs/complete_bt.PNG)

### Full Binary Tree

A full binary tree (sometimes referred to as a proper or plane binary tree) is a tree in which every node has either 
`0` or `2` children.

![Complete Binary Tree](imgs/full_bt.PNG)

<hr>

## Approaches
Tree Traversal is the process of visiting (checking or updating) each node in a tree data structure, exactly once. 
Unlike linked lists or one-dimensional arrays that are canonically traversed in linear order, 
trees maybe traversed in multiple ways. They may be traversed in `depth-first` or `breadth-first` 
order.

There are three common ways to traverse a tree in depth-first order

- Pre-order
- In-order
- Post-order

#### Pre-order Traversal

Here is common approach/algorithm considered while considering `pre-order` traversal.

- 1- Check if current node is empty/null.
- 2- Display or Store `data/value` part of the root(current node)
- 3- Traverse the left sub-tree by recursively calling the pre-order method.
- 4- Traverse the right sub-tree by recursively calling pre-order method.

#### In-order Traversal

Here is common approach/algorithm considered while considering `in-order` traversal.

- 1- Check if current node is empty/null.
- 2- Traverse the left sub-tree by recursively calling the Display or Store `data/value` part of the root(current node)
- 3- Display or Store `data/value` part of the root(current node)
- 4- Traverse the right sub-tree by recursively calling in-order method.

#### Post-order Traversal

Here is common approach/algorithm considered while considering `post-order` traversal.

- 1- Check if current node is empty/null.
- 2- Traverse the left sub-tree by recursively calling the post-order method.
- 3- Traverse the right sub-tree by recursively calling post-order method.
- 4- Display or Store `data/value` part of the root(current node).

<hr>

### Level Order Traversal
The output of the level order traversal is shown in te figure below. This tells how
this traversal operates on binary tree.

![Level Order](imgs/level_order.PNG)