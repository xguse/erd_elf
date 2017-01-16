#!/usr/bin/env python
"""Provide logic to import, parse, and recode project data into usable structures for analysis."""

# Imports
import os
from pathlib import Path
import logging

import pandas as pd
import numpy as np

from munch import Munch

import erd_elf.errors as e

# Metadata
__author__ = "Gus Dunn"
__email__ = "w.gus.dunn@gmail.com"


# Functions
def load_relations(path):
    """Return dataframe of loaded and recoded "relationships".
    
    Args:
        path (Path): Path obj to input file.
    
    Returns:
        pd.DataFrame
    """
    
    df = pd.read_csv(str(path))
    
    return df
