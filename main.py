import os, sys
from qtpy.QtWidgets import QApplication, QStyleFactory
from PyQt5 import QtWidgets
from qtpy.QtGui import QIcon

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from example_calculator.calc_window import CalculatorWindow

style = """
QMessageBox {
    color: black;
    background: #dfdfdf;    
}

QtWidgets {
    color: black;
    background: #dfdfdf;    
}

QDialog {
    color: black;
    background: #f2f2f2;
}

QLineEdit {
    color: black;    
    border-radius: 4px;   
    border:2px solid #3a3a3a;
    background: #f2f2f2;
}

QPushButton {
    color: black;    
    border-radius: 4px;   
    border: 2px solid #3a3a3a;
    background: #f2f2f2;
    padding-left: 0px;
    padding-right: 0px;
    selection-background-color: #dfdfdf;
    padding: 6px;
}
"""

########################################################################
# Удалив этот блок уберем проверку логина
########################################################################
s = ""


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setWindowTitle("Валидация")
        self.setStyleSheet(style)

        open_img_fa = "i64.ico"
        put = os.path.dirname(__file__)
        path_img_fa = f"{put}\\example_calculator\\nodes\\icons\\{open_img_fa}"
        print(path_img_fa)

        self.setWindowIcon(QIcon(path_img_fa))
        self.textName = QtWidgets.QLineEdit(self)
        self.textName.setStyleSheet(style)
        self.textPass = QtWidgets.QLineEdit(self)
        self.textPass.setStyleSheet(style)
        self.buttonLogin = QtWidgets.QPushButton("Войти", self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        self.buttonLogin.setStyleSheet(style)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

        try:
            path = f"X:\Инженерный Центр\УТПП\Барулин МА\log.txt"  # смотрим развод у матвеевой в папке
            with open(path) as file:
                self.s = file.read().splitlines()

        except:
            open_img_fa = "log.txt"
            put = os.getcwd()
            path_img_fa = f"{put}\\{open_img_fa}"
            with open(path_img_fa) as file:
                self.s = file.read().splitlines()

    def handleLogin(self):
        # print(self.s)
        if self.textName.text() == self.s[0] and self.textPass.text() == self.s[1]:
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self,
                "Ошибка",
                "<p style='color: black;'> Неправильный логин или пароль </p>",
            )


# class Window(QtWidgets.QMainWindow):
#     def __init__(self, parent=None):
#         super(Window, self).__init__(parent)
#         # self.ui = Ui_MainWindow()
#         # self.ui.setupUi(self)


########################################################################


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # ['Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion']
    login = Login()  # это вызов окна логина
    if login.exec_() == QtWidgets.QDialog.Accepted:  # это проверка пароля

        print(QStyleFactory.keys())
        # app.setStyle('Fusion')#['Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion']

        wnd = CalculatorWindow()
        wnd.show()

        sys.exit(app.exec_())
