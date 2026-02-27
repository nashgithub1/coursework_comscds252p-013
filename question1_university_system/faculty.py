"""Faculty module for the university system.

Defines the :class:`Faculty` class, a subclass of :class:`Person`, which
represents teaching staff and their employment details.
"""

from person import Person


class Faculty(Person):
    def __init__(self, name, person_id, email, phone,
                 employee_id, department, hire_date):
        super().__init__(name, person_id, email, phone)

        self.employee_id = employee_id
        self.department = department
        self.hire_date = hire_date

    def get_responsibilities(self):
        return "Teach courses, conduct research, and supervise students."