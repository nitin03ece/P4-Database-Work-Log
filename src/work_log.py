import inputStr
import database
import entry


# This function takes details of a single entry and store it, 
# later to be logged.
def collect_new_entry(entry):
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
    entry.name = name
    entry.title = title
    entry.time_spent = time_spent
    entry.notes = notes


# Main function to start the work log program
def start(entry):
    while True:
        inputStr.clear_screen()
        print("WORK LOG")
        prompt = input(inputStr.prompt).strip().lower()
        if prompt == 'a':
            collect_new_entry(entry)
            entry.databaseWrite(entry)
        elif prompt == 'b':
            entry.search_old_entries()
        elif prompt == 'c':
            inputStr.clear_screen()
            print("Thank You for using the work log program!")
            print("Come again soon.")
            break


if __name__ == "__main__":
    entry = entry.Entry()
    database.db.connect()
    database.db.create_tables([database.Employee], safe=True)
    start(entry)
    database.db.close()
