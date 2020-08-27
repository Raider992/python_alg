"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""


class BinaryTreeError(Exception):
    """
    Exception raised if the newly added nod or leaf
    disrupts the structure of the binary tree
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


'''
Лучшее что у меня получилось на тему добавления кастомного исключения.
Я не знаю, как можно добавить проверку узлов внутрь класса(и можно ли), как мне 
изначально хотелось. С моей точки зрения, это всё будет очень сильно привязано к 
архитектуре, которую создаст разработчик на каждой конкретной реализации класса 
для работы с бинарными деревьями, то есть, создать универсальную проверку 
на исключение, которая бы работала для любых бинарных деревьев, невозможно.
Поправьте пожалуйста, если ошибаюсь.
'''




class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        # Проверяем, будущего левого потомка, если он не меньше или равен
        # корневому узлу - вызываем исключение, останавливаем работу метода
        # и сообщаем об ошибке.

        if not new_node <= self.get_root_val():
            raise BinaryTreeError('Incorrect node value insertion')

        try:
            isinstance(new_node, int)
        except TypeError('Введён узел неверного типа'):
            print('Тип должен быть целочисленным')

        # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # Проверяем, будущего правого потомка, если он не больше
        # корневого узла - вызываем исключение, останавливаем работу метода
        # и сообщаем об ошибке.

        if not new_node > self.get_root_val():
            raise BinaryTreeError('Incorrect node value insertion')

        try:
            isinstance(new_node, int)
        except TypeError('Введён узел неверного типа'):
            print('Тип должен быть целочисленным')


        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

# Добавил метод получения всех узлов дерева

    def get_tree_nodes(self):
        nodes = []
        if self.root != None:
            nodes.append(self.get_root_val())
        if self.left_child != None:
            nodes.append(self.left_child.get_root_val())
            self.left_child.get_tree_nodes()
        if self.right_child != None:
            nodes.append(self.right_child.get_root_val())
            self.right_child.get_tree_nodes()
        return nodes



r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(4)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
print(r.get_tree_nodes())

'''
Пожалуй, кроме валидации и обхода для тренировочного дерева особенно ничего и не придумаю.
В принципе, всё понятно, если возникнут какие-то комментарии или где-то ошибся, 
всегда готов поправить/принять к сведению =)
'''
