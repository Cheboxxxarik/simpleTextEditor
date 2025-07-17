from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox
import config, default_config


class SettingsGUI(QDialog):
    def __init__(self):
        super(SettingsGUI, self).__init__()
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('Настройки')
        # Фоновая картинка
        self.wallpaper = QtWidgets.QLabel(self)
        self.wallpaper.setGeometry(0, 0, 800, 600)
        self.wallpaper.setText('')
        self.wallpaper.setPixmap(QtGui.QPixmap(config.default_wallpaper))
        self.wallpaper_settings = QtWidgets.QLabel(self)
        self.wallpaper_settings.setGeometry(20, 20, 170, 31)
        self.wallpaper_settings.setText(f' Фоновая картинка:')
        self.wallpaper_settings.setStyleSheet(f"font: {config.default_font_size} \"{config.default_font}\";\n"
                                       f"background-color: {config.default_background_color}")
        self.wallpaper_path = QtWidgets.QLabel(self)
        self.wallpaper_path.setGeometry(199, 20, 522, 31)
        self.wallpaper_path.setText(config.default_wallpaper)
        self.wallpaper_path.setStyleSheet(f"font: {config.default_font_size} \"{config.default_font}\";\n"
                                            f"background-color: {config.default_background_color};\n"
                                            f"padding-left: 3px")
        # Кнопка для выбора фоновой картинки
        self.select_image_button = QtWidgets.QPushButton(self)
        self.select_image_button.setGeometry(730, 23, 58, 28)
        self.select_image_button.setText('Выбрать')
        self.select_image_button.clicked.connect(self.select_image)
        # Выбор шрифта обычного текста
        self.font_settings = QtWidgets.QLabel(self)
        self.font_settings.setGeometry(20, 70, 81, 31)
        self.font_settings.setText(' Шрифт:')
        self.font_settings.setStyleSheet(f"font: {config.default_font_size} \"{config.default_font}\";\n"
                                            f"background-color: {config.default_background_color}")
        self.set_font = QtWidgets.QLineEdit(self)
        self.set_font.setGeometry(110, 70, 161, 31)
        self.set_font.setText(config.default_font)
        self.set_font.setStyleSheet(f"font: {config.default_font_size} \"{config.default_font}\";\n"
                                            f"background-color: {config.default_background_color};\n"
                                            "border: None")
        self.font_size_settings = QtWidgets.QLabel(self)
        self.font_size_settings.setGeometry(20, 120, 291, 31)
        self.font_size_settings.setStyleSheet(f"font: {config.default_font_size} \"{config.default_font}\";\n"
                                       f"background-color: {config.default_background_color}")
        self.font_size_settings.setText(' Размер шрифта обычного текста:')
        self.set_font_size = QtWidgets.QLineEdit(self)
        self.set_font_size.setGeometry(320, 120, 113, 31)
        self.set_font_size.setText(f'{config.default_font_size}')
        self.set_font_size.setStyleSheet(f"font: {config.default_font_size} \"{config.default_font}\";\n"
                                            f"background-color: {config.default_background_color};\n"
                                            "border: None")
        # Выбор шрифта заголовка
        self.label_font_size_settings = QtWidgets.QLabel(self)
        self.label_font_size_settings.setGeometry(20, 170, 291, 31)
        self.label_font_size_settings.setStyleSheet(f"font: {config.default_font_size} \"{config.default_font}\";\n"
                                              f"background-color: {config.default_background_color}")
        self.label_font_size_settings.setText(' Размер шрифта заголовка:')
        self.set_label_font_size = QtWidgets.QLineEdit(self)
        self.set_label_font_size.setGeometry(320, 170, 113, 31)
        self.set_label_font_size.setText(f'{config.default_label_font_size}')
        self.set_label_font_size.setStyleSheet(f"font: {config.default_font_size} \"{config.default_font}\";\n"
                                         f"background-color: {config.default_background_color};\n"
                                         "border: None")
        # Выбор фонового цвета
        self.background_color_settings = QtWidgets.QLabel(self)
        self.background_color_settings.setGeometry(20, 220, 321, 31)
        self.background_color_settings.setText(' Фоновый цвет текстовых полей (rgb):')
        self.background_color_settings.setStyleSheet(f"font: {config.default_font_size} \"{config.default_font}\";\n"
                                               f"background-color: {config.default_background_color};\n")
        self.set_background_color = QtWidgets.QLineEdit(self)
        self.set_background_color.setGeometry(350, 220, 171, 31)
        self.set_background_color.setText(f'{config.default_background_color_rgb_code}')
        self.set_background_color.setStyleSheet(f"font: {config.default_font_size} \"{config.default_font}\";\n"
                                                f"background-color: {config.default_background_color};\n"
                                                'border: None')
        # Непрозрачность
        self.transparent_settings = QtWidgets.QLabel(self)
        self.transparent_settings.setGeometry(20, 270, 150, 31)
        self.transparent_settings.setText(' Непрозрачность: ')
        self.transparent_settings.setStyleSheet(f"font: {config.default_font_size} \"{config.default_font}\";\n"
                                       f"background-color: {config.default_background_color};\n"
                                       "border: None")
        self.set_transparency = QtWidgets.QLineEdit(self)
        self.set_transparency.setGeometry(179, 270, 113, 31)
        self.set_transparency.setText(config.default_transparency)
        self.set_transparency.setStyleSheet(f"font: {config.default_font_size} \"{config.default_font}\";\n"
                                                f"background-color: {config.default_background_color};\n"
                                                "border: None")
        # Папка для сохранения текстовых документов по умолчанию
        self.default_folder_settings = QtWidgets.QLabel(self)
        self.default_folder_settings.setGeometry(20, 320, 201, 31)
        self.default_folder_settings.setText(' Папка по умолчанию:')
        self.default_folder_settings.setStyleSheet(f"font: {config.default_font_size} \"{config.default_font}\";\n"
                                                f"background-color: {config.default_background_color};\n"
                                                "border: None")
        self.set_default_folder = QtWidgets.QLabel(self)
        self.set_default_folder.setGeometry(230, 320, 491, 31)
        self.set_default_folder.setText(config.default_folder)
        self.set_default_folder.setStyleSheet(f"font: {config.default_font_size} \"{config.default_font}\";\n"
                                                   f"background-color: {config.default_background_color};\n"
                                                   "border: None;\n"
                                                    "padding-left: 3px")
        self.select_default_folder = QtWidgets.QPushButton(self)
        self.select_default_folder.setGeometry(730, 320, 58, 28)
        self.select_default_folder.setText('Выбрать')
        self.select_default_folder.clicked.connect(self.select_folder)
        # Кнопка сохранения настроек
        self.save_settings = QtWidgets.QPushButton(self)
        self.save_settings.setGeometry(488, 560, 91, 28)
        self.save_settings.setText('Сохранить')
        self.save_settings.setStyleSheet("QPushButton {\n"
                                            "background-color: #f0f0f0;\n"
                                            "border: 1.3px solid rgb(99, 146, 255);\n"
                                            "}\n"
                                        "QPushButton:hover {\n"
                                            "border: 1px solid rgb(99, 146, 255);\n"
                                            "background-color: rgb(217, 242, 252);\n"
                                            "}\n")
        self.save_settings.clicked.connect(self.save_changes)
        # Кнопка сброса настроек
        self.reset_settings = QtWidgets.QPushButton(self)
        self.reset_settings.setGeometry(588, 560, 100, 28)
        self.reset_settings.setText('Сброс настроек')
        self.reset_settings.clicked.connect(self.reset)
        # Кнопка отмены изменений
        self.cancel = QtWidgets.QPushButton(self)
        self.cancel.setGeometry(697, 560, 91, 28)
        self.cancel.setText('Отмена')
        self.cancel.clicked.connect(self.cancel_changes)

    def select_image(self):
        file_name = QFileDialog.getOpenFileName(self, 'Выбрать изображение', 'images',
                                                'Изображения (*jpg *jpeg *png)')[0]
        if file_name != '':
            self.wallpaper_path.setText(file_name)

    def select_folder(self):
        folder_name = QFileDialog.getExistingDirectory(self)
        if folder_name != '':
            self.set_default_folder.setText(folder_name)

    @staticmethod
    def information_window():
        info = QMessageBox()
        info.setWindowTitle('Настройки')
        info.setIcon(QMessageBox.Information)
        info.setText('Для применения изменений перезапустите приложение.')
        info.exec_()

    @staticmethod
    def warning_window():
        info = QMessageBox()
        info.setWindowTitle('Настройки')
        info.setIcon(QMessageBox.Warning)
        info.setText('Указанного(-ой) Вами файла/шрифта/папки не существует')
        info.exec_()

    def save_changes(self):
        try:
            with open('config.py', 'w') as configuration:
                changes = (f'default_wallpaper = "{self.wallpaper_path.text()}"\n',
                           f'default_font = "{self.set_font.text()}"\n'
                           f'default_folder = "{self.set_default_folder.text()}"\n')
                configuration.writelines(changes)
        except FileNotFoundError:
            try:
                with open('config.py', 'w') as configuration:
                    changes = (f'default_wallpaper = "{config.default_wallpaper}"\n',
                               f'default_font = "{config.default_font}"\n'
                               f'default_folder = "{config.default_folder}')
                    configuration.writelines(changes)
            except FileNotFoundError:
                SettingsGUI.warning_window()
        with open('config.py', 'a') as configuration:
            changes = (f'default_font_size = "{self.set_font_size.text()}"\n',
                        f'default_label_font_size = "{self.set_label_font_size.text()}"\n',
                        f'default_background_color_rgb_code = "{self.set_background_color.text()}"\n',
                        f'default_transparency = "{self.set_transparency.text()}"\n',
                       'default_background_color = f"rgba({default_background_color_rgb_code}, '
                       '{default_transparency})"')
            configuration.writelines(changes)
        SettingsGUI.information_window()

    def reset(self):
        try:
            with open('config.py', 'w') as configuration:
                changes = (f'default_wallpaper = "{default_config.default_wallpaper}"\n',
                           f'default_font = "{default_config.default_font}"\n')
                configuration.writelines(changes)
        except FileNotFoundError:
            try:
                with open('config.py', 'w') as configuration:
                    changes = (f'default_wallpaper = "{config.default_wallpaper}"\n',
                               f'default_font = "{config.default_font}"\n')
                    configuration.writelines(changes)
            except FileNotFoundError:
                SettingsGUI.warning_window()
        with open('config.py', 'a') as configuration:
            changes = (f'default_font_size = "{default_config.default_font_size}"\n',
                        f'default_label_font_size = "{default_config.default_label_font_size}"\n',
                        f'default_background_color_rgb_code = '
                        f'"{default_config.default_background_color_rgb_code}"\n',
                        f'default_transparency = "{default_config.default_transparency}"\n',
                       'default_background_color = f"rgba({default_background_color_rgb_code}, '
                       '{default_transparency})"')
            configuration.writelines(changes)

        self.wallpaper_path.setText(default_config.default_wallpaper)
        self.set_font.setText(default_config.default_font)
        self.set_font_size.setText(default_config.default_font_size)
        self.set_label_font_size.setText(default_config.default_label_font_size)
        self.set_background_color.setText(default_config.default_background_color_rgb_code)
        self.set_transparency.setText(default_config.default_transparency)

        SettingsGUI.information_window()

    def cancel_changes(self):
        self.close()