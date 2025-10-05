from src.linked_list import LinkedList


def merge_linked_lists(first: "LinkedList", second: "LinkedList") -> "LinkedList":
    merged_linked_list = LinkedList()

    first_pointer = first.head
    second_pointer = second.head
    while (first_pointer and second_pointer):
        if (first_pointer.value <= second_pointer.value):
            merged_linked_list.append(first_pointer.value)
            first_pointer = first_pointer.next
        else:
            merged_linked_list.append(second_pointer.value)
            second_pointer = second_pointer.next

    while(first_pointer):
        merged_linked_list.append(first_pointer.value)
        first_pointer = first_pointer.next

    while(second_pointer):
        merged_linked_list.append(second_pointer.value)
        second_pointer = second_pointer.next

    return merged_linked_list