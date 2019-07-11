from collections import OrderedDict
from pydoc import locate
import pickle
import json

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def to_ordered_dict(root):
    """
    Converts the tree defined by the root Node to an OrderedDict and returns it
    
    This will be converted later to a JSON string
    """

    if not root:
        return None
    
    obj = OrderedDict([
        ('val', root.val),
        ('type', type(root.val).__name__),
        ('left', to_ordered_dict(root.left)),
        ('right', to_ordered_dict(root.right))
    ])

    return obj

def from_json(obj):
    """
    Takes a deserialized object and converts it to our Node structure

    Returns the root Node identified by the base parameters of obj
    """

    if not obj:
        return None
    
    node = Node(locate(obj['type'])(obj['val']),
                from_json(obj['left']),
                from_json(obj['right']))
    
    return node

def serialize(root):
    return json.dumps(to_ordered_dict(root))

def deserialize(s):
    """
    Assumes s is a JSON-serialized string of the format in to_ordered_dict

    Deserializes the string and returns the root Node
    """

    return from_json(json.loads(s))

def serialize_with_pickle(root):
    return str(pickle.dumps(root))

def deserialize_with_pickle(s):
    return pickle.loads(bytes(s))

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
assert deserialize_with_pickle(serialize_with_pickle(node)).left.left.val == 'left.left'