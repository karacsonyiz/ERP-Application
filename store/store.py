import os
import ui
import data_manager
import common
import main


def start_module():
    table = data_manager.get_table_from_file("store/games.csv")
    id_ = ""
    manufacturer = ""

    options = ["Show table",
               "Add to table",
               "Remove from table",
               "Update table",
               "Games count by manufacturers",
               "Avarage amount of games of a manufacturer"]
    ui.print_menu("Store manager", options, "Back to main menu")
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
        get_counts_by_manufacturers(table)
        ui.print_result(get_counts_by_manufacturers(table),
                        "Game count available by manufacturers: ")
        start_module()
    elif option == "6":
        manufacturer = ui.get_inputs(["manufacturer: "], "Please provide the ")
        manufacturer = manufacturer[0]
        try:
            get_average_by_manufacturer(table, manufacturer)
            ui.print_result(get_average_by_manufacturer(
                table, manufacturer), "Average amount of games in stock by manufacturer: ")
        except ZeroDivisionError:
                ui.print_error_message("There is no such manufacturer")         
        start_module()
    elif option == "0":
        os.system("clear")
        main.main()
    else:
        raise KeyError("There is no such option.")


def show_table(table):
    title_list = ["id", "title", "manufacturer", "price", "in stock"]
    ui.print_table(table, title_list)


def add(table):
    inputs = ui.get_inputs(["\nTitle: ", "Manufacturer: ",
                            "Price: ", "In Stock: ", ], "Please provide the records!")
    newitem = []
    newid = common.generate_random(table)
    newitem.append(newid)

    record_index_counter = 0
    for i in inputs:
        newitem.append(inputs[record_index_counter])
        record_index_counter += 1
    table.append(newitem)
    data_manager.write_table_to_file("store/games.csv", table)

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
            data_manager.write_table_to_file("store/games.csv", table)
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
            newtitle = ui.get_inputs(
                [""], "Please add a new record for title: ")
            line[1] = "".join(newtitle)
            newmanufacturer = ui.get_inputs(
                [""], "Please add a new record for manufacturer: ")
            line[2] = "".join(newmanufacturer)
            newprice = ui.get_inputs(
                [""], "Please add a new record for price: ")
            line[3] = "".join(newprice)
            newstock = ui.get_inputs(
                [""], "Please add a new record for stock: ")
            line[4] = "".join(newstock)
            data_manager.write_table_to_file("store/games.csv", table)
            os.system("clear")
            show_table(table)
            return table
        elif id_[0] != line[0] and row_counter == len(table):
            ui.print_error_message("There is no such ID!")


def get_counts_by_manufacturers(table):
    manufacture = {}
    for item in table:
        if item[2] in manufacture:
            manufacture[item[2]] += 1
        else:
            manufacture[item[2]] = 1

    return manufacture


def get_average_by_manufacturer(table, manufacturer):
    total_stock_by_manufacturer = 0
    total_item_by_manufacturer = 0
    for line in table:
        if manufacturer == line[2]:
            line[4] = int(line[4])
            total_stock_by_manufacturer += line[4]
            total_item_by_manufacturer += 1

    avg_by_manufacturer = total_stock_by_manufacturer / total_item_by_manufacturer

    return avg_by_manufacturer
