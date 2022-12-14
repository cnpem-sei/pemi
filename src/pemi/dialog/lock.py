import pydrs
from PyQt5 import QtCore, QtWidgets, uic

from ..consts import LOCK_UI
from ..util import show_message


class PasswordDialog(QtWidgets.QDialog):
    lock_changed = QtCore.pyqtSignal()

    def __init__(self, parent: QtWidgets.QMainWindow):
        super().__init__(parent)
        uic.loadUi(LOCK_UI, self)
        self.parent = parent
        self.buttonBox.accepted.connect(self.unlock_udc)

    @QtCore.pyqtSlot()
    def unlock_udc(self):
        try:
            password = int(self.passwordEdit.text(), 10 if self.decRadio.isChecked() else 16)
            if self.parent.locked:
                self.parent.pydrs.unlock_udc(password)
            else:
                self.parent.pydrs.lock_udc(password)
        except (ValueError, pydrs.validation.SerialInvalidCmd):
            show_message("Error", "Invalid password")

        self.lock_changed.emit()
        self.close()
