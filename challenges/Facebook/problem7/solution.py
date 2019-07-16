# variable used for encoding mapping, no matter how we build it
mapping = {}
num_encoded = 26

for x in range(num_encoded):
    char = chr(ord('a') + x)
    mapping[char] = x + 1

class Node(object):
    def __init__(self, flag=False):
        self.flag = flag
        self.children = [None for _ in range(256)]
    
    def add(self, idx, flag=False):
        self.children[idx] = Node(flag)

    def set_flag(self, flag):
        self.flag = flag
    
    def get_child(self, idx):
        return self.children[idx]
    
    def search(self, so_far, val):
        result = []
        if self.flag:
            result.append(so_far)
        if not val:
            return result
        
        first = val[0]
        idx = ord(first)
        if self.get_child(idx):
            result.extend(self.get_child(idx).search(so_far + first, val[1:]))
        
        return result

def add_to_tree(node, val):
    if not val:
        node.set_flag(True)
    else:
        first = val[0]
        idx = ord(first)
        if not node.get_child(idx):
            node.add(idx)
        add_to_tree(node.get_child(idx), val[1:])

root = Node()
for x in mapping.values():
    add_to_tree(root, str(x))

def decode(encoded_str):
    """
    Decodes the argument encoded_str in all possible ways.

    Returns the number of encodings.
    """

    # if our input is empty, we've found a successful encoding!
    if not encoded_str:
        return 1
    
    # otherwise, for each encoding, check if it starts with a decoded value
    # if it does, add the number of decodings of the remainder
    encodings = 0
    for encoded_value in root.search('', encoded_str):
        val = str(encoded_value)
        if encoded_str.startswith(val):
            encodings += decode(encoded_str[len(val):])
    return encodings

assert decode('111') is 3
assert decode('51555') is 2
assert decode('10201') is 1