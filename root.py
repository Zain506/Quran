"""
Author: Zain Nomani
Date: 12.4.2024
Description: Arabic root which stores arabic letters, description and words associated with it (graphically)
"""
from word import Word

class Root:
    """
    When adding derivation, sync up references
    Initialise root with just Arabic and Description
    Then add later
    """
    def __init__(self, root: str = None, description: str = None, words: dict = {}):
        self.root: str = root
        self.description: str = description
        self.words: dict = {} # Referenced by arabic spelling ie arabic: Word

    def add(self, new: Word) -> None:
        """Add Word to current Root"""
        if new.arabic in self.words:
            self.words[new.arabic].addRef(new.references)
        else:
            self.words[new.arabic] = new
            new.setRoot(self)
