from typing import Any


def reverse(text: str) -> str:
    stack = Stack()
    for char in text:
        stack.push(char)

    reversed_text: str = ""
    while stack.read():
        reversed_text += stack.pop()

    return reversed_text


class Linter:
    def __init__(self) -> None:
        self.stack = Stack()

    def lint(self, text: str) -> str:
        for char in text:
            if Linter.__is_opening_brace(char):
                self.stack.push(char)

            elif Linter.__is_closing_brace(char):
                popped_opening_brace: str = self.stack.pop()
                if not popped_opening_brace:
                    return f"{char} does not have opening brace"

                if Linter.__is_not_a_match(
                    opening_brace=popped_opening_brace, closing_brace=char
                ):
                    return f"{char} has mismatched opening brace"

        if self.stack.read():
            return f"{self.stack.read()} does not have closing brace"

        return "Success: no issues found"

    @staticmethod
    def __is_opening_brace(char: str) -> bool:
        return char in ("(", "[", "{")

    @staticmethod
    def __is_closing_brace(char: str) -> bool:
        return char in (")", "]", "}")

    @staticmethod
    def __is_not_a_match(opening_brace: str, closing_brace: str) -> bool:
        brace_pairs: dict = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        return closing_brace != brace_pairs.get(opening_brace)


class Stack:
    def __init__(self) -> None:
        self.data: list = []

    def push(self, element) -> None:
        self.data.append(element)

    def pop(self) -> Any:
        return None if not self.data else self.data.pop()

    def read(self) -> Any:
        return None if not self.data else self.data[-1]


class PrintManager:
    def __init__(self) -> None:
        self.queue = Queue()

    def queue_print_job(self, document: str) -> None:
        self.queue.enqueue(document)

    def run(self) -> None:
        while self.queue.read():
            PrintManager.__print(self.queue.dequeue())

    @staticmethod
    def __print(document: str) -> None:
        print(document)


class Queue:
    def __init__(self) -> None:
        self.data: list = []

    def enqueue(self, element) -> None:
        self.data.append(element)

    def dequeue(self) -> Any:
        return None if not self.data else self.data.pop(0)

    def read(self) -> Any:
        return None if not self.data else self.data[0]
