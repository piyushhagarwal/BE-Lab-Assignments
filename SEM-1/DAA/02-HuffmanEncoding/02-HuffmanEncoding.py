# Huffman Encoding is a widely-used algorithm for data compression, which uses variable-length codes for encoding symbols based on their frequencies. 
# It uses a greedy strategy by building the optimal encoding tree from the bottom up, always merging the two lowest-frequency nodes. 
# Here is the implementation along with comments.

# Theory
# Greedy Approach: Huffman Encoding is a classic example of a greedy algorithm. 
# It repeatedly chooses the two least-frequent nodes, combines them, and repeats until a single tree is formed.
# Encoding Tree: The final Huffman tree represents the optimal encoding, where each symbol's path from the root to the leaf node forms its binary code.


# Steps
# 1. Count the frequency of each character in the input data.
# 2. Create a priority queue (or min-heap) of nodes, with the lowest frequency at the root.
# 3. While there are more than one node in the heap:
# 4. Extract the two nodes with the lowest frequency.
# 5. Combine them to form a new node with a frequency equal to the sum of the two nodes.
# 6. Insert this new node back into the priority queue.
# 7. Assign binary codes to each character based on their position in the tree.

"""
Context: Compressing & decompressing data before/after transmission
"""

import heapq

class HuffmanCoding:
    def __init__(self):
        self.text = "" # text to be encoded/decoded text
        self.frequency = {} # stores characters in the text and their number of occurrences
        self.priority_queue = [] # store the occurrences in increasing order
        self.codes = {} # stores the codes of each character: char -> code
        self.reverse_code_mapping = {} # reverse mapping of codes: code -> char
        self.encoded_text = "" # text to be decoded

    class PriorityQueueNode:
        def __init__(self, char, freq):
            self.char = char # stores character
            self.freq = freq # stores number of occurrences of the character in the text
            self.left = None # left child
            self.right = None # right child
           
        # override these inbuilt functions to correctly make comparisons when creating heap 
        # The reason for this is that the heapq module in Python uses the less than operator to compare elements in the heap.
        # Now we need to define the less than and equal to operators for our PriorityQueueNode class so that the heapq module can correctly compare the nodes based on their frequencies.
        # The char with the lowest frequency should have the highest priority in the heap.
        def __lt__(self, other):
            return self.freq < other.freq
           
        def __eq__(self, other):
            if other == None:
                return False
            return self.freq == other.freq
    
    def make_frequency_dict(self):
        for char in self.text:
            if not char in self.frequency:
                self.frequency[char] = 0
            self.frequency[char] += 1
   
    def make_priority_queue(self):
        for key in self.frequency:
            node = self.PriorityQueueNode(key, self.frequency[key])
            heapq.heappush(self.priority_queue, node)
   
    def build_huffman_tree(self):
        while(len(self.priority_queue) > 1):
            node1 = heapq.heappop(self.priority_queue)
            node2 = heapq.heappop(self.priority_queue)
           
            summed_node = self.PriorityQueueNode(None, node1.freq + node2.freq)
            summed_node.left = node1
            summed_node.right = node2
           
            heapq.heappush(self.priority_queue, summed_node)
           
    def make_codes_helper(self, node, current_code):
        if node is None:
            return
        if not node.char is None:
            self.codes[node.char] = current_code
            self.reverse_code_mapping[current_code] = node.char
           
        self.make_codes_helper(node.left, current_code + "0")
        self.make_codes_helper(node.right, current_code + "1")
   
    def generate_codes(self):
        # generate codes for characters
        root = heapq.heappop(self.priority_queue)
        current_code = ""
       
        self.make_codes_helper(root, current_code)
   
    def encode_text(self):
        # replace input characters with generated codes
        for char in self.text:
            self.encoded_text += self.codes[char]
   
    def compress(self, text):
        self.text = text
        self.make_frequency_dict()
        self.make_priority_queue()
        self.build_huffman_tree()
        self.generate_codes()
        self.encode_text()
        # you can add padding into the bit string if data is to be saved in a file in bytes

        print("Original text: ", self.text)
        print("Compressed text: ", self.encoded_text)
       
    def decode_text(self):
        current_code = ""
        self.text = ""
       
        for bit in self.encoded_text:
            current_code += bit
            if current_code in self.reverse_code_mapping:
                character = self.reverse_code_mapping[current_code]
                self.text += character
                current_code = ""
               
       
    def decompress(self, encoded_text):
        self.encoded_text = encoded_text
        # first remove the padding if data saved in a file in bytes
        self.decode_text()
        print("Compressed text: ", self.encoded_text)
        print("Decoded text: ", self.text)
       
       
text = "BCAADDDCCACACAC"
huffman_coding_algo = HuffmanCoding()

huffman_coding_algo.compress(text)
encoded_text = huffman_coding_algo.encoded_text
print("\n")
huffman_coding_algo.decompress(encoded_text)