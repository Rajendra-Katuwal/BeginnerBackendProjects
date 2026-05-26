# Task Tracker
Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on. This project will help you practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

---

## Requirements
The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

- [ x ] Add, Update, and Delete tasks
- [ x ] Mark a task as in progress or done
- [ x ] List all tasks
- [ x ] List all tasks that are done
- [ x ] List all tasks that are not done
- [ x ] List all tasks that are in progress

---

**Here are some constraints to guide the implementation:**
- [ x ] You can use any programming language to build this project.
    - used python for the development
- [ x ] Use positional arguments in command line to accept user inputs.
- [ x ] Use a JSON file to store the tasks in the current directory.
- [ x ] The JSON file should be created if it does not exist.
- [ x ] Use the native file system module of your programming language to interact with the JSON file.
- [ x ] Do not use any external libraries or frameworks to build this project.
    - used the built in json module for parsing the json text
- [ ] Ensure to handle errors and edge cases gracefully.

---

### How to run this project
- first clone this project using git clone or download the zip of this folder
- then the root directory of this project which is TaskTracker/
- then run the following command to build and install this as a package and run the cli tool
    ```python
    pip install .  # for production installation of the package
    ```
    ```python
    pip install -e .  # for development installation of the package
    ```

