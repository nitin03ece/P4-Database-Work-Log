"""
import database


def databaseWrite(employee):
    record = database.Employee.create(
        name=employee.name, 
        title=employee.title, 
        time_spent=employee.time_spent, 
        notes=employee.notes
    )
    return record
"""