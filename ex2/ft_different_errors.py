def garden_operation(operation_number: int):
    if operation_number == 0:
        return int("abc")
    if operation_number == 1:
        return 1 / 0
    if operation_number == 2:
        return open("/non/existent/file", "r")
    if operation_number == 3:
        return " " + 2


def test_error_types() -> None:
    test_operations: list[int] = [0, 1, 2, 3]
    for operation in test_operations:
        print(f"Testing operation {operation}")
        garden_operation(operation)


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()

#ValueError
#ZeroDivisionError
#FileNotFoundError
#TypeError