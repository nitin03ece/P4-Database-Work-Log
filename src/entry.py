import datetime
import inputStr
import database
import copy
import re


class Entry:
    def __init__(self, name="", title="", time_spent=0, notes=""):
        self.name = name
        self.title = title
        self.time_spent = time_spent
        self.notes = notes

    def __eq__(self, other):
        return type(self) == type(other)

    # Write to the database
    def databaseWrite(self, employee):
        database.Employee.create(
            name=employee.name, 
            title=employee.title, 
            time_spent=employee.time_spent, 
            notes=employee.notes
        )
        input("The entry has been added.\nPress enter to return to the menu ")

    # Main function for searching the old entries.
    def search_old_entries(self):
        while True:
            inputStr.clear_screen()
            prompt = input(inputStr.searchEntry).strip().lower()
            if prompt == 'a':
                inputStr.clear_screen()
                self.find_by_date()
            
            if prompt == 'b':
                inputStr.clear_screen()
                self.find_by_date_range()

            elif prompt == 'c':
                inputStr.clear_screen()
                self.find_by_employee_name()

            elif prompt == 'd':
                inputStr.clear_screen()
                self.find_by_timeSpent()

            elif prompt == 'e':
                inputStr.clear_screen()
                self.find_by_exactSearch()

            elif prompt == 'f':
                return

    # For displaying current log on the screen
    def display_log(self, item):
        inputStr.clear_screen()
        print("Log Date: " + str(item.date) + ",\n")
        print("Employee Name: " + item.name + ",")
        print("Task Title: " + item.title + ",")
        print("Time Spent: " + str(item.time_spent) + " minutes,")
        print("Notes: " + item.notes + ".")

    # The function displays various log entries matching the input
    # provide by the user. Also provides option to navigate through
    # the different log along with edit and delete option.
    def __main_Search(self, list_value):
        index = 0
        prompt_option = ""
        list_value = list(list_value)
        while True:
            if len(list_value):
                data = list_value[index]
                self.display_log(data)
                print("\nResult " +
                    str(list_value.index(data)+1) +
                    " of " + str(len(list_value)) +
                    "\n")

                prompt_option = input(inputStr.search_by_date_option).strip().lower()
                if prompt_option == 'n':
                    index += 1
                    if index >= len(list_value):
                        index = 0
                elif prompt_option == 'p':
                    index -= 1
                    if index < 0:
                        index = len(list_value)-1
                elif prompt_option == 'e':
                    edit = self.__delete_edit(data, 'edit')
                    if edit == 'exit':
                        return "exit"
                    print("Editing Complete!")
                    if input("Press Enter to go back ").strip() == "":
                        return "edit"
                elif prompt_option == 'd':
                    self.__delete_edit(data, 'delete')
                    print("Successfully deleted!")
                    if input("Press Enter to go back ").strip() == "":
                        return "delete"
                elif prompt_option == 'r':
                    return "exit"
                else:
                    pass
            else:
                input("No logs found.\nPress enter to continue ")
                break

    # This function edit or delete a specific record.
    def __delete_edit(self, data, option):
        #temp = copy.copy(data)
        if option == 'delete':
            data.delete_instance()
        elif option == 'edit':
            flag = True
            while flag:
                self.display_log(data)
                prompt = input(inputStr.edit_data)
                if prompt == 'a':
                    namePrompt = input(inputStr.datePrompt)
                    data.name = namePrompt
                    flag = False

                elif prompt == 'b':
                    titlePrompt = input(inputStr.titlePrompt)
                    data.title = titlePrompt
                    flag = False

                elif prompt == 'c':
                    timePrompt = input(inputStr.timePrompt)
                    data.time_spent = timePrompt
                    flag = False

                elif prompt == 'd':
                    notesPrompt = input(inputStr.notesPrompt)
                    data.notes = notesPrompt
                    flag = False

                elif prompt == 'e':
                    flag = False
                    return "exit"

            data.save()

    # This Function takes the date as an input and 
    # provides the log(s) relevant to the date provided
    def find_by_date(self):
        while True:
            inputStr.clear_screen()
            try:
                prompt = str(datetime.datetime.strptime(input(
                    inputStr.find_by_date),
                    "%d/%m/%Y").date())
            except ValueError as val:
                value = str(val).split(" ")
                print("Error: {} is not a valid date".format(value[2]))
                if "" == input("Press Enter to Try Again ").strip():
                    pass
            else:
                rows = database.Employee.select().where(database.Employee.date == prompt)
                option = self.__main_Search(rows)
                if option == 'exit':
                    return
                elif option == 'edit':
                    return
                elif option == 'delete':
                    return

    # This Function takes the start date and end date as an input and 
    # provides the log(s) relevant to the date range provided
    def find_by_date_range(self):
        while True:
            inputStr.clear_screen()
            try:
                start_date = datetime.datetime.strptime(input(
                    inputStr.search_by_date_range_start),
                    "%d/%m/%Y").date()
                end_date = datetime.datetime.strptime(input(
                    inputStr.search_by_date_range_end),
                    "%d/%m/%Y").date()
            except ValueError as val:
                value = str(val).split(" ")
                print("Error: {} is not a valid date".format(value[2]))
                if "" == input("Press Enter to Try Again ").strip():
                    pass
            else:
                rows = database.Employee.select().where(
                    database.Employee.date >= start_date |
                    database.Employee.date <= end_date
                )
                option = self.__main_Search(rows)
                if option == 'exit':
                    return
                elif option == 'edit':
                    return
                elif option == 'delete':
                    return

    # This Function takes the start date and end date as an input and 
    # provides the log(s) relevant to the date range provided
    def find_by_employee_name(self):
        while True:
            inputStr.clear_screen()
            employeeName = input(inputStr.find_by_employee_name).strip().lower()
            list_value = database.Employee.select().where(database.Employee.name == employeeName)
            option = self.__main_Search(list_value)
            if option == 'exit':
                return
            elif option == 'edit':
                return
            elif option == 'delete':
                return

    # This Function takes the string and provide the log with matched string
    def find_by_exactSearch(self):
        inputStr.clear_screen()
        prompt = input(inputStr.find_by_exactSearch).strip().lower()
        list_value = database.Employee.select().where(
            database.Employee.name.contains(prompt)|
            database.Employee.notes.contains(prompt)
        )

        option = self.__main_Search(list_value)
        if option == 'exit':
            return
        elif option == 'edit':
            return
        elif option == 'delete':
            return

    # This Function takes the regex string and provide the log with matched string
    def find_by_timeSpent(self):
        while True:
            inputStr.clear_screen()
            try:
                prompt = int(input(inputStr.find_by_timeSpent).strip().lower())
            except ValueError:
                input("Please provide a number as an input.\nPress Enter to try again ")
            else:
                list_value = database.Employee.select().where(database.Employee.time_spent == prompt)
                option = self.__main_Search(list_value)
                if option == 'exit':
                    return
                elif option == 'edit':
                    return
                elif option == 'delete':
                    return
