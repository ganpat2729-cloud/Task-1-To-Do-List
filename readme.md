# To-Do List Application ✅

A console-based To-Do List Management System built using Python as part of the DecodeLabs Internship Project. 
This application allows users to manage their daily tasks through a command-line interface, utilizing an efficient in-memory database structure.

### 📌 Features

*   ✅ Add new tasks with auto-generating unique IDs
*   ✅ View all tasks with their current status
*   ✅ Mark tasks as "Done"
*   ✅ Remove tasks safely using their ID
*   ✅ Input validation to prevent crashes from invalid keystrokes
*   ✅ Continuous interactive menu loop

### 🛠️ Technologies Used

*   Python 3

### 🧠 Concepts Implemented

This project demonstrates the following Python concepts:
*   Functions (Modularity)
*   Lists (Dynamic Arrays)
*   Dictionaries (Data structuring for rows)
*   Loops (`while` and `for` iterations)
*   Conditional Statements (`if/elif/else`)
*   Exception Handling (`try-except` blocks)
*   Variable Scoping (`global` keyword)

### 📂 Project Structure

```text
Task-1-ToDo-List/
│
├── main.py
└── README.md
```

### ▶️ How to Run

**1. Clone the Repository**
```bash
git clone <repository-link>
```

**2. Navigate to Project Folder**
```bash
cd Task-1-ToDo-List
```

**3. Run the Application**
```bash
python main.py
```

### 💾 Data Storage

*   The application currently utilizes an **In-Memory Database** architecture.
*   Tasks are stored dynamically in a Python list during runtime, with each task formatted as a dictionary containing its ID, name, and status. 
*   *Note: Because this relies on volatile memory (RAM), data clears when the program exits. This lays the logic foundation for implementing JSON or SQL file storage in future updates.*

### 📷 Project Overview

The To-Do List Application is a Python-based task management system designed to practice programming fundamentals, data structures, and real-world application logic. 
It provides users with an easy, crash-resistant way to organize and manage their daily tasks directly from the terminal.