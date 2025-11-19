import config as config

# Поле для заголовка
TITLE_EDITOR_STYLESHEET = f'''
    QLineEdit {{
        font-family: {config.FONT_FAMILY};
        font-size: {config.LABEL_FONT_SIZE};
        border: 1px solid rgba(212, 212, 212, 0.8);
        border-radius: 20px;
        padding: 16px 20px;
        selection-background-color: rgba({config.ACCENT_COLOR}, 0.3);
        background-color: rgba({config.BACKGROUND_COLOR_RGBA_CODE});    
    }}
    QLineEdit:focus {{
        border: 2.25px solid rgba({config.BORDER_COLOR});
        padding: 13.75px 18.75px;
    }}
'''
# Поля для ввода настроек
SETTINGS_LINE_EDITOR_STYLESHEET = f'''
    QLineEdit {{
        font-family: {config.FONT_FAMILY};
        font-size: {config.FONT_SIZE};
        background-color: rgba({config.BACKGROUND_COLOR_RGBA_CODE});
        border-radius: 10px;
        padding-top: 5px;
        padding-left: 5px;
        padding-bottom: 5px;
        selection-background-color: rgba({config.ACCENT_COLOR}, 0.3);
    }}
    QLineEdit:focus {{
        border: 2.25px solid rgba({config.BORDER_COLOR});
        padding: 2.75px;
    }}
'''
# Поля для ввода текста
TEXT_EDITOR_STYLESHEET = f'''
    QTextEdit {{
        font-family: {config.FONT_FAMILY};
        font-size: {config.FONT_SIZE};
        border: 1px solid rgba(212, 212, 212, 0.7);
        border-radius: 20px;
        padding: 16px 20px;
        background: rgba({config.BACKGROUND_COLOR_RGBA_CODE});
    }}
    QTextEdit:focus {{
        border: 2.25px solid rgba({config.BORDER_COLOR});
        padding: 13.75px 18.75px;
    }}
'''
# Стиль для текста
LABEL_STYLESHEET = f'''
    QLabel {{
        font-family: {config.FONT_FAMILY};
        font-size: {config.FONT_SIZE};
        background-color: rgba({config.BACKGROUND_COLOR_RGBA_CODE});
        border-radius: 10px;
        padding-top: 5px;
        padding-left: 5px;
        padding-bottom: 5px;
        selection-background-color: rgba({config.ACCENT_COLOR}, 0.3);
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
        border-radius: 6px;
        margin: 2px;
    }}
    
    QMenuBar::item:selected {{
        background-color: rgba({config.ACCENT_COLOR}, 0.15);
        color: rgb({config.ACCENT_COLOR});
    }}
    
    QMenuBar::item:pressed {{
        background-color: rgba({config.ACCENT_COLOR}, 0.25);
    }}

    QMenu {{
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 6px;
        font-family: {config.FONT_FAMILY};
        font-size: 13px;
    }}
    
    QMenu::item {{
        padding: 8px 16px;
        border-radius: 6px;
        margin: 2px 0;
    }}
    
    QMenu::item:selected {{
        background-color: rgba({config.ACCENT_COLOR}, 0.15);
        color: rgb({config.ACCENT_COLOR});
    }}
    
    QMenu::item:pressed {{
        background-color: rgba({config.ACCENT_COLOR}, 0.25);
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
        background-color: rgba({config.ACCENT_COLOR}, 0.8);
        border: 1px solid rgba({config.ACCENT_COLOR}, 0.9);
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
        background-color: rgba({config.ACCENT_COLOR}, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }}

    QMessageBox QPushButton:pressed {{
        background-color: rgba({config.ACCENT_COLOR}, 0.6);
        padding: 7px 13px;
    }}

    QMessageBox QPushButton:focus {{
        border: 2px solid rgba({config.BORDER_COLOR});
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