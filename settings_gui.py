from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (QDialog, QFileDialog, QVBoxLayout, QHBoxLayout, QGridLayout, QMessageBox)
from PyQt6.QtGui import QIcon
import config, config_stylesheet, default_config


class SettingsGUI(QDialog):
    def __init__(self):
        super(SettingsGUI, self).__init__()
        # self.resize(800, 600)
        self.setWindowTitle('Настройки')
        # Добавление иконки приложения
        self.setWindowIcon(QIcon('simpleTextEditor.png'))
        self.main_layout = QVBoxLayout(self)
        self.grid_layout = QGridLayout()
        self.main_layout.addLayout(self.grid_layout)
        # Выбор семейства шрифтов
        self.font_family_settings = QtWidgets.QLabel(self)
        self.font_family_settings.setText('Шрифт:')
        self.font_family_settings.setStyleSheet(config_stylesheet.label_stylesheet)
        self.select_font_family = QtWidgets.QLineEdit(self)
        self.select_font_family.setText(config.font_family)
        self.select_font_family.setStyleSheet(config_stylesheet.settings_line_editor_stylesheet)
        # Выбор размера шрифта
        self.font_size_settings = QtWidgets.QLabel(self)
        self.font_size_settings.setText('Размер шрифта обычного текста:')
        self.font_size_settings.setStyleSheet(config_stylesheet.label_stylesheet)
        self.set_font_size = QtWidgets.QLineEdit(self)
        self.set_font_size.setText(config.font_size)
        self.set_font_size.setStyleSheet(config_stylesheet.settings_line_editor_stylesheet)
        # Выбор размера шрифта заголовка
        self.label_font_size_settings = QtWidgets.QLabel(self)
        self.label_font_size_settings.setText('Размер шрифта заголовка:')
        self.label_font_size_settings.setStyleSheet(config_stylesheet.label_stylesheet)
        self.set_label_font_size = QtWidgets.QLineEdit(self)
        self.set_label_font_size.setText(config.label_font_size)
        self.set_label_font_size.setStyleSheet(config_stylesheet.settings_line_editor_stylesheet)
        # Выбор фонового цвета
        self.background_color_settings = QtWidgets.QLabel(self)
        self.background_color_settings.setText('Фоновый цвет текстовых полей (rgba):')
        self.background_color_settings.setStyleSheet(config_stylesheet.label_stylesheet)
        self.set_background_color = QtWidgets.QLineEdit(self)
        self.set_background_color.setText(config.background_color_rgba_code)
        self.set_background_color.setStyleSheet(config_stylesheet.settings_line_editor_stylesheet)
        # Папка для сохранения текстовых документов по умолчанию
        self.default_folder_settings = QtWidgets.QLabel(self)
        self.default_folder_settings.setText('Папка по умолчанию:')
        self.default_folder_settings.setStyleSheet(config_stylesheet.label_stylesheet)
        self.default_diretory = QtWidgets.QLabel(self)
        self.default_diretory.setText(config.default_folder)
        self.default_diretory.setStyleSheet(config_stylesheet.label_stylesheet)
        self.select_default_folder = QtWidgets.QPushButton(self)
        self.select_default_folder.setText('Выбрать')
        self.select_default_folder.clicked.connect(self.select_folder)
        self.select_default_folder.setStyleSheet(config_stylesheet.button_stylesheet)
        # Настройки акцентного цвета
        self.accent_color = QtWidgets.QLabel(self)
        self.accent_color.setText('Акцентный цвет:')
        self.accent_color.setStyleSheet(config_stylesheet.label_stylesheet)
        self.choose_accent_color = QtWidgets.QLineEdit(self)
        self.choose_accent_color.setText(config.accent_colour)
        self.choose_accent_color.setStyleSheet(config_stylesheet.settings_line_editor_stylesheet)
        # Кнопка сохранения настроек
        self.save_settings = QtWidgets.QPushButton(self)
        self.save_settings.setText('Сохранить')
        self.save_settings.clicked.connect(self.save_changes)
        self.save_settings.setStyleSheet(config_stylesheet.button_stylesheet)
        # Кнопка сброса настроек
        self.reset_settings = QtWidgets.QPushButton(self)
        self.reset_settings.setText('Сброс настроек')
        self.reset_settings.clicked.connect(self.reset)
        self.reset_settings.setStyleSheet(config_stylesheet.button_stylesheet)
        # Кнопка отмены изменений
        self.cancel_changes = QtWidgets.QPushButton(self)
        self.cancel_changes.setText('Отмена')
        self.cancel_changes.clicked.connect(self.cancel)
        self.cancel_changes.setStyleSheet(config_stylesheet.button_stylesheet)

        self.grid_layout.addWidget(self.font_family_settings, 0, 0)
        self.grid_layout.addWidget(self.select_font_family, 0, 1)
        self.grid_layout.addWidget(self.font_size_settings, 1, 0)
        self.grid_layout.addWidget(self.set_font_size, 1, 1)
        self.grid_layout.addWidget(self.label_font_size_settings, 2, 0)
        self.grid_layout.addWidget(self.set_label_font_size, 2, 1)
        self.grid_layout.addWidget(self.background_color_settings, 3, 0)
        self.grid_layout.addWidget(self.set_background_color, 3, 1)
        self.grid_layout.addWidget(self.default_folder_settings, 4, 0)
        self.grid_layout.addWidget(self.default_diretory, 4, 1)
        self.grid_layout.addWidget(self.select_default_folder, 4, 2)
        self.grid_layout.addWidget(self.accent_color, 5, 0)
        self.grid_layout.addWidget(self.choose_accent_color, 5, 1)

        self.button_layout = QHBoxLayout()
        self.main_layout.addLayout(self.button_layout)
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.save_settings)
        self.button_layout.addWidget(self.reset_settings)
        self.button_layout.addWidget(self.cancel_changes)

    def select_folder(self):
        folder_name = QFileDialog.getExistingDirectory(self)
        if folder_name != '':
            self.default_diretory.setText(folder_name)

    @staticmethod
    def information_window():
        info = QMessageBox()
        info.setWindowTitle('Настройки')
        info.setIcon(QMessageBox.Icon.Information)
        info.setText('Для применения изменений перезапустите приложение.')
        info.exec()

    @staticmethod
    def warning_window():
        info = QMessageBox()
        info.setWindowTitle('Настройки')
        info.setIcon(QMessageBox.Icon.Warning)
        info.setText('Указанного(-ой) Вами файла/шрифта/папки не существует')
        info.exec()

    def save_changes(self):
        new_font_family = self.select_font_family.text()
        new_label_font_size = self.set_label_font_size.text()
        # new_font_size
        new_background_color = self.set_background_color.text()
        new_default_directory = self.default_diretory.text()
        new_accent_color = self.choose_accent_color.text()

        with open(config.py, 'w') as config:
            config.writelines('')

        SettingsGUI.information_window()

    def reset(self):
        SettingsGUI.information_window()

    def cancel(self):
        self.close()

if __name__ == '__main__':
    import sys
    application = QtWidgets.QApplication(sys.argv)
    settings_window = SettingsGUI()
    settings_window.show()
    sys.exit(application.exec())