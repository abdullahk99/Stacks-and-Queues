"""
code that uses queue
"""

from csc148_queue import Queue


def list_queue(list_, qu: Queue):
    """
    pass
    """
    for values in list_:
        qu.add(values)

    while not qu.is_empty():
        remove_el = qu.remove()
        if isinstance(remove_el, list):
            for v in remove_el:
                qu.add(v)
        else:
            print(remove_el)


if __name__ == "__main__":
    new_queue = Queue()
    i = int(input('Enter an Integer: '))
    while not i == 148:
        new_queue.add(i)
        i = int(input('Enter an Integer: '))

    accumulate = 0
    while not new_queue.is_empty():
        accumulate += new_queue.remove()
    print(accumulate)

list_queue([1, 3, 5], Queue())
