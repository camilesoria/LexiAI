# Quick Start Guide - Lexi AI

## Installation

```bash
# Clone the repository
git clone https://github.com/camilesoria/LexiAI.git
cd LexiAI

# Install dependencies
pip install -r requirements.txt

# Or install as a package
pip install -e .
```

## First Steps

### 1. Run the Demo
See Lexi AI in action with a pre-configured example:
```bash
python lexi_ai.py
```

### 2. Try Interactive Examples
Explore all features step by step:
```bash
python examples.py
```

### 3. Use the CLI
Interactive command-line interface:
```bash
python cli.py
```

## Basic Usage Pattern

```python
from lexi_ai import LexiAI

# 1. Initialize for your user
lexi = LexiAI("your_user_id")

# 2. Teach it your preferences
lexi.learn_preference(
    {"title": "Movie Name", "genre": "sci-fi"},
    "positive",  # or "negative" for things you don't like
    "media"      # category
)

# 3. Get recommendations
recommendations = lexi.get_recommendations("media", limit=5)

# 4. Combat decision fatigue
options = [...]  # Your list of options
best_choices = lexi.combat_decision_fatigue("media", options)
```

## Key Concepts

### Virtual Persona
Your "second brain" that remembers what you like and dislike:
- Learns from every interaction
- Persists across sessions
- Maintains positive and negative preferences

### Negative Filters
Explicitly tell Lexi what to NEVER recommend:
```python
lexi.learn_preference(
    {"genre": "horror"},
    "negative",  # This will filter out ALL horror content
    "media"
)
```

### Ethical Guardrails
Built-in protections for your wellbeing:
- Max 5 recommendations per session
- Max 50 interactions per day
- Break suggestions after heavy use
- Health status reports

### Decision Fatigue Combat
Reduce overwhelming choices:
```python
# From 10 options to top 3 matches
filtered = lexi.combat_decision_fatigue("category", options)
```

## File Organization

```
LexiAI/
├── lexi/              # Core package
│   ├── persona.py     # Virtual Persona
│   ├── recommendations.py  # Recommendation engine
│   └── guardrails.py  # Ethical safeguards
├── lexi_ai.py         # Main class
├── cli.py             # Interactive CLI
├── examples.py        # Feature examples
└── user_data/         # Your personal data (auto-created)
```

## Common Tasks

### Check Your Persona
```python
summary = lexi.get_persona_summary()
print(summary)
```

### Check Health Status
```python
report = lexi.guardrails.get_health_report(lexi.persona)
print(report)
```

### Export Your Data
Your data is stored in `user_data/persona_<user_id>.json`

### Delete Your Data
Simply delete the JSON file in `user_data/` directory

## What Makes Lexi AI Different?

1. **You're in control** - It helps, doesn't decide
2. **Respects your time** - Built-in usage limits
3. **Learns what you DON'T want** - Negative filters are first-class
4. **Transparent** - Always explains its reasoning
5. **Private** - All data stored locally

## Next Steps

- Try the examples to see all features
- Customize for your specific use cases
- Add your own recommendation sources
- Contribute improvements!

## Need Help?

- Check the main README.md for full documentation
- Run examples.py to see feature demonstrations
- Read the code - it's well-commented and straightforward
