"""
Lexi AI - Hyper-Personalized AI Assistant
Main module for orchestrating the AI assistant functionality
"""

from lexi.persona import VirtualPersona
from lexi.recommendations import RecommendationEngine
from lexi.guardrails import EthicalGuardrails


class LexiAI:
    """
    Main Lexi AI Assistant class.
    
    Combines Virtual Persona, Recommendation Engine, and Ethical Guardrails
    to provide hyper-personalized recommendations while respecting user wellbeing.
    """
    
    def __init__(self, user_id: str):
        """
        Initialize Lexi AI for a specific user.
        
        Args:
            user_id: Unique identifier for the user
        """
        self.user_id = user_id
        self.persona = VirtualPersona(user_id)
        self.recommendation_engine = RecommendationEngine()
        self.guardrails = EthicalGuardrails()
        
    def learn_preference(self, item: dict, rating: str, category: str = "general"):
        """
        Learn from user feedback on an item.
        
        Args:
            item: Dictionary containing item details
            rating: User rating ('positive', 'negative', 'neutral')
            category: Category of the item (e.g., 'media', 'style', 'food')
        """
        self.persona.update_preference(item, rating, category)
        
    def get_recommendations(self, category: str, context: dict = None, limit: int = 5):
        """
        Get personalized recommendations for the user.
        
        Args:
            category: Category to get recommendations for
            context: Optional context information (time of day, mood, etc.)
            limit: Maximum number of recommendations to return
            
        Returns:
            List of recommended items filtered by ethical guardrails
        """
        # Get user preferences from persona
        preferences = self.persona.get_preferences(category)
        
        # Generate recommendations based on preferences
        recommendations = self.recommendation_engine.generate(
            preferences, category, context, limit
        )
        
        # Apply ethical guardrails
        filtered_recommendations = self.guardrails.filter_recommendations(
            recommendations, self.persona, context
        )
        
        return filtered_recommendations
    
    def get_persona_summary(self):
        """
        Get a summary of the user's virtual persona.
        
        Returns:
            Dictionary containing persona information
        """
        return self.persona.get_summary()
    
    def combat_decision_fatigue(self, category: str, options: list):
        """
        Help user make decisions by filtering options based on learned preferences.
        
        Args:
            category: Category of the decision
            options: List of options to choose from
            
        Returns:
            Filtered and ranked list of options
        """
        preferences = self.persona.get_preferences(category)
        
        # Score each option based on preferences
        scored_options = []
        for option in options:
            score = self._score_option(option, preferences)
            if score > 0:  # Only include options that match preferences
                scored_options.append({
                    'option': option,
                    'score': score,
                    'reasoning': self._explain_score(option, preferences)
                })
        
        # Sort by score descending
        scored_options.sort(key=lambda x: x['score'], reverse=True)
        
        # Apply guardrails to limit choices
        return self.guardrails.limit_choices(scored_options)
    
    def _score_option(self, option: dict, preferences: dict) -> float:
        """
        Score an option based on user preferences.
        
        Args:
            option: Option to score
            preferences: User preferences
            
        Returns:
            Score between 0 and 1
        """
        score = 0.5  # Neutral starting score
        
        # Check positive preferences
        for key, value in preferences.get('positive', {}).items():
            if key in option and option[key] in value:
                score += 0.2
        
        # Check negative filters - strong penalty
        for key, value in preferences.get('negative', {}).items():
            if key in option and option[key] in value:
                score -= 0.5
        
        return max(0, min(1, score))
    
    def _explain_score(self, option: dict, preferences: dict) -> str:
        """
        Explain why an option received its score.
        
        Args:
            option: Option that was scored
            preferences: User preferences
            
        Returns:
            Human-readable explanation
        """
        reasons = []
        
        for key, value in preferences.get('positive', {}).items():
            if key in option and option[key] in value:
                reasons.append(f"Matches your preference for {key}: {option[key]}")
        
        if reasons:
            return " | ".join(reasons)
        
        return "Neutral - no strong preference match"


def main():
    """Example usage of Lexi AI"""
    print("=== Lexi AI - Hyper-Personalized AI Assistant ===\n")
    
    # Initialize Lexi AI for a user
    lexi = LexiAI("user_001")
    
    # Learn some preferences
    print("Learning user preferences...")
    lexi.learn_preference(
        {"title": "Inception", "genre": "sci-fi", "director": "Nolan"},
        "positive",
        "media"
    )
    lexi.learn_preference(
        {"title": "Reality Show X", "genre": "reality", "type": "tv"},
        "negative",
        "media"
    )
    
    print("✓ Preferences learned\n")
    
    # Get persona summary
    print("Virtual Persona Summary:")
    summary = lexi.get_persona_summary()
    print(f"User ID: {summary['user_id']}")
    print(f"Preferences tracked: {summary['total_preferences']}")
    print()
    
    # Combat decision fatigue example
    print("Combating Decision Fatigue - Movie Selection:")
    movie_options = [
        {"title": "Interstellar", "genre": "sci-fi", "director": "Nolan"},
        {"title": "The Bachelor", "genre": "reality", "type": "tv"},
        {"title": "Blade Runner", "genre": "sci-fi", "director": "Scott"},
    ]
    
    filtered = lexi.combat_decision_fatigue("media", movie_options)
    print(f"Reduced from {len(movie_options)} options to {len(filtered)} best matches:")
    for item in filtered:
        print(f"  - {item['option']['title']}: {item['reasoning']}")
    
    print("\n✓ Lexi AI is working to reduce decision fatigue!")


if __name__ == "__main__":
    main()
