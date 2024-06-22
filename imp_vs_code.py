import os
import zipfile

# Папка с настройками Visual Studio
settings_folder = r'c:\Users\yuriy\AppData\Roaming\Code\User'

# Папка, куда будем сохранять ZIP-файл
output_folder = r'e:\proect python 3'

# Имя ZIP-файла
output_filename = 'VisualStudioSettings.zip'

# Создаем объект ZipFile для записи
with zipfile.ZipFile(os.path.join(output_folder, output_filename), 'w') as zipf:
    # Рекурсивно добавляем все файлы из папки settings_folder в ZIP-архив
    for foldername, subfolders, filenames in os.walk(settings_folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            zipf.write(file_path, os.path.relpath(file_path, settings_folder))

print('Настройки Visual Studio успешно экспортированы в ZIP-файл:', output_filename)

import os
import shutil
import json

# Папка с настройками расширений Visual Studio
extensions_folder = r'c:\Users\yuriy\AppData\Roaming\Code\User\sync\extensions'

# Папка, куда будем сохранять настройки
output_folder = r'E:\proect python 3\extensions vs code'

# Создаем папку для сохранения настроек, если она не существует
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Копируем файлы настроек расширений в новую папку
for foldername, subfolders, filenames in os.walk(extensions_folder):
    for filename in filenames:
        if filename.endswith('lastSyncextensions.json'):
            file_path = os.path.join(foldername, filename)
            shutil.copy2(file_path, output_folder)

print('Настройки расширений Visual Studio успешно экспортированы в папку:', output_folder)
