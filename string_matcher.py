# Sara Derakhshani, 21.01.21
# Programmierung 1: Projekt
# String-Matching-Tool


class StringMatcher:

    methods = ['naive', 'finite-state']

    def __init__(self, method='naive'):
        if method not in self.methods:
            raise NotImplementedError
        self.method = method
