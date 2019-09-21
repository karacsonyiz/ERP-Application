import os
import ui
import data_manager
import common
import main


def start_module():
    table = data_manager.get_table_from_file("crm/customers.csv")
    id_ = 0
    options = ["Show table",
               "Add to table",
               "Remove from table",
               "Update table",
               "Get longest name's ID",
               "Get subscribed e-mails"]
    ui.print_menu("Customer Relationship Management (CRM)",
                  options, "Back to main menu")
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
        get_longest_name_id(table)
        ui.print_result(get_longest_name_id(table), "Longest name's ID: ")
        start_module()
    elif option == "6":
        get_subscribed_emails(table)
        ui.print_result(get_subscribed_emails(table), "Subscribed e-mails: ")
        start_module()
    elif option == "0":
        os.system("clear")
        main.main()
    else:
        raise KeyError("There is no such option.")


def show_table(table):
    title_list = ["id", "name", "e-mail", "subscription"]
    ui.print_table(table, title_list)


def add(table):
    inputs = ui.get_inputs(["\nName: ", "Surname: ", "E-mail: ",
                            "Subscribed: "], "Please provide your personal information!")
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
    data_manager.write_table_to_file("crm/customers.csv", table)

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
            data_manager.write_table_to_file("crm/customers.csv", table)
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
        if id_[0] == line[0]:
            newname = ui.get_inputs([""], "Please add a new record for name: ")
            newsurname = ui.get_inputs(
                [""], "Please add a new record for surname: ")
            newname = newname[0] + " " + newsurname[0]
            line[1] = "".join(newname)
            newemail = ui.get_inputs(
                [""], "Please add a new record for e-mail: ")
            line[2] = "".join(newemail)
            newsub = ui.get_inputs(
                [""], "Please add a new record for subscription: ")
            line[3] = "".join(newsub)
            data_manager.write_table_to_file("crm/customers.csv", table)
            os.system("clear")
            show_table(table)
            return table
        elif id_[0] != line[0] and row_counter == len(table):
            ui.print_error_message("There is no such ID!")


def get_longest_name_id(table):
    name_list = []
    for item in table:
        name_list.append(item[1])

    alphabetical_name_list = common.get_alphabetical(name_list)
    the_name = alphabetical_name_list[0]

    for item in table:
        if the_name in item:
            solution = item[0]

    return solution


def get_subscribed_emails(table):
    subs = []
    for line in table:
        if line[3] == "1":
            subs.append(line[2] + ";" + line[1])

    return subs


# functions supports data analyser
# --------------------------------


def get_name_by_id(id):

    """
    Reads the table with the help of the data_manager module.
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the customer

    Returns:
        str the name of the customer
    """

    # your code

    pass


def get_name_by_id_from_table(table, id):

    """
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the customer table
        id (str): the id of the customer

    Returns:
        str the name of the customer
    """

    # your code

    pass
