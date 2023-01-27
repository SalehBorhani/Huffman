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
    
    def make_heap(self, frequency):
        for key in frequency:
            node = HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        while(len(self.heap) > 1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            merged = HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(self.heap, merged)

    def make_codes_helper(self, root, current_code):
        if(root == None):
            return
        if(root.char != None):
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return
        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def make_codes(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)

    def get_encoded_text(self, text):
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text
    
    def pad_encoded_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"
        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text
    
    def get_byte_array(self, padded_encoded_text):
        if(len(padded_encoded_text) % 8 != 0):
            print("Encoded text not padded properly")
            exit(0)
        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            b.append(int(byte, 2))
        return b
    
    def compress(self):
        # Get file from path
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + ".cmp"
        
        # Read text from file
        with open(self.path, 'r') as file, open(output_path, 'wb') as output:
            text = file.read()
            text = text.rstrip()

            # Make frequency dictionary using the text
            frequency = self.make_frequency_dict(text)

            # Calculate the length of the frequency dictionary
            frequency_dict_length = len(frequency)

            # Construct the Huffman tree
            self.make_heap(frequency)
            self.merge_nodes()
            self.make_codes()

            # Add the encoded of the frequency of every character for decompression
            # And also the encoded length of the frequency dictionary
            freq_encoded_text = ""
            for key in frequency:
                freq_encoded_text += '{0:08b}'.format(len('{0:08b}'.format(ord(key))))
                freq_encoded_text += '{0:08b}'.format(ord(key))
                freq_encoded_text += '{0:08b}'.format(len('{0:08b}'.format(frequency[key])))
                freq_encoded_text += '{0:08b}'.format(frequency[key])

            frequency_dict_length = '{0:08b}'.format(frequency_dict_length)    
            # Create encoded text

            encoded_text = self.get_encoded_text(text)
            encoded_text = frequency_dict_length + freq_encoded_text + encoded_text

            # Pad encoded text
            padded_encoded_text = self.pad_encoded_text(encoded_text)

            # Convert padded encoded text to bytes
            b = self.get_byte_array(padded_encoded_text)

            # Write to output file
            output.write(bytes(b))

        return output_path
    
    # Functions for decompression

    def remove_padding(self, padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)

        padded_encoded_text = padded_encoded_text[8:] 
        encoded_text = padded_encoded_text[:-1*extra_padding]

        return encoded_text
    
    



