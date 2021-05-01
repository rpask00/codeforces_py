import functools


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
    if type(exp) == str and exp.count('%'):
        index = exp.index('%')
        return float(exp[:index]) % float(exp[index+1:])

    return float(exp)


def solve_expression(exp):
    if exp[0] == '-':
        exp.insert(0, 0)

    while len(exp) > 1:
        for i, e in enumerate(exp):
            if e == '*':
                exp[i-1] = handle_modulo(exp.pop(i-1)) * \
                    handle_modulo(exp.pop(i))
            elif e == '/':
                exp[i-1] = handle_modulo(exp.pop(i-1)) / \
                    handle_modulo(exp.pop(i))

            elif not exp.count('*') and not exp.count('/'):
                if e == '+':
                    exp[i-1] = handle_modulo(exp.pop(i-1)) + \
                        handle_modulo(exp.pop(i))
                elif e == '-':
                    exp[i-1] = handle_modulo(exp.pop(i-1)) - \
                        handle_modulo(exp.pop(i))
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

    def _to_string_array(self, arr):
        return [str(a) for a in arr]

    def _validate_expression(self, exp):
        splited = exp.split(' ')
        for i in range(len(splited)-1):
            operators = ['*', '/', '+', '-', '%', '=', '(', ')']
            prev = splited[i]
            curr = splited[i+1]

            if prev in operators and curr in operators:
                return False

            if prev.isnumeric() and curr.isnumeric():
                return False

            if prev.isalpha() and curr.isalpha():
                return False

        return True

    def _valid_argument_list(self, rest):
        call_stack = []
        rest = rest.copy()

        for i, r in enumerate(rest):
            if r in self.functions:
                call_stack.insert(0, r)
            else:
                rest[i] = '0'

        expression = ' '.join(rest)
        while call_stack:
            current_call = call_stack.pop()
            required_args = len(self.functions[current_call]['args'])
            current_call = ['0 ' for i in range(
                required_args)] + [current_call]
            current_call = ''.join(current_call)

            if expression.count(current_call) == 0:
                return True

            expression = expression.replace(current_call, '0', 1)

        if len(expression) > 1:
            return True

    def _get_vars_form_expression(self, exp):
        exp = exp.replace('(', '')
        exp = exp.replace(')', '')

        exp = exp.split(' ')

        return [e for e in exp if e.isalpha()]


    def define_function(self, exp):
        exp = exp.split(' ')
        index = exp.index('=>')
        name = exp[1]
        args_names = exp[2:index]

        if len(set(args_names)) != len(args_names):
            return False

        if name in self.vars:
            return False

        expression = " ".join(exp[index+1:])
        for var in self._get_vars_form_expression(expression):
            if var not in args_names:
                return False

        for exp in expression.split(' '):
            if exp.isalpha():
                if exp not in self.vars and exp not in args_names:
                    return False

        self.functions[name] = {
            'args': args_names,
            'expression': expression
        }

        return True

    def call_function(self, name, args):
        expression = self.functions[name]['expression']
        arguments = self.functions[name]['args']
        for i, arg in enumerate(args):
            expression = expression.replace(arguments[i], str(arg))

        return self.input(expression)

    def input(self, expression):
        if not expression.replace(' ', ''):
            return ''

        splited = expression.split(' ')

        if expression.count('fn'):
            if expression.index('fn') is not 0:
                raise ValueError()

            if self.define_function(expression):
                return ''

            raise ValueError()

        if expression.count(' = '):
            expression = expression.replace('(', '')
            expression = expression.replace(')', '')
            assigments = reversed(expression.split(' = '))

            def asign(right, left):
                var_name = left[-1]
                left = left[:-1]
                if var_name in self.functions:
                    raise ValueError()

                right_expression = str(right).split(' ')
                for i, s in enumerate(right_expression):
                    if s.isalpha():
                        if s in self.vars:
                            right_expression[i] = str(self.vars[s])
                        else:
                            raise ValueError()

                var_value = int(calc(''.join(right_expression)))

                self.vars[var_name] = var_value
                return self.input(left + str(var_value))

            return functools.reduce(asign, assigments)

        reversed_splited = list(reversed(splited))

        while True:
            prev_len = len(reversed_splited)
            for i, s in enumerate(reversed_splited):
                if str(s).isalpha():
                    if s in self.vars:
                        reversed_splited[i] = self.vars[s]
                    elif s in self.functions:
                        args_number = len(self.functions[s]['args'])
                        func = list(reversed(reversed_splited[:i+1]))
                        args_list = func[1:args_number + 1]

                        if self._valid_argument_list(reversed_splited):
                            raise ValueError()

                        resolved_func = self.call_function(func[0], args_list)

                        header = i-args_number
                        reversed_splited = reversed_splited[:header] + [
                            resolved_func] + reversed_splited[args_number+header+1:]

                        break
                    else:
                        raise ValueError()

            if prev_len == len(reversed_splited):
                break

        splited = list(reversed(reversed_splited))
        if self._validate_expression(' '.join(self._to_string_array(splited))):
            return int(calc(''.join(self._to_string_array(splited))))
        else:
            raise ValueError()


i = Interpreter()

print(i.input('fn avg x y => (x + y) / 2'))
print(i.input('fn echo x => x'))
print(i.input('avg echo 4 echo 2'))
