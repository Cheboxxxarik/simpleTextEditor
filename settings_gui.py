from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QFileDialog, QMessageBox
import config, default_config


class SettingsGUI(QDialog):
    def __init__(self):
        super(SettingsGUI, self).__init__()
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('Настройки')
        # Выбор шрифта заголовка
        self.label_font_size_settings = QtWidgets.QLabel(self)
        self.label_font_size_settings.setGeometry(20, 20, 291, 31)
        self.label_font_size_settings.setText(' Размер шрифта заголовка:')
        self.set_label_font_size = QtWidgets.QLineEdit(self)
        self.set_label_font_size.setGeometry(170, 20, 113, 31)
        self.set_label_font_size.setText(f'{config.default_label_font_size}')
        # Выбор фонового цвета
        self.background_color_settings = QtWidgets.QLabel(self)
        self.background_color_settings.setGeometry(20, 70, 321, 31)
        self.background_color_settings.setText(' Фоновый цвет текстовых полей (rgb):')
        self.set_background_color = QtWidgets.QLineEdit(self)
        self.set_background_color.setGeometry(350, 70, 171, 31)
        self.set_background_color.setText(f'{config.default_background_color_rgb_code}')
        # Непрозрачность
        self.transparent_settings = QtWidgets.QLabel(self)
        self.transparent_settings.setGeometry(20, 120, 150, 31)
        self.transparent_settings.setText(' Непрозрачность: ')
        self.set_transparency = QtWidgets.QLineEdit(self)
        self.set_transparency.setGeometry(179, 120, 113, 31)
        self.set_transparency.setText(config.default_transparency)
        # Папка для сохранения текстовых документов по умолчанию
        self.default_folder_settings = QtWidgets.QLabel(self)
        self.default_folder_settings.setGeometry(20, 170, 201, 31)
        self.default_folder_settings.setText(' Папка по умолчанию:')
        self.set_default_folder = QtWidgets.QLabel(self)
        self.set_default_folder.setGeometry(230, 170, 491, 31)
        self.set_default_folder.setText(config.default_folder)
        self.select_default_folder = QtWidgets.QPushButton(self)
        self.select_default_folder.setGeometry(730, 170, 58, 28)
        self.select_default_folder.setText('Выбрать')
        self.select_default_folder.clicked.connect(self.select_folder)
        # Кнопка сохранения настроек
        self.save_settings = QtWidgets.QPushButton(self)
        self.save_settings.setGeometry(488, 560, 91, 28)
        self.save_settings.setText('Сохранить')
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