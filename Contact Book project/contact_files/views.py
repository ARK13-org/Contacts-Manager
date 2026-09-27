""" this module provides views to manage the contacts """

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView,
    QHBoxLayout, 
    QMainWindow, 
    QWidget,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QMessageBox,
    QLineEdit,
)
from .model import ContactModel

class Window(QMainWindow) :
    """ main window """

    def __init__(self , parent=None) :
        super().__init__(parent)
        self.setWindowTitle('ARK13 | Contacts')
        self.resize(550 , 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.contactModel = ContactModel()
        self.setupUI()

    def setupUI(self) :
        self.table = QTableView()
        self.table.setModel(self.contactModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        #creating buttons
        self.addButton = QPushButton('Add...')
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton('Delete')
        self.deleteButton.clicked.connect(self.deleteConcact)
        self.clearButton = QPushButton('Clear All')
        self.clearButton.clicked.connect(self.clearContacts)

        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)


    def openAddDialog(self) :
        dialog = AddDialogs(self)
        if dialog.exec() == QDialog.Accepted :
            self.contactModel.addContacts(dialog.data)
            self.table.resizeColumnsToContents()

    def deleteConcact(self) :
        row = self.table.currentIndex().row()
        if row < 0 :
            return

        massageBox = QMessageBox.warning(
            self,
            'Warning!!!',
            'do you want to remove the selected contact???',
            QMessageBox.Ok | QMessageBox.Cancel ,
        )
        if massageBox == QMessageBox.Ok :
            self.contactModel.deleteContact(row)

    def clearContacts(self) :
        messageBox = QMessageBox.warning(
            self,
            'Warning!!!',
            'do you want to remove all your contacts???' ,
            QMessageBox.Ok | QMessageBox.Cancel,
        )
        if messageBox == QMessageBox.Ok :
            self.contactModel.clearContacts()
    

class AddDialogs(QDialog) :
    """ Add contact Dialogs """

    def __init__(self , parent=None) :
        super().__init__(parent=parent)
        self.setWindowTitle('Add Contacts')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None
        self.setupUI()

    def setupUI(self) :
        """ setup the add contact dialog """

        self.nameField = QLineEdit()
        self.nameField.setObjectName('Name')
        self.jobField = QLineEdit()
        self.jobField.setObjectName('Job')
        self.emailField = QLineEdit()
        self.emailField.setObjectName('Email')

        layout = QFormLayout()
        layout.addRow('Name:', self.nameField)
        layout.addRow('Job:', self.jobField)
        layout.addRow('Email:', self.emailField)
        self.layout.addLayout(layout)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonBox)

    def accept(self) :
        """ accept the data provided in the dialog """
        self.data = []
        for field in (self.nameField , self.jobField , self.emailField) :
            if not field.text() :
                QMessageBox.critical(
                    self,
                    "ERROR" ,
                    f'you must provided a contact {field.objectName}'
                )
                self.data = None
                return

            self.data.append(field.text())
        super().accept()