class Course:
    def __init__(self, name, professor, min_, max_, duration):
        self.name = name
        self.professor = professor
        self.min = min_
        self.max = max_
        self.duration = duration
        self.enroled = []
