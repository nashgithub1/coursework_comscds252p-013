"""Staff module for the university system.

Defines the :class:`Staff` class, a :class:`Person` subclass representing
administrative or support staff within a department.
"""

from person import Person


class Staff(Person):
    def __init__(self, name, person_id, email, phone,
                 employee_id, role, department):
        super().__init__(name, person_id, email, phone)

        self.employee_id = employee_id
        self.role = role
        self.department = department

    def get_responsibilities(self):
        return f"Handle {self.role} responsibilities and support department operations."