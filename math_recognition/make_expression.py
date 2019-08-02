from operator import attrgetter
from math_recognition import predict_expression
expression = ""
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operands = ['+', '-']
variables = ['x']


def prepare_from_path(img_path):
    elements = predict_expression.predict_expression(img_path)
    new_el = elements[:]
    new_ex = prepare_expression(elements)
    new1_ex = new_ex
    count_added = 0
    for i in range(1,len(new_ex)):
        if(new_ex[i] in variables):
            if(new_ex[i-1] in digits):
                part1 = new1_ex[0:i+count_added] + "*"
                new1_ex = part1 + new1_ex[i+count_added:]
                count_added += 1
    new_ex = new1_ex
    print(new1_ex)
    elements.clear()
    global expression
    expression = ""
    return new_el, new_ex



def prepare_expression(elements):
    sum_widths = 0
    # start with first leftmost, topmost element, check if it is part of an expression(fraction)
    first = get_first_element(elements)
    if first:
        #first.image.show()
        global expression
        line = check_below(first, elements)

        if line:
            # line.image.show()
            exp, used = prepare_fraction(line, elements)
            expression += exp
            elements = [el for el in elements if el not in used]

        else:
            expression += first.label[0]
            elements = [el for el in elements if el != first]

        prepare_expression(elements)
    return expression


def check_below(this_symbol, elements):
    below = None
    all_bellow = []
    for el in elements:
        # the element is under this_symbol
        if this_symbol.bottom < el.top:
            if (this_symbol.left in range(el.left, el.right)) or (this_symbol.right in range(el.left, el.right)):
                all_bellow.append(el)
    if all_bellow:
        below = el_with_min(all_bellow, 'top')
    return below


# position should say top, right, left
def el_with_min(elements,pos):
    f = attrgetter(pos)
    min_el = None
    all = [f(el) for el in elements]
    min_val = min(all)
    for el in elements:
        if f(el) == min_val:
            min_el = el
    return min_el

# get the topmost, leftmost element - sum of top and left is min
# top attribute is multiplied by 1.5 because the top elements are with higher priority
def get_first_element(elements):
    all_pos = [1.5*el.top + el.left for el in elements]
    min_el = None
    if all_pos:
        min_pos = min(all_pos)
        for el in elements:
            if 1.5*el.top + el.left == min_pos:
                min_el = el
    return min_el


def prepare_fraction(line, elements):
    top = {}
    bottom = {}
    for el in elements:
        # check all that are within its width
        if el.left in range(line.left, line.right) or el.right in range(line.left, line.right):
            # check the ones on top
            if el.bottom < line.top:
                top[el.left] = el
            # check the ones on bottom
            if el.top > line.bottom:
                bottom[el.left] = el

    top_list = sorted(top)
    bottom_list = sorted(bottom)
    top_list_el = [top[key] for key in top_list]
    bottom_list_el = [bottom[key] for key in bottom_list]

    expression = "("
    if len(top_list_el) > 1:
        expression += "("
    for el in top_list_el:
        expression += el.label[0]
    if len(top_list_el) > 1:
        expression += ")"
    expression += "/"
    if len(bottom_list_el) > 1:
        expression += "("
    for el in bottom_list_el:
        expression += el.label[0]
    if len(bottom_list_el) > 1:
        expression += ")"
    expression += ")"

    #return all elements that i have used so i can continue making the expression without them
    used = top_list_el + bottom_list_el
    used.append(line)
    return expression, used
