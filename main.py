from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (QApplication, QMainWindow, QMenuBar, 
                             QMenu, QVBoxLayout, QHBoxLayout)
from PyQt6.QtGui import QIcon
import config_stylesheet, functionality


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('simpleTextEditor')
        self.resize(800, 600)
        # Создание центрального виджета
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        # Добавление иконки приложения
        self.setWindowIcon(QIcon('simpleTextEditor.ico'))
        # Создание основного слоя
        self.main_layout = QVBoxLayout(central_widget)
        self.main_layout.setSpacing(15)
        self.main_layout.setContentsMargins(20, 20, 20, 20) 
        # Создание слоя, на котором будут находиться виджеты для работы с текстом
        self.text_layout = QVBoxLayout()
        self.main_layout.addLayout(self.text_layout)
        # Поле для названия текста
        self.text_title = QtWidgets.QLineEdit(self)
        self.text_title.setText('.txt')
        self.text_title.setCursorPosition(0)
        self.text_title.setStyleSheet(config_stylesheet.line_editor_stylesheet)
        self.text_title.setMinimumHeight(50)
        # Поле для ввода текста
        self.text_editor = QtWidgets.QTextEdit(self)
        self.text_editor.setAutoFillBackground(False)
        self.text_editor.setStyleSheet(config_stylesheet.text_editor_stylesheet)
        # Кнопка для сохранения текста
        self.save_button = QtWidgets.QPushButton(self)
        self.save_button.setText('Сохранить')
        self.save_button.setMaximumWidth(100)
        self.save_button.clicked.connect(lambda: functionality.save_file(self))
        self.save_button.setStyleSheet(config_stylesheet.button_stylesheet)
        # Добавление виджетов
        self.text_layout.addWidget(self.text_title)
        self.text_layout.addWidget(self.text_editor) 
        # Создание слоя для кнопок
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # Добавляем растягивающее пространство слева
        button_layout.addWidget(self.save_button)
        # Добавление слоя для кнопок
        self.text_layout.addLayout(button_layout)
        # Создание меню-бара
        self.menu_bar = QMenuBar()
        self.setMenuBar(self.menu_bar)
        # Создание меню-бара
        file_menu = QMenu('&Файл', self)
        self.menu_bar.addMenu(file_menu)
        file_menu.addAction('Открыть', lambda: functionality.open_file(self))
        file_menu.addAction('Сохранить', lambda: functionality.save_file(self))
        file_menu.addAction('Сохранить как', lambda: functionality.save_file_as(self))


# Запуск приложения
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())