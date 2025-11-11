#!/usr/bin/env python3
"""
Lexi AI Examples
Demonstrates various features of the Lexi AI system
"""

from lexi_ai import LexiAI


def example_1_basic_learning():
    """Example 1: Basic preference learning"""
    print("\n" + "="*60)
    print("Example 1: Learning User Preferences")
    print("="*60)
    
    lexi = LexiAI("example_user_1")
    
    # Learn positive preferences
    print("\n📚 Teaching Lexi about movies I like...")
    lexi.learn_preference(
        {"title": "The Matrix", "genre": "sci-fi", "year": "1999"},
        "positive",
        "media"
    )
    lexi.learn_preference(
        {"title": "Blade Runner 2049", "genre": "sci-fi", "director": "Villeneuve"},
        "positive",
        "media"
    )
    
    # Learn negative preferences (filters)
    print("📚 Teaching Lexi what I want to avoid...")
    lexi.learn_preference(
        {"genre": "horror", "type": "movie"},
        "negative",
        "media"
    )
    
    print("\n✓ Preferences learned successfully!")
    
    # Show persona summary
    summary = lexi.get_persona_summary()
    print(f"\n📊 Persona Summary:")
    print(f"   Total preferences: {summary['total_preferences']}")
    print(f"   Categories: {', '.join(summary['categories'])}")


def example_2_decision_fatigue():
    """Example 2: Combat decision fatigue"""
    print("\n" + "="*60)
    print("Example 2: Combating Decision Fatigue")
    print("="*60)
    
    lexi = LexiAI("example_user_2")
    
    # Set up preferences
    lexi.learn_preference(
        {"style": "minimalist", "color": "neutral"},
        "positive",
        "style"
    )
    lexi.learn_preference(
        {"style": "maximalist", "pattern": "busy"},
        "negative",
        "style"
    )
    
    # Present many options
    print("\n🤔 You have 5 clothing options to choose from...")
    options = [
        {"item": "White T-Shirt", "style": "minimalist", "color": "neutral"},
        {"item": "Patterned Shirt", "style": "maximalist", "pattern": "busy"},
        {"item": "Gray Sweater", "style": "minimalist", "color": "neutral"},
        {"item": "Bright Jacket", "style": "bold", "color": "bright"},
        {"item": "Black Hoodie", "style": "minimalist", "color": "neutral"},
    ]
    
    for i, opt in enumerate(options, 1):
        print(f"   {i}. {opt['item']}")
    
    # Combat decision fatigue
    print("\n🎯 Lexi AI filtering based on your preferences...")
    filtered = lexi.combat_decision_fatigue("style", options)
    
    print(f"\n✓ Reduced to {len(filtered)} best matches:")
    for item in filtered:
        print(f"\n   • {item['option']['item']}")
        print(f"     Reason: {item['reasoning']}")


def example_3_ethical_guardrails():
    """Example 3: Ethical guardrails in action"""
    print("\n" + "="*60)
    print("Example 3: Ethical Guardrails")
    print("="*60)
    
    lexi = LexiAI("example_user_3")
    
    # Simulate multiple interactions
    print("\n⚡ Simulating user interactions...")
    for i in range(15):
        lexi.learn_preference(
            {"item": f"Item {i}", "category": "test"},
            "positive",
            "general"
        )
    
    # Check health status
    print("\n🏥 Checking usage health status...")
    report = lexi.guardrails.get_health_report(lexi.persona)
    
    usage = report['usage_status']
    print(f"\n📊 Usage Statistics:")
    print(f"   Interactions today: {usage['interactions_today']}/{usage['limit']}")
    print(f"   Usage percentage: {usage['percentage_used']:.1f}%")
    
    if usage['warnings']:
        print(f"\n⚠️  Warnings:")
        for warning in usage['warnings']:
            print(f"   - {warning}")
    
    print(f"\n💡 Health Tips:")
    for tip in report['health_tips'][:3]:
        print(f"   - {tip}")


def example_4_negative_filters():
    """Example 4: Negative filters in action"""
    print("\n" + "="*60)
    print("Example 4: Negative Filters - The Killer Feature")
    print("="*60)
    
    lexi = LexiAI("example_user_4")
    
    # Set up strong negative filters
    print("\n🚫 Setting up negative filters (things to NEVER recommend)...")
    
    negative_filters = [
        {"genre": "reality", "type": "tv"},
        {"violence": "extreme"},
        {"ads": "heavy"}
    ]
    
    for nf in negative_filters:
        lexi.learn_preference(nf, "negative", "media")
        filter_desc = ", ".join([f"{k}={v}" for k, v in nf.items()])
        print(f"   ✗ Added filter: {filter_desc}")
    
    # Add some positive preferences too
    lexi.learn_preference(
        {"genre": "documentary", "topic": "science"},
        "positive",
        "media"
    )
    
    print("\n🎬 Testing recommendations with filters active...")
    
    # Simulate recommendations that should be filtered
    test_items = [
        {"title": "Science Doc", "genre": "documentary", "topic": "science"},
        {"title": "Reality Show", "genre": "reality", "type": "tv"},
        {"title": "Action Movie", "violence": "extreme"},
        {"title": "Streaming Service", "ads": "heavy"},
    ]
    
    print(f"\n📋 Original list: {len(test_items)} items")
    for item in test_items:
        print(f"   - {item['title']}")
    
    # Apply filters through guardrails
    filtered = lexi.guardrails.filter_recommendations(
        test_items, lexi.persona
    )
    
    print(f"\n✓ After negative filters: {len(filtered)} items")
    for item in filtered:
        print(f"   ✓ {item['title']}")
    
    print(f"\n🎯 Filtered out {len(test_items) - len(filtered)} items you don't want!")


def example_5_persistence():
    """Example 5: Data persistence across sessions"""
    print("\n" + "="*60)
    print("Example 5: Persistent Memory Across Sessions")
    print("="*60)
    
    user_id = "persistent_user"
    
    # First session
    print("\n📝 Session 1: Learning preferences...")
    lexi1 = LexiAI(user_id)
    lexi1.learn_preference(
        {"cuisine": "italian", "dish": "pasta"},
        "positive",
        "food"
    )
    summary1 = lexi1.get_persona_summary()
    print(f"   Interactions: {summary1['total_interactions']}")
    
    # Second session (new instance, same user)
    print("\n📝 Session 2: Loading saved preferences...")
    lexi2 = LexiAI(user_id)
    summary2 = lexi2.get_persona_summary()
    print(f"   Interactions: {summary2['total_interactions']}")
    
    # Add more preferences
    lexi2.learn_preference(
        {"cuisine": "japanese", "dish": "sushi"},
        "positive",
        "food"
    )
    summary3 = lexi2.get_persona_summary()
    print(f"   After new learning: {summary3['total_interactions']}")
    
    print("\n✓ Preferences persist across sessions!")
    print("   Your 'second brain' remembers everything.")


def main():
    """Run all examples"""
    print("\n" + "="*60)
    print("  LEXI AI - Feature Demonstrations")
    print("  Hyper-Personalized AI with Ethical Guardrails")
    print("="*60)
    
    examples = [
        example_1_basic_learning,
        example_2_decision_fatigue,
        example_3_ethical_guardrails,
        example_4_negative_filters,
        example_5_persistence
    ]
    
    for example in examples:
        try:
            example()
            input("\nPress Enter to continue to next example...")
        except KeyboardInterrupt:
            print("\n\n👋 Exiting examples...")
            break
        except Exception as e:
            print(f"\n❌ Error in example: {e}")
    
    print("\n" + "="*60)
    print("  Examples completed!")
    print("  Try 'python cli.py' for interactive mode")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
