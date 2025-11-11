# LexiAI 🎯

**Hyper-Personalized AI Assistant with Ethical Guardrails**

Lexi AI é um protótipo de assistente de IA focado em recomendações hiper-personalizadas, combatendo a 'fadiga de decisão' ao construir uma 'Persona Virtual' que aprende as preferências do usuário, incluindo filtros negativos específicos. Este projeto é construído com 'Guardrails Éticos', respeitando a saúde mental e evitando dependência emocional.

## 🌟 Core Features

### 1. Virtual Persona - Your Second Brain
- **Learns your preferences** across multiple categories (media, style, food, etc.)
- **Negative filters**: Explicitly remembers what you DON'T want
- **Persistent memory**: Saves your preferences across sessions
- **Privacy-focused**: All data stored locally

### 2. Ethical Guardrails 🛡️
Unlike engagement-focused AIs, Lexi AI includes built-in safeguards:
- **Limited recommendations**: Max 5 per session to prevent overwhelm
- **Usage limits**: Daily interaction caps to prevent dependency
- **Break suggestions**: Encourages autonomy when detecting heavy usage
- **Transparency**: Explains why recommendations are made

### 3. Decision Fatigue Combat
- **Option reduction**: Narrows down choices based on your preferences
- **Smart filtering**: Automatically removes options you've indicated you dislike
- **Confidence scoring**: Shows how well each option matches your profile
- **Reasoning provided**: Explains why each option is suggested

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/camilesoria/LexiAI.git
cd LexiAI

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

#### 1. Interactive CLI
```bash
python cli.py
```

The CLI provides an interactive interface to:
- Learn your preferences
- Get personalized recommendations
- Combat decision fatigue by filtering options
- View your virtual persona
- Check ethical health status

#### 2. Python API
```python
from lexi_ai import LexiAI

# Initialize for a user
lexi = LexiAI("user_001")

# Learn preferences
lexi.learn_preference(
    {"title": "Inception", "genre": "sci-fi", "director": "Nolan"},
    "positive",
    "media"
)

# Add negative filters
lexi.learn_preference(
    {"genre": "reality", "type": "tv"},
    "negative",
    "media"
)

# Get recommendations
recommendations = lexi.get_recommendations("media", limit=5)

# Combat decision fatigue
options = [
    {"title": "Interstellar", "genre": "sci-fi"},
    {"title": "Reality Show", "genre": "reality"},
    {"title": "Blade Runner", "genre": "sci-fi"}
]
filtered = lexi.combat_decision_fatigue("media", options)
```

#### 3. Run Demo
```bash
python lexi_ai.py
```

## 📁 Project Structure

```
LexiAI/
├── lexi/                      # Main package
│   ├── __init__.py           # Package initialization
│   ├── persona.py            # Virtual Persona system
│   ├── recommendations.py    # Recommendation engine
│   └── guardrails.py         # Ethical guardrails
├── lexi_ai.py                # Main LexiAI class and demo
├── cli.py                    # Interactive CLI interface
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## 🎯 Philosophy

### What Makes Lexi AI Different?

1. **Anti-Engagement Design**: Unlike most AIs that maximize engagement, Lexi AI optimizes for your efficiency and wellbeing.

2. **Respect for Autonomy**: Built-in limits prevent over-reliance. The goal is to help you make decisions faster, not make decisions for you.

3. **Negative Filters**: Explicitly learns what you DON'T want, a crucial feature missing from many recommendation systems.

4. **Mental Health First**: Includes usage tracking and break suggestions to prevent unhealthy patterns.

5. **Transparency**: Always explains recommendations so you understand the reasoning.

## 🔧 Architecture

### Virtual Persona
- Maintains three types of preferences: positive, negative, and neutral
- Stores interaction history for learning patterns
- Persists data locally in JSON format
- Provides summary statistics and insights

### Recommendation Engine
- Generates personalized suggestions based on learned preferences
- Scores recommendations by preference matching
- Applies confidence levels to suggestions
- Extensible architecture for adding data sources

### Ethical Guardrails
- Limits recommendations per session (max 5)
- Tracks daily usage (max 50 interactions)
- Suggests breaks after heavy usage (10+ in 30 minutes)
- Applies negative filters from user preferences
- Provides health reports and tips

## 📊 Use Cases

1. **Media Choices**: Find movies, shows, or books that match your taste while avoiding genres you dislike

2. **Style Decisions**: Get fashion or design recommendations filtered by your aesthetic preferences

3. **Food Selection**: Narrow down restaurant or recipe options based on dietary preferences and dislikes

4. **General Decision Making**: Reduce any multi-option decision to your top 3 choices

## 🤝 Contributing

This is a prototype demonstrating ethical AI principles. Contributions are welcome to:
- Add new recommendation sources
- Improve filtering algorithms
- Enhance ethical guardrails
- Add new categories
- Improve documentation

## ⚖️ Ethics & Privacy

- **All data stored locally**: No external servers or data sharing
- **User control**: You own your data and can delete it anytime
- **No tracking**: No analytics or usage data sent anywhere
- **Open source**: Code is transparent and auditable
- **Opt-in learning**: System only learns what you explicitly teach it

## 📝 License

This project is a prototype for educational and demonstration purposes.

## 🎓 Concept

Lexi AI demonstrates how AI assistants can be built with user wellbeing as the primary goal, rather than engagement or profit. It's a "second brain" that respects your autonomy, helps you make decisions efficiently, and actively prevents unhealthy usage patterns.
