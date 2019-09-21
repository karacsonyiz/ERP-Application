import os
import ui
import data_manager
import common
import main


def start_module():
    table = data_manager.get_table_from_file("accounting/items.csv")
    id_ = ""
    year = 0
    options = ["Show table",
               "Add to table",
               "Remove from table",
               "Update table",
               "Most profitable year",
               "Avarage profit in a year"]
    ui.print_menu("Accounting manager", options, "Back to main menu")
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
        which_year_max(table)
        ui.print_result(which_year_max(table), "Most profitable year: ")
        start_module()
    elif option == "6":
        year_question = ui.get_inputs([""], "Which year? ")
        year = year_question[0]
        try:
            avg_amount(table, year)
            ui.print_result(avg_amount(table, year),
                            "Average profit in given year: ")
            start_module()
        except ZeroDivisionError:
            ui.print_error_message("There is no such year in the database!")
    elif option == "0":
        os.system("clear")
        main.main()
    else:
        raise KeyError("There is no such option.")


def show_table(table):
    title_list = ["id", "month", "day", "year", "type", "amount"]
    ui.print_table(table, title_list)


def add(table):
    inputs = ui.get_inputs(["\nMonth: ", "Day: ", "Year: ",
                            "Type: ", "Amount: "], "Please provide the records!")
    newitem = []
    newid = common.generate_random(table)
    newitem.append(newid)

    row_counter = 0
    for i in inputs:
        newitem.append(inputs[row_counter])
        row_counter += 1
    table.append(newitem)
    data_manager.write_table_to_file("accounting/items.csv", table)

    os.system("clear")
    show_table(table)
    return table


def remove(table, id_):
    row_counter = 0
    table = data_manager.get_table_from_file("accounting/items.csv")
    id_ = ui.get_inputs(
        [""], "Please provide the ID of the item you want to remove: ")
    for line in table:
        row_counter += 1
        if id_[0] == line[0]:
            table.remove(line)
            data_manager.write_table_to_file("accounting/items.csv", table)
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
            newmonth = ui.get_inputs(
                [""], "Please add a new record for month: ")
            line[1] = "".join(newmonth)
            newday = ui.get_inputs([""], "Please add a new record for day: ")
            line[2] = "".join(newday)
            newyear = ui.get_inputs([""], "Please add a new record for year: ")
            line[3] = "".join(newyear)
            newtype = ui.get_inputs([""], "Please add a new record for type: ")
            line[4] = "".join(newtype)
            newamount = ui.get_inputs(
                [""], "Please add a new record for amount: ")
            line[5] = "".join(newamount)
            data_manager.write_table_to_file("accounting/items.csv", table)
            os.system("clear")
            show_table(table)
            return table
        elif id_[0] != line[0] and row_counter == len(table):
            ui.print_error_message("There is no such ID!")


def which_year_max(table):
    years_list = []

    for line in table:
        if line[3] not in years_list:
            years_list.append(line[3])

    years_profit_dict = {}

    for year in years_list:
        if year not in years_profit_dict.keys():
            years_profit_dict.update({year: 0})

    row_counter = 0
    for year in years_list:
        for line in table:
            if years_list[row_counter] in line:
                if "in" in line:
                    line[5] = int(line[5])
                    years_profit_dict[year] += line[5]
                else:
                    line[5] = int(line[5])
                    years_profit_dict[year] -= line[5]
        row_counter += 1

    most_profit = 0
    most_profitable_year = ""
    for key, value in years_profit_dict.items():
        if value > most_profit:
            most_profit = value
            most_profitable_year = key

    most_profitable_year = int(most_profitable_year)
    return most_profitable_year


def avg_amount(table, year):

    profit = 0
    years = 0

    try:
        year = int(year)
    except ValueError:
<<<<<<< HEAD
        ui.print_error_message("This is not a valid unput for year!")
=======
        ui.print_error_message("This is not a valid input for year!")
>>>>>>> 5a3af5bda610c1ff97656e3292b328f8bb78d746

    for line in table:
        if year == int(line[3]):
            years += 1
            if "in" == line[4]:
                line[5] = int(line[5])
                profit += line[5]
            else:
                line[5] = int(line[5])
                profit -= line[5]

    avarage_amount = profit / years
    return avarage_amount
