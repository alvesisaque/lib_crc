from peewee import *


class CreditOperation(Model):
    # define os  atributos

    class Meta:
        database = database
        db_table = "usuarios"
class ImovelOperation(Model):
    # define os  atributos

    class Meta:
        database = database
        db_table = "usuarios"

class Operation(Model):

    class Meta:
        database = database
        db_table = "usuarios"