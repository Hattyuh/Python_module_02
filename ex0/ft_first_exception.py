def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    test_values: list[str] = ["25", "abc"]
    for value in test_values:
        print(f"Input data is '{value}'")
        try:
            print(
                "Temperature is now "
                f"{input_temperature(value)}°C"
                )
        except ValueError:
            print(
                "Caught input_temperature error: "
                f"invalid literal for int() with base 10: '{value}'"
                )
        print()


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print("All tests completed - program didn't crash!")
