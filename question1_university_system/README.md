# University Management System (OOP)

##  Overview

This project implements a **University Management System** using Object-Oriented Programming (OOP) principles in Python. The system models core university entities such as students, faculty, staff, courses, and departments, demonstrating real-world relationships and interactions.

The implementation carries **inheritance, encapsulation, polymorphism, and data validation**, as required in the coursework.

---

##  Objectives

* Design a scalable class hierarchy
* Implement student course management with GPA calculation
* Apply data validation using property decorators
* Demonstrate polymorphism across different roles
* Model relationships between departments, courses, and users

---

##  System Architecture

### Class Hierarchy

```
Person (Base Class)
│
├── Student
├── Faculty
└── Staff
```

### Relationships

* **Department → Course** (Composition)
* **Course → Student** (Association)
* **Course → Faculty** (Instructor assignment)

---

##  Project Structure

```
question1_university_system/

├── person.py
├── student.py
├── faculty.py
├── staff.py
├── course.py
├── department.py
├── main.py
└── README.md
```

---

##  Features

### 1. Inheritance

* `Person` serves as the base class
* `Student`, `Faculty`, and `Staff` extend common attributes and methods

### 2. Student Course Management

* Enroll in courses (max 6)
* Add grades (0.0 – 4.0 scale)
* Automatic GPA calculation
* Academic status classification:

  * Dean’s List (GPA ≥ 3.5)
  * Good Standing (GPA ≥ 2.0)
  * Probation (GPA < 2.0)

### 3. Encapsulation & Validation

* GPA implemented as a **read-only property**
* Grade validation enforced
* Course enrollment limit enforced
* Error handling using `ValueError`

### 4. Polymorphism

* `get_responsibilities()` method overridden in:

  * Student
  * Faculty
  * Staff
* Demonstrated using a heterogeneous object list

### 5. Course Management

* Add/remove students
* Capacity control
* Instructor assignment
* Bidirectional enrollment consistency

### 6. Department Management

* Manage faculty and courses
* Department-level summary reporting

---

##  How to Run

1. Navigate to the project folder:

```bash
cd question1_university_system
```

2. Run the main program:

```bash
python main.py
```

---

##  Demonstrations Included

* Student enrolling in multiple courses
* GPA calculation and academic status display
* Error handling for invalid grade input
* Polymorphism demonstration
* Department summary output

---

##  Example Output

```
Student GPA: 3.2
Academic Status: Good Standing

Error: Grade must be between 0.0 and 4.0.

Attend lectures, complete assignments...
Teach courses, conduct research...
Handle Admin responsibilities...

--- Department Info ---
Department: IT
...
```

---

##  Key OOP Concepts Demonstrated

| Concept       | Implementation                     |
| ------------- | ---------------------------------- |
| Inheritance   | Person → Student, Faculty, Staff   |
| Encapsulation | Protected attributes, GPA property |
| Polymorphism  | Method overriding                  |
| Abstraction   | Class-based modular design         |

---

## Requirements

* Python 3.x
3.11 is the version im using to work on



---
