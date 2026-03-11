# SPDX-FileCopyrightText: 2026 EasyScience contributors <https://github.com/easyscience>
# SPDX-License-Identifier: BSD-3-Clause
"""Utility functions for EasyPeasy."""

from __future__ import annotations


def dummy_method(
    left: str,
    right: str,
) -> str:
    """Dummy method for testing. It concatenates the left and right
    strings.

    Args:
        left (str): Left side of the new string.
        right (bool): Right side of the new string.
        middle (int): Middle part of the new string.

    Returns:
        str: The output string.
    """

    output = left + right
    return output


def dummy_method_2(left, right):
    """Dummy method for testing. It concatenates the left and right
    strings.

    Args:
        left (bool): Left side of the new string.
        right (str): Right side of the new string.

    Returns:
        str: The output string.
    """

    output = left + right
    return output


def dummy_method_3(left, right):
    """Dummy method for testing.

    It concatenates the left and right strings.
    """

    output = left + right
    return output
