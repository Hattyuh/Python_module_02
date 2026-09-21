def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    test_values: list[str] = ["25", "abc", "100", "-50"]
    max_value = 40
    min_value = 0
    for value in test_values:
        print(f"Input data is '{value}'")
        try:
            test_value = input_temperature(value)
            if int(test_value) > max_value:
                print(
                    f"Caught input_temperature error: {value}°C "
                    f"is too hot for plants (max {max_value}°C)"
                    )
            elif int(test_value) < min_value:
                print(
                    f"Caught input_temperature error: {value}°C "
                    f"is too cold for plants (min {min_value}°C)")
            else:
                print(
                        "Temperature is now "
                        f"{test_value}°C"
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
