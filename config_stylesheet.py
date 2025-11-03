import config

line_editor_stylesheet = f'''
    QLineEdit {{
        font-family: {config.font_family};
        font-size: {config.label_font_size};
        border: 1px solid rgba(212, 212, 212, 0.8);
        border-radius: 20px;
        padding: 16px 20px;
        selection-background-color: rgba({config.accent_color}, 0.3);
        background-color: rgba({config.background_color_rgba_code});    
    }}
    QLineEdit:focus {{
        border: 2.25px solid rgba({config.border_color});
        padding: 13.75px 18.75px;
    }}
'''
settings_line_editor_stylesheet = f'''
    QLineEdit {{
        font-family: {config.font_family};
        font-size: {config.font_size};
        background-color: rgba({config.background_color_rgba_code});
        border-radius: 10px;
        padding-top: 5px;
        padding-left: 5px;
        padding-bottom: 5px;
        selection-background-color: rgba({config.accent_color}, 0.3);
    }}
    QLineEdit:focus {{
        border: 2.25px solid rgba({config.border_color});
        padding: 2.75px;
    }}
'''
text_editor_stylesheet = f'''
    QTextEdit {{
        font-family: {config.font_family};
        font-size: {config.font_size};
        border: 1px solid rgba(212, 212, 212, 0.7);
        border-radius: 20px;
        padding: 16px 20px;
        background: rgba({config.background_color_rgba_code});
    }}
    QTextEdit:focus {{
        border: 2.25px solid rgba({config.border_color});
        padding: 13.75px 18.75px;
    }}
'''
label_stylesheet = f'''
    QLabel {{
        font-family: {config.font_family};
        font-size: {config.font_size};
        background-color: rgba({config.background_color_rgba_code});
        border-radius: 10px;
        padding-top: 5px;
        padding-left: 5px;
        padding-bottom: 5px;
        selection-background-color: rgba({config.accent_color}, 0.3);
    }}
'''

menu_bar_stylesheet = f'''
    QMenuBar {{
        border: none;
        padding: 4px 8px;
        font-family: {config.font_family};
        font-size: 13px;
    }}
    
    QMenuBar::item {{
        padding: 6px 12px;
        border-radius: 6px;
        margin: 2px;
    }}
    
    QMenuBar::item:selected {{
        background-color: rgba({config.accent_color}, 0.15);
        color: rgb({config.accent_color});
    }}
    
    QMenuBar::item:pressed {{
        background-color: rgba({config.accent_color}, 0.25);
    }}

    QMenu {{
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 6px;
        font-family: {config.font_family};
        font-size: 13px;
    }}
    
    QMenu::item {{
        padding: 8px 16px;
        border-radius: 6px;
        margin: 2px 0;
    }}
    
    QMenu::item:selected {{
        background-color: rgba({config.accent_color}, 0.15);
        color: rgb({config.accent_color});
    }}
    
    QMenu::item:pressed {{
        background-color: rgba({config.accent_color}, 0.25);
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
        background-color: rgba({config.accent_color}, 0.8);
        border: 1px solid rgba({config.accent_color}, 0.9);
    }}
'''

button_stylesheet = f"""
    QPushButton {{
        font-family: {config.font_family};
        font-size: 12pt;
        font-weight: 500;
        background-color: rgb({config.accent_color});
        color: white;
        border: none;
        border-radius: 6px;
        padding: 8px;
    }}
    QPushButton:hover {{
        background-color: rgba({config.accent_color}, 0.8);
    }}
    QPushButton:pressed {{
        background-color: rgba({config.accent_color}, 0.6);
    }}
"""

message_box_stylesheet = f'''
    QMessageBox {{
        font-family: {config.font_family};
        min-width: 200px;
        max-width: 200px;
        min-height: 100px;
    }}

    QMessageBox QLabel {{
        font-family: {config.font_family};
        font-size: {config.font_size};
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
        font-family: {config.font_family};
        font-size: 11pt;
        font-weight: 500;
        background-color: rgb({config.accent_color});
        color: white;
        border-radius: 8px;
        padding: 6px 12px;
        min-width: 50px;
        margin: 3px;
    }}

    QMessageBox QPushButton:hover {{
        background-color: rgba({config.accent_color}, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }}

    QMessageBox QPushButton:pressed {{
        background-color: rgba({config.accent_color}, 0.6);
        padding: 7px 13px;
    }}

    QMessageBox QPushButton:focus {{
        border: 2px solid rgba({config.border_color});
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