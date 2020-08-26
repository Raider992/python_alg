"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""

# Я решил сделать реализацию алгоритма с помощью модуля Heapq
# Этот модуль предоставляет возможность создать min-кучу, бинарное дерево, в котором каждый k элемент не
# больше каждого 2k+1 элемента и каждый k элемент не больше каждого 2k+2 элемента. Это условие работает для всех k,
# начиная с 0.

# Ссылка на код модуля на гитхабе: "https://github.com/python/cpython/bleftb/master/Lib/heapq.py"

'''
Общий алгоритм:
1. Создаём листовой узел для каждого символа и добавляем их в очередь с приоритетами(в нашем случае, min-кучу)
2. Пока в очереди больше одного элемента:
    1) Дважды достаём узел в наибольшим приоритетом(то есть, наименьшей частотой). Получаем два узла.
    2) Создаём новый внутренний узел с этими двумя узлами в качестве потомков и частотой равной сумме их частот.
    3) Добавляем новый узел в очередь
3. Оставшийся узел - корень, дерево завершено.
'''

from heapq import heapify, heappop, heappush
from collections import defaultdict

def huffman_encode(defdict):
    heap = [[w, [ch, '']] for ch, w in defdict.items()]  #
    heapify(heap)

    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        for i in left[1:]:
            i[1] = '0' + i[1]
        for i in right[1:]:
            i[1] = '1' + i[1]
        heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

orig_str = 'example string for Huffman encoding'

defdict = defaultdict(int)

for ch in orig_str:
    defdict[ch] += 1

huff_code = huffman_encode(defdict)

d = dict(huff_code)
print(d)

huff_dict = dict(huff_code)
encoded_str = ''
for ch in orig_str:
    encoded_str += huff_dict[ch]

print(f'Original: {orig_str}')
print(f'Encoded: {encoded_str}')

print('\tCharacter\tWeight\tHuffman_code')
for p in huff_code:
    print('\t%s\t%s\t%s' % (p[0], defdict[p[0]], p[1]))