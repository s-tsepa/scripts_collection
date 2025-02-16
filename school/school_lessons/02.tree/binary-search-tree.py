import random

class Node:
    def __init__(self, key, value, l=None, r=None):
        self.key = key
        self.value = value
        self.l = l
        self.r = r

    def find(self, key):
        if self.key == key:
            return self

        if key < self.key and self.l:
            return self.l.find(key)
        elif key > self.key and self.r:
            return self.r.find(key)

    def find_ge(self, key):
        # import pdb; pdb.set_trace()
        if self.key == key:
            return self

        if not self.l and self.key > key:
            return self

        l_res, r_res = None, None

        if self.r and key > self.key:
            r_res = self.r.find_ge(key)

        if self.l and key < self.key:
            l_res = self.l.find_ge(key)


        if l_res or r_res:
            if l_res and r_res:

                if l_res.key <= r_res:
                    return l_res
                else:
                    return r_res
            elif l_res:
                return l_res
            elif r_res:
                return r_res

        else:
            if self.key >= key:
                return self

    

    def __str__(self):
        return f'{self.key} -> {self.l.key if self.l else None}, {self.r.key if self.r else None}'

    def __repr__(self):
        return f'{self.key} -> {self.l.key if self.l else None}, {self.r.key if self.r else None}'

rand_value = lambda : random.randint(50, 100)

def gen_tree():
    n8 = Node(8, rand_value())
    n7 = Node(7, rand_value(), None, n8)
    n5 = Node(5, rand_value(), n8, None)
    n6 = Node(6, rand_value(), n5, n7)
    n3 = Node(3, rand_value())
    n1 = Node(1, rand_value())
    n2 = Node(2, rand_value(), n1, n3)
    n4 = Node(4, rand_value(), n2, n6)

    return n4

root = gen_tree()
# print(root)

# print(root.get_all_children())
# print(root.find(6))
print(root.find_ge(6.5))
