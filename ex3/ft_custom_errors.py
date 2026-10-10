import typing


class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    raise WaterError("Not enough water in the tank!")


def test_errors() -> None:
    test_functions: list[typing.Callable[[], None]] = [
        check_plant,
        check_water
    ]
    error_types: list[type[GardenError]] = [
        PlantError,
        WaterError,
        GardenError
    ]
    for error_type in error_types:
        print()
        print(f"Testing {error_type.__name__}...")
        for func in test_functions:
            try:
                func()
            except (error_type) as error:
                print(
                    f"Caught {error.__class__.__name__}: {error}"
                )
            except GardenError:
                pass
    print()


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_errors()
