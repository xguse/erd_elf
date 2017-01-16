#!/usr/bin/env python
"""Provide error classes for erd_elf."""

# Imports


# Metadata
__author__ = "Gus Dunn"
__email__ = "w.gus.dunn@gmail.com"




class ErdElfError(Exception):

    """Base error class for erd_elf."""


class ValidationError(ErdElfError):

    """Raise when a validation/sanity check comes back with unexpected value."""
