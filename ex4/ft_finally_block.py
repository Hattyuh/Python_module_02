class GardenError(Exception):
    def __init__(self, message:str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name} [OK]")
    else:
        raise PlantError(
            f"Invalid plant name to water: '{plant_name}'"
        )


def test_watering_system(plants: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught {error.__class__.__name__}: {error}")
        return
    finally:
        print(".. ending tests and returning to main")
        print("Closing watering system")


if __name__ == "__main__":
    valid_plants: list[str] = [
        "Tomato",
        "Lettuce",
        "Carrots"
    ]
    invalid_plants: list[str] = [
        "Tomato",
        "lettuce",
        "carrots"
    ]
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    test_watering_system(valid_plants)
    print()
    print("Testing invalid plants...")
    test_watering_system(invalid_plants)
    print()
    print("Cleanup always happens, even with errors!")
