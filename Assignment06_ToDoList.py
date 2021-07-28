# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Hedy Khalatbari,07.27.2021,Added code to complete assignment 6
# ----------------------------------------------------------------------------- #

# Data ------------------------------------------------------------------------ #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # name of the data file
objFile = None                # object that represents a file
dicRow = {}                   # row of data; dictionary {Task,Priority}
lstTable = []                 # list of dicRow
strChoice = ""                # Captures the user option selection
strTask = ""                  # Captures the user task data
strPriority = ""              # Captures the user priority data
strStatus = ""                # Captures the status of processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :return: (list) of dictionary rows
        """
        list_of_rows = []  # local variable, list of dictionary rows
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            if "," in line:  # added this condition as was getting an error when text file empty
                task, priority = line.split(",")
                row = {"Task": task.strip(), "Priority": priority.strip()}
                list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds user input data (task, priority) to a list of dictionary rows

        :param task: (string) task we want to add:
        :param priority: (string) priority of task to add:
        :param list_of_rows: (list) of dictionary rows
        :return:(list) of dictionary rows
        """
        list_of_rows = list(list_of_rows) # declares list type
        task = task.strip()
        priority = priority.strip()
        row = {"Task":task.lower(), "Priority":priority.lower()}
        list_of_rows.append(row)
        return list_of_rows

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Removes task from list of dictionaries

        :param task: (string) task we want to remove:
        :param list_of_rows: (list) of dictionary rows
        :return: (list) of dictionary rows
        """
        task = task.strip() # task to be removed
        task = task.lower()
        list_of_rows_local = []   # local list to write the new rows to
        for row in list_of_rows:
            task_local = row["Task"]
            if task != task_local:   # remove the user selected task
                list_of_rows_local.append(row)
        list_of_rows.clear()  # clear contents
        list_of_rows = list_of_rows_local    # populate with current list
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Write data from a list of dictionary rows into a file

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) of dictionary rows:
        """
        file = open(file_name, "w")
        for row in list_of_rows:
            file.write(row["Task"] + ", " + row["Priority"] + "\n")
        file.close()
        # no return necessary as no changes made to table list


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options:
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Show Current To Do List
        6) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 6] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("**    Current tasks in the To Do List are:    **")
        counter = 1
        for row in list_of_rows:
            print(str(counter),") ",row["Task"]," (",row["Priority"], " )")
            counter += 1
        print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        choice = str(input(message))
        choice = choice.strip()
        choice = choice.lower()
        return choice

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Asks user to input new task and priority

        :return: (strings) task, priority
        """
        task = str(input("Enter task: "))
        priority = str(input("Enter priority: "))
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """ Asks user which task they would like to remove

        :return: (string) task
        """
        task = str(input("Enter task to remove: "))
        return task


# Main Body of Script  ------------------------------------------------------ #

objFile = open(strFileName, "a")   # I need to create a text file first if not present
objFile.close()

# Step 1 - When the program starts, Load data from ToDoFile.txt and print To Do List
lstTable = Processor.read_data_from_file(strFileName)  # read file data into list table
IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list of dictionary rows

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show menu and ask user to choose a menu option
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice == '1':  # Add a new Task
        strTask, strPriority = IO.input_new_task_and_priority()
        lstTable = Processor.add_data_to_list(strTask, strPriority, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        strTask = IO.input_task_to_remove()
        lstTable = Processor.remove_data_from_list(strTask, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.write_data_to_file(strFileName,lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            lstTable = Processor.read_data_from_file(strFileName)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Show current data in the list of dictionary rows
        IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list of dictionary rows

    elif strChoice == '6':  # Exit Program
        print("Goodbye!")
        break  # and Exit

    else:
        print("Please choose from menu options")
