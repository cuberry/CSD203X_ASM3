"""
This is supporting class modules for BST constructing with AVLTRee
    - In order traversal
    - BFS
Date created: 31-Aug-2022
Originator: anhvtFX17909

<This code/ method is referred from the presentation of Mr. Samaksh Namdev Drum
                          www.instagram.com/samaksh_namdev>

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

    Assessment: with three first nodes, to balance during adding new node,
                            if L-R or R-L is occurred, we can swap the 3rd node to root or leaf to parent of parent
                            as formular to re-balance the AVLTree
                            
    LL Heavy                       LR Heavy                    RR Heavy                    RL Heavy
            3                                    3                                     1                                      1 
           /                                   /                                           \                                       \
         2                                  1                                               2                                       3
        /                                       \                                            \                                   /
    1                                            2                                           3                           2
    
            2                                   3                                      2                                     1
        /       \                               /                                      /   \                                       \
    1           3                           2                                     1      3                                      2
                                            /                                                                                           \
                                        1                                                                                                 3      

                                                2                                                                                2  
                                            /       \                                                                           /   \
                                        1            3                                                                      1       3


"""


class Node:
    def __init__(self, data, parent=None):
        """
        input p: is one list of one personal info
        """
        self.data = data  # Person info >> using p for personal info
        self.parent = parent
        self.height = 0
        self.left = None
        self.right = None


"""
Can use queue or dequeue library but the small class Queue shall be
used in this assignment
"""


class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        self.queue.append(data)
        self.size += 1

    def dequeue(self):
        self.queue.pop(0)
        self.size -= 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        #   Calculate the height of AVLTree
        if not node:
            return -1
        return node.height

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.__insert_node__(data, self.root)

    def __insert_node__(self, data, node):
        node_id = node.data[0]  # data managed by ID
        if data[0] < node_id:  # compare by ID (p[0])
            #   If node.left is unavailable, insert this node to the left
            #   else add the new node
            #   then balance the tree
            if node.left:
                self.__insert_node__(data, node.left)
            else:
                node.left = Node(data, node)
                self.__re_balance__(node.left)

        #   If node.right is unavailable, insert this node to the right
        #   else add the new node
        #   then balance the tree
        if data[0] > node_id:
            if node.right:
                self.__insert_node__(data, node.right)
            else:
                node.right = Node(data, node)
                self.__re_balance__(node.right)

    def __re_balance__(self, node):
        """
        :input: the node added to AVLTree
        :return: re-balance the AVLTree
        calculate the height = max(left child's height, right child's height) + 1
        """
        while node:
            node.height = max(self.height(node.left), self.height(node.right)) + 1
            self.__balance_fix__(node)
            node = node.parent  # iterable the node in AVLTree

    def __balance_fix__(self, node):
        """
        :param node:
        :return:    refer top explanation about the rotation method
         c1. left - left unbalanced: balanced_factor > 1: rotate to the right
         c2. left - right unbalanced: balanced_factor of node. Left < 0 or -1
         c3. right - right unbalanced: balanced_factor < -1: rotate to the left
         c4: right - left unbalanced: balanced_factor of node. Right > 0 or 1
        """
        #   left-left unbalance >> rotate the tree to right
        if self._balance_factor(node) > 1:
            #   left-right heavy >> rotate tree to left then to right
            if self._balance_factor(node.left) < 0:  # -1 give the infinite loop>
                self.__rotate_left__(node.left)
            self.__rotate_right__(node)

        #   right-right unbalance >> rotate the tree to left
        if self._balance_factor(node) < -1:
            #   right-left heavy >> rotate tree to right then to left
            if self._balance_factor(node.right) > 0:
                self.__rotate_right__(node.right)
            self.__rotate_left__(node)

    def _balance_factor(self, node):
        """
        :input node: the node at position
        :output: calculate the different between left node child and right node child
                        balance_factor = [node.left] - [node.right]
        """
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def __rotate_left__(self, node):
        #   creat a temporary node to move the node
        temp = node.right
        p = node.right.left

        #   update the reference temporary
        temp.left = node
        node.right = p

        #   update parent to child
        temp_parent = node.parent
        temp.parent = temp_parent
        node.parent = temp
        if p:
            p.parent = node

        #   update parent to child
        if temp.parent:
            if temp.parent.left == node:
                temp.parent.left = temp
            elif temp.parent.right == node:
                temp.parent.right = temp
        else:
            self.root = temp

        # update the height of the nodes
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        temp.height = max(self.height(temp.left),
                          self.height(temp.right)) + 1
        print(f"left rotation on {node.data}...")

    def __rotate_right__(self, node):
        temp = node.left
        p = node.left.right

        # update the references temporary
        temp.right = node
        node.left = p

        # child to parent
        temp_parent = node.parent
        temp.parent = temp_parent
        node.parent = temp
        if p:
            p.parent = node

        # parent to child
        if temp.parent:
            if temp.parent.left == node:
                temp.parent.left = temp
            elif temp.parent.right == node:
                temp.parent.right = temp
        else:
            self.root = temp
        print(f"right rotation on {node.data}...")

        # update the height of the nodes
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        temp.height = max(self.height(temp.left),
                          self.height(temp.right)) + 1

    def remove(self, ids):
        if self.root:
            self.__remove__(self.root, ids)

    def __remove__(self, node, ids):
        #   find the node to be removed:
        id = node.data[0]
        if ids < id:
            if node.left:
                self.__remove__(node.left, ids)
        elif ids > id:
            if node.right:
                self.__remove__(node.right, ids)
        #   if found
        elif ids == id:
            #   Case 1: if the node is leaf:
            #       delete the node then
            #       update all left - right of parent to none
            if not node.left and not node.right:
                node_parent = node.parent
                if node_parent.left == node:
                    node_parent.left = None
                elif node_parent.right == node:
                    node_parent.right = None
                else:
                    self.root = None
                del node
                self.__re_balance__(node_parent)
            #   Case 2: if the node has left child:
            #       delete the node then
            #       update left node to parent then delete node/ balance the tree
            elif node.left and not node.right:
                node_parent = node.parent
                if node_parent.left == node:    # this node to be deleted
                    node_parent.left = node.left
                elif node_parent.right == node:
                    node_parent.right = node.left
                else:
                    self.root = node.left
                #   update the current parent to new node moved from left
                node.left.parent = node_parent
                del node
                self.__re_balance__(node_parent)
            #   Case 3: if the node has right child:
            #       update the right child to new parent
            #       update right node to parent then delete node/ balance the tree
            elif not node.left and node.right:
                node_parent = node.parent
                if node_parent.left == node:
                    node_parent.left = node.right
                elif node_parent.right == node:
                    node_parent.right = node.right
                else:
                    self.root = node.right
                #   update the current parent to new node moved from left
                node.right.parent = node_parent
                del node
                self.__re_balance__(node_parent)
            #   Case 4: if the node has both right child and left child:
            #       find successor nodes - smallest node in the right branches of tree
            #       move the data of node to that successor node
            #       re-balance the tree
            elif node.left and node.right:
                s_node = self.__find_successor_node__(node.right)
                s_node.data, node.data = node.data, s_node.data
                #   After swapping the value, recall the function back to previous case
                self.__remove__(node.right, s_node.data[0])

    def __find_successor_node__(self, node):
        if node.left:
            return self.__find_successor_node__(node.left)
        return node

    def inoder_traversal(self):
        if self.root:
            self.__inorder__(self.root)

    def __inorder__(self, node):
        if node.left:
            self.__inorder__(node.left)
        i = node.data
        print('{:<8}{:<30}{:<20}{:<10}'.format(i[0], i[1], i[2], i[3]))
        # print('{:<8}{:<30}'.format(i[0], i[1]))
        if node.right:
            self.__inorder__(node.right)

    def postorder_traversal(self):
        # This method is created for reference only
        if self.root:
            self.__postorder__(self.root)

    def __postorder__(self, node):
        if node.left:
            self.__postorder__(node.left)
        if node.right:
            self.__postorder__(node.right)
        print(node.data)

    def search(self, ids):
        if self.root:
            return self.__search__(ids, self.root)

    def __search__(self, ids, node):
        node_id = node.data[0]
        if ids < node_id:
            if node.left:
                return self.__search__(ids, node.left)
        elif ids > node_id:
            if node.right:
                return self.__search__(ids, node.right)
        elif ids == node_id:
            i = node.data
            print('{:<8}{:<30}{:<20}{:<10}'.format('ID', 'Name', 'DOB', 'Birth Place'))
            print('{:<8}{:<30}{:<20}{:<10}'.format(i[0], i[1], i[2], i[3]))
            return True
        print('This person id is not available, please add if required.....')
        return False

    def bfs_traversal(self):
        if self.root:
            self.__bfs__(self.root)

    def __bfs__(self, node):
        """
        :param node:
        :output: implement the queue for BFS traversal
                 use FIFO to insert the visited node
        """
        if not node:
            return
        #   Start initiate the Queue
        q = Queue()
        q.enqueue(node)

        #   start the bfs for AVLTree
        while not q.is_empty():
            temp = q.queue[0]
            t = temp.data
            print('{:<8}{:<30}{:<20}{:<10}'.format(t[0], t[1], t[2], t[3]))
            if temp.left:
                q.enqueue(temp.left)
            if temp.right:
                q.enqueue(temp.right)
            q.dequeue()

