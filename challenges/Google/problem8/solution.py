class Node(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self._left = left
        self._right = right
    
    def get_left(self):
        return self._left
    
    def get_right(self):
        return self._right
    
    def unival_subtrees(self):
        """
        Accumulates number of unival subtrees recursively

        Returns whether or not self is unival and the amount of subtrees in a tuple
        """

        if self._left and self._left.val != self.val:
            _, left_subtrees = self._left.unival_subtrees()
            _, right_subtrees = self._right.unival_subtrees() if self._right else (True, 0)
            return (False, left_subtrees + right_subtrees)
        
        elif self._right and self._right.val != self.val:
            _, left_subtrees = self._left.unival_subtrees() if self._left else (True, 0)
            _, right_subtrees = self._right.unival_subtrees()
            return (False, left_subtrees + right_subtrees)
        
        else:
            left_unival, left_subtrees = self._left.unival_subtrees() if self._left else (True, 0)
            right_unival, right_subtrees = self._right.unival_subtrees() if self._right else (True, 0)
            unival = left_unival and right_unival
            return (unival, (1 if unival else 0) + left_subtrees + right_subtrees)
    
    def num_unival_subtrees(self):
        """
        Uses self.unival_subtrees() to return just the amount of unival subtrees under self
        """

        _, num_subtrees = self.unival_subtrees()
        return num_subtrees

root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
assert root.num_unival_subtrees() is 5