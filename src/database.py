import peewee
import datetime


db = peewee.SqliteDatabase("output\employee.db")


class Employee(peewee.Model):
    name = peewee.CharField(max_length=255)
    title = peewee.CharField(max_length=255)
    time_spent = peewee.IntegerField()
    notes = peewee.TextField()
    date = peewee.DateField(default=datetime.datetime.now().date)

    class Meta:
        database = db
