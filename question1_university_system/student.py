"""Student module for the university system.

Defines the :class:`Student` class which extends :class:`Person` to
manage enrollment, grades, and GPA calculation for a student.
"""

from person import Person


class Student(Person):
    MAX_COURSES = 6

    def __init__(self, name, person_id, email, phone,
                 student_id, major, enrollment_date):
        super().__init__(name, person_id, email, phone)

        self.student_id = student_id
        self.major = major
        self.enrollment_date = enrollment_date

        self.enrolled_courses = []
        self._grades = {}  # protected (encapsulation)

    # -------------------------
    # Course Enrollment
    # -------------------------
    def enroll_course(self, course_code):
        if len(self.enrolled_courses) >= Student.MAX_COURSES:
            raise ValueError("Cannot enroll in more than 6 courses.")

        if course_code not in self.enrolled_courses:
            self.enrolled_courses.append(course_code)

    # -------------------------
    # Add Grades (Validation)
    # -------------------------
    def add_grade(self, course_code, grade):
        if course_code not in self.enrolled_courses:
            raise ValueError("Student is not enrolled in this course.")

        if not (0.0 <= grade <= 4.0):
            raise ValueError("Grade must be between 0.0 and 4.0.")

        self._grades[course_code] = grade

    # -------------------------
    # GPA Calculation (Read-Only)
    # -------------------------
    @property
    def gpa(self):
        return self.calculate_gpa()

    def calculate_gpa(self):
        if not self._grades:
            return 0.0

        return sum(self._grades.values()) / len(self._grades)

    # -------------------------
    # Academic Status
    # -------------------------
    def get_academic_status(self):
        gpa = self.gpa

        if gpa >= 3.5:
            return "Dean's List"
        elif gpa >= 2.0:
            return "Good Standing"
        else:
            return "Probation"

    # -------------------------
    # Polymorphism
    # -------------------------
    def get_responsibilities(self):
        return "Attend lectures, complete assignments, and maintain academic performance."