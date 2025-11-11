"""
Tests for Lexi AI Ethical Guardrails
"""

import unittest
from datetime import datetime, timedelta
from lexi.guardrails import EthicalGuardrails
from lexi.persona import VirtualPersona


class TestEthicalGuardrails(unittest.TestCase):
    """Test cases for Ethical Guardrails functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.guardrails = EthicalGuardrails()
        self.test_user_id = "test_guardrails_user"
        self.persona = VirtualPersona(self.test_user_id)
    
    def tearDown(self):
        """Clean up test data"""
        import os
        filepath = self.persona._get_persona_file()
        if os.path.exists(filepath):
            os.remove(filepath)
    
    def test_limit_recommendations(self):
        """Test that recommendations are limited"""
        recommendations = [
            {"title": f"Movie {i}"} for i in range(10)
        ]
        
        filtered = self.guardrails._limit_recommendations(recommendations)
        
        self.assertLessEqual(
            len(filtered), 
            self.guardrails.MAX_RECOMMENDATIONS_PER_SESSION
        )
    
    def test_limit_choices(self):
        """Test decision fatigue mitigation by limiting choices"""
        options = [
            {"option": {"name": f"Option {i}"}, "score": i} 
            for i in range(10)
        ]
        
        limited = self.guardrails.limit_choices(options, max_choices=3)
        
        self.assertEqual(len(limited), 3)
    
    def test_negative_filters_applied(self):
        """Test that negative filters are applied"""
        # Add negative preference to persona
        self.persona.update_preference(
            {"genre": "horror"},
            "negative",
            "media"
        )
        
        recommendations = [
            {"title": "Good Movie", "genre": "comedy"},
            {"title": "Scary Movie", "genre": "horror"},
            {"title": "Drama Film", "genre": "drama"}
        ]
        
        filtered = self.guardrails.filter_recommendations(
            recommendations,
            self.persona
        )
        
        # Horror movie should be filtered out
        titles = [r['title'] for r in filtered]
        self.assertNotIn("Scary Movie", titles)
        self.assertIn("Good Movie", titles)
    
    def test_usage_limits_tracking(self):
        """Test usage limits are tracked"""
        # Simulate interactions
        for i in range(5):
            self.persona.update_preference(
                {"item": f"Item {i}"},
                "positive",
                "test"
            )
        
        status = self.guardrails.check_usage_limits(self.persona)
        
        self.assertIn('interactions_today', status)
        self.assertIn('limit', status)
        self.assertIn('percentage_used', status)
        self.assertEqual(status['interactions_today'], 5)
    
    def test_usage_warnings(self):
        """Test that usage warnings are generated"""
        # Simulate many interactions
        for i in range(45):
            self.persona.update_preference(
                {"item": f"Item {i}"},
                "positive",
                "test"
            )
        
        status = self.guardrails.check_usage_limits(self.persona)
        
        # Should have warning at 90% usage
        self.assertGreater(len(status['warnings']), 0)
    
    def test_break_suggestion(self):
        """Test break suggestions"""
        # Add recent interactions
        for i in range(15):
            self.persona.update_preference(
                {"item": f"Item {i}"},
                "positive",
                "test"
            )
        
        should_break = self.guardrails.suggest_break(self.persona)
        
        # With 15 recent interactions, should suggest break
        self.assertTrue(should_break)
    
    def test_health_report(self):
        """Test health report generation"""
        report = self.guardrails.get_health_report(self.persona)
        
        self.assertIn('usage_status', report)
        self.assertIn('break_recommended', report)
        self.assertIn('health_tips', report)
        self.assertIsInstance(report['health_tips'], list)


if __name__ == '__main__':
    unittest.main()
