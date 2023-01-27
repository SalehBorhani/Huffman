import heapq
import os

# Define a class to represent a node in the Huffman tree
class HeapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    # Defining comparators less_than and equals
    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, HeapNode)):
            return False
        return self.freq == other.freq

class HuffmanCoding:
    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    # Functions for compression
    def make_frequency_dict(self, text):
        frequency = {}
        for character in text:
            if not character in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency
    
    
