""" this module provides a database connection """

from PySide6.QtWidgets import QMessageBox
from PySide6.QtSql import QSqlDatabase , QSqlQuery

def _creatContactTable() :
    """ creat the contact table in dataBase """
    creatTableQuery = QSqlQuery()
    return creatTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL
        )
        """
    )


def creatConnection(dataBaseName) :
    """ creat and open a dataBase connection """

    connection = QSqlDatabase.addDatabase('QSQLITE')
    connection.setDatabaseName(dataBaseName)

    if not connection.open() :
        QMessageBox.warning(
            None,
            'Contact',
            f'dataBase Error : {connection.lastError().text()}',
        )
        return False
    _creatContactTable()
    return True