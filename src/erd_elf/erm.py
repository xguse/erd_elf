#!/usr/bin/env python
"""Provide code to model entiy-relationships."""

# Imports


# Metadata
__author__ = "Gus Dunn"
__email__ = "w.gus.dunn@gmail.com"


# Functions
def add_relation_uids(df):
    """Add unique ID column to the 
    
    Extra information section
    
    Args:
        param1 (type): The first parameter.
        param2 (type): The second parameter.
    
    Returns:
        type: The return value. True for success, False otherwise.
    """
    df['relation_uid'] = df.object + "__" + df.relation.str.replace(' ','_')

# Classes
class BaseData(object):
    """Implement shared characteristics of ERD edge/node data objects."""
    def __init__(self):
        self.g = None
        self.label = None
        self.uid = None
        
    def __str__(self):
        return self.uid
        

class NodeData(BaseData):
    """docstring for NodeData"""
    def __init__(self, ):
        super(NodeData, self).__init__()
        self.arg = arg
        
        
        
class EdgeData(BaseData):
    """docstring for EdgeData"""
    def __init__(self, n1, n2, label):
        super(EdgeData, self).__init__()
        self.n1 = n1
        self.n2 = n2
        self.label = label
        

        
    
        


        