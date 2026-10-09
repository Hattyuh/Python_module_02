def input_temperature(temp_str: str) -> int:
    max_temp: int = 40
    min_temp: int = 0
    temp: int = int(temp_str)
    if temp < min_temp:
        raise ValueError(f"{temp}°C is too cold for plants (min {min_temp}°C)")
    if temp > max_temp:
        raise ValueError(f"{temp}°C is too hot for plants (max {max_temp}°C)")
    return temp


def test_temperature() -> None:
    test_values: list[str] = ["25", "abc", "100", "-50", "0", "40", "-1", "41"]
    for value in test_values:
        print(f"Input data is '{value}'")
        try:
            test_value: int = input_temperature(value)
            print(
                "Temperature is now "
                f"{test_value}°C"
            )
        except ValueError as error:
            print(
                f"Caught input_temperature error: {error}"
            )
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature()
