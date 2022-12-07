# ===== importing libraries =====

# ===== functions Section =====

def log_in():
    """ Asks user to log in with her username """

    while True:
        # Ask to enter username
        u_login = input("Enter your username to log in: ")
        if u_login == "":
            print("Invalid input. Please, enter your username: ")

        # Ask to enter the password
        else:
            user_password = input("Enter your password: ")
            if user_password == "":
                print("Invalid input. Please, enter your password: ")

            # Validate username and password
            else:
                # Open the user.txt
                f_user = open("user.txt", "r")

                # Initialize validation
                validation_user = False
                validation_pass = False

                # Loop over the file to find similar username and password
                for lines in f_user:
                    content = lines.strip()
                    user_content = content.split(', ')

                    # If username valid
                    # Toggle validation
                    for user in user_content:
                        if user == u_login:
                            validation_user = not validation_user
                            break
                        else:
                            continue

                    # If password valid
                    # Toggle validation
                    for password in user_content:
                        if password == user_password:
                            validation_pass = not validation_pass
                            break
                        else:
                            continue

                f_user.close()

                # If both username and password are valid
                # Log in as entered user
                if validation_user and validation_pass:
                    print(f"You have logged as {u_login}!")
                    break

                # If password is wrong, print error
                elif not validation_pass and validation_user:
                    print(f"Wrong password for user {u_login}!")

                # If no user has been found, print error
                elif not validation_user:
                    print(f"No user with name {u_login}!")

    return u_login


def reg_user(login):
    """ Registering new user """

    if login == "admin":
        # Open the user.txt for reading and writing on new line
        user_file = open("user.txt", "a")

        # Request input of a new username
        while True:
            username_input = input("Enter a username of person you want to add: ")
            if username_input == "":
                print("Invalid input. Please, enter a username of person you want to add: ")

            # Check if entered username is duplicate
            elif username_input == duplicate_check(username_input):
                print(f"User with name '{username_input}' already exist!")
                continue
            else:
                break

        # Add new user to the user.txt
        user_file.write("\n" + username_input + "," + " ")

        # Request input of a new password and its confirmation
        while True:
            password_input = input("Enter your password: ")
            password_conf = input("Enter confirmation of your password: ")
            if password_input != password_conf:
                print("Your passwords need to be the same!")
            else:
                break

        # Add new user's password to the user.txt
        print(f"""
New user with name {username_input} successfully registered.""")

        user_file.write(password_input)
        user_file.close()

    else:
        print("Only admin is allowed to register new users.")


def add_task():
    """ Adds new task """

    tasks_file = open('tasks.txt', 'a')

    # Request input of the username and information about task
    while True:
        # Request to enter username
        username = input('Enter a username: ')
        if username == '':
            print('Invalid input. Please, enter a username: ')

        # Request to enter title of a task
        else:
            task_title = input('Enter a title of a task: ')
            if task_title == '':
                print('Invalid input. Please, a title of a task: ')

            # Request to enter a task description
            else:
                task_desc = input('Enter a task description: ')
                if task_desc == '':
                    print('Invalid input. Please, a task description: ')

                # Request to enter a current date
                else:
                    current_date = input('Enter a current date: ')
                    if current_date == '':
                        print('Invalid input. Please, a current date: ')

                    # Request to enter a due date
                    else:
                        due_date = input('Enter a due date: ')
                        if due_date == '':
                            print('Invalid input. Please, a due date: ')
                        else:
                            break

    # Add information to the tasks.txt
    tasks_file.write(f'\n{username}, {task_title}, {task_desc}, {current_date}, {due_date}, No')

    tasks_file.close()


def view_all():
    """ Shows all tasks to user """

    tasks_file = open('tasks.txt', 'r')

    # tasks_content[0] - username
    # tasks_content[1] - task_title
    # tasks_content[2] - task_desc
    # tasks_content[3] - current_date
    # tasks_content[4] - due_date
    # tasks_content[5] - completeness

    # Check task number
    task_num = 0
    # Loop over file and print the data
    for t_line in tasks_file:
        t_content = t_line
        tasks_content = t_content.split(', ')
        task_num += 1
        print(f'''
Task number:        {task_num}
Task name:          {tasks_content[1]}
Assigned to:        {tasks_content[0]}
Date assigned:      {tasks_content[3]}
Due date:           {tasks_content[4]}
Task complete?      {tasks_content[5]}
Task description:
{tasks_content[2]}
{'—' * 110}
    ''')
    tasks_file.close()


def view_mine():
    """ Shows all tasks to logged user """

    tasks_file = open('tasks.txt', 'r')

    # tasks_content[0] - username
    # tasks_content[1] - task_title
    # tasks_content[2] - task_desc
    # tasks_content[3] - current_date
    # tasks_content[4] - due_date
    # tasks_content[5] - completeness

    # Check task number
    task_num = 0
    # Loop over file and print the data
    for t_line in tasks_file:
        t_content = t_line
        tasks_content = t_content.split(', ')
        task_num += 1
        if tasks_content[0] == user_login:
            print(f'''
Task number:        {task_num}
Task name:          {tasks_content[1]}
Assigned to:        {tasks_content[0]}
Date assigned:      {tasks_content[3]}
Due date:           {tasks_content[4]}
Task complete?      {tasks_content[5]}
Task description:
{tasks_content[2]}
{'—' * 110}
    ''')
    tasks_file.close()


def duplicate_check(login):
    """ Checks usernames for duplicates """

    user_file = open("user.txt", "r")
    for lines in user_file:
        all_content = lines.strip()
        user_file_content = all_content.split(', ')

        # If username valid
        for name in user_file_content:
            if name == login:
                return name
            else:
                continue


def mark_task(file_name, line_to_mark):
    """ Mark specific task as completed """

    read_f = open(file_name, 'r')
    lines = read_f.readlines()

    current_line = 1
    write_f = open(file_name, 'w')
    for ln in lines:
        if current_line == line_to_mark:
            write_f.write(ln[:-3] + " Yes")
        else:
            write_f.write(ln)

        current_line += 1


def change_user(file_name, name, task_to_change):
    """ Changes the username in task """

    read_f = open(file_name, "r")
    lines = read_f.readlines()

    current_line = 1
    changed_line = ""
    write_f = open(file_name, "w")

    for ln in lines:

        if current_line == task_to_change:
            file_content = ln.split(", ")
            file_content[0] = name

            for word in file_content:
                changed_line += word + "," + " "
            write_f.write(changed_line.strip(", "))

        else:
            write_f.write(ln)

        current_line += 1


def change_due_date(file_name, new_date, task_to_change):
    """ Changes the due date in task """

    read_f = open(file_name, "r")
    lines = read_f.readlines()

    current_line = 1
    changed_line = ""
    write_f = open(file_name, "w")

    for ln in lines:

        if current_line == task_to_change:
            file_content = ln.split(", ")
            file_content[4] = new_date

            for word in file_content:
                changed_line += word + "," + " "
            write_f.write(changed_line.strip(", "))

        else:
            write_f.write(ln)

        current_line += 1


def toggle_menu(main_menu):
    """ Shows / Hides the main menu """
    return not main_menu


def task_editing():
    """ Opens task editing menu """

    # Count number of lines in tasks.txt
    t_file = open('tasks.txt', 'r')
    task_file_length = len(t_file.readlines())

    # Ask user to enter input to return to the main menu or select a task
    while True:
        num_input = int(input("""Enter the number of task, to select it
Enter '-1' to return to the main menu
: """))
        print()

        # Return to the main menu
        if num_input == -1:
            toggle_menu(show_menu)
            break

        # If task with entered number presented in tasks.txt file
        # Show new menu with editing variants
        elif num_input <= task_file_length and num_input != 0:

            t_file.close()
            # Variants menu
            while True:
                variant = input(f"""Select what do you want to do with the task {num_input}:
m - Mark the task as complete
e - Edit the task
rt - To return to the previous menu
: """).lower()
                print()

                # Mark task as completed (No -> Yes)
                if variant == "m":
                    mark_task("tasks.txt", num_input)
                    print(f"Completeness status of the task {num_input} changed to 'Yes'")
                    print()
                    continue

                # Return to previous menu
                elif variant == "rt":
                    toggle_menu(show_menu)
                    break

                # Show editing menu
                elif variant == "e":
                    while True:
                        editing_variant = input(f"""Select what do you want to edit in the task {num_input}:
u - Change the username of the person to whom the task was assigned
d - Change the due date
rt - To return to the previous menu
: """).lower()
                        print()

                        # Change username in the task with entered number
                        if editing_variant == "u":
                            new_username = input(f"Enter new username for the task {num_input}: ")
                            change_user("tasks.txt", new_username, num_input)
                            print(f"Username in the task {num_input} changed to {new_username}")
                            print()
                            break

                        # Change due date in the task with entered number
                        elif editing_variant == "d":
                            new_due_date = input(f"Enter new due date for the task {num_input}: ")
                            change_due_date("tasks.txt", new_due_date, num_input)
                            print(f"Due date in the task {num_input} changed to {new_due_date}")
                            print()
                            break

                        # Return to previous menu
                        elif editing_variant == "rt":
                            break

                        else:
                            print("Invalid input!")
                            continue

                # Show error if input is invalid
                else:
                    print("Invalid input!")
                    continue

        else:
            print("No task with entered number.")
            continue


def task_report(tasks_total):
    """ Generates tasks report """

    tasks_f = open("tasks.txt", "r")

    # Initialize variables
    t_uncompleted = 0
    t_completed = 0
    t_overdue = 0

    # Count completed, uncompleted and overdue tasks
    for lines in tasks_f:
        f_content = lines.strip().split(", ")

        # Took dates from list
        current_date = f_content[3]
        due_date = f_content[4]
        current_month = int(current_date.split()[0])
        due_month = int(due_date.split()[0])

        if "No" in f_content and current_month > due_month:
            t_overdue += 1
        elif "No" in f_content:
            t_uncompleted += 1
        elif "Yes" in f_content:
            t_completed += 1

    tasks_f.close()

    percent_of_uncompleted = calculate_percentage(t_uncompleted, tasks_total)
    percent_of_overdue = calculate_percentage(t_overdue, tasks_total)

    # Add new report information
    t_overview = open("tasks_overview.txt", "a")

    t_overview.write(f"""
Total number of generated tasks:      {tasks_total}
Completed tasks:                      {t_completed}
Uncompleted tasks:                    {t_uncompleted}
Uncompleted overdue tasks overdue:    {t_overdue}
Percent of uncompleted tasks:         {percent_of_uncompleted}%
Percent of tasks that are overdue:    {percent_of_overdue}%""")

    t_overview.close()


def calculate_percentage(part, whole):
    """ Calculates percentage of part and whole numbers """

    percentage = round(100 * float(part) / float(whole))
    return str(percentage)


def user_report(users_list, user_index, tasks_total):
    """ Generates users report """

    task_f = open("tasks.txt", "r")

    # Initialize variables
    completed = 0
    uncompleted = 0
    overdue = 0

    # Loop over task.txt
    # Count user's completed, uncompleted and overdue tasks
    for lines in task_f:
        task_content = lines.strip().split(", ")

        # Took dates from list
        c_date = task_content[3]
        d_date = task_content[4]
        c_day = int(c_date.split()[0])
        d_day = int(d_date.split()[0])

        if users_list[user_index] == task_content[0] and task_content[5] == "No" and c_day > d_day:
            overdue += 1
        elif users_list[user_index] == task_content[0] and task_content[5] == "No":
            uncompleted += 1
        elif users_list[user_index] == task_content[0] and task_content[5] == "Yes":
            completed += 1
        else:
            continue

    assigned = completed + uncompleted + overdue

    assigned_percent = round((assigned / tasks_total) * 100)

    # Calculate percent of completed tasks
    if completed != 0:
        completed_percent = calculate_percentage(completed, assigned)
    else:
        completed_percent = 0

    # Calculate percent of uncompleted tasks
    if uncompleted != 0:
        uncompleted_percent = calculate_percentage(uncompleted, assigned)
    else:
        uncompleted_percent = 0

    # Calculate percent of overdue tasks
    if overdue != 0:
        overdue_percent = calculate_percentage(overdue, assigned)
    else:
        overdue_percent = 0

    # Add new report information
    u_overview = open("users_overview.txt", "a")

    u_overview.write(f"""
Name of user:                         {users_list[user_index]}
Total tasks assigned:                 {assigned_percent}%
Total completed tasks:                {completed_percent}%
Total uncompleted tasks:              {uncompleted_percent}%
Total uncompleted overdue tasks:      {overdue_percent}%
{'-' * 44}
""")

    u_overview.close()
    task_f.close()


def statistics(login):
    """ Shows statistics to admin """

    if login == "admin":

        t_overview = open('tasks_overview.txt', 'r')

        print(f"""
{'=' * 14} TASKS OVERVIEW {'=' * 14}""")

        # Loop over file and print the data
        t_overview_content = ""
        for t_line in t_overview:
            t_overview_content += t_line
        print(t_overview_content)

        t_overview.close()

        u_overview = open('users_overview.txt', 'r')

        print(f"""
{'=' * 14} USERS OVERVIEW {'=' * 14}""")

        # Loop over file and print the data
        u_overview_content = ""
        for u_line in u_overview:
            u_overview_content += u_line
        print(u_overview_content)

        t_overview.close()

    else:
        print("Only admin is allowed to see the statistics.")


# ===== login Section =====

user_login = log_in()

while True:

    # Presenting the menu to the user
    show_menu = True
    while show_menu:
        menu = input('''
Select one of the following Options below:
r - Register a new user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
s - Display statistics
e - Exit
: ''').lower()

        # Register a new user
        if menu == 'r':
            reg_user(user_login)

        # Add a new task
        elif menu == 'a':
            add_task()

        # View all tasks
        elif menu == 'va':
            view_all()

            # Close the main menu
            toggle_menu(show_menu)

            # Show the task editing menu
            task_editing()

        # Show task to logged user
        elif menu == 'vm':
            view_mine()

            # Close the main menu
            toggle_menu(show_menu)

            # Show the task editing menu
            task_editing()

        # Generate report
        elif menu == 'gr':

            users_file = open("user.txt", "r")

            # Initialize variables
            all_users_list = []
            users_total = 0

            # Loop over user.txt
            # Add usernames to list
            for counter, line in enumerate(users_file):
                users_total = counter + 1
                users_content = line.strip().split(", ")
                all_users_list.append(users_content[0])

            task_fl = open("tasks.txt", "r")
            tasks_count = len(task_fl.readlines())

            # Open the file and clean it from old report
            open("users_overview.txt", "w").close()

            index = 0
            while index < len(all_users_list):
                """ Generate users report """
                user_report(all_users_list, index, tasks_count)
                index += 1

            users_file.close()

            """ Generate tasks report """

            # Open the file and clean it from old report
            open("tasks_overview.txt", "w").close()

            task_report(tasks_count)

            print("""
The reports are generated and added to the files.
Admin can view them in the statistics""")

        # Show statistics to admin
        elif menu == 's':
            statistics(user_login)

        # Exit from program
        elif menu == 'e':
            print("Goodbye!")
            exit()

        else:
            print("You have made a wrong choice, Please Try again")
