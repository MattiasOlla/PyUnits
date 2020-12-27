from . import quantities


class Unit:
    def __init__(
        self, name: str, quantity: quantities.Quantity, slope: float, intercept: float = 0
    ) -> None:
        self.name = name
        self.quantity = quantity
        self.slope = slope
        self.intercept = intercept

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"


class SIUnit(Unit):
    def __init__(self, name: str, quantity: quantities.Quantity) -> None:
        super().__init__(name, quantity, slope=1, intercept=0)


class SIUnits:
    kilogram = SIUnit("kg", quantities.Base.MASS)
    meter = SIUnit("m", quantities.Base.LENGTH)
    second = SIUnit("s", quantities.Base.TIME)
    kelvin = SIUnit("K", quantities.Base.TEMPERATURE)
    ampere = SIUnit("A", quantities.Base.CURRENT)
    mole = SIUnit("mol", quantities.Base.SUBSTANCE_AMOUNT)
    candela = SIUnit("cd", quantities.Base.LUMINOUS_INTENSITY)
    radian = SIUnit("rad", quantities.Base.PLANE_ANGLE)
    steradian = SIUnit("sr", quantities.Base.SOLID_ANGLE)

    quantity_map = {
        unit.quantity: unit
        for unit in [kilogram, meter, second, kelvin, ampere, mole, candela, radian, steradian]
    }
