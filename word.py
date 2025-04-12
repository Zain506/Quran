"""
Author: Zain Nomani
Date: 12/4/2024
Description: Data Structure to store Arabic word, meaning and root
"""
from root import Root

class Word:
    """
    Arabic word with description of meaning, and references to where it is found in Qur'an
    Initialise with just Arabic and Description.
    Then add root and reference
    """
    def __init__(self, arabic: str, description: str, references: set, root: "Root" = None):
        self.arabic = arabic
        self.description = description
        self.references = references  # assume this is a set of tuples
        self.root = root
    
    def setRoot(self, newRoot: "Root") -> None:
        self.root = newRoot
    
    def setDesc(self, newDesc: str) -> None:
        self.description = newDesc
    
    def addRef(self, ref: tuple) -> None:
        self.references.add(ref)