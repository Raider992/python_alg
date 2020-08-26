"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median

Второй вариант задачи, массив отсортирую с помощью бинарного дерева
Сложность сортировки деревом O(log n)
"""

from random import randint
from statistics import median


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, node):
        if self.key > node.key:
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        elif self.key <= node.key:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)

    def in_order(self, lst):
        if self.left is not None:
            self.left.in_order(lst)
        print(self.key, end=' ')
        lst.append(self.key)
        if self.right is not None:
            self.right.in_order(lst)


class BSTree:
    def __init__(self):
        self.root = None
        self.node_keys_list = []

    def in_order(self):
        if self.root is not None:
            self.root.in_order(self.node_keys_list)

    def add(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(new_node)





m = int(input('Введите m: '))
any_list = [randint(0,100) for i in range(2*m + 1)]
print(any_list)


def bstree_median(lst):
    bstree = BSTree()
    
    for i in lst:
        bstree.add(i)

    bstree.in_order()

    print(f'Sorted list: {bstree.node_keys_list}')

    return bstree.node_keys_list[m]

print(f'Найденная методом медиана: \n {bstree_median(any_list)}')
print(f'Медиана, найденная встроенной функцией: \n {median(any_list)}')
