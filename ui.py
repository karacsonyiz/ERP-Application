import os
import main


def print_table(table, title_list):
    longestword = 0
    maxlength = -4
    for i in table:
        for k in i:
            if len(k) >= longestword:
                longestword = len(k)

    g = ''
    j = 0
    for i in title_list:
        g += ' | {:{align}{width}}'.format(title_list[j], align='^', width=longestword+2)
        j+=1


    for i in g:
        maxlength += 1
    maxlength2 = maxlength + 2
    maxlength3 = maxlength + 4

    print(" /"+"-"*maxlength2+"\\")       
    print(g+"|")
    print(" "+"-"*maxlength3)

    for row in table:
        s = ''
        for cell in row:
            s += ' | {:{align}{width}}'.format(cell, align='^', width=longestword+2)
        print(s+"|")
        print(" "+"-"*maxlength3)


def print_result(result, label):
    print(label, end="")
    print(result)


def print_menu(title, list_options, exit_message):
    print(title)
    k = 1
    for i in list_options:
        print("    ("+str(k)+")",i)
        k += 1
    print("    (0) "+exit_message)


def get_inputs(list_labels, title):
    inputs = []
    print(title, end="")
    k = 0
    for i in list_labels:
        print(list_labels[k], end = "")
        inputs.append(str(input()))
        k += 1
    
    return inputs


def print_error_message(message):
    print(message)
