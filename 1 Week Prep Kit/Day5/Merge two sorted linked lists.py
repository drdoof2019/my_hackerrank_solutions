class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeLists(head1, head2):
    resulting_list = []
    while head1 != None:
        resulting_list.append(head1.data)
        head1 = head1.next
    while head2 != None:
        resulting_list.append(head2.data)
        head2 = head2.next
    resulting_list.sort()

    # create a new linked list
    result = Node(-1)
    current_node = result

    for i in range(len(resulting_list)):
        new_node = Node(resulting_list[i])
        current_node.next = new_node
        current_node = new_node

    # return the head of the new linked list
    return result.next
