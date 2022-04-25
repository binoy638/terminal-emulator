from Command import Command
import os


def execute():
    dir_list = os.listdir()
    return "fetching files..."


ls = Command("ls", "Show files & folders in current directory", execute)
