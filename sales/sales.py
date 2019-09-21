# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual sale price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the sale was made
# customer_id: string, id from the crm

# importing everything you need
import os
import ui
import data_manager
import common
import main


def start_module():
    table = data_manager.get_table_from_file("sales/sales.csv")
    id_ = 0
    month_from = 0
    day_from = 0
    year_from = 0
    month_to = 0
    day_to = 0
    year_to = 0
    options = ["Show table",
               "Add to table",
               "Remove from table",
               "Update table",
               "Get lowest priced item's id",
               "Get items sold between"]
    ui.print_menu("Sales manager", options, "Back to main menu")
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
        get_lowest_price_item_id(table)
        ui.print_result(get_lowest_price_item_id(
            table), "Lowest priced item's ID: ")
        start_module()
    elif option == "6":
        inputs = ui.get_inputs(["Year from: ", "Month from: ", "Day from: ",
                                "Year to: ", "Month to: ", "Day to: "], "Please provide\n")
        year_from = inputs[0]
        month_from = inputs[1]
        day_from = inputs[2]
        year_to = inputs[3]
        month_to = inputs[4]
        day_to = inputs[5]
        get_items_sold_between(table, month_from, day_from,
                               year_from, month_to, day_to, year_to)
        ui.print_result(get_items_sold_between(table, month_from, day_from, year_from,
                                               month_to, day_to, year_to), "Items sold between given dates: \n")
        start_module()
    elif option == "0":
        os.system("clear")
        main.main()
    else:
        raise KeyError("There is no such option.")


def show_table(table):
    title_list = ["id", "game", "sold", "month", "day", "year"]
    ui.print_table(table, title_list)


def add(table):
    inputs = ui.get_inputs(["\nTitle: ", "Price: ", "Month: ",
                            "Day: ", "Year: "], "Please provide the information!")
    newitem = []
    newid = common.generate_random(table)
    newitem.append(newid)

    iterator = 0
    for i in inputs:
        newitem.append(inputs[iterator])
        iterator += 1
    table.append(newitem)
    data_manager.write_table_to_file("sales/sales.csv", table)

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
            data_manager.write_table_to_file("sales/sales.csv", table)
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
            newgame = ui.get_inputs(
                [""], "Please add a new record for title: ")
            line[1] = "".join(newgame)
            newprice = ui.get_inputs(
                [""], "Please add a new record for price: ")
            line[2] = "".join(newprice)
            newsold = ui.get_inputs(
                [""], "Please add a new record for month: ")
            line[3] = "".join(newsold)
            newday = ui.get_inputs([""], "Please add a new record for day: ")
            line[4] = "".join(newday)
            newyear = ui.get_inputs([""], "Please add a new record for year: ")
            line[4] = "".join(newyear)
            data_manager.write_table_to_file("sales/sales.csv", table)
            os.system("clear")
            show_table(table)
            return table
        elif id_[0] != line[0] and row_counter == len(table):
            ui.print_error_message("There is no such ID!")


def get_lowest_price_item_id(table):
    firstline = table[1]
    lowestprice = firstline[2]
    lowestpriced = ""
    for line in table:
        if int(line[2]) < int(lowestprice):
            lowestpriced = line[0]
            lowestprice = int(line[2])

    return lowestpriced


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    sold_between = []
    try:
        date_from_as_days = (int(year_from) * 364) + (int(month_from) * 30) + int(day_from)
        date_to_as_days = (int(year_to) * 364) + (int(month_to) * 30) + int(day_to)
       
        for line in table:
            date_as_days = (int(line[5]) * 364) + (int(line[3]) * 30) + (int(line[4]))
            if date_as_days > date_from_as_days and date_as_days < date_to_as_days:
                line[0] = (str(line[0]))
                line[1] = (str(line[1]))
                line[2] = (int(line[2]))
                line[3] = (int(line[3]))
                line[4] = (int(line[4]))
                line[5] = (int(line[5]))
                sold_between.append(line)
    except ValueError:
            ui.print_error_message("You entered an invalid date!")        
    if len(sold_between) != 0:
        return sold_between
    else:
        return "No games were sold"


# functions supports data abalyser
# --------------------------------


def get_title_by_id(id):

    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str the title of the item
    """

    # your code

    pass


def get_title_by_id_from_table(table, id):

    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str the title of the item
    """

    # your code

    pass


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        (str) the _id_ of the item that was sold most recently.
    """

    # your code

    pass


def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        (str) the _id_ of the item that was sold most recently.
    """

    # your code

    pass


def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        (str) the _title_ of the item that was sold most recently.
    """

    # your code

    pass


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        (number) the sum of the items' prices
    """

    # your code

    pass


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        (number) the sum of the items' prices
    """

    # your code

    pass


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.
    Args:
         sale_id (str): sale id to search for
    Returns:
         customer_id that belongs to the given sale id
    """

    # your code

    pass


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.
    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
         customer_id that belongs to the given sale id
    """

    # your code

    pass


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.
    Returns a set of customer_ids that are present in the table.
    Returns:
         set of customer_ids that are present in the table
    """

    # your code

    pass


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.
    Args:
        table (list of list): the sales table
    Returns:
         set of customer_ids that are present in the table
    """

    # your code

    pass


def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    # your code

    pass


def get_all_sales_ids_for_customer_ids_form_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    # your code

    pass


def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code

    pass


def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code

    pass
