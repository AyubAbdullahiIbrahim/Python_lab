
# Python Lab Assignment

## Part A - Project Setup Using the CLI

### Commands Used

The project was created using the command-line interface (CLI). The `mkdir python_lab` command creates the main project directory, while `cd python_lab` moves into that directory. The `mkdir src, tests, docs` command creates separate folders for source code, tests, and documentation. The `New-Item` command creates the Python files `main.py`, `utils.py`, and `config.py`. Output redirection was used to create `README.md` and write the text `My Python Lab Project`. Commands such as `Get-ChildItem` and recursive directory listing commands can be used to display the project structure.

### Why Separate src, tests, and docs?

Separating a project into `src`, `tests`, and `docs` is good practice because it keeps the project organized. The `src` folder contains the main application code, the `tests` folder contains automated tests used to verify that the code works correctly, and the `docs` folder contains documentation. Even in a small project, this structure makes files easier to find, maintain, test, and expand in the future.

---

## Part B - Git Initialization and First Commit

### What is .gitignore?

The `.gitignore` file tells Git which files and folders should not be tracked or committed to the repository. In this project, `__pycache__/` ignores Python cache folders, `*.pyc` ignores compiled Python files, and `.env` ignores environment files that may contain sensitive configuration information. Ignoring these files helps keep the repository clean and prevents unnecessary or private files from being uploaded.

### What Does Commit History Show?

Git commit history records changes made to a project over time. Each commit has a unique identifier, a message, and information about when the change was made. The commit history helps developers understand how a project developed, identify when changes were introduced, and review or restore previous versions when necessary.

---

## Part C - Writing and Committing Python Code

### Python Import System

Python's import system allows one Python file to use functions and code from another file. In this project, `main.py` imports `square`, `is_even`, and `celsius_to_fahrenheit` from `utils.py` using the `from utils import ...` statement. This allows the functions to be defined once in `utils.py` and reused in `main.py`. Separating reusable functions from the main program improves organization and makes the code easier to maintain and test.

### Testing the Program

The program was tested with multiple input values, including 0, 5, and 10. The program correctly calculated the square of each number, identified whether the number was even or odd, and converted the Celsius value to Fahrenheit.

---

## Part D - Publishing to GitHub and Branch Workflow

### Why Developers Use Branches

Developers use branches to work on new features or changes without directly affecting the main branch. The `main` branch usually contains the stable version of the project, while a feature branch allows development and testing to happen safely. In this project, the `feature/add-greeting` branch was created to add a personalized greeting feature without immediately changing the code on `main`.

### Why Pull Requests Are Used

A pull request allows developers to propose changes from one branch to another, usually from a feature branch into `main`. Pull requests provide an opportunity to review the code before it becomes part of the main project. During a code review, developers can examine the changes, leave comments, suggest improvements, request modifications, and approve the code. Once the changes are approved, they can be merged into the main branch.

### Greeting Feature

A new function called `greet(name)` was added to `utils.py`. The function returns a personalized greeting message. The function was then imported and called from `main.py`. The feature was developed on the `feature/add-greeting` branch, committed, and pushed to GitHub before creating a pull request into the `main` branch.

---

## Project Structure

```text
python_lab/
├── .gitignore
├── README.md
├── docs/
│   └── README.md
├── src/
│   ├── main.py
│   ├── utils.py
│   └── config.py
├── tests/
│   └── test_utils.py
└── screenshot2.PNG