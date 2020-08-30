class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__grades = []

    def __str__(self):
        return '{name} - {age}: {grades}'.format(
            name=self.__name,
            age=self.__age,
            grades=' '.join('(' + str(grade) + ')' for grade in self.__grades)
        )

    def __set_name(self, name):
        if self.__name != name:
            self.__name = name

    def set_age(self, age):
        if 16 <= age < 100:
            self.__age = age

    def add_grades(self, *grades):
        for grade in grades:
            if 0 <= grade <= 100:
                self.__grades.append(grade)

    def __get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_grades(self):
        return self.__grades

    name = property(__get_name, __set_name)


class Group:
    def __init__(self, name):
        self.__name = name
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)

    def add_students(self, *students):
        for student in students:
            self.__students.append(student)

    def show_group(self):
        for student in self.__students:
            print(student)

    def get_group(self):
        return self.__students

# Благодаря методам класса Students мы можем вносить в контейнер Group информацию о студентах с последующим
# редактированием.


print('')
st1 = Student('Egor', 22)
st1.add_grades(100, 100, -2, 80, 80, 70)

st2 = Student('Evgeniy', 33)
st2.set_age(34)


st3 = Student('Nataly', 27)
st3.add_grades(100, 90, 100, 56, 2332, 0, 90)

group = Group('Python courses')
group.add_students(st1, st2, st3)
print('List of students with some mistakes:\n')
group.show_group()
students = group.get_group()

students[0].name = 'Igor'

students[2].set_age(28)
st2.add_grades(100, 100, 100, 100, 200, 455)

print('\nRefreshed list of students:\n')
group.show_group()
