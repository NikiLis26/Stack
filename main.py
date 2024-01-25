# Необходимо реализовать класс Stack со следующими методами:
# isEmpty - проверка стека на пустоту. Метод возвращает True или False.
# push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
# pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
# peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
# size - возвращает количество элементов в стеке.


class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) > 0:
            return True
        else:
            return False

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return None
        result = self.stack.pop()
        return result

    def peek(self):
        result = self.stack[-1]
        return result

    def size(self):
        return len(self.stack)

    def is_balanced(str_input):
        stack = []
        brackets = {'(': ')', '[': ']', '{': '}'}

        for char in str_input:
            if char in brackets.keys():
                stack.append(char)
            elif char in brackets.values():
                if not stack or brackets[stack.pop()] != char:
                    return False

        return not stack

    print(is_balanced("((([{}])))"))