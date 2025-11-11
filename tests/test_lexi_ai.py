"""
Tests for main Lexi AI integration
"""

import unittest
import os
from lexi_ai import LexiAI


class TestLexiAI(unittest.TestCase):
    """Test cases for main Lexi AI functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_user_id = "test_lexi_user"
        self.lexi = LexiAI(self.test_user_id)
    
    def tearDown(self):
        """Clean up test data"""
        filepath = self.lexi.persona._get_persona_file()
        if os.path.exists(filepath):
            os.remove(filepath)
    
    def test_initialization(self):
        """Test Lexi AI initializes correctly"""
        self.assertEqual(self.lexi.user_id, self.test_user_id)
        self.assertIsNotNone(self.lexi.persona)
        self.assertIsNotNone(self.lexi.recommendation_engine)
        self.assertIsNotNone(self.lexi.guardrails)
    
    def test_learn_preference(self):
        """Test learning preferences"""
        item = {"title": "Test Movie", "genre": "sci-fi"}
        self.lexi.learn_preference(item, "positive", "media")
        
        summary = self.lexi.get_persona_summary()
        self.assertGreater(summary['total_preferences'], 0)
    
    def test_get_recommendations(self):
        """Test getting recommendations"""
        # Learn some preferences first
        self.lexi.learn_preference(
            {"genre": "sci-fi"},
            "positive",
            "media"
        )
        
        recommendations = self.lexi.get_recommendations("media", limit=3)
        
        # Should return list
        self.assertIsInstance(recommendations, list)
        # Should be limited
        self.assertLessEqual(len(recommendations), 5)
    
    def test_combat_decision_fatigue(self):
        """Test decision fatigue combat"""
        # Set preferences
        self.lexi.learn_preference(
            {"style": "minimalist"},
            "positive",
            "style"
        )
        
        options = [
            {"name": "Minimalist Watch", "style": "minimalist"},
            {"name": "Ornate Watch", "style": "ornate"},
            {"name": "Simple Band", "style": "minimalist"}
        ]
        
        filtered = self.lexi.combat_decision_fatigue("style", options)
        
        # Should filter and score options
        self.assertIsInstance(filtered, list)
        self.assertGreater(len(filtered), 0)
        
        # Should have reasoning
        for item in filtered:
            self.assertIn('reasoning', item)
            self.assertIn('option', item)
    
    def test_score_option(self):
        """Test option scoring"""
        preferences = {
            'positive': {'genre': ['sci-fi']},
            'negative': {'genre': ['horror']}
        }
        
        # Positive match
        option1 = {"genre": "sci-fi"}
        score1 = self.lexi._score_option(option1, preferences)
        self.assertGreater(score1, 0.5)
        
        # Negative match
        option2 = {"genre": "horror"}
        score2 = self.lexi._score_option(option2, preferences)
        self.assertLess(score2, 0.5)
    
    def test_explain_score(self):
        """Test score explanation"""
        preferences = {
            'positive': {'genre': ['sci-fi', 'drama']},
            'negative': {}
        }
        
        option = {"genre": "sci-fi", "title": "Test"}
        explanation = self.lexi._explain_score(option, preferences)
        
        self.assertIsInstance(explanation, str)
        self.assertIn("preference", explanation.lower())
    
    def test_persona_summary(self):
        """Test getting persona summary"""
        summary = self.lexi.get_persona_summary()
        
        self.assertIn('user_id', summary)
        self.assertIn('total_preferences', summary)
        self.assertEqual(summary['user_id'], self.test_user_id)


if __name__ == '__main__':
    unittest.main()
