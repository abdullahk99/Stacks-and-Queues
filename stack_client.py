"""
code that uses Stack
"""


from stack import Stack


def list_stack(list_, stk: "Stack"):
    """
    Add elements of list_ to Stack stk, and then print all
    the non-list elements.

    st is assumed to be empty.

    @param list list_: a Python list, possibly noted
    @param Stack stk: an empty Stack
    @rtype: None
    """
    for elements in list_:
        stk.add(elements)

    while not stk.is_empty():
        popped = stk.remove()
        if isinstance(popped, list):
            for values in popped:
                stk.add(values)
        else:
            print(popped)


if __name__ == "__main__":
    new_stack = Stack()
    new_input = input("Type a string: ")
    while new_input != 'end':
        new_stack.add(new_input)
        new_input = input('Type a string: ')
    while not new_stack.is_empty():
        print(new_stack.remove())

    list_stack([1, 3, 5], Stack())

