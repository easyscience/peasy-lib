# SPDX-FileCopyrightText: 2021-2026 EasyDiffraction contributors <https://github.com/easyscience/diffraction>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations


def dummy_method(
    left: str,
    right: str,
) -> str:
    """Dummy method for testing. It concatenates the left and right
    strings.

    Args:
        left (str): Left side of the new string.
        right (str): Right side of the new string.

    Returns:
        str: The output string.
    """

    output = left + right
    return output
