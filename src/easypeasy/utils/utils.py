# SPDX-FileCopyrightText: 2026 EasyScience contributors <https://github.com/easyscience>
# SPDX-License-Identifier: BSD-3-Clause
"""Utility functions for EasyPeasy."""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


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

    logger.debug('Calling dummy method')

    return left + right
