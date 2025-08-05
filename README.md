# TODO List Application

A simple command-line TODO list manager built with Python. This project was created as part of the Elevate Labs Internship program.

## Features

- Add new tasks
- View all tasks with completion status
- Mark tasks as completed
- Remove tasks from the list
- Simple command-line interface

## Requirements

- Python 3.x

## Installation

Clone or download this repository

## Usage

1. Run the program:

```bash
python todo.py
```

2. Use the menu options:
   - Option 1: Add a new task
   - Option 2: View all tasks
   - Option 3: Mark a task as completed
   - Option 4: Remove a task
   - Option 5: Exit the program

## Example

```
=== TODO List Manager ===
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Remove Task
5. Exit

Enter your choice (1-5): 1
Enter task description: Complete Python assignment

Your TODO List:
1. [ ] Complete Python assignment
```

## Project Structure

- `todo.py` - Main application file containing the TodoList class and program logic

## Implementation Details

- Uses a class-based approach for task management
- Tasks are stored in memory as a list of dictionaries
- Each task has a description and completion status
- Input validation for task operations

## Learning Objectives

- Object-Oriented Programming in Python
- Data structures (Lists, Dictionaries)
- User input handling
- Basic error handling
- Command-line interface design

## Future Improvements

- Persistent storage using files
- Task due dates
- Priority levels
- Task categories
- Data export functionality

## Author

Shivam Ramola
Created as part of Elevate Labs Internship - Day 2 Task
