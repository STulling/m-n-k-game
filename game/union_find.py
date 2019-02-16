

class UnionFind:
    parent = None
    rank = None

    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

    def union(self, other):
        self.find().rank = self.find().rank + other.find().rank
        other.find().parent = self.find()

    def find(self):
        if self.parent is None:
            return self
        self.parent = self.parent.find()
        return self.parent

    def __str__(self):
        return str(self.find().rank)

    def __repr__(self):
        return str(self)
