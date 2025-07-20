from linked_list import LinkedList

if __name__ == "__main__":
    # 1) Create a LinkedList instance
    ll = LinkedList()

    # 2) Insert sample data
    ll.insert_at_front(10)
    ll.insert_at_front(20)
    ll.insert_at_end(5)
    # List now: 20 -> 10 -> 5

    # 3) Display the list
    print("Initial list:")
    ll.display()

    # 4) Compute and print sum of all IDs
    total = ll.recursive_sum()
    print(f"Recursive sum of list IDs: {total}")

    # 5) Search for specific IDs
    for target in (10, 999):
        found = ll.recursive_search(target)
        print(f"Search {target}: {found}")

    # 6) Reverse the list in-place, then display
    ll.recursive_reverse()
    print("List after recursive reverse:")
    ll.display()