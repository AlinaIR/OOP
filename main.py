class Mentor:
    def __init__(self, name, surname, courses_attached):
        self.name = name
        self.surname = surname
        self.courses_attached = courses_attached

class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname, courses_attached)
        self.grades = {}

    def __str__(self):
        average_grade = self._calculate_average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade}"

    def _calculate_average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        count_grades = sum(len(grades) for grades in self.grades.values())
        return total_grades / count_grades if count_grades != 0 else 0

class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname, courses_attached)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Student:
    def __init__(self, name, surname, courses_in_progress, finished_courses):
        self.name = name
        self.surname = surname
        self.courses_in_progress = courses_in_progress
        self.finished_courses = finished_courses
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        average_grade = self._calculate_average_grade()
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def _calculate_average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        count_grades = sum(len(grades) for grades in self.grades.values())
        return total_grades / count_grades if count_grades != 0 else 0

# Примеры создания экземпляров и вызова методов
lecturer1 = Lecturer('John', 'Doe', ['Python'])
lecturer2 = Lecturer('Jane', 'Smith', ['Git'])

reviewer1 = Reviewer('Alice', 'Johnson', ['Python'])
reviewer2 = Reviewer('Bob', 'Brown', ['Git'])

student1 = Student('Ruoy', 'Eman', ['Python'], ['Введение в программирование'])
student2 = Student('Lily', 'Evans', ['Git'], ['Введение в программирование'])

reviewer1.rate_hw(student1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 9)

print(lecturer1)
print(reviewer1)
print(student1)     

     def average_grade_students(students, course):
    total_grades = 0
    count_grades = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            count_grades += len(student.grades[course])
    return total_grades / count_grades if count_grades != 0 else 0

     def average_grade_lecturers(lecturers, course):
    total_grades = 0
    count_grades = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            count_grades += len(lecturer.grades[course])
    return total_grades / count_grades if count_grades != 0 else 0