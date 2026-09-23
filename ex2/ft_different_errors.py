def garden_operation(operation_number: int):
    if operation_number == 0:
        try:
            return int("abc")
        except ValueError:
            print(
                "Caught ValueError: "
                "invalid literal for int() with base 10: 'abc'"
                )
    if operation_number == 1:
        try:
            return 1 / 0
        except ZeroDivisionError:
            print(
                "Caught ZeroDivisionError: "
                "division by zero"
                )
    if operation_number == 2:
        try:
            return open("/non/existent/file", "r")
        except FileNotFoundError:
            print(
                "Caught FileNotFoundError: "
                "[Errno 2] No such file or directory: '/non/existent/file'"
                )
    if operation_number == 3:
        try:
            return " " + 2
        except TypeError:
            print(
                "Caught TypeError: "
                'can only concatenate str (not "int") to str'
                )
    if operation_number > 3:
        print("Operation completed successfully")


def test_error_types() -> None:
    test_operations: list[int] = [0, 1, 2, 3, 4]
    for operation in test_operations:
        print(f"Testing operation {operation}...")
        garden_operation(operation)
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
