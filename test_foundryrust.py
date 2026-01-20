# test_foundryrust.py
"""
Tests for FoundryRust module.
"""

import unittest
from foundryrust import FoundryRust

class TestFoundryRust(unittest.TestCase):
    """Test cases for FoundryRust class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FoundryRust()
        self.assertIsInstance(instance, FoundryRust)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FoundryRust()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
