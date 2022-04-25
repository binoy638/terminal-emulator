from Command import Command


def execute():
    return "fetching files..."


ls = Command("ls", "Show files & folders in current directory", execute)
