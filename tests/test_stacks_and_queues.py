from data_structures_and_algorithms.stacks_and_queues import (
    Linter,
    PrintManager,
    Queue,
    Stack,
    reverse,
)


def test_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    for i in range(3, 0, -1):
        assert stack.read() == i
        assert stack.pop() == i


def test_reverse():
    text = "abcde"
    actual = reverse(text)
    expected = "edcba"
    assert actual == expected


def test_linter_when_correct_braces():
    linter = Linter()
    text = "( var x = { y: [1, 2, 3] } )"
    actual = linter.lint(text)
    expected = "Success: no issues found"
    assert actual == expected


def test_linter_when_missing_opening_brace():
    linter = Linter()
    text = "var x = { y: [1, 2, 3] } )"
    actual = linter.lint(text)
    expected = ") does not have opening brace"
    assert actual == expected


def test_linter_when_missing_closing_brace():
    linter = Linter()
    text = "( var x = { y: [1, 2, 3] }"
    actual = linter.lint(text)
    expected = "( does not have closing brace"
    assert actual == expected


def test_linter_when_mismatched_opening_brace():
    linter = Linter()
    text = "[ var x = { y: [1, 2, 3] } )"
    actual = linter.lint(text)
    expected = ") has mismatched opening brace"
    assert actual == expected

    linter = Linter()
    text = "( var x = { y: [1, 2, 3] }"
    actual = linter.lint(text)
    expected = "( does not have closing brace"
    assert actual == expected


def test_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    for i in range(1, 4):
        assert queue.read() == i
        assert queue.dequeue() == i


def test_print_manager(capfd):
    print_manager = PrintManager()
    print_manager.queue_print_job("First document")
    print_manager.queue_print_job("Second document")
    print_manager.queue_print_job("Third document")

    print_manager.run()
    out, _ = capfd.readouterr()
    assert out == "First document\nSecond document\nThird document\n"
