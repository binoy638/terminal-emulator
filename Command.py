class Command():
    def __init__(self, name, description, func):
        self.name = name
        self.description = description
        self.func = func

    def execute(self, *kw):
        return self.func(*kw)
