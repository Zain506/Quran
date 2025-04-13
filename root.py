"""
Author: Zain Nomani
Date: 12.4.2024
Description: Arabic root which stores arabic letters, description and words associated with it (graphically)
"""
class Word:
    """
    Arabic word with description of meaning, and references to where it is found in Qur'an
    Initialise with just Arabic and Description.
    Then add root and reference
    """
    def __init__(self, arabic: str, description: str, root: "Root", references: set):
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

class Root:
    """
    When adding derivation, sync up references
    Initialise root with just Arabic and Description
    Then add later
    """
    def __init__(self, arabic: str = None, description: str = None, words: dict = {}):
        self.arabic: str = arabic
        self.description: str = description
        self.words: dict = {} # Referenced by arabic spelling ie arabic: Word

    def add(self, new: Word) -> None:
        """Add Word to current Root"""
        if new.arabic in self.words:
            self.words[new.arabic].addRef(new.references)
        else:
            self.words[new.arabic] = new
            new.setRoot(self)
