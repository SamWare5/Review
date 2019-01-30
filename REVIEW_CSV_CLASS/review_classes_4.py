from datetime import datetime

class Document():
    def __init__(self, date, authors=[]):
        self.authors = authors
        self.date = date
