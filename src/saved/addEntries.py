"""

import entry
import datetime
import inputStr
import write


# This function takes details of a single entry and store it, 
# later to be logged.
def add_new_entries():
    # Collect the 'Name' of the Employee
    inputStr.clear_screen()
    name = input(inputStr.employeeName).strip().lower()

    # Collect the 'Title' of the task
    inputStr.clear_screen()
    title = input(inputStr.taskTitle)

    # Collect the 'Time' of the task
    while True:
        inputStr.clear_screen()
        try:
            time_spent = round(int(input(inputStr.taskTime)))
        except ValueError as val2:
            value2 = str(val2).split(" ")
            print("Error: {} is not the time value ".format(value2[-1]))
            if "" == input("Press Enter to Try Again ").strip():
                pass
        else:
            break

    # Collect the 'Notes' of the task
    inputStr.clear_screen()
    notes = input(inputStr.taskNotes)

    inputStr.clear_screen()
    new_entry = entry.Entry(name, title, time_spent, notes)
    write.databaseWrite(new_entry)
    input("The entry has been added.\nPress enter to return to the menu ")
    return
"""