# implement stack to hold value and recursion
def calculator(str):

    str = str.replace(' ', '')

    if str == '':
        return ''  # return an empty string when no input

    try:
        # dictionrary of stack's operation based on a arithmetic operartions
        oper_dict = {   '+' : lambda stack, v: stack.append(v),
                        '-' : lambda stack, v: stack.append(-v),
                        '*' : lambda stack, v: stack.append(stack.pop()*v),
                        '**' : lambda stack, v: stack.append(stack.pop()**v),
                        '/' : lambda stack, v: stack.append(float(stack.pop()/v)),
                        '//' : lambda stack, v: stack.append(stack.pop()//v),
                    } 


        idx, num, stack, sign = 0, 0, [], '+'

        while idx < len(str):
            if str[idx].isdigit():
                num = num * 10 + int(str[idx])  # get the digit when its a number
            elif str[idx] in ['+', '-']:
                oper_dict[sign](stack, num)
                num = 0
                sign = str[idx]
            elif str[idx] in ['/', '*']:
                idx_temp = idx + 1
                if str[idx_temp] in [ '*', '/']:
                    oper_dict[sign](stack, num)
                    num = 0
                    sign = 2*str[idx]
                    idx += 1
                else:
                    oper_dict[sign](stack, num)
                    num = 0
                    sign = str[idx]
            elif str[idx] == '(':
                num, offset = calculator(str[(idx+1):])
                idx = idx + offset + 1
            elif str[idx] == ')':
                oper_dict[sign](stack, num)
                return sum(stack), idx
            else:
                raise Exception("non arithmetic input")
            idx += 1

        oper_dict[sign](stack, num)
        return float(sum(stack))
    except Exception as e:
        return f'Errors "{e}" has occurred. '



