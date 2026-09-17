from activity.student import Student

NAME_1 = "Samara"
GRADE_1 = "junior"
CLASSES_1 = [
    "Pre-Calc", 
    "English III", 
    "World History", 
    "Gym", 
    "Chemistry",
    "Music Composition"
]

def test_create_one_student():
    name = NAME_1
    grade = GRADE_1
    classes = list(CLASSES_1)
    classes_copy = list(CLASSES_1)

    student = Student(name, grade, classes)

    assert student.name == name
    assert student.grade == grade
    assert student.classes == classes_copy

def test_add_additional_class():
    name = NAME_1
    grade = GRADE_1
    classes = list(CLASSES_1)
    classes_added = list(CLASSES_1)
    classes_added.append("Painting")
    student = Student(name, grade, classes)

    result = student.add_class("Painting")

    assert student.classes == classes_added
    assert result == classes_added

def test_get_classes_count():
    name = NAME_1
    grade = GRADE_1
    classes = list(CLASSES_1)
    student = Student(name, grade, classes)

    result = student.get_num_classes()

    assert result == 6

def test_gets_expected_summary():
    name = NAME_1
    grade = GRADE_1
    classes = list(CLASSES_1)
    student = Student(name, grade, classes)

    result = student.summary()

    assert result == "Samara is a junior enrolled in 6 classes"
