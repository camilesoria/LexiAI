"""
Tests for Lexi AI Virtual Persona
"""

import unittest
import os
import json
import tempfile
from lexi.persona import VirtualPersona


class TestVirtualPersona(unittest.TestCase):
    """Test cases for Virtual Persona functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_user_id = "test_user_123"
        self.persona = VirtualPersona(self.test_user_id)
    
    def tearDown(self):
        """Clean up test data"""
        # Remove test persona file if exists
        filepath = self.persona._get_persona_file()
        if os.path.exists(filepath):
            os.remove(filepath)
    
    def test_persona_initialization(self):
        """Test persona initializes correctly"""
        self.assertEqual(self.persona.user_id, self.test_user_id)
        self.assertIn('positive', self.persona.preferences)
        self.assertIn('negative', self.persona.preferences)
        self.assertIn('neutral', self.persona.preferences)
    
    def test_update_positive_preference(self):
        """Test adding positive preference"""
        item = {"title": "Test Movie", "genre": "sci-fi"}
        self.persona.update_preference(item, "positive", "media")
        
        prefs = self.persona.get_preferences("media")
        self.assertIn("media", self.persona.preferences['positive'])
        self.assertIn("title", prefs['positive'])
        self.assertIn("Test Movie", prefs['positive']['title'])
    
    def test_update_negative_preference(self):
        """Test adding negative preference (filter)"""
        item = {"genre": "horror"}
        self.persona.update_preference(item, "negative", "media")
        
        filters = self.persona.get_negative_filters("media")
        self.assertIn("genre", filters)
        self.assertIn("horror", filters['genre'])
    
    def test_invalid_rating(self):
        """Test that invalid ratings raise error"""
        item = {"title": "Test"}
        with self.assertRaises(ValueError):
            self.persona.update_preference(item, "invalid", "media")
    
    def test_interaction_history(self):
        """Test interaction history is tracked"""
        initial_count = len(self.persona.interaction_history)
        
        item = {"title": "Test"}
        self.persona.update_preference(item, "positive", "media")
        
        self.assertEqual(len(self.persona.interaction_history), initial_count + 1)
        self.assertEqual(self.persona.interaction_history[-1]['item'], item)
        self.assertEqual(self.persona.interaction_history[-1]['rating'], "positive")
    
    def test_get_summary(self):
        """Test persona summary generation"""
        summary = self.persona.get_summary()
        
        self.assertIn('user_id', summary)
        self.assertIn('total_preferences', summary)
        self.assertIn('total_interactions', summary)
        self.assertIn('categories', summary)
        self.assertEqual(summary['user_id'], self.test_user_id)
    
    def test_persistence(self):
        """Test that persona data persists"""
        # Add a preference
        item = {"title": "Persistent Movie", "genre": "drama"}
        self.persona.update_preference(item, "positive", "media")
        
        # Create new persona instance with same user_id
        new_persona = VirtualPersona(self.test_user_id)
        
        # Check that preference was loaded
        prefs = new_persona.get_preferences("media")
        self.assertIn("title", prefs['positive'])
        self.assertIn("Persistent Movie", prefs['positive']['title'])


if __name__ == '__main__':
    unittest.main()
