import functools
import itertools


def flat_list(arr):
    send_back = []
    for i in arr:
        if type(i) == list:
            send_back += flat_list(i)
        else:
            send_back.append(i)
    return send_back


def insert_plus(seq, a):
    operators = ['+', '-', '*', '/']
    if type(seq) == str:
        seq = [seq]

    if a not in operators and seq[-1] not in operators:
        seq.append('+')

    seq.append(a)

    return seq


def calc(expression):
    stack = []
    current_index = 0
    while True:
        if not expression.count('('):
            break

        if not current_index:
            current_index = expression.index('(')

        for i, c in enumerate(expression[current_index+1:]):
            if c == '(':
                current_index += i+1
                break

            if c == ')':
                stack.append(
                    expression[current_index+1: current_index + i + 1])
                expression = expression[:current_index] + \
                    f'${len(stack)-1}$' + expression[current_index + i+2:]
                current_index = 0
                break

    for i, s in enumerate(stack):
        if not s.count('$'):
            stack[i] = solve_expression(split_expression(clear_expression(s)))
        else:
            insert_index = s.index('$') + 1
            insert_value = str(stack[int(s[insert_index])])
            single_expression = s[:insert_index-1] + \
                insert_value + s[insert_index+2:]
            stack[i] = solve_expression(split_expression(
                clear_expression(single_expression)))

    for i, s in enumerate(stack):
        if str(s).count('e'):
            stack[i] = '%.20f' % s
            continue

        if type(s) == str:
            stack[i] = solve_expression(split_expression(clear_expression(s)))

    while expression.count('$'):
        insert_index = expression.index('$') + 1
        insert_value = str(stack[int(expression[insert_index])])
        expression = expression[:insert_index-1] + \
            insert_value + expression[insert_index+2:]

    return solve_expression(split_expression(clear_expression(expression)))


def clear_expression(exp):
    exp = exp.replace(' ', '')
    exp = exp.replace('(', '')
    exp = exp.replace(')', '')
    exp = exp.replace('e', '')
    exp = exp.replace('---', '-')
    exp = exp.replace('*--', '*')
    exp = exp.replace('/--', '/')
    exp = exp.replace('+--', '+')
    exp = exp.replace('-+', '-')
    exp = exp.replace('+-', '-')
    exp = exp.replace(' ', '')
    exp = exp.replace('/', ' / ')
    exp = exp.replace('+', ' + ')
    exp = exp.replace('*', ' * ')
    exp = exp.split(' ')
    return exp


def split_expression(exp):
    for i, e in enumerate(exp):
        if e.count('-'):
            e = e.replace('-', ' -')
        exp[i] = [ee for ee in e.split(' ') if ee]

    exp = functools.reduce(insert_plus, flat_list(exp))

    return [exp] if type(exp) == str else exp


def handle_modulo(exp): 
    if type(exp) == str and  exp.count('%'):
        index = exp.index('%')
        return float(exp[:index]) % float(exp[index+1:])

    return float(exp)


def solve_expression(exp):
    if exp[0] == '-':
        exp.insert(0, 0)

    while len(exp) > 1:
        for i, e in enumerate(exp):
            if e == '*':
                exp[i-1] = handle_modulo(exp.pop(i-1)) * handle_modulo(exp.pop(i))
            elif e == '/':
                exp[i-1] = handle_modulo(exp.pop(i-1)) / handle_modulo(exp.pop(i))

            elif not exp.count('*') and not exp.count('/'):
                if e == '+':
                    exp[i-1] = handle_modulo(exp.pop(i-1)) + handle_modulo(exp.pop(i))
                elif e == '-':
                    exp[i-1] = handle_modulo(exp.pop(i-1)) - handle_modulo(exp.pop(i))
                else:
                    continue
            else:
                continue
            break

    return handle_modulo(str(exp[0]))


def tokenize(expression):
    if expression.count('%'):
        pass

    return solve_expression(expression)


class Interpreter:
    def __init__(self):
        self.vars = {}
        self.functions = {}

    def is_just_expression(self, exp):
        for e in exp:
            if e == '=':
                return False

            if e.isalpha():
                return False

        return True

    def input(self, expression):
        if not expression.replace(' ',''):
            return ''

        # if self.is_just_expression(expression):
        #     return int(calc(expression))

        splited = expression.split(' ')

        for i in range(len(splited)-1):
            operators = ['*', '/', '+', '-', '%', '=', '(', ')']
            prev = splited[i]
            curr = splited[i+1]

            if prev in operators and curr in operators:
                raise ValueError()

            if prev.isnumeric() and curr.isnumeric():
                raise ValueError()
        
            if prev.isalpha() and curr.isalpha():
                raise ValueError()

        if expression.count('='):
            index = splited.index('=')

            for i, s in enumerate(splited[index:]):
                if s.isalpha():
                    if s in self.vars:
                        splited[i + index] = self.vars[s]
                    else:
                        raise ValueError()

            var_name = splited[index - 1]
            var_value = ''.join([str(s) for s in splited[index+1:]])

            self.vars[var_name] = int(calc(var_value))

            return self.vars[var_name]

        for i, s in enumerate(splited):
            if s.isalpha():
                if s in self.vars:
                    splited[i] = self.vars[s]
                else:
                    raise ValueError()

        return int(calc(''.join([str(s) for s in splited])))


i = Interpreter()

print(i.input("7 % 4"))
