"""
Ethical Guardrails Module
Implements safeguards to protect user mental health and prevent over-engagement
"""

from typing import List, Dict, Any
from datetime import datetime, timedelta


class EthicalGuardrails:
    """
    Ethical Guardrails to ensure Lexi AI respects user wellbeing.
    
    Unlike engagement-focused AIs, these guardrails actively prevent:
    - Overwhelming users with too many options
    - Encouraging addictive behavior patterns
    - Disrespecting user time and mental energy
    """
    
    # Configuration for ethical limits
    MAX_RECOMMENDATIONS_PER_SESSION = 5
    MAX_DAILY_INTERACTIONS = 50
    COOLDOWN_PERIOD_MINUTES = 30
    
    def __init__(self):
        """Initialize ethical guardrails."""
        self.interaction_log = []
    
    def filter_recommendations(
        self, 
        recommendations: List[Dict[str, Any]], 
        persona: Any,
        context: Dict[str, Any] = None
    ) -> List[Dict[str, Any]]:
        """
        Filter recommendations through ethical guardrails.
        
        Args:
            recommendations: List of recommendation items
            persona: User's virtual persona
            context: Optional context information
            
        Returns:
            Filtered list of recommendations
        """
        filtered = recommendations.copy()
        
        # Limit number of recommendations to prevent overwhelm
        filtered = self._limit_recommendations(filtered)
        
        # Apply negative filters from persona
        filtered = self._apply_negative_filters(filtered, persona)
        
        # Check for engagement patterns and warn if necessary
        self._check_engagement_patterns(persona)
        
        return filtered
    
    def limit_choices(self, options: List[Dict[str, Any]], max_choices: int = 3) -> List[Dict[str, Any]]:
        """
        Limit choices to combat decision fatigue.
        
        This is a core feature - actively reducing options rather than
        overwhelming users with choices.
        
        Args:
            options: List of options
            max_choices: Maximum number of choices to present
            
        Returns:
            Limited list of best options
        """
        # Take only the top-scored options
        return options[:max_choices]
    
    def check_usage_limits(self, persona: Any) -> Dict[str, Any]:
        """
        Check if user is approaching usage limits.
        
        This helps prevent over-reliance and protects mental health.
        
        Args:
            persona: User's virtual persona
            
        Returns:
            Dictionary with usage status and warnings
        """
        today = datetime.now().date()
        
        # Count today's interactions
        today_interactions = sum(
            1 for interaction in persona.interaction_history
            if datetime.fromisoformat(interaction['timestamp']).date() == today
        )
        
        status = {
            'interactions_today': today_interactions,
            'limit': self.MAX_DAILY_INTERACTIONS,
            'percentage_used': (today_interactions / self.MAX_DAILY_INTERACTIONS) * 100,
            'warnings': []
        }
        
        # Add warnings based on usage
        if today_interactions >= self.MAX_DAILY_INTERACTIONS:
            status['warnings'].append(
                "Daily interaction limit reached. Take a break and trust your own judgment!"
            )
        elif today_interactions >= self.MAX_DAILY_INTERACTIONS * 0.8:
            status['warnings'].append(
                "You're using Lexi AI quite a bit today. Remember, it's a tool to help efficiency, not replace your autonomy."
            )
        
        return status
    
    def suggest_break(self, persona: Any) -> bool:
        """
        Suggest if user should take a break.
        
        Args:
            persona: User's virtual persona
            
        Returns:
            True if break is recommended
        """
        if not persona.interaction_history:
            return False
        
        # Check recent interaction frequency
        now = datetime.now()
        recent_cutoff = now - timedelta(minutes=self.COOLDOWN_PERIOD_MINUTES)
        
        recent_interactions = sum(
            1 for interaction in persona.interaction_history
            if datetime.fromisoformat(interaction['timestamp']) > recent_cutoff
        )
        
        # If more than 10 interactions in cooldown period, suggest break
        return recent_interactions > 10
    
    def _limit_recommendations(self, recommendations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Limit number of recommendations per session.
        
        Args:
            recommendations: List of recommendations
            
        Returns:
            Limited list
        """
        return recommendations[:self.MAX_RECOMMENDATIONS_PER_SESSION]
    
    def _apply_negative_filters(
        self, 
        recommendations: List[Dict[str, Any]], 
        persona: Any
    ) -> List[Dict[str, Any]]:
        """
        Apply user's negative filters to recommendations.
        
        This is crucial for respecting user boundaries and preferences.
        
        Args:
            recommendations: List of recommendations
            persona: User's virtual persona
            
        Returns:
            Filtered list with negative filters applied
        """
        negative_filters = persona.get_negative_filters()
        
        filtered = []
        for rec in recommendations:
            should_include = True
            
            # Check each negative filter category
            for category, filters in negative_filters.items():
                for key, blocked_values in filters.items():
                    if key in rec and rec[key] in blocked_values:
                        should_include = False
                        break
                
                if not should_include:
                    break
            
            if should_include:
                filtered.append(rec)
        
        return filtered
    
    def _check_engagement_patterns(self, persona: Any):
        """
        Check for potentially unhealthy engagement patterns.
        
        Args:
            persona: User's virtual persona
        """
        # Log this check
        self.interaction_log.append({
            'timestamp': datetime.now().isoformat(),
            'type': 'engagement_check'
        })
        
        # Could be extended to detect patterns like:
        # - Using recommendations as procrastination
        # - Over-reliance on AI for simple decisions
        # - Late-night usage affecting sleep
        pass
    
    def get_health_report(self, persona: Any) -> Dict[str, Any]:
        """
        Generate a report on healthy usage of Lexi AI.
        
        Args:
            persona: User's virtual persona
            
        Returns:
            Dictionary with health metrics and suggestions
        """
        usage_limits = self.check_usage_limits(persona)
        should_break = self.suggest_break(persona)
        
        report = {
            'usage_status': usage_limits,
            'break_recommended': should_break,
            'health_tips': [
                "Use Lexi AI to save mental energy, not replace decision-making skills",
                "The goal is efficiency, not dependency",
                "Trust your own judgment for important decisions"
            ]
        }
        
        if should_break:
            report['health_tips'].insert(0, "Consider taking a break - you've been quite active recently")
        
        return report
