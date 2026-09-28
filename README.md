# OOP Calculator

This project is a command-line calculator built with Python using object-oriented programming. It can add and subtract numbers, save calculations in a history, remove calculations, and handle invalid input without crashing.

## Setup

Run these commands from the root project folder.

Create a virtual environment:

`python -m venv .venv`

Activate it on macOS/Linux:

`source .venv/bin/activate`

Install the required packages:

`python -m pip install -r requirements.txt`

## Running the Calculator

Run the calculator with:

`python -m calculator`

The available commands are:

- add
- subtract
- history
- remove
- help
- exit

## Running Tests

Run all tests with:

`python -m pytest`

The project requires 100% line and branch coverage. The pytest configuration checks the coverage automatically.

## Design

The calculator uses object-oriented programming to separate different responsibilities. `Calculation` provides a common structure for calculations. `Add` and `Subtract` perform their own versions of `get_result()`.

`History` stores and removes calculation objects. It does not need to know how each calculation performs its math. The CLI handles commands and user input, while the calculation classes handle the operations.

## Stage 6 Reflection

### 1. Where would Multiply belong?

I would create a `Multiply` class that follows the same structure as `Add` and `Subtract` and gives its own implementation of `get_result()`. I would add `multiply` to the operations dictionary in the CLI and add it to the help message. I would also add tests for multiplication and test the command in a calculator session.

The `History` class would not need multiplication-specific code because it already stores calculation objects through their shared structure. It does not need to know whether the calculation is addition, subtraction, or multiplication.

### 2. What contract could email and text-message notifications share?

Email and text-message notification objects could both have a `send()` method. Each object could perform `send()` differently, but the rest of the program could use the same method for either type. This is similar to how the calculator uses `get_result()` with different calculation objects.

### 3. What design knowledge transfers to another language?

Ideas like abstraction, encapsulation, polymorphism, separating responsibilities, and testing can transfer to other programming languages. The overall design ideas would still be useful, but I would need to learn the new language's syntax, class system, type rules, libraries, and runtime behavior.

## Reproducing the Project

I followed the setup instructions in a fresh environment by creating a virtual environment, installing `requirements.txt`, and running the tests. One instruction that can be confusing is remembering that the commands need to be run from the root project folder. I made this clearer in the setup section.

If the tests pass but coverage fails, I would look at the coverage table and especially the `Missing` column. This shows which lines or branches were not executed. I would find the behavior connected to the missing path and add a meaningful test for it instead of removing application code.

## Continuous Integration

GitHub Actions runs the tests using Python 3.11, 3.12, 3.13, and 3.14. The workflow installs the dependencies and runs `python -m pytest`.

If CI fails, I would look at the failing step and find the first useful error or assertion. An assertion failure means a test did not get the expected result, while an installation failure happens before the tests can run.