"""
Recommendation Engine Module
Generates hyper-personalized recommendations based on user preferences
"""

from typing import List, Dict, Any
import random


class RecommendationEngine:
    """
    Recommendation Engine for generating personalized suggestions.
    
    Unlike typical recommendation engines that optimize for engagement,
    this one optimizes for user efficiency and preference matching.
    """
    
    def __init__(self):
        """Initialize the recommendation engine."""
        # In a real implementation, this would connect to databases,
        # APIs, or ML models. For the prototype, we'll use a simple approach.
        self.recommendation_sources = {}
    
    def generate(
        self, 
        preferences: Dict[str, Any], 
        category: str, 
        context: Dict[str, Any] = None,
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """
        Generate recommendations based on user preferences.
        
        Args:
            preferences: User preferences from Virtual Persona
            category: Category to generate recommendations for
            context: Optional context (time, mood, etc.)
            limit: Maximum number of recommendations
            
        Returns:
            List of recommended items
        """
        recommendations = []
        
        # In a real system, this would query databases or APIs
        # For the prototype, we generate sample recommendations
        recommendations = self._generate_sample_recommendations(
            preferences, category, limit
        )
        
        # Score and rank recommendations
        scored_recs = self._score_recommendations(recommendations, preferences)
        
        # Sort by score
        scored_recs.sort(key=lambda x: x.get('score', 0), reverse=True)
        
        return scored_recs[:limit]
    
    def _generate_sample_recommendations(
        self, 
        preferences: Dict[str, Any], 
        category: str, 
        limit: int
    ) -> List[Dict[str, Any]]:
        """
        Generate sample recommendations for demonstration.
        
        In a production system, this would be replaced with actual
        recommendation algorithms and data sources.
        
        Args:
            preferences: User preferences
            category: Category of recommendations
            limit: Number of recommendations to generate
            
        Returns:
            List of sample recommendations
        """
        # Sample data based on category
        sample_data = {
            'media': [
                {'title': 'Dune', 'genre': 'sci-fi', 'type': 'movie', 'director': 'Villeneuve'},
                {'title': 'The Expanse', 'genre': 'sci-fi', 'type': 'series', 'creator': 'Franck'},
                {'title': 'Arrival', 'genre': 'sci-fi', 'type': 'movie', 'director': 'Villeneuve'},
                {'title': 'Black Mirror', 'genre': 'sci-fi', 'type': 'series', 'creator': 'Brooker'},
                {'title': 'Ex Machina', 'genre': 'sci-fi', 'type': 'movie', 'director': 'Garland'},
            ],
            'style': [
                {'item': 'Minimalist Watch', 'style': 'minimalist', 'color': 'black'},
                {'item': 'Classic Sneakers', 'style': 'casual', 'color': 'white'},
                {'item': 'Modern Backpack', 'style': 'minimalist', 'color': 'gray'},
            ],
            'food': [
                {'dish': 'Grilled Salmon', 'cuisine': 'seafood', 'healthy': True},
                {'dish': 'Veggie Bowl', 'cuisine': 'healthy', 'healthy': True},
                {'dish': 'Pasta Carbonara', 'cuisine': 'italian', 'healthy': False},
            ]
        }
        
        # Get sample data for category or generate generic
        items = sample_data.get(category, [
            {'name': f'Item {i}', 'category': category} 
            for i in range(limit)
        ])
        
        return items[:limit]
    
    def _score_recommendations(
        self, 
        recommendations: List[Dict[str, Any]], 
        preferences: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """
        Score recommendations based on preference matching.
        
        Args:
            recommendations: List of recommendations
            preferences: User preferences
            
        Returns:
            Recommendations with scores added
        """
        positive_prefs = preferences.get('positive', {})
        negative_prefs = preferences.get('negative', {})
        
        for rec in recommendations:
            score = 0.5  # Neutral base score
            
            # Increase score for positive matches
            for key, values in positive_prefs.items():
                if key in rec:
                    if isinstance(values, list):
                        if rec[key] in values:
                            score += 0.3
                    elif rec[key] == values:
                        score += 0.3
            
            # Decrease score for negative matches
            for key, values in negative_prefs.items():
                if key in rec:
                    if isinstance(values, list):
                        if rec[key] in values:
                            score -= 0.5
                    elif rec[key] == values:
                        score -= 0.5
            
            # Keep score in valid range
            rec['score'] = max(0, min(1, score))
            
            # Add confidence level
            if score > 0.8:
                rec['confidence'] = 'high'
            elif score > 0.5:
                rec['confidence'] = 'medium'
            else:
                rec['confidence'] = 'low'
        
        return recommendations
    
    def explain_recommendation(self, item: Dict[str, Any], preferences: Dict[str, Any]) -> str:
        """
        Explain why an item was recommended.
        
        Transparency is important for user trust and autonomy.
        
        Args:
            item: Recommended item
            preferences: User preferences
            
        Returns:
            Human-readable explanation
        """
        reasons = []
        positive_prefs = preferences.get('positive', {})
        
        for key, values in positive_prefs.items():
            if key in item:
                if isinstance(values, list) and item[key] in values:
                    reasons.append(f"matches your preference for {key}: {item[key]}")
                elif item[key] == values:
                    reasons.append(f"matches your preference for {key}")
        
        if reasons:
            return f"Recommended because it {', '.join(reasons)}"
        
        return "Recommended based on general preferences"
    
    def register_source(self, category: str, source_function):
        """
        Register a data source for a category.
        
        This allows extending the recommendation engine with real data sources.
        
        Args:
            category: Category name
            source_function: Function that returns items for the category
        """
        self.recommendation_sources[category] = source_function
    
    def get_similar_items(self, item: Dict[str, Any], limit: int = 3) -> List[Dict[str, Any]]:
        """
        Find items similar to a given item.
        
        Args:
            item: Reference item
            limit: Maximum number of similar items
            
        Returns:
            List of similar items
        """
        # In a real system, this would use similarity algorithms
        # For the prototype, we return empty list
        return []
