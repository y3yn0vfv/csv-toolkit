"""Small CLI utilities for slicing, filtering and joining CSV files."""

from __future__ import annotations

__all__ = ["csvToolkit"]


def csvToolkit(value):
    """Small CLI utilities for slicing, filtering and joining CSV files."""
    if value is None:
        raise ValueError("value must not be None")
    return value
