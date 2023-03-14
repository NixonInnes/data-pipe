__all__ = [
    "PipeTransformerAdd",
    "PipeTransformerSubtract",
    "PipeTransformerMultiply",
    "PipeTransformerDivide",
    "PipeTransformerFloorDivide",
    "PipeTransformerPower",
    "PipeTransformerMath",
]

import pandas as pd
from typing import Any, Callable

from .. import PipeTransformer, PipePieces


@PipePieces.register_transformer("PipeTransformerMath")
class PipeTransformerMath(PipeTransformer):
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y,
        "floordiv": lambda x, y: x // y,
        "power": lambda x, y: x ** y,
    }

    @staticmethod
    def math(
        df: pd.DataFrame,
        source: str,
        value: Any,
        operation: str,
        result: str | None = None,
        value_is_column: bool = False,
    ):
        if operation not in PipeTransformerMath.operations:
            raise ValueError(f"Invalid operation: {operation}")
        
        if result is None:
            result = source
        if value_is_column:
            value = df[value]
        df[result] = PipeTransformerMath.operations[operation](df[source], value)
        return df
    
    _func: Callable = math


@PipePieces.register_transformer("PipeTransformerAdd")
class PipeTransformerAdd(PipeTransformer):
    @staticmethod
    def add(
        df: pd.DataFrame,
        source: str,
        value: Any,
        result: str | None = None,
        value_is_column: bool = False,
    ):
        if result is None:
            result = source
        if value_is_column:
            value = df[value]
        df[result] = df[source] + value
        return df

    _func: Callable = add


@PipePieces.register_transformer("PipeTransformerSubtract")
class PipeTransformerSubtract(PipeTransformer):
    @staticmethod
    def subtract(
        df: pd.DataFrame,
        source: str,
        value: Any,
        result: str | None = None,
        value_is_column: bool = False,
    ):
        if result is None:
            result = source
        if value_is_column:
            value = df[value]
        df[result] = df[source] - value
        return df

    _func: Callable = subtract


@PipePieces.register_transformer("PipeTransformerMultiply")
class PipeTransformerMultiply(PipeTransformer):
    @staticmethod
    def multiply(
        df: pd.DataFrame,
        source: str,
        value: Any,
        result: str | None = None,
        value_is_column: bool = False,
    ):
        if result is None:
            result = source
        if value_is_column:
            value = df[value]
        df[result] = df[source] * value
        return df

    _func: Callable = multiply


@PipePieces.register_transformer("PipeTransformerDivide")
class PipeTransformerDivide(PipeTransformer):
    @staticmethod
    def divide(
        df: pd.DataFrame,
        source: str,
        value: Any,
        result: str | None = None,
        value_is_column: bool = False,
    ):
        if result is None:
            result = source
        if value_is_column:
            value = df[value]
        df[result] = df[source] / value
        return df

    _func: Callable = divide


@PipePieces.register_transformer("PipeTransformerFloorDivide")
class PipeTransformerFloorDivide(PipeTransformer):
    @staticmethod
    def floordiv(
        df: pd.DataFrame,
        source: str,
        value: Any,
        result: str | None = None,
        value_is_column: bool = False,
    ):
        if result is None:
            result = source
        if value_is_column:
            value = df[value]
        df[result] = df[source] // value
        return df

    _func: Callable = floordiv


@PipePieces.register_transformer("PipeTransformerPower")
class PipeTransformerPower(PipeTransformer):
    @staticmethod
    def power(
        df: pd.DataFrame,
        source: str,
        value: Any,
        result: str | None = None,
        value_is_column: bool = False,
    ):
        if result is None:
            result = source
        if value_is_column:
            value = df[value]
        df[result] = df[source] ** value
        return df

    _func: Callable = power