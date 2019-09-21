import os
import ui
import data_manager
import common
import main


def start_module():
    table = data_manager.get_table_from_file("inventory/inventory_test.csv")
    id_ = ""

    options = ["Show table",
               "Add to table",
               "Remove from table",
               "Update table",
               "Items in good shape",
               "Avarage durability of manufacturers"]
    ui.print_menu("Inventory manager", options, "Back to main menu")
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
        get_available_items(table)
        ui.print_result(get_available_items(table), "Available items: ")
        start_module()
    elif option == "6":
        get_average_durability_by_manufacturers(table)
        ui.print_result(get_average_durability_by_manufacturers(
            table), "Average durability by manufacturers: ")
    elif option == "0":
        os.system("clear")
        main.main()
    else:
        raise KeyError("There is no such option.")


def show_table(table):
    title_list = ["id", "name", "manufacturer", "purcahse date", "durability"]
    ui.print_table(table, title_list)


def add(table):
    inputs = ui.get_inputs(["\nName: ", "Manufacturer: ", "Purchase date: ",
                            "Durability: ", ], "Please provide the records!")
    newitem = []
    newid = common.generate_random(table)
    newitem.append(newid)

    row_counter = 0
    for i in inputs:
        newitem.append(inputs[row_counter])
        row_counter += 1
    table.append(newitem)
    data_manager.write_table_to_file("inventory/inventory_test.csv", table)

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
            data_manager.write_table_to_file("inventory/inventory_test.csv", table)
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
            line[1] = "".join(newname)
            newmanufacturer = ui.get_inputs(
                [""], "Please add a new record for manufacturer: ")
            line[2] = "".join(newmanufacturer)
            newpurchase_date = ui.get_inputs(
                [""], "Please add a new record for purchase date ")
            line[3] = "".join(newpurchase_date)
            newdurability = ui.get_inputs(
                [""], "Please add a new record for durability: ")
            line[4] = "".join(newdurability)
            data_manager.write_table_to_file("inventory/inventory_test.csv", table)
            os.system("clear")
            show_table(table)
            return table
        elif id_[0] != line[0] and row_counter == len(table):
            ui.print_error_message("There is no such ID!")


def get_available_items(table):
    durable = []
    for item in table:
        item[3] = int(item[3])
        item[4] = int(item[4])
        if 2017 - int(item[3]) <= int(item[4]):
            durable.append(item)
    return durable


def get_average_durability_by_manufacturers(table):
    manufacturers_list = []

    for line in table:
        if line[2] not in manufacturers_list:
            manufacturers_list.append(line[2])

    manufacturers_durabilites_dict = {}

    for manufacturer in manufacturers_list:
        if manufacturer not in manufacturers_durabilites_dict.keys():
            manufacturers_durabilites_dict.update({manufacturer: 0})

    items_by_manufacturer = 0
    row_counter = 0

    for manufacturer in manufacturers_list:
        items_by_manufacturer = 0
        for line in table:
            if manufacturers_list[row_counter] in line:
                items_by_manufacturer += 1
                line[4] = int(line[4])
                manufacturers_durabilites_dict[manufacturer] += line[4]
        row_counter += 1
        manufacturers_durabilites_dict[manufacturer] /= items_by_manufacturer

    return manufacturers_durabilites_dict
