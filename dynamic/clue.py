# clue.py

class Clue:
    def __init__(self, description, related_to, evidence):
        self.description = description
        self.related_to = related_to
        self.evidence = evidence

    def __str__(self):
        return f"{self.description} (Related to: {self.related_to})\nEvidence: {self.evidence}"