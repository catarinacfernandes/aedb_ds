from abc import abstractmethod

from .tad_dictionary import Dictionary


class OrderedDictionary(Dictionary):
    # Returns an iterator of the elements in the dictionary
    def iterator(self): pass

    # Returns the element with the smallest key
    def get_min_element(self): pass
    

    # Returns the element with the largest key
    def get_max_element(self): pass
    
