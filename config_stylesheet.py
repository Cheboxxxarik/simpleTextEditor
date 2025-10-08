import config

line_editor_stylesheet = f'''
    QLineEdit {{
        font-family: {config.font_family};
        font-size: {config.label_font_size};
        background-color: rgba({config.background_color_rgba_code});
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 20px;
        padding: 16px 20px;
        selection-background-color: rgba(59, 130, 246, 0.3);
    }}
    QLineEdit:focus {{
        border: 2.25px solid rgba({config.border_color});
    }}
'''
label_stylesheet = f'''
    QLabel {{
        font-family: {config.font_family};
        font-size: {config.font_size};
        background-color: rgba({config.background_color_rgba_code});
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 10px;
        padding-top: 5px;
        padding-left: 5px;
        padding-bottom: 5px;
        selection-background-color: rgba(59, 130, 246, 0.3);
    }}
'''
settings_line_editor_stylesheet = f'''
    QLineEdit {{
        font-family: {config.font_family};
        font-size: {config.font_size};
        background-color: rgba({config.background_color_rgba_code});
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 10px;
        padding-top: 5px;
        padding-left: 5px;
        padding-bottom: 5px;
        selection-background-color: rgba(59, 130, 246, 0.3);
    }}
    QLineEdit:focus {{
        border: 2.25px solid rgba({config.border_color});
    }}
'''
text_editor_stylesheet = f'''
    QTextEdit {{
        font-family: {config.font_family};
        font-size: {config.font_size};
        background-color: rgba({config.background_color_rgba_code});
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 20px;
        padding: 16px 20px;
    }}
    QTextEdit:focus {{
        border: 2.25px solid rgba({config.border_color});
    }}
'''
button_stylesheet = """
            QPushButton {
                background: #eff6ff;
                color: #1d4ed8;
                border: 1px solid #dbeafe;
                padding: 14px 10px;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: #dbeafe;
                border: 1px solid #93c5fd;
            }
            QPushButton:pressed {
                background: #bfdbfe;
            }
        """