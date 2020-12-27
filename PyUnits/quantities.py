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


class Base:
    MASS = Quantity(mass=1)
    LENGTH = Quantity(length=1)
    TIME = Quantity(time=1)
    TEMPERATURE = Quantity(temperature=1)
    CURRENT = Quantity(current=1)
    SUBSTANCE_AMOUNT = Quantity(substance_amount=1)
    LUMINOUS_INTENSITY = Quantity(luminous_intensity=1)
    PLANE_ANGLE = Quantity(plane_angle=1)
    SOLID_ANGLE = Quantity(solid_angle=1)


class Derived:
    FREQUENCY = Base.TIME ** -1
    VELOCITY = Base.LENGTH / Base.TIME
    ACCELERATON = VELOCITY / Base.TIME
    FORCE = Base.MASS * ACCELERATON
    MOMENTUM = Base.MASS * VELOCITY
    ENERGY = FORCE * Base.LENGTH
    AREA = Base.LENGTH ** 2
    VOLUME = Base.LENGTH ** 3
    ANGULAR_VELOCITY = Base.PLANE_ANGLE / Base.TIME
    DENSITY = Base.MASS / VOLUME
    PRESSURE = FORCE / AREA
    POWER = ENERGY / Base.TIME
    CHARGE = Base.CURRENT * Base.TIME
    LUMINANCE = Base.LUMINOUS_INTENSITY / Base.SOLID_ANGLE ** 2
    HEAT_CAPACITY = ENERGY / Base.TEMPERATURE
    MOLARITY = Base.MASS / Base.SUBSTANCE_AMOUNT


if __name__ == "__main__":
    for name, rep in (vars(Base) | vars(Derived)).items():
        if isinstance(rep, Quantity):
            print(name, rep)
