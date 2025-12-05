# User Authentication System (Python)

A simple command-line authentication system written in Python.
This project allows users to register and log in, while storing user data in a JSON file and verifying passwords using secure hashing.

---

## Features

- User registration
- Login system
- Password length validation
- Password hashing (PBKDF2 + salt)
- Persistent storage using JSON
- Clear separation between logic and storage

---

## Project Structure

student_grade_manager/ │ ├── main.py └── src/ ├── student.py      # User logic (register, login, password validation) └── storage.py      # JSON load/save operations

---

## How to Run

Make sure Python 3.8 or newer is installed.

Run the program using:

python main.py

---

## Menu Options

Login 1 Register 2 Enter 0 to exit

---

## Register a User

Example:

choice: 2 name: ali Password: 123456 User saved.

Rules:
- Password must be at least 6 characters long.
- Usernames must be unique.

---

## Login

Example:

choice: 1 name: ali Password: 123456 Login successful

Possible errors:
- User not found → Username does not exist
- Wrong password → Incorrect password

---

## Data Storage

User data is saved locally in a JSON file.

Example:

`json
{
  "ali": "hashed_password_here"
}

Passwords are never stored in plain text.


---

Notes

This project is for learning purposes only.

No external libraries are used.

Not intended for real-world deployment.

Can be extended with:

Password change

Account deletion

Database integration

GUI interface
