import pytest

from data_structures_and_algorithms.linked_lists import (
    DoublyLinkedList,
    LinkedList,
    Node,
    Queue,
)


@pytest.fixture
def linked_list():
    node_1 = Node("once")
    node_2 = Node("upon")
    node_3 = Node("a")
    node_4 = Node("time")

    node_1.next_node = node_2
    node_2.next_node = node_3
    node_3.next_node = node_4

    linked_list = LinkedList(first_node=node_1)

    return linked_list


def test_linked_list_first_node(linked_list):
    assert linked_list.first_node.data == "once"


def test_linked_list_read_index_in_range(linked_list):
    assert linked_list.read(0) == "once"
    assert linked_list.read(1) == "upon"
    assert linked_list.read(2) == "a"
    assert linked_list.read(3) == "time"


def test_linked_list_read_index_out_of_range(linked_list):
    assert linked_list.read(4) is None


def test_linked_list_index_of_existing_value(linked_list):
    assert linked_list.index_of("time") == 3


def test_linked_list_index_of_nonexisting_value(linked_list):
    assert linked_list.index_of("not in list") is None


def test_linked_list_insert_at_start(linked_list):
    linked_list.insert_at_index(0, "start")
    assert linked_list.read(0) == "start"
    assert linked_list.read(1) == "once"
    assert linked_list.read(2) == "upon"
    assert linked_list.read(3) == "a"
    assert linked_list.read(4) == "time"
    assert linked_list.read(5) is None


def test_linked_list_insert_at_end(linked_list):
    linked_list.insert_at_index(4, "end")
    assert linked_list.read(0) == "once"
    assert linked_list.read(1) == "upon"
    assert linked_list.read(2) == "a"
    assert linked_list.read(3) == "time"
    assert linked_list.read(4) == "end"
    assert linked_list.read(5) is None


def test_linked_list_insert_in_middle(linked_list):
    linked_list.insert_at_index(2, "middle")
    assert linked_list.read(0) == "once"
    assert linked_list.read(1) == "upon"
    assert linked_list.read(2) == "middle"
    assert linked_list.read(3) == "a"
    assert linked_list.read(4) == "time"
    assert linked_list.read(5) is None


def test_linked_list_delete_first(linked_list):
    linked_list.delete_at_index(0)
    assert linked_list.read(0) == "upon"
    assert linked_list.read(1) == "a"
    assert linked_list.read(2) == "time"
    assert linked_list.read(3) is None


def test_linked_list_delete_last(linked_list):
    linked_list.delete_at_index(3)
    assert linked_list.read(0) == "once"
    assert linked_list.read(1) == "upon"
    assert linked_list.read(2) == "a"
    assert linked_list.read(3) is None


def test_linked_list_delete_in_middle(linked_list):
    linked_list.delete_at_index(2)
    assert linked_list.read(0) == "once"
    assert linked_list.read(1) == "upon"
    assert linked_list.read(2) == "time"
    assert linked_list.read(3) is None


def test_linked_list_print(linked_list, capfd):
    linked_list.print()
    out, _ = capfd.readouterr()
    assert out == "once\nupon\na\ntime\n"


def test_linked_list_last(linked_list):
    assert linked_list.last() == "time"


def test_linked_list_reverse(linked_list, capfd):
    linked_list.reverse()
    linked_list.print()
    out, _ = capfd.readouterr()
    assert out == "time\na\nupon\nonce\n"


def test_doubly_linked_list_first_in_first_out():
    linked_list = DoublyLinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    assert linked_list.remove_from_front().data == 1  # pyright: ignore
    assert linked_list.remove_from_front().data == 2  # pyright: ignore
    assert linked_list.remove_from_front().data == 3  # pyright: ignore


def test_doublylinked_list_print_in_reverse(capfd):
    linked_list = DoublyLinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    linked_list.print_in_reverse()
    out, _ = capfd.readouterr()
    assert out == "3\n2\n1\n"


def test_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.read() == 1
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
