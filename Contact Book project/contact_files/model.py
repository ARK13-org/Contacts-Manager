""" this module provides a model to manage contact tables """

from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlTableModel

class ContactModel :
    def __init__(self) :
        self.model = self._creatModel()

    @staticmethod
    def _creatModel():
        """ creat and seUp model """
        tableModel = QSqlTableModel()
        tableModel.setTable('contacts')
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ('ID' , 'Name' , 'Job' , 'Email')
        for columnIndex , header in enumerate(headers) :
            tableModel.setHeaderData(columnIndex , Qt.Horizontal , header)

        return tableModel


    def addContacts(self , data):
        """ add a contact to the dataBase """
        rows = self.model.rowCount()
        self.model.insertRows(rows , 1)
        for column , field in enumerate(data) :
            self.model.setData(self.model.index(rows , column + 1) , field)
        self.model.submitAll()
        self.model.select()

    def deleteContact(self , row) :
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    def clearContacts(self) :
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0 , self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()