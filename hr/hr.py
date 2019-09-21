import os
import ui
import data_manager
import common
import main


def start_module():
    table = data_manager.get_table_from_file("hr/persons.csv")
    id_ = 0
    options = ["Show table",
               "Add to table",
               "Remove from table",
               "Update table",
               "Get oldest person",
               "Closest person to avarage age"]
    ui.print_menu("Human resources manager", options, "Back to main menu")
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        os.system("clear")
        show_table(table)
        start_module()
    elif option == "2":
        add(table)
        start_module()
    elif option == "3":
        remove(table, id_)
        start_module()
    elif option == "4":
        update(table, id_)
        start_module()
    elif option == "5":
        get_oldest_person(table)
        ui.print_result(get_oldest_person(table), "Oldest person(s): ")
        start_module()
    elif option == "6":
        get_persons_closest_to_average(table)
        ui.print_result(get_persons_closest_to_average(
            table), "Closest person to average: ")
        start_module()
    elif option == "0":
        os.system("clear")
        main.main()
    else:
        raise KeyError("There is no such option.")


def show_table(table):
    title_list = ["id", "name", "age"]
    ui.print_table(table, title_list)


def add(table):
    inputs = ui.get_inputs(["\nName: ", "Surname: ", "Year: "],
                           "Please provide your personal information!")
    newitem = []
    newid = common.generate_random(table)
    newitem.append(newid)
    inputs[0] = inputs[0] + " " + inputs[1]
    inputs.pop(1)

    iterator = 0
    for i in inputs:
        newitem.append(inputs[iterator])
        iterator += 1
    table.append(newitem)
    data_manager.write_table_to_file("hr/persons.csv", table)

    os.system("clear")
    show_table(table)
    return table


def remove(table, id_):
    row_counter = 0
    id_ = ui.get_inputs(
        [""], "Please provide the ID of the item you want to remove: ")
    for line in table:
        row_counter += 1
        if id_[0] == line[0]:
            table.remove(line)
            data_manager.write_table_to_file("hr/persons.csv", table)
            os.system("clear")
            show_table(table)
            return table
        elif id_[0] != line[0] and row_counter == len(table):
            ui.print_error_message("There is no such ID!")


def update(table, id_):
    row_counter = 0
    id_ = ui.get_inputs(
        [""], "Please provide the ID of the item you want to update: ")
    for line in table:
        row_counter += 1
        if id_[0] in line[0]:
            newname = ui.get_inputs([""], "Please add a new record for name: ")
            newsurname = ui.get_inputs(
                [""], "Please add a new record for surname: ")
            newname = newname[0] + " " + newsurname[0]
            line[1] = "".join(newname)
            newyear = ui.get_inputs([""], "Please add a new record for year: ")
            line[2] = "".join(newyear)
            data_manager.write_table_to_file("hr/persons.csv", table)
            os.system("clear")
            show_table(table)
            return table
        elif id_[0] != line[0] and row_counter == len(table):
            ui.print_error_message("There is no such ID!")


def get_oldest_person(table):
    ages = []

    for line in table:
        ages.append(line[2])

    minimum = min(ages)

    oldest_persons = []

    for line in table:
        if minimum in line:
            oldest_persons.append(line[1])

    return oldest_persons


def get_persons_closest_to_average(table):
    ages = []

    for line in table:
        ages.append(line[2])

    avg = 0
    sum_of_ages = 0

    for item in ages:
        item = int(item)
        sum_of_ages += item

    avg = sum_of_ages / len(ages)

    difference_list = []
    persons_difference_from_avg_dict = {}

    for line in table:
        line[2] = float(line[2])
        diff = (abs(avg - line[2]))
        difference_list.append(diff)
        diff = str(diff)
        persons_difference_from_avg_dict.update({line[1]: diff})

    minimum_diff = min(difference_list)
    closest_persons_to_avg = []
    for key, value in persons_difference_from_avg_dict.items():
        value = float(value)
        if minimum_diff == value:
            closest_persons_to_avg.append(key)

    return closest_persons_to_avg
