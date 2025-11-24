#finished_courses - курс, который студент уже прошел
#courses_attache - закрепленный за преподавателями список курсов
#courses_progress - список курсов, которые сейчас изучаются


class Student:
    student_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}
        Student.student_list.append(self)

    def add_courses(self, courses_name):
        self.finished_courses.append(courses_name)


    def rate_lect(self, lecturer, course, grades):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grades]
            else:
                lecturer.grades[course] = [grades]
        else:
            return 'Ошибка'

    def average_rating_st(self):
        f = 0
        g = 0
        for value in self.grades.values():
            f += sum(value)
            g += len(value)
            av_grade_st = f/g
            return av_grade_st

    def __str__(self):
         rez = f' \n Студент: \n Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за домашние задания: {self.average_rating_st()} \n ' \
             f'Курсы в процессе изучения: {self.courses_in_progress} \n Завершенные курсы: {self.finished_courses}'
         return rez

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    lecturer_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        Lecturer.lecturer_list.append(self)

    def average_rating_lec(self):
        ff = 0
        gg = 0
        for value in self.grades.values():
            ff += sum(value)
            gg += len(value)
            ave_grade_lec = ff/gg
            return ave_grade_lec

    def __str__(self):
        rez = f' \n Лектор: \n Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {self.average_rating_lec()}'
        return rez

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        else:
            #return some_lecturer.average_rating_lec() < some_student.average_rating_st()
            return lecturer_1.average_rating_lec() < student_1.average_rating_st()

class Reviewer(Mentor):
    reviewer_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        Reviewer.reviewer_list.append(self)

    def rate_stud(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        rez = f' \n Проверяющий: \n Имя: {self.name} \n Фамилия: {self.surname}'
        return rez

#some_lecturer = Lecturer('Some', 'Buddy')
#some_lecturer.courses_attached += ['Введение в программирование']

#some_student = Student('Ruoy', 'Eman', 'M')
#some_student.courses_in_progress += ['Python']
#some_student.courses_in_progress += ['Git']
#some_student.finished_courses += ['Введение в программирование']

#some_student.rate_lect(some_lecturer, 'Введение в программирование', 9)
#some_student.rate_lect(some_lecturer, 'Введение в программирование', 9)
#some_student.rate_lect(some_lecturer, 'Введение в программирование', 8)

#some_reviewer = Reviewer('Some', 'Buddy')
#some_reviewer.courses_attached = ['Python', 'Git']

#some_reviewer.rate_stud(some_student, 'Python', 8)
#some_reviewer.rate_stud(some_student, 'Python', 9)
#some_reviewer.rate_stud(some_student, 'Python', 10)
#some_reviewer.rate_stud(some_student, 'Git', 5)
#some_reviewer.rate_stud(some_student, 'Git', 4)
#some_reviewer.rate_stud(some_student, 'Git', 3)

#print(*Reviewer.reviewer_list)
#print( )
#print(*Lecturer.lecturer_list)
#print( )
#print(*Student.student_list)

#print(some_lecturer.average_rating_lec())
#print(some_student.average_rating_st())
#print(some_lecturer.average_rating_lec() < some_student.average_rating_st())

#print(   )
#print(   )

lecturer_1 = Lecturer('Антон', 'Антонов')
lecturer_1.courses_attached += ['Введение в программирование']

lecturer_2 = Lecturer('Роман', 'Романов')
lecturer_2.courses_attached += ['Python']

student_1 = Student('Михаил', 'Михайлов', 'М')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_1.rate_lect(lecturer_1, 'Введение в программирование', 3)
student_1.rate_lect(lecturer_1, 'Введение в программирование', 8)
student_1.rate_lect(lecturer_1, 'Введение в программирование', 5)

student_1.rate_lect(lecturer_2, 'Python', 2)
student_1.rate_lect(lecturer_2, 'Python', 6)
student_1.rate_lect(lecturer_2, 'Python', 8)

student_2 = Student('Кирилл', 'Кириллов', 'М')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

student_2.rate_lect(lecturer_1, 'Введение в программирование', 5)
student_2.rate_lect(lecturer_1, 'Введение в программирование', 7)
student_2.rate_lect(lecturer_1, 'Введение в программирование', 9)

student_2.rate_lect(lecturer_2, 'Python', 7)
student_2.rate_lect(lecturer_2, 'Python', 6)
student_2.rate_lect(lecturer_2, 'Python', 5)

reviewer_1 = Reviewer('Иван', 'Иванов')
reviewer_1.courses_attached = ['Python', 'Git']

reviewer_1.rate_stud(student_1, 'Python', 3)
reviewer_1.rate_stud(student_1, 'Python', 4)
reviewer_1.rate_stud(student_1, 'Python', 5)
reviewer_1.rate_stud(student_1, 'Git', 6)
reviewer_1.rate_stud(student_1, 'Git', 7)
reviewer_1.rate_stud(student_1, 'Git', 3)

reviewer_1.rate_stud(student_2, 'Python', 5)
reviewer_1.rate_stud(student_2, 'Python', 8)
reviewer_1.rate_stud(student_2, 'Python', 9)
reviewer_1.rate_stud(student_2, 'Git', 10)
reviewer_1.rate_stud(student_2, 'Git', 7)
reviewer_1.rate_stud(student_2, 'Git', 8)

reviewer_2 = Reviewer('Петр', 'Петров')
reviewer_2.courses_attached = ['Python', 'Git']

reviewer_2.rate_stud(student_1, 'Python', 6)
reviewer_2.rate_stud(student_1, 'Python', 4)
reviewer_2.rate_stud(student_1, 'Python', 5)
reviewer_2.rate_stud(student_1, 'Git', 10)
reviewer_2.rate_stud(student_1, 'Git', 8)
reviewer_2.rate_stud(student_1, 'Git', 5)

reviewer_2.rate_stud(student_2, 'Python', 5)
reviewer_2.rate_stud(student_2, 'Python', 5)
reviewer_2.rate_stud(student_2, 'Python', 4)
reviewer_2.rate_stud(student_2, 'Git', 6)
reviewer_2.rate_stud(student_2, 'Git', 7)
reviewer_2.rate_stud(student_2, 'Git', 10)

print(*Reviewer.reviewer_list)
print( )
print(*Lecturer.lecturer_list)
print( )
print(*Student.student_list)
print(  )
print(' Пример сравнения средних оценок: Лектор 1 и Студент 1')
print(f' Лектор 1: {lecturer_1.average_rating_lec()}')
print(f' Студент 1: {student_1.average_rating_st()}')
print(f' Итог: {lecturer_1.average_rating_lec() < student_1.average_rating_st()}')
print(  )

def av_st_all(course = 'Git'):
    q = 0
    w = 0
    for student in Student.student_list:
        if course in student.courses_in_progress or course in student.finished_courses:
            q += sum(student.grades.get(course))
            w += len(student.grades.get(course))
    aver = q / w
    return aver

print(f' Средняя оценка за домашние задания по всем студентам в рамках конкретного курса: {av_st_all()}')

def av_lec_all(course = 'Введение в программирование'):
    q = 0
    w = 0
    for lecturer in Lecturer.lecturer_list:
        if course in lecturer.courses_attached:
            q += sum(lecturer.grades.get(course))
            w += len(lecturer.grades.get(course))
    aver = q / w
    return aver
print(f' Средняя оценка за лекции всех лекторов в рамках конкретного курса: {av_lec_all()}')