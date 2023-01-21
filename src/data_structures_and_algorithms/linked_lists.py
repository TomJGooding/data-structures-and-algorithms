from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    data: Any
    next_node: Optional[Node] = None
    prev_node: Optional[Node] = None


class LinkedList:
    def __init__(self, first_node: Optional[Node] = None) -> None:
        self.first_node: Node | None = first_node

    def read(self, index: int) -> Any:
        if not self.first_node:
            return None

        current_node: Node = self.first_node
        current_index: int = 0

        while current_index < index:
            if not current_node.next_node:
                return None
            else:
                current_node = current_node.next_node
                current_index += 1

        return current_node.data

    def index_of(self, value: Any) -> Any:
        if not self.first_node:
            return None

        current_node: Node = self.first_node
        current_index: int = 0

        while True:
            if current_node.data == value:
                return current_index
            elif not current_node.next_node:
                return None
            else:
                current_node = current_node.next_node
                current_index += 1

    def insert_at_index(self, index: int, value: Any) -> None:
        new_node: Node = Node(value)

        if index == 0 or not self.first_node:
            new_node.next_node = self.first_node
            self.first_node = new_node
            return

        current_node: Node = self.first_node
        current_index: int = 0

        while current_index < index - 1:
            if not current_node.next_node:
                break
            current_node = current_node.next_node
            current_index += 1

        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def delete_at_index(self, index: int) -> None:
        if not self.first_node:
            return

        if index == 0:
            self.first_node = self.first_node.next_node
            return

        current_node: Node = self.first_node
        current_index: int = 0

        while current_index < index - 1:
            if not current_node.next_node:
                break
            current_node = current_node.next_node
            current_index += 1

        if not current_node.next_node:
            return

        node_after_deleted_node: Node | None = current_node.next_node.next_node
        current_node.next_node = node_after_deleted_node

    def print(self) -> None:
        current_node: Node | None = self.first_node
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node

    def last(self) -> Any:
        if not self.first_node:
            return

        current_node: Node = self.first_node
        while current_node:
            if current_node.next_node:
                current_node = current_node.next_node
            else:
                break

        return current_node.data

    def reverse(self) -> None:
        current_node: Node | None = self.first_node
        previous_node: Node | None = None

        while current_node:
            next_node: Node | None = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node

        self.first_node = previous_node


class DoublyLinkedList:
    def __init__(
        self,
        first_node: Optional[Node] = None,
        last_node: Optional[Node] = None,
    ) -> None:
        self.first_node: Node | None = first_node
        self.last_node: Node | None = last_node

    def insert_at_end(self, value: Any) -> None:
        new_node: Node = Node(value)

        if not self.first_node or not self.last_node:
            self.first_node = new_node
            self.last_node = new_node
            return

        new_node.prev_node = self.last_node
        self.last_node.next_node = new_node
        self.last_node = new_node

    def remove_from_front(self) -> Node | None:
        if not self.first_node:
            return None

        removed_node: Node = self.first_node
        self.first_node = self.first_node.next_node

        return removed_node

    def print_in_reverse(self) -> None:
        current_node: Node | None = self.last_node
        while current_node:
            print(current_node.data)
            current_node = current_node.prev_node


class Queue:
    def __init__(self) -> None:
        self.data = DoublyLinkedList()

    def enqueue(self, value: Any) -> None:
        self.data.insert_at_end(value)

    def dequeue(self) -> Any:
        removed_node: Node | None = self.data.remove_from_front()
        if not removed_node:
            return None
        else:
            return removed_node.data

    def read(self) -> Any:
        if not self.data.first_node:
            return None
        else:
            return self.data.first_node.data
