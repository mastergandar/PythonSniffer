import Main
import requests

import time
import PySimpleGUI as sg


class Update:
    def version_check(alive):
        print("Получаем код версии")
        newest_version = "v0.1.1"

        print("Сверяем версии приложений")
        if Main.StartUp.version != newest_version:
            Update.get_update_download(True)

    def get_update_list(self):
        print("Получаем список")
        checklist = [1, 2, 3, 4, 5, 6, 7, 8]
        print("Возвращаем список")
        return checklist

    def get_update_download(alive):

        copied_list = Update.get_update_list(alive)

        for i, item in enumerate(copied_list):

            sg.one_line_progress_meter('This is my progress meter!', i + 1, len(copied_list), '-key-')

            time.sleep(1)


if __name__ == "__main__":
    print("Начало")
    Update.version_check(True)
    print("Конец")
