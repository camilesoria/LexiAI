"""
Virtual Persona Module
Learns and maintains user preferences including positive preferences and negative filters
"""

from datetime import datetime
from typing import Dict, List, Any
import json
import os


class VirtualPersona:
    """
    Virtual Persona that learns and maintains user preferences.
    
    This is the "second brain" that remembers what the user likes and dislikes,
    helping to combat decision fatigue by filtering out unwanted options.
    """
    
    def __init__(self, user_id: str):
        """
        Initialize a Virtual Persona for a user.
        
        Args:
            user_id: Unique identifier for the user
        """
        self.user_id = user_id
        self.preferences = {
            'positive': {},  # Things the user likes
            'negative': {},  # Negative filters - things to avoid
            'neutral': {}    # Things user is indifferent about
        }
        self.interaction_history = []
        self.created_at = datetime.now().isoformat()
        self.last_updated = self.created_at
        
        # Load existing persona if available
        self._load_persona()
    
    def update_preference(self, item: Dict[str, Any], rating: str, category: str = "general"):
        """
        Update preferences based on user feedback.
        
        Args:
            item: Dictionary containing item attributes
            rating: 'positive', 'negative', or 'neutral'
            category: Category of the item
        """
        if rating not in ['positive', 'negative', 'neutral']:
            raise ValueError("Rating must be 'positive', 'negative', or 'neutral'")
        
        # Initialize category if not exists
        if category not in self.preferences[rating]:
            self.preferences[rating][category] = {}
        
        # Extract learnable attributes from the item
        for key, value in item.items():
            if key not in self.preferences[rating][category]:
                self.preferences[rating][category][key] = []
            
            # Add value if not already present
            if value not in self.preferences[rating][category][key]:
                self.preferences[rating][category][key].append(value)
        
        # Record the interaction
        self.interaction_history.append({
            'timestamp': datetime.now().isoformat(),
            'item': item,
            'rating': rating,
            'category': category
        })
        
        self.last_updated = datetime.now().isoformat()
        self._save_persona()
    
    def get_preferences(self, category: str = None) -> Dict[str, Any]:
        """
        Get preferences, optionally filtered by category.
        
        Args:
            category: Optional category filter
            
        Returns:
            Dictionary of preferences
        """
        if category is None:
            return self.preferences
        
        # Return preferences for specific category
        result = {
            'positive': self.preferences['positive'].get(category, {}),
            'negative': self.preferences['negative'].get(category, {}),
            'neutral': self.preferences['neutral'].get(category, {})
        }
        return result
    
    def get_negative_filters(self, category: str = None) -> Dict[str, List]:
        """
        Get negative filters (things to avoid).
        
        This is a key feature for combating decision fatigue - explicitly
        filtering out unwanted content.
        
        Args:
            category: Optional category filter
            
        Returns:
            Dictionary of negative filters
        """
        if category is None:
            return self.preferences['negative']
        
        return self.preferences['negative'].get(category, {})
    
    def get_summary(self) -> Dict[str, Any]:
        """
        Get a summary of the persona.
        
        Returns:
            Dictionary with persona summary information
        """
        total_prefs = sum(
            len(cats) for rating_type in self.preferences.values() 
            for cats in rating_type.values()
        )
        
        return {
            'user_id': self.user_id,
            'created_at': self.created_at,
            'last_updated': self.last_updated,
            'total_preferences': total_prefs,
            'total_interactions': len(self.interaction_history),
            'categories': list(set(
                cat for rating_type in self.preferences.values() 
                for cat in rating_type.keys()
            ))
        }
    
    def _get_persona_file(self) -> str:
        """Get the file path for storing persona data."""
        os.makedirs('user_data', exist_ok=True)
        return f'user_data/persona_{self.user_id}.json'
    
    def _save_persona(self):
        """Save persona to disk."""
        data = {
            'user_id': self.user_id,
            'preferences': self.preferences,
            'interaction_history': self.interaction_history,
            'created_at': self.created_at,
            'last_updated': self.last_updated
        }
        
        filepath = self._get_persona_file()
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
    
    def _load_persona(self):
        """Load persona from disk if it exists."""
        filepath = self._get_persona_file()
        
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                
                self.preferences = data.get('preferences', self.preferences)
                self.interaction_history = data.get('interaction_history', [])
                self.created_at = data.get('created_at', self.created_at)
                self.last_updated = data.get('last_updated', self.last_updated)
            except Exception as e:
                # If loading fails, start with fresh persona
                print(f"Warning: Could not load persona data: {e}")
