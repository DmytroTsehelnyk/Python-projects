from tabulate import tabulate

"""
● Code a Python program that will read from the text file inventory.txt and perform the following on the data,
to prepare for presentation to your managers:

    o We’ve provided a template for you in a file named inventory.py, where a Shoe class should be defined.

    o Inside this file, create a class named Shoes with the following attributes:
        ● country,
        ● code,
        ● product,
        ● cost,
        ● quantity.

    o Inside this class define the following methods:
        ▪ get_cost - Returns the cost of the shoes.
        ▪ get_quantity - Returns the quantity of the shoes.
        ▪ __str__ - This method returns a string representation of a class.

    o Outside this class create a variable with an empty list.
    This variable will be used to store a list of shoes objects

    o Then you must define the following functions outside the class:

        ▪ read_shoes_data - This function will open the file inventory.txt and read the data from this file,
        then create a shoes object with this data and append this object into the shoes list.
        One line in this file represents data to create one object of shoes.
        You must use the try-except in this function for error handling.
        Remember to skip the first line using your code.

        ▪ capture_shoes - This function will allow a user to capture data about a shoe and use this data
        to create a shoe object and append this object inside the shoe list.

        ▪ view_all - This function will iterate over the shoes list and print the details of the shoes
        returned from the __str__ function.
        Optional: you can organise your data in a table format by using Python’s tabulate module.

        ▪ re_stock - This function will find the shoe object with the lowest quantity,
        which is the shoes that need to be re-stocked. Ask the user if they want to add this quantity of shoes
        and then update it. This quantity should be updated on the file for this shoe.

        ▪ search_shoe - This function will search for a shoe from the list using the shoe code
        and return this object so that it will be printed.

        ▪ value_per_item - This function will calculate the total value for each item.
        Please keep the formula for value in mind; value = cost * quantity.
        Print this information on the console for all the shoes.

        ▪ highest_qty - Write code to determine the product with the highest quantity
        and print this shoe as being for sale.

    o Now in your main create a menu that executes each function above.
    This menu should be inside the while loop. Be creative!
"""


# ============== The beginning of the class ==============
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        """ Returns cost of the product """
        return self.cost

    def get_quantity(self):
        """ Returns quantity of the product """
        return self.quantity

    def __str__(self):
        """ Returns a string representation of a class """
        return f'''{self.country},{self.code},{self.product},{self.cost},{self.quantity}'''


# ==================== Shoe list ======================

shoes_list = []

# =========== Functions outside the class =============


def read_shoes_data():
    """ Opens the inventory.txt and adds shoes objects to the list """

    try:
        # Open the inventory file
        f_inventory = open("inventory.txt", "r")

        # Loop over lines except the 1st one
        # Create shoes object and add it to the shoes list
        for line_number, line in enumerate(f_inventory):
            if line_number != 0:
                data = line.strip().split(",")
                shoe = Shoe(data[0], data[1], data[2], data[3], data[4])
                shoes_list.append(shoe)

        # Close the inventory file
        f_inventory.close()

        # data[0] - country
        # data[1] - code
        # data[2] - product
        # data[3] - cost
        # data[4] - quantity

    except FileNotFoundError:
        print("File 'inventory.txt' doesn't exist!")


def capture_shoes():
    """ Shows 'blueprint' information to create new shoe object """

    try:
        # Open the inventory file
        f_inventory = open("inventory.txt", "r")

        # Loop over lines except the 1st one
        for line_number, line in enumerate(f_inventory):
            if line_number != 0:
                print(line)
                break

        # Close the inventory file
        f_inventory.close()

    except FileNotFoundError:
        print("File 'inventory.txt' doesn't exist!")


def add_shoe(country_input, code_input, product_input, cost_input, quantity_input):
    """ Creates new shoe object and adds it to the shoes list """

    new_shoe = Shoe(country_input, code_input, product_input, cost_input, quantity_input)

    try:
        # Open the inventory file
        f_inventory = open("inventory.txt", "a")

        f_inventory.write("\n" + new_shoe.__str__())

        # Close the inventory file
        f_inventory.close()

    except FileNotFoundError:
        print("File 'inventory.txt' doesn't exist!")


def view_all():
    """ Prints the details of the shoes """

    # Initialize 2d list
    shoes_2dlist = []

    # Loop over shoe list
    # Convert data into string
    # Append data to the 2d list
    for shoe in shoes_list:
        shoe_str = shoe.__str__().split(",")
        shoes_2dlist.append([shoe_str[0], shoe_str[1], shoe_str[2], shoe_str[3], shoe_str[4]])

    # Print data in a table format using tabulate module
    print(f"""
{tabulate(shoes_2dlist, headers=["Country", "Code", "Product", "Cost", "Quantity"])}""")


def re_stock():
    """ Determines the product with the lowest quantity """

    # Initialize variables
    lowest = 10
    restock_product = ""

    # Loop over the shoes list
    # Find product with the lowest quantity
    for shoe in shoes_list:
        shoe_str = shoe.__str__().split(",")
        shoe_str[4] = int(shoe_str[4])
        if shoe_str[4] < lowest:
            lowest = shoe_str[4]
            restock_product = shoe_str

    return restock_product


def search_shoe(shoe_id):
    """ Return the shoe by entered ID (Code) """

    # Initialize 2d list
    shoes_2dlist = []
    find = False

    for shoe in shoes_list:
        current_product = shoe.__str__().split(",")
        if shoe_id == current_product[1]:
            # Append data to the 2d list
            data = current_product
            shoes_2dlist.append([data[0], data[1], data[2], data[3], data[4]])

            print(f"""
{tabulate(shoes_2dlist, headers=["Country", "Code", "Product", "Cost", "Quantity"])}""")
            find = not find
            break

    if not find:
        print("No product found with the specified code!")


def value_per_item():
    """ Calculates products values and prints data """

    # Initialize 2d list
    shoes_2dlist = []

    # Loop over the shoes list
    # Find product with the lowest quantity
    for shoe in shoes_list:
        shoe_str = shoe.__str__().split(",")
        shoe_str[3] = int(shoe_str[3])  # cast cost to int
        shoe_str[4] = int(shoe_str[4])  # cast quantity to int

        # Calculate the product value
        value = shoe_str[3] * shoe_str[4]

        # Append data to the 2d list
        shoes_2dlist.append([shoe_str[0], shoe_str[1], shoe_str[2], value])

    # Print data in a table format using tabulate module
    print(f"""
{tabulate(shoes_2dlist, headers=["Country", "Code", "Product", "Value"])}""")


def highest_qty():
    """ Determines the product with the highest quantity """

    # Initialize variables
    highest = 50
    for_sale_product = ""

    # Loop over the shoes list
    # Find product with the highest quantity
    for product_number, shoe in enumerate(shoes_list):
        shoe_str = shoe.__str__().split(",")
        shoe_str[4] = int(shoe_str[4])
        if shoe_str[4] > highest:
            highest = shoe_str[4]
            for_sale_product = shoe_str

    return for_sale_product


def change_quantity(file_name, line_number, product_quantity):
    """ Changes product quantity in the file """

    # Open th file and count number of lines
    read_f = open(file_name, 'r')
    lines = read_f.readlines()

    current_line = 1
    write_f = open(file_name, 'w')

    # Loop over the file
    for line in lines:

        # Change last number to new quantity
        if current_line == line_number:
            write_f.write(line[:-2] + str(product_quantity) + "\n")
        else:
            write_f.write(line)

        current_line += 1

    read_f.close()
    write_f.close()


# ========== Main Menu =============

while True:
    menu = input("""
Choose one of the option below:
i - show inventory information
s - search product by code number
c - add new product to the inventory
l - show product with the lowest quantity
h - show product with the highest quantity
v - show value of all products
e - exit the program
: """).lower()

    # Initialize shoes
    read_shoes_data()

    # show inventory information
    if menu == "i":
        view_all()

    # search product by code number
    elif menu == "s":
        shoe_code = input("Enter the code of the product you are looking for: ")
        search_shoe(shoe_code)

    # add new product to the inventory
    elif menu == "c":
        print("You can add new product using the values below:")
        capture_shoes()

        while True:

            # Ask to enter country of origin
            new_country = input("Enter the product's country of origin: ").capitalize().strip()
            if new_country == "" or new_country.isdigit():
                print("Invalid input!")

            # Ask to enter product code
            else:
                new_code = input("Enter the product's code: ").upper().strip()
                if new_code == "" or new_code.isdigit():
                    print("Invalid input!")

                # Ask to enter product name
                else:
                    new_product = input("Enter the product's name: ").strip()
                    if new_product == "" or new_product.isdigit():
                        print("Invalid input!")

                    # Ask to enter product cost
                    else:
                        new_cost = input("Enter the product's cost: ").strip()
                        if new_cost == "" or not new_cost.isdigit():
                            print("Invalid input!")

                        # Ask to enter product quantity
                        else:
                            new_quantity = input("Enter the product's quantity: ").strip()
                            if new_quantity == "" or not new_quantity.isdigit():
                                print("Invalid input!")
                            else:
                                # Add new shoe to the shoes list
                                add_shoe(new_country, new_code, new_product, new_cost, new_quantity)
                                print(f"Product '{new_product}' added to the inventory.")
                                break

    # show product with the lowest quantity
    elif menu == "l":

        # Initialize variable
        product_line = 0

        re_stock()
        print(f"""
Product '{re_stock()[2]}' from {re_stock()[0]} has the lowest quantity: {re_stock()[4]}""")

        # Find line of product to re stock in inventory
        try:
            f_inv = open("inventory.txt", "r")

            for lines_count, shoes in enumerate(f_inv):
                line_content = shoes.__str__().split(",")
                if line_content[1] == re_stock()[1]:
                    product_line = lines_count + 1
                    break

            f_inv.close()

        except FileNotFoundError:
            print("File 'inventory.txt' doesn't exist!")

        choice = input("Do you want to change quantity for this product? (y/n): ").lower()

        # Ask to enter new quantity
        # Change it for the product with the lowest quantity
        if choice == "y":
            number = int(input("Enter new quantity for product: "))

            change_quantity("inventory.txt", product_line, number)
            print("New information added to the inventory file.")
            continue

        elif choice == "n":
            pass

        else:
            print("Invalid input!")

    # show product with the highest quantity
    elif menu == "h":

        # Print information about the product with the highest quantity
        print(f"""
Product '{highest_qty()[2]}' from {highest_qty()[0]} has the highest quantity: {highest_qty()[4]}""")

    # show value of all products
    elif menu == "v":
        value_per_item()

    # exit the program
    elif menu == "e":
        print("Goodbye!")
        exit()

    else:
        print("Something wrong. Try again!")
