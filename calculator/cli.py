from calculator.calculation import Add, Subtract, Calculation
from calculator.history import History


def describe(calculation: Calculation) -> str:
    name = calculation.__class__.__name__
    return f"{name}: {calculation.a:g}, {calculation.b:g} = {calculation.get_result():g}"


def show_history(history: History) -> None:
    calculations = history.get_history()

    if not calculations:
        print("No calculations in history.")
        return

    print("Calculation History")

    for number, calculation in enumerate(calculations, start=1):
        print(f"{number}. {describe(calculation)}")


def run() -> None:
    operations = {
        "add": Add,
        "subtract": Subtract,
    }

    history = History()

    print("Calculator")
    print("Type 'help' for commands.")

    while True:
        command = input("> ").strip().lower()

        if command == "exit":
            print("Goodbye!")
            break

        if command == "help":
            print("Commands: add, subtract, history, remove, help, exit")
            continue

        if command == "history":
            show_history(history)
            continue

        if command == "remove":
            if not history.get_history():
                print("No calculations in history.")
                continue

            number = int(input("Entry number: "))
            removed = history.remove(number - 1)
            print(f"Removed: {describe(removed)}")
            continue

        if command in operations:
            a = float(input("First number: "))
            b = float(input("Second number: "))

            calculation = operations[command](a, b)
            history.add(calculation)

            print(f"Result: {calculation.get_result():g}")
            continue

        print("Unknown command.")
