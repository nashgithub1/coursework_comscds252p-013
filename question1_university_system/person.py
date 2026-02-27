"""Person module for the university system.

Defines the :class:`Person` base class used by students, faculty, and
staff for shared contact and identification information.
"""

class Person:
    def __init__(self, name, person_id, email, phone):
        self.name = name
        self.person_id = person_id
        self.email = email
        self.phone = phone

    def get_info(self):
        return f"Name: {self.name}, ID: {self.person_id}, Email: {self.email}, Phone: {self.phone}"

    def update_contact(self, email=None, phone=None):
        if email:
            self.email = email
        if phone:
            self.phone = phone

    def get_responsibilities(self):
        return "General responsibilities of a university member."