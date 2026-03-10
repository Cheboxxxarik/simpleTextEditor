"""
config.stylesheet.py

GUI theme configuration.

Содержит цветовые схемы, стили и константы интерфейса
для использования в PyQt-приложении.
"""

from PyQt6.QtGui import QPalette, QColor
import json
import config, resources.resources_rc

def theme_applier(app):
    palette = QPalette()
    
    theme_colors = config.THEME_COLORS
    # Основные цвета
    window_color = QColor(theme_colors.get('window_color'))        # Фон окон
    window_text_color = QColor(theme_colors.get('window_text_color'))
    text_color = QColor(theme_colors.get('text_color')) # Основной текст
    button_text_color = QColor(theme_colors.get('button_text_color'))         # Текст кнопок

    # Дополнительные цвета
    placeholder_color = QColor(theme_colors.get('placeholder_color'))   # Цвет плейсхолдера
    # Цвета для состояний (disabled)
    disabled_window_color = QColor(theme_colors.get('disabled_window_color')) # Цвет окна
    disabled_text_color = QColor(theme_colors.get('disabled_text_color')) # Цвет текста
    disabled_highlight_color = QColor(theme_colors.get('disabled_highlight_color')) # Цвет выделения
    disabled_highlighted_text_color = QColor(theme_colors.get('disabled_highlighted_text_color')) # Цвет выделенного текста
    
    # === Установка цветов в палитру ===
    
    # Активные элементы
    palette.setColor(QPalette.ColorRole.Window, window_color)
    palette.setColor(QPalette.ColorRole.WindowText, window_text_color)
    palette.setColor(QPalette.ColorRole.Text, text_color)
    palette.setColor(QPalette.ColorRole.ButtonText, button_text_color)
        
    # Дополнительные цвета
    palette.setColor(QPalette.ColorRole.PlaceholderText, placeholder_color)
        
    # Цвета для состояний (disabled)
    palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, disabled_window_color)
    palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, disabled_text_color)
    palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, disabled_highlight_color)
    palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, disabled_highlighted_text_color)
    
    app.setPalette(palette)

# Поле для заголовка
LINE_EDITOR_STYLESHEET = f'''
    QLineEdit {{
        font-family: {config.FONT_FAMILY};
        font-size: {config.LABEL_FONT_SIZE};
        font-weight: 600;
        border: 1px solid {config.BORDER_COLOR};
        border-radius: 20px;
        padding: 16px 20px;
        selection-background-color: rgb({config.ACCENT_COLOR});
        background-color: {config.BACKGROUND_COLOR};    
    }}
    QLineEdit:hover {{
        border: 1px solid rgb({config.ACCENT_COLOR});
    }}
    QLineEdit:focus {{
        border: 2.25px solid rgb({config.ACCENT_COLOR});
        padding: 13.75px 18.75px;
    }}
'''
# Поля для ввода настроек
SETTINGS_LINE_EDITOR_STYLESHEET = f'''
    QLineEdit {{
        font-family: {config.FONT_FAMILY};
        font-size: {config.FONT_SIZE};
        background-color: {config.BACKGROUND_COLOR};
        border: 1px solid {config.BORDER_COLOR};
        border-radius: 10px;
        padding-top: 5px;
        padding-left: 5px;
        padding-bottom: 5px;
        selection-background-color: rgb({config.ACCENT_COLOR});
    }}
    QLineEdit:hover {{
        border: 1px solid rgb({config.ACCENT_COLOR});
    }}
    QLineEdit:focus {{
        border: 2.25px solid rgb({config.ACCENT_COLOR});
        padding: 2.75px;
    }}
'''
# Поля для ввода текста
TEXT_EDITOR_STYLESHEET = f'''
    QTextEdit {{
        font-family: {config.FONT_FAMILY};
        font-size: {config.FONT_SIZE};
        border: 1px solid {config.BORDER_COLOR};
        border-radius: 20px;
        padding: 16px 20px;
        background: {config.BACKGROUND_COLOR};
        selection-background-color: rgb({config.ACCENT_COLOR});
    }}
    QTextEdit:hover {{
        border: 1px solid rgb({config.ACCENT_COLOR});
    }}
    QTextEdit:focus {{
        border: 2.25px solid rgb({config.ACCENT_COLOR});
        padding: 13.75px 18.75px;
    }}
'''
# Стиль для текста
LABEL_STYLESHEET = f'''
    QLabel {{
        font-family: {config.FONT_FAMILY};
        font-size: {config.FONT_SIZE};
        background-color: {config.BACKGROUND_COLOR};
        border-radius: 10px;
        padding-top: 5px;
        padding-left: 5px;
        padding-bottom: 5px;
        selection-background-color: rgb({config.ACCENT_COLOR});
    }}
'''
# Меню-бар
MENU_BAR_STYLESHEET = f'''
    QMenuBar {{
        border: none;
        padding: 4px 8px;
        font-family: {config.FONT_FAMILY};
        font-size: 13px;
    }}
    
    QMenuBar::item {{
        padding: 6px 12px;
        border-radius: 8px;
        margin: 2px;
    }}
    
    QMenuBar::item:selected {{
        background-color: {config.BACKGROUND_COLOR};
        color: rgb({config.ACCENT_COLOR});
    }}
    
    QMenuBar::item:pressed {{
        background-color: {config.BACKGROUND_COLOR};
    }}

    QMenu {{
        background-color: {config.WINDOW_COLOR};
        padding: 6px;
        font-family: {config.FONT_FAMILY};
        font-size: 13px;
    }}
    
    QMenu::item {{
        outline: none;
        padding: 8px 16px;
        border-radius: 8px;
        margin: 2px 0;
    }}
    
    QMenu::item:selected {{
        background-color: {config.BACKGROUND_COLOR};
        color: rgb({config.ACCENT_COLOR});
    }}
    
    /* Индикаторы (галочки) */
    QMenu::indicator {{
        width: 14px;
        height: 14px;
        border-radius: 3px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        margin-right: 8px;
    }}
    
    QMenu::indicator:checked {{
        background-color: rgb({config.ACCENT_COLOR});
        border: 1px solid rgb({config.ACCENT_COLOR});
    }}
'''
# Стиль для кнопок
BUTTON_STYLESHEET = f"""
    QPushButton {{
        font-family: {config.FONT_FAMILY};
        font-size: 12pt;
        font-weight: 500;
        background-color: rgb({config.ACCENT_COLOR});
        color: white;
        border: none;
        border-radius: 6px;
        padding: 8px;
    }}
    QPushButton:hover {{
        background-color: rgba({config.ACCENT_COLOR}, 0.8);
    }}
    QPushButton:pressed {{
        background-color: rgba({config.ACCENT_COLOR}, 0.6);
    }}
"""
# Стиль для выпадающих списков
COMBO_BOX_STYLESHEET = f'''
    QComboBox {{
        font-family: {config.FONT_FAMILY};
        font-size: {config.FONT_SIZE};
        background-color: {config.BACKGROUND_COLOR};
        border: 1px solid {config.BORDER_COLOR};
        border-radius: 10px;
        padding-top: 5px;
        padding-left: 5px;
        padding-right: 30px; /* Место для стрелки */
        padding-bottom: 5px;
        min-width: 120px;
    }}
    
    QComboBox:hover {{
        border: 1px solid rgb({config.ACCENT_COLOR});
    }}
    
    QComboBox:focus {{
        border: 2px solid rgb({config.ACCENT_COLOR});
    }}
    
    QComboBox:on {{
        background-color: {config.BACKGROUND_COLOR};
        border-radius: 10px;
    }}
    
    /* Стиль для выпадающего списка */
    QComboBox QAbstractItemView {{
        background-color: {config.BACKGROUND_COLOR};
        padding: 6px; 
        outline: none;
        selection-background-color: rgb({config.ACCENT_COLOR}); 
        selection-color: rgb({config.ACCENT_COLOR});
    }}
    
    QComboBox QAbstractItemView::item:hover {{
        background-color: rgba(255, 255, 255, 0.3);
    }}

    QComboBox QAbstractItemView::item {{
        padding: 8px 12px;
        border-radius: 6px;
        margin: 2px;
    }}

    /* Стиль для стрелки */
    QComboBox::drop-down {{
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 25px;
        border-left: 1px solid rgba(255, 255, 255, 0.2);
        border-top-right-radius: 9px;
        border-bottom-right-radius: 9px;
        border: none;
    }}
    
    QComboBox::down-arrow {{
        image: url(:/images/down_arrow.svg);
        color: rgba(148, 147, 146, 0.5);
        width: 12px;
        height: 12px;
        margin-left: 8px;
        margin-right: 8px;
    }}

    /* Стиль для неактивного состояния */
    QComboBox:disabled {{
        color: rgba(255, 255, 255, 0.4);
        background-color: {config.BACKGROUND_COLOR};
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}
    
    QComboBox::down-arrow:disabled {{
        border-top: 5px solid rgba(255, 255, 255, 0.3);
    }}
'''
# Стиль для всплывающих окон
MESSAGE_BOX_STYLESHEET = f'''
    QMessageBox {{
        font-family: {config.FONT_FAMILY};
        min-width: 200px;
        max-width: 200px;
        min-height: 100px;
    }}

    QMessageBox QLabel {{
        font-family: {config.FONT_FAMILY};
        font-size: {config.FONT_SIZE};
        background-color: transparent;
        border: none;
        padding: 8px;
    }}

    QMessageBox QLabel#qt_msgbox_label {{
        /* Основной текст сообщения */
        font-size: 14px;
        font-weight: bold;
        padding: 10px 12px 5px 12px;
    }}

    QMessageBox QPushButton {{
        font-family: {config.FONT_FAMILY};
        font-size: 11pt;
        font-weight: 500;
        background-color: rgb({config.ACCENT_COLOR});
        color: white;
        border-radius: 8px;
        padding: 6px 12px;
        min-width: 50px;
        margin: 3px;
    }}

    QMessageBox QPushButton:hover {{
        background-color: rgb({config.ACCENT_COLOR});
        border: 1px solid rgba(255, 255, 255, 0.3);
    }}

    QMessageBox QPushButton:pressed {{
        background-color: rgb({config.ACCENT_COLOR});
        padding: 7px 13px;
    }}

    QMessageBox QPushButton:focus {{
        border: 2px solid rgb({config.ACCENT_COLOR});
        outline: none;
    }}

    /* Увеличиваем иконку */
    QMessageBox QLabel#qt_msgboxex_icon_label {{
        background-color: transparent;
        border: none;
        padding: 15px;
    }}

    /* Область с кнопками - делаем компактнее */
    QMessageBox QDialogButtonBox {{
        background-color: transparent;
        border: none;
        padding: 8px 12px 12px 12px;
    }}
'''