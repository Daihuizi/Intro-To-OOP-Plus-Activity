# add your Student class here!

class Student:
    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.classes = classes

    def add_class(self, new_class):
        self.classes.append(new_class)
        return self.classes

    def get_num_classes(self):
        return len(self.classes)


    def summary(self):
        return f"{self.name} is a {self.grade} enrolled in {self.get_num_classes()} classes"
    
