
OPERATORS = ['+', '-', '*', '/', '(', ')']
OPERATOR_PRIOTIRY = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': 0
}

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

OPERATOR_FUNCTIONS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

def isOperator(ch):
    global OPERATORS
    if (ch in OPERATORS):
        return True

def getValue(numStr):
    if '.' in numStr:
        return float(numStr)
    else:
        return int(numStr)

def getInfix(expr):
    start = 0
    end = 0
    stack = []
    for i, ch in enumerate(expr):
        if isOperator(ch):
            value = expr[start:end].strip()
            if (value):
                stack.append(getValue(value))
            stack.append(ch)
            start = end = i + 1
        else:
            end = i + 1
    print('check expr start %s end %s: %s' % (start, end, expr[start:end]))
    value = expr[start:end].strip()
    stack.append(getValue(value))
    return stack

def getPostFix(infix):
    global OPERATOR_PRIOTIRY
    stack = []
    operatorStack = []
    for item in infix:
        if isinstance(item, str):
            if item == '(':
                operatorStack.append(item)
            elif item == ')':
                foundMatch = False
                while operatorStack:
                    top = operatorStack.pop()
                    if top == '(':
                        foundMatch = True
                        break
                    else:
                        stack.append(top)
                if not foundMatch:
                    raise Exception("do not find matched '(' for ')'")
            else:
                while operatorStack:
                    top = operatorStack.pop()
                    topPriority = OPERATOR_PRIOTIRY[top]
                    itemPriority = OPERATOR_PRIOTIRY[item]
                    if itemPriority <= topPriority:
                        stack.append(top)
                    else:
                        operatorStack.append(top)
                        break
                operatorStack.append(item)
        else:
            stack.append(item)
    while operatorStack:
        stack.append(operatorStack.pop())
    return stack


def calcPostFix(postFix):
    global OPERATOR_FUNCTIONS
    stack = []
    for item in postFix:
        if isinstance(item, str):
            second = stack.pop()
            first = stack.pop()
            function = OPERATOR_FUNCTIONS[item]
            stack.append(function(first, second))
        else:
            stack.append(item)
    return stack.pop()


if __name__ == "__main__":
    infix = getInfix('1 + 2 * 3.5 * (3 + 1) * 6 + 4')
    print(infix)
    postFix = getPostFix(infix)
    print(postFix)
    value = calcPostFix(postFix)
    print(value)