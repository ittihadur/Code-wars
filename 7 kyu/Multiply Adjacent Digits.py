# Multiply the adjacent digits which are not separated by a '-' or a '+' in a string, then do the sum.

# Examples
# "53+5"    -->   20  # = 5 * 3 + 5
# "266-66"  -->   36  # = 2 * 6 * 6 - 6 * 6
# "555"     -->  125  # = 5 * 5 * 5

# Solution
def digit_multiplication(expression):
    result = 0
    product = 1
    operator = '+'

    for i in expression:
        if i.isdigit():
            product *= int(i)

        elif i == '+' or i == '-':
            if operator == '+':
                result += product
            else:
                result -= product

            operator = i
            product = 1

    
    if operator == '+':
        result += product
    else:
        result -= product

    return result