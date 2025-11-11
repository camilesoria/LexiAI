"""
Lexi AI Package
Hyper-personalized AI assistant with ethical guardrails
"""

__version__ = "0.1.0"
__author__ = "Lexi AI Team"

from .persona import VirtualPersona
from .recommendations import RecommendationEngine
from .guardrails import EthicalGuardrails

__all__ = ['VirtualPersona', 'RecommendationEngine', 'EthicalGuardrails']
