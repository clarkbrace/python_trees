from BinaryTreeNode import BinaryTree
from LinkedList import *

# print("begin")
# bt = BinaryTree([1, 1, 3, 4, 3])
# print(bt)
# bt.insert(88)
# print(50 in bt)
# print(88 in bt)
# print(bt)

print('begin')

ll = create_linked_list([1,2,3,4])
print_linked_list(ll)
# rll = reverse_linked_list(ll) TODO: Currently breaks links of original
# print_linked_list(rll)


rllr = recursive_reverse(ll)
print(rllr)
print('end')

