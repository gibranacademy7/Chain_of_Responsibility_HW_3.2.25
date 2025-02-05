# number_check/__init__.py

class NumberCheck:
    def __init__(self):
        self.next = None

    def set_next(self, next_check):
        """Sets the next check in the chain."""
        self.next = next_check

    def check(self, number):
        """Perform the check. If no check is performed, pass it to the next check."""
        if self.next:
            return self.next.check(number)
        return True
