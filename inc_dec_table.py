from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import sys

x = Symbol('x')
y = Symbol('y')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
m = Symbol('m')
n = Symbol('n')


COLUMN_SPACE = 6    # Even number recommended


def main():

    # Get values from user input.
    xn_tuple_origin, sympy_fx, sympy_fpx = get_input_values()

    # Add value at the beginning and the end.
    xn_list_modified = list(xn_tuple_origin)
    xn_list_modified.sort()

    af = xn_tuple_origin[0]
    bf = xn_tuple_origin[-1]

    xn_list_modified.append(float(af-1))
    xn_list_modified.append(float(bf+1))

    xn_list_modified = list(set(xn_list_modified))
    xn_list_modified.sort()

    print(xn_list_modified)

    # Now get results of fx and fpx each in list
    # Do not sort() fx and fpx list.
    result_fx_list = []
    result_fpx_list = []

    for xn in xn_list_modified:

        # Calculate f(x) and f'(x) with x values entered.
        # If it makes TypeError, f(x) may contain more variable such as a or b. Then don't round its result.
        r_fx = sympy_fx.subs({x: xn})
        try:
            rf_fx = round(r_fx, 1)

        except TypeError:
            rf_fx = r_fx
        result_fx_list.append(rf_fx)

        r_fpx = sympy_fpx.subs({x: xn})
        try:
            rf_fpx = round(r_fpx, 1)

        except TypeError:
            rf_fpx = r_fpx
        result_fpx_list.append(rf_fpx)

    # check if all the results are correctly stored.
    if len(xn_list_modified) == len(result_fx_list) == len(result_fpx_list):
        print("Calculate succeed")
    else:
        print("Calculate failed!")
        sys.exit(0)

    # Finally, draw the table to show the result.
    print(f'\n\nf(x): {sympy_fx}')
    print("=============================")

    xn_list_final, result_fx, result_fpx = \
        replace_with_signs(xn_tuple_origin, xn_list_modified, result_fx_list, result_fpx_list)

    draw_table(xn_list_final, result_fx, result_fpx)


def replace_with_signs(x_origin, xn, fx, fpx):

    result_xn = xn
    result_fx = fx
    result_fpx = fpx

    for (i, item) in enumerate(xn):

        if item in x_origin:
            try:
                if xn[i-1] in x_origin:

                    if fx[i] > fx[i-1]:

                        result_xn.insert(i, "...")
                        result_fx.insert(i, "/")
                        result_fpx.insert(i, "+")

                    elif fx[i] < fx[i-1]:

                        result_xn.insert(i, "...")
                        result_fx.insert(i, "\\")
                        result_fpx.insert(i, "-")

            except IndexError:
                continue

            except TypeError:
                continue

        else:

            try:
                if fx[i] > fx[i+1]:

                    result_xn[i] = "..."
                    result_fx[i] = "\\"
                    result_fpx[i] = "-"

                elif fx[i] < fx[i+1]:

                    result_xn[i] = "..."
                    result_fx[i] = "/"
                    result_fpx[i] = "+"

                else:
                    continue

            except IndexError:
                try:
                    if fx[i] < fx[i-1]:

                        result_xn[i] = "..."
                        result_fx[i] = "\\"
                        result_fpx[i] = "-"

                    elif fx[i] > fx[i-1]:

                        result_xn[i] = "..."
                        result_fx[i] = "/"
                        result_fpx[i] = "+"
                    else:
                        continue
                except TypeError:
                    continue

            except TypeError:
                continue

    return result_xn, result_fx, result_fpx


def draw_table(xn_list, result_fx, result_fpx):

    # Set column space as biggest string size and make it even number
    space = COLUMN_SPACE

    for i in xn_list:
        if len(str(i)) > space:
            space = len(str(i))

    for ii in result_fx:
        if len(str(ii)) > space:
            space = len(str(ii))

    for iii in result_fpx:
        if len(str(iii)) > space:
            space = len(str(iii))

    if space / 2 != int(space / 2):
        space += 1

    # At the beginning of the lists, rows title should be displayed.
    xn_list.insert(0, 'x')
    result_fx.insert(0, 'f(x)')
    result_fpx.insert(0, 'f\'(x)')

    sp = ' '

    # At first loop, display row title, and display each value between spaces.
    # Spaces are determined based on string length.
    first = True
    for s in xn_list:
        if first:
            first = False
            print(f'\nx{5*sp}', end='|')
        else:
            s_len = len(str(s))
            s_sp = int((space-s_len) / 2)
            if s_len / 2 == int(s_len / 2):
                print(f'{s_sp*sp}{s}{s_sp*sp}', end='|')
            else:
                print(f'{s_sp*sp}{s}{s_sp*sp}{sp}', end='|')

    first = True
    for t in result_fpx:
        if first:
            first = False
            print(f'\nf\'(x) ', end='|')
        else:
            t_len = len(str(t))
            t_sp = int((space-t_len) / 2)
            if t_len / 2 == int(t_len / 2):
                print(f'{t_sp*sp}{t}{t_sp*sp}', end='|')
            else:
                print(f'{t_sp*sp}{t}{t_sp*sp}{sp}', end='|')

    first = True
    for u in result_fx:
        if first:
            first = False
            print('\nf(x)  ', end='|')
        else:
            u_len = len(str(u))
            u_sp = int((space-u_len) / 2)
            if u_len / 2 == int(u_len / 2):
                print(f'{u_sp*sp}{u}{u_sp*sp}', end='|')
            else:
                print(f'{u_sp*sp}{u}{u_sp*sp}{sp}', end='|')

    print('\n')


# get input in input_x_values() and input_fx() methods and check correctness in this method,
# then finally get variables. tuple with int, 2 sympy object
def get_input_values():

    # get x values in tuple and check if the values are correct.
    while True:

        xn_list = input_x_values()

        if len(xn_list) > 0:

            # Print xn_list entered to see if it is correct.
            print(f'\n{xn_list}')
            print("are values correct?")
            correct_ans = input("yes(enter), no or exit: ")

            if correct_ans == 'yes' or correct_ans == '':
                break
            elif correct_ans == 'no':
                pass
            elif correct_ans == 'exit':
                sys.exit(0)
            else:
                pass
        else:
            print(f'tuple variable entered: {xn_list}')
            print("\nx values are not exist, or you didn't put correct int values")
            sys.exit(0)

    # get fx and fx prime functions and check if it is correct.
    while True:

        sympy_fx = input_fx('fx')
        sympy_fpx = input_fx('FX PRIME')

        print(f'\nf(x):  {sympy_fx}')
        print(f'f\'(x):  {sympy_fpx}\n')
        fx_ans = input("are f(x)s correct? yes(enter), no or exit")
        print("\n")

        if fx_ans == 'yes' or fx_ans == '':
            break
        elif fx_ans == 'no':
            continue
        elif fx_ans == 'exit':
            sys.exit(0)
        else:
            break

    return xn_list, sympy_fx, sympy_fpx


def input_x_values():

    xn = []
    i = 0

    while True:
        i += 1
        input_x = input(f'x{i} = ')
        if input_x == "":
            break
        else:
            try:
                xn.append(round(float(input_x), 1))
                print(input_x)
            except TypeError:
                continue
            except ValueError:
                if '/' in input_x:
                    af, bf = input_x.split('/')
                    abf = int(af) / int(bf)
                    xn.append(round(float(abf), 1))

    xn_list = list(set(xn))
    xn_list.sort()

    return tuple(xn_list)


def input_fx(fx_name):
    fx = input(f"\nwrite {fx_name} in the form sympy understand : ex) 2*x**3 + 2*(x+3)\n: ")

    try:

        # Sympy method that convert typed string function to sympy object.
        expression = parse_expr(fx)
        return expression

    except SyntaxError:
        print(fx)
        fx = input(f"\nYou may put wrong expression, type {fx_name} again in correct form\n: ")
        try:
            expression = parse_expr(fx)
            return expression
        except SyntaxError:
            print("Check out the document to see how to use script correctly.")
            sys.exit(0)


main()
