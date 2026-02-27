"""Department module for the university system.

Provides the :class:`Department` class to manage faculty and course
collections for an academic department.
"""

class Department:
    def __init__(self, dept_name, dept_head):
        self.dept_name = dept_name
        self.dept_head = dept_head  # Faculty object
        self.faculty_list = []
        self.course_list = []

    # -------------------------
    # Add Faculty
    # -------------------------
    def add_faculty(self, faculty):
        if faculty not in self.faculty_list:
            self.faculty_list.append(faculty)

    # -------------------------
    # Add Course
    # -------------------------
    def add_course(self, course):
        if course not in self.course_list:
            self.course_list.append(course)

    # -------------------------
    # Department Summary
    # -------------------------
    def get_department_info(self):
        info = f"Department: {self.dept_name}\n"
        info += f"Head: {self.dept_head.name}\n"

        info += "\nFaculty Members:\n"
        for f in self.faculty_list:
            info += f"- {f.name}\n"

        info += "\nCourses:\n"
        for c in self.course_list:
            info += f"- {c.course_code}: {c.course_name} ({len(c.enrolled_students)} students)\n"

        return info