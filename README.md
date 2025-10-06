# simpleTextEditor

**simpleTextEditor** - это кроссплатформенный редактор .txt-файлов, написанный на языке программированиия Python с помощью библиотеки PyQt6.

## Установка и запуск
### 1-й способ
1. Скачайте и установите шрифт [Adwaita Sans](https://gitlab.gnome.org/GNOME/adwaita-fonts)
2. Установите [Python](https://www.python.org).
3. Установите [Git](https://git-scm.com/downloads).
4. Склонируйте репозиторий с помощью команды `git clone https://github.com/Cheboxxxarik/simpleTextEditor`.
5. Откройте папку, куда вы склонировали репозиторий, в терминале.
6. Создайте виртуальное окружение Python с помощью команды ```python -m venv .venv```.
7. Активируйте виртуальное окружение.  
   **На Windows**: `.venv/Scripts/activate` (Если при выполнении команды выводится ошибка, попробуйте открыть PowerShell от имени администратора и выполнить команду `Set-ExecutionPolicy Bypass`, а затем снова попробуйте активировать виртуальное окружение)  
   **На Linux**: `source .venv/bin/activate`
8. Установите библиотеку PyQt6 с помощью команды `pip install pyqt6` или `pip3 install pyqt6`.
9. Запустите программу.  
   На Windows: `python main.py`  
   На Linux и Mac: `python3 main.py`
### 2-й способ (Для Windows)
1. Установите шрифт [Adwaita Sans](https://gitlab.gnome.org/GNOME/adwaita-fonts)
2. Перейдите на вкладку Releases
3. Скачайте .zip-архив "simpleTextEditor (Для Windows).zip" и распакуйте его в любом удобном для Вас месте
4. Откройте папку dist, которая находится внутри папки.
5. Запустите файл simpleTextEditor.exe для начала работы с программой.
#### Внимание!
В версии для Windows вырезаны все функции связанные с кастомизацией приложения. Поэтому, если вы хотите настроить внешний вид текстового редактора под себя, пользуйтесь другими способами установки приложения.
### 3-й способ (Для Linux и MacOS)
1. Установите шрифт [Adwaita Sans](https://gitlab.gnome.org/GNOME/adwaita-fonts)
2. Установите [Git](https://git-scm.com/downloads).
3. Склонируйте репозиторий с помощью команды `git clone https://github.com/Cheboxxxarik/simpleTextEditor`.
4. Откройте папку, куда вы склонировали репозиторий, в проводнике.
5. Запустите bash-скрипт install_packages.sh для того, чтобы установить нужные библиотеки для работы программы.
6. После установки завсимостей запустите скрипт main для начала работы с программой.
