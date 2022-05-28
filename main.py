class Student:
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = []
        self.score = score

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = age

    def add_track(self, track):
        self.tracks.append(track)

    def get_score(self):
        print(self.score)

    
        



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
