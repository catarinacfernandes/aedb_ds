from .tad_tree import Tree
from ..dictionaries.tad_ordered_dictionary import OrderedDictionary
from ..exceptions import DuplicatedKeyException, NoSuchElementException, \
    EmptyDictionaryException
from .nodes.binary_nodes import BinarySearchTreeNode


class BinarySearchTree(OrderedDictionary, Tree):
    def __init__(self):
        self.num_elements = 0
        self.root = None
        self.height = 0

    # Returns the number of elements in the dictionary.
    def size(self):
        return self.num_elements

    # Returns true if the dictionary is full.
    def is_full(self): pass

    # Returns the value associated with key k.
    # Throws NoSuchElementException
    def get(self, k):
        if self.root == None:
            raise NoSuchElementException()
        else:
            return self.search_value (self.root, k)
            
    def search_value(self, root, k):
        if root.get_key() == k:
            return root.get_element()
        elif root.get_key() > k:
            self.search_value(root.get_left_child(), k)
        elif root.get_key() < k:
            self. search_value(root.get_right_child(), k)

    # Inserts a new value, associated with key k.
    # Throws DuplicatedKeyException
    def insert(self,k,v):
        self.root = self.insert_element(self.root, k, v)

    def insert_element(self, root, k, v):
        if root is None:
            root = BinarySearchTreeNode(k, v)
            self.num_elements += 1
        else:
            if root.get_key() == k:
                raise DuplicatedKeyException()
            elif root.get_key() > k:
                node = self.insert_element(root.get_left_child(), k, v)
                root.set_left_child(node)
            else:
                node = self.insert_element(root.get_right_child(), k, v)
                root.set_right_child(node)
        return root

    # Updates the value associated with key k.
    # Throws NoSuchElementException
    def update(self, k, v):
        if self.root == None:
            raise NoSuchElementException()
        else:
            return self.update_value (self.root, k, v)
            
    def update_value(self, root, k, v):
        if root.get_key() == k:
            root.set_element(v)
        elif root.get_key() > k:
            self.update_value(root.get_left_child(), k, v)
        elif root.get_key() < k:
            self.update_value(root.get_right_child(), k, v)

    # Removes the key k, and the value associated with it.
    # Throws NoSuchElementException
    def remove(self, k): 
        if self.root = None:
            raise.NoSuchElementException
        else:
            self.root = self.remove_key(self.root, k)

    def remove_key(self, root, k, previous_root = None):
        if root.get_key() < k:
            self.remove_key(self.root.get_right_child(), k)
        elif root.get_key() > k:
            self.remove_key(self.root.get_left_child(), k)
        else:
            if root.is_leaf():
                if self.size() == 1:
                   root = None
                   self.num_elements() -= 1
                else:            
                if previous_root.get_right_child().get_key() == k:
                    current_root = previous_root.get_right_child()
                    current_root = None
                    self.num_elements () -= 1
                elif previous_root.get_left_child().get_key() == k:
                    current_root = previous_root.get_left_child()
                    current_root = None
                    self.num_elements() -= 1
            elif root.get_right_child() != None:
                pass
            elif root.get_left_child() != None:
                pass
            

    # Returns a List with all the keys in the dictionary.
    def keys(self): pass

    # Returns a List with all the values in the dictionary.
    def values(self): pass

    # Returns a List with all the key value pairs in the dictionary.
    def items(self): pass

    # Returns an iterator of the elements in the dictionary
    def iterator(self): pass

    # Returns the element with the smallest key
    # Throws EmptyTreeException
    def get_min_element(self):
        if self.is_empty():
            raise EmptyDictionaryException()
        return self.get_min_node(self.root).get_element()

    def get_min_node(self,root):
        if root.get_left_child() is None:
            return root
        return self.get_min_node(root.get_left_child())

    # Returns the element with the largest key
    # Throws EmptyTreeException
    def get_max_node(self,root):
        if root.get_right_child() is None:
            return root
        return self.get_max_node(root.get_right_child())

    # Returns the root of the tree
    # Throws EmptyTreeException
    def get_root(self):
        if self.root == None:
            raise EmptyTreeException()
        else:
            return self.root

    # Returns the height of the tree
    # Throws EmptyTreeException
    def height(self):
        return self.height

    # Returns True if the tree is empty
    def is_empty(self):
        if self.num_elements == 0:
            return True
        else:
            return False
    