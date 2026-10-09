def garden_operation(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        " " + 2
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    test_operations: list[int] = [0, 1, 2, 3, 4]
    for operation in test_operations:
        print(f"Testing operation {operation}...")
        try:
            garden_operation(operation)
        except (
            ValueError,
            ZeroDivisionError,
            FileNotFoundError,
            TypeError
        ) as error:
            print(
                f"Caught {error.__class__.__name__}: {error}"
            )
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
