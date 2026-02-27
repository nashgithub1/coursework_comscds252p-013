"""Demo script for the university system modules.

Creates sample faculty, students, staff, courses, and departments and
demonstrates enrollment, grading, and department summaries. Intended
to be run as a simple example or script.
"""

from student import Student
from faculty import Faculty
from staff import Staff
from course import Course
from department import Department

# -------------------------
# Create Faculty
# -------------------------
f1 = Faculty("Dr. John", "P201", "john@email.com", "0771111111", "F001", "IT", "2020")
f2 = Faculty("Dr. Smith", "P202", "smith@email.com", "0772222222", "F002", "IT", "2019")
f3 = Faculty("Dr. Jane", "P203", "jane@email.com", "0773333333", "F003", "Business", "2018")

# -------------------------
# Create Students
# -------------------------
s1 = Student("Ali", "P101", "ali@email.com", "0770000000", "S001", "IT", "2023")
s2 = Student("Sara", "P102", "sara@email.com", "0779999999", "S002", "IT", "2023")
s3 = Student("Nimal", "P103", "nimal@email.com", "0778888888", "S003", "Business", "2023")

# -------------------------
# Create Staff
# -------------------------
st1 = Staff("Kamal", "P301", "kamal@email.com", "0774444444", "ST001", "Admin", "IT")
st2 = Staff("Sunil", "P302", "sunil@email.com", "0775555555", "ST002", "Support", "IT")
st3 = Staff("Ravi", "P303", "ravi@email.com", "0776666666", "ST003", "Clerk", "Business")

# -------------------------
# Create Courses
# -------------------------
c1 = Course("CS101", "Programming", 3, f1, 3)
c2 = Course("CS102", "Data Science", 3, f2, 3)
c3 = Course("CS103", "Databases", 3, f1, 3)

c4 = Course("BM101", "Marketing", 3, f3, 3)
c5 = Course("BM102", "Finance", 3, f3, 3)

# -------------------------
# Create Departments
# -------------------------
d1 = Department("IT", f1)
d2 = Department("Business", f3)

# Add faculty
d1.add_faculty(f1)
d1.add_faculty(f2)

d2.add_faculty(f3)

# Add courses
d1.add_course(c1)
d1.add_course(c2)
d1.add_course(c3)

d2.add_course(c4)
d2.add_course(c5)

# -------------------------
# Enroll Students
# -------------------------
c1.add_student(s1)
c2.add_student(s1)
c3.add_student(s1)
c4.add_student(s1)

# Add grades
s1.add_grade("CS101", 3.5)
s1.add_grade("CS102", 3.0)
s1.add_grade("CS103", 2.5)
s1.add_grade("BM101", 3.8)

print("Student GPA:", s1.gpa)
print("Academic Status:", s1.get_academic_status())

# -------------------------
# Error Handling Demo
# -------------------------
try:
    s1.add_grade("CS101", 5.0)
except ValueError as e:
    print("Error:", e)

# -------------------------
# Polymorphism Demo
# -------------------------
people = [s1, f1, st1]

for p in people:
    print(p.get_responsibilities())

# -------------------------
# Department Info
# -------------------------
print("\n--- Department Info ---")
print(d1.get_department_info())
print(d2.get_department_info())