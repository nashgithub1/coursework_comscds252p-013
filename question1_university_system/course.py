"""Course module for the university system.

Defines the :class:`Course` class for handling course attributes and
student enrollment management.
"""

class Course:
    def __init__(self, course_code, course_name, credits, instructor, max_capacity):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits
        self.instructor = instructor  # Faculty object
        self.max_capacity = max_capacity
        self.enrolled_students = []

    # -------------------------
    # Add Student
    # -------------------------
    def add_student(self, student):
        if self.is_full():
            raise ValueError(f"Course {self.course_code} is full.")

        if student not in self.enrolled_students:
            self.enrolled_students.append(student)

            # Sync with student side (important design)
            student.enroll_course(self.course_code)

    # -------------------------
    # Remove Student
    # -------------------------
    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)

            if self.course_code in student.enrolled_courses:
                student.enrolled_courses.remove(self.course_code)

    # -------------------------
    # Check Capacity
    # -------------------------
    def is_full(self):
        return len(self.enrolled_students) >= self.max_capacity

    # -------------------------
    # Course Info
    # -------------------------
    def get_course_info(self):
        return f"{self.course_code} - {self.course_name} ({len(self.enrolled_students)}/{self.max_capacity})"