import os


prompt = """What would you like to do?
a) Add new entry
b) Search in existing entries
c) Quit Program
> """

employeeName = """Name of the employee: """

taskTitle = "Title of the task: "

taskTime = "Time spent(rounded minutes): "

taskNotes = "Notes (Optional, you can leave this empty): "

searchEntry = """Do you want to search by:
a) find by date
b) find by date range
c) find by employee
d) find by time spent
e) find by search term
f) Return to menu
> """

find_by_date = """Search by Exact Date
Enter the date
Please use DD/MM/YYYY: """

search_by_date_range_start = """Search by Range of Dates
Enter the start date(DD/MM/YYYY): """

search_by_date_range_end = """Enter the end date(DD/MM/YYYY): """

find_by_employee_name = """Enter the Employee name: """

search_by_date_option = """[N]ext, [P]revious, [E]dit, [D]elete, [R]eturn to search menu
> """

find_by_timeSpent = """Search by time spent: """

find_by_exactSearch = ""

edit_data = """\nWhat would you like to edit?
a) Employee Name
b) Employee Task Title
c) Time Spent on the task
d) Notes provide for the task
e) exit
> """

datePrompt = """~ Edit Employee Name ~
Enter Correct Name: """

titlePrompt = """~ Edit Title ~
Enter Correct Title: """

timePrompt = """~ Edit Time Spent ~
Enter Correct Time Spent: """

notesPrompt = """~ Edit Notes ~
Enter Correct Notes: """


def clear_screen():
    # os.system("cls" if os.name == "nt" else "clear")
    if os.name == 'nt':
        os.system("cls")
    else:
        os.name("clear")
    pass
