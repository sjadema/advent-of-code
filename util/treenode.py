from typing import List, Optional


class TreeNode:

    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight
        self.parent = None
        self.children = {}

    def get_name(self) -> str:
        return self.name

    def get_weight(self, total: bool = False, include_self: bool = True) -> int:
        if not total:
            return self.weight

        weight = 0
        if include_self:
            weight = self.weight

        for child in self.get_children():
            weight += child.get_weight(total, include_self)

        return weight

    def add_child(self, child: 'TreeNode') -> None:
        self.children[child.get_name()] = child
        child.set_parent(self)

    def add_children(self, children: List['TreeNode']) -> None:
        for child in children:
            self.add_child(child)

    def get_child(self, name: str):
        return self.children[name]

    def get_children(self) -> List['TreeNode']:
        return list(self.children.values())

    def set_parent(self, parent: 'TreeNode') -> None:
        self.parent = parent

    def get_parent(self) -> Optional['TreeNode']:
        return self.parent

    def __str__(self):
        return '{name} ({weight})'.format(name=self.name, weight=self.weight)
