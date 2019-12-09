from __future__ import annotations

from typing import Optional, List


class Node:
    def __init__(self, value: str):
        self.value = value
        self.__parent = None
        self.__children = []

    def set_parent(self, parent: Optional[Node]) -> None:
        if self.__parent != parent:
            self.__parent = parent
            parent.add_child(self)

    def get_parent(self) -> Optional[Node]:
        return self.__parent

    def get_ancestors(self) -> List[Node]:
        parent = self.get_parent()
        while parent:
            node = parent
            parent = parent.get_parent()

            yield node

    def add_child(self, child: Node):
        if child not in self.__children:
            child.set_parent(self)
            self.__children.append(child)

    def get_children(self) -> List[Node]:
        return self.__children

    def is_root(self) -> bool:
        return None is self.get_parent()

    def is_leaf(self) -> bool:
        return [] == self.get_children()

    def depth(self) -> int:
        return sum(1 for _ in self.get_ancestors())

    def __repr__(self):
        return '{}. Children: {}.'.format(self.value, self.get_children())
