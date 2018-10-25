class CustomValueError(ValueError):
    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}
try:
    raise CustomValueError("Value must be between 1 and 10.")
except CustomValueError as e:
    print("CustomValueError Exception!", e.strerror)
