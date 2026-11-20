from main import add_student


def test_add_student():

    student = add_student("Kiran", 24, "Python")

    assert student is not None

    print("New student added:")
    print(student)
