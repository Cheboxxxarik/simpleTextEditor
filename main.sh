#!/bin/bash
export QT_ENABLE_HIGHDPI_SCALING=1
QT_QPA_PLATFORM=gnome
source .venv/bin/activate
python3 main.py