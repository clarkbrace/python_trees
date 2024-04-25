

class LinkedListNode:

    def __init__(self, value: int = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return f'LLNode({self.value}) -> ({self.next})'


def print_linked_list(head: LinkedListNode = None):

    new_head = head
    if new_head == None:
        print('(None)')
        return

    print(f' ({head.value})\n  |\n  v')
    return print_linked_list(new_head.next)

def create_linked_list(values: [int]):

    head = None
    tail = None

    for value in values:
        if head == None:
            head = LinkedListNode(value)
            tail = head
        else:
            tail.next = LinkedListNode(value)
            tail = tail.next

    return head


def reverse_linked_list(head):

    itr_head = head
    new_head = None

    while itr_head != None:
        next_node = itr_head.next
        old_head = new_head
        new_head = itr_head
        new_head.next = old_head
        itr_head = next_node


    return new_head


def recursive_reverse(head):

    if head == None:
        return None

    head.next = recursive_reverse(head.next)
    return head

