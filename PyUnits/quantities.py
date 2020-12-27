# -*- coding: utf-8 -*-
from __future__ import annotations

from typing import NamedTuple


class Quantity(NamedTuple):
    mass: int = 0
    length: int = 0
    time: int = 0
    temperature: int = 0
    current: int = 0
    luminous_intensity: int = 0
    substance_amount: int = 0
    plane_angle: int = 0
    solid_angle: int = 0

    def short_dict(self) -> dict[str, int]:
        return dict(
            M=self.mass,
            L=self.length,
            T=self.time,
            Θ=self.temperature,
            I=self.current,
            N=self.substance_amount,
            J=self.luminous_intensity,
            A=self.plane_angle,
            S=self.solid_angle,
        )

    def __repr__(self) -> str:
        rep = ""
        for symbol, val in self.short_dict().items():
            if val == 1:
                rep += symbol
            elif val != 0:
                rep += f"{symbol}^{val}"
        return rep

    def __mul__(self, other: Quantity) -> Quantity:
        if not isinstance(other, Quantity):
            raise ValueError(f"Can't multiply types {type(self)} and {type(other)}")
        other_dict = other._asdict()
        return Quantity(
            **{symbol: val + other_dict[symbol] for symbol, val in self._asdict().items()}
        )

    def __truediv__(self, other: Quantity) -> Quantity:
        if not isinstance(other, Quantity):
            raise ValueError(f"Can't multiply types {type(self)} and {type(other)}")
        other_dict = other._asdict()
        return Quantity(
            **{symbol: val - other_dict[symbol] for symbol, val in self._asdict().items()}
        )

    def __pow__(self, exponent: int) -> Quantity:
        if not isinstance(exponent, int):
            raise ValueError(f"Can't raise type {type(self)} to exponent of type {type(exponent)}")
        return Quantity(**{symbol: val * exponent for symbol, val in self._asdict().items()})


# region BaseQuantities
M = Quantity(mass=1)
L = Quantity(length=1)
T = Quantity(time=1)
Θ = Quantity(temperature=1)
I = Quantity(current=1)  # noqa: E741
N = Quantity(substance_amount=1)
J = Quantity(luminous_intensity=1)
A = Quantity(plane_angle=1)
S = Quantity(solid_angle=1)
# endregion

# region DerivedQuantities
FREQUENCY = T ** -1
VELOCITY = L / T
ACCELERATON = VELOCITY / T
FORCE = M * ACCELERATON
MOMENTUM = M * VELOCITY
ENERGY = FORCE * L
AREA = L ** 2
VOLUME = L ** 3
ANGULAR_VELOCITY = A / T
DENSITY = M / VOLUME
PRESSURE = FORCE / AREA
POWER = ENERGY / T
CHARGE = I * T
LUMINANCE = J / S ** 2
HEAT_CAPACITY = ENERGY / T
MOLARITY = M / N
# endregion DerivedQuantities


if __name__ == "__main__":
    for quant in [
        M,
        L,
        T,
        Θ,
        I,
        N,
        J,
        A,
        S,
        FREQUENCY,
        VELOCITY,
        ACCELERATON,
        FORCE,
        MOMENTUM,
        ENERGY,
        AREA,
        VOLUME,
        ANGULAR_VELOCITY,
        DENSITY,
        PRESSURE,
        POWER,
        CHARGE,
        LUMINANCE,
        HEAT_CAPACITY,
        MOLARITY,
    ]:
        print(quant)
