# **ASSIGNMENT 3 OF PYTHON DATABASE AND ALGORYTHM**

### **INTRODUCTION**
Assignment 3 of this course is the order to process below requirements:

* Understanding the BST
* Perform and apply the function/ balance of AVL TREE

### **CORE AVL-TREE**

To have the efficiency code, the AVLTree is applied for BST in this assignment
 Important notes:
1. BST is always balanced
2. AVLTree is used instead of normal BST
3. The parameters/ method to keep the Tree balanced:
    a. height = max(left.node's height, right.node's height) + 1, "None" will be -1
    b. balanced_factor = left.node's height - right.node's height:
        balanced_factor = {-1,0,1} (not more than 1)
    c. 4 requirements:
        c1. left - left unbalanced: balanced_factor > 1: rotate to the right
        c2. left - right unbalanced: balanced_factor of node.left < 0
        c3. right - right unbalanced: balanced_factor < -1: rotate to the left
        c4: right - left unbalanced: balanced_factor > 0

    Assessment: 
with three first nodes, to balance during adding new node,
                            if L-R or R-L is occurred, we can swap the 3rd node to root or leaf to parent of parent
                            as formular to re-balance the AVLTree
                            
    LL Heavy             LR Heavy                    RR Heavy                    RL Heavy
            3               3                                     1                                      1 
           /              /                                           \                                       \
         2               1                                               2                                       3
        /                 \                                            \                                   /
    1                       2                                           3                           2
    
            2              3                                      2                                     1
        /       \         /                                      /   \                                       \
    1           3        2                                     1      3                                      2
                        /                                                                                           \
                        1                                                                                                 3      

                           2                                                                                2  
                         /   \                                                                           /   \
                       1       3                                                                       1       3


