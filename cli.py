#!/usr/bin/env python3
"""
Lexi AI Command Line Interface
Interactive CLI for using the Lexi AI assistant
"""

import sys
from lexi_ai import LexiAI


def print_header():
    """Print CLI header."""
    print("=" * 60)
    print("  Lexi AI - Your Hyper-Personalized Assistant")
    print("  Combating Decision Fatigue with Ethical AI")
    print("=" * 60)
    print()


def print_menu():
    """Print main menu."""
    print("\nWhat would you like to do?")
    print("  1. Learn a preference")
    print("  2. Get recommendations")
    print("  3. Combat decision fatigue")
    print("  4. View persona summary")
    print("  5. Check health status")
    print("  6. Exit")
    print()


def learn_preference(lexi):
    """Interactive preference learning."""
    print("\n--- Learn a Preference ---")
    category = input("Category (media/style/food): ").strip().lower()
    
    print("\nTell me about something you like, dislike, or are neutral about:")
    item_name = input("Item name: ").strip()
    
    # Get attributes
    print("\nAdd attributes (press Enter without value to finish):")
    item = {'name': item_name}
    while True:
        key = input("  Attribute name (e.g., 'genre', 'style', 'type'): ").strip()
        if not key:
            break
        value = input(f"  Value for '{key}': ").strip()
        if value:
            item[key] = value
    
    # Get rating
    rating = input("\nRating (positive/negative/neutral): ").strip().lower()
    while rating not in ['positive', 'negative', 'neutral']:
        rating = input("Please enter 'positive', 'negative', or 'neutral': ").strip().lower()
    
    # Learn the preference
    lexi.learn_preference(item, rating, category)
    print(f"\n✓ Learned your {rating} preference for {item_name}")


def get_recommendations(lexi):
    """Get recommendations for a category."""
    print("\n--- Get Recommendations ---")
    category = input("Category (media/style/food): ").strip().lower()
    
    recommendations = lexi.get_recommendations(category, limit=5)
    
    if recommendations:
        print(f"\n✓ Here are my recommendations for {category}:")
        for i, rec in enumerate(recommendations, 1):
            print(f"\n{i}. {rec}")
    else:
        print("\nI don't have enough information yet to make recommendations.")
        print("Try teaching me some preferences first!")


def combat_fatigue(lexi):
    """Help user make a decision."""
    print("\n--- Combat Decision Fatigue ---")
    print("I'll help you narrow down your options.\n")
    
    category = input("Category: ").strip().lower()
    num_options = int(input("How many options do you have? "))
    
    options = []
    for i in range(num_options):
        print(f"\nOption {i+1}:")
        name = input("  Name: ").strip()
        option = {'name': name}
        
        # Get a few attributes
        attr = input("  Key attribute (e.g., 'genre'): ").strip()
        if attr:
            value = input(f"  Value for '{attr}': ").strip()
            if value:
                option[attr] = value
        
        options.append(option)
    
    # Get filtered options
    filtered = lexi.combat_decision_fatigue(category, options)
    
    print(f"\n✓ Reduced from {len(options)} to {len(filtered)} best matches:")
    for i, item in enumerate(filtered, 1):
        print(f"\n{i}. {item['option']['name']}")
        print(f"   {item['reasoning']}")


def view_persona(lexi):
    """View persona summary."""
    print("\n--- Virtual Persona Summary ---")
    summary = lexi.get_persona_summary()
    
    print(f"User ID: {summary['user_id']}")
    print(f"Preferences tracked: {summary['total_preferences']}")
    print(f"Total interactions: {summary['total_interactions']}")
    print(f"Categories: {', '.join(summary['categories']) if summary['categories'] else 'None yet'}")
    print(f"Created: {summary['created_at']}")
    print(f"Last updated: {summary['last_updated']}")


def check_health(lexi):
    """Check ethical health status."""
    print("\n--- Health Status ---")
    
    report = lexi.guardrails.get_health_report(lexi.persona)
    
    usage = report['usage_status']
    print(f"Interactions today: {usage['interactions_today']}/{usage['limit']}")
    print(f"Usage: {usage['percentage_used']:.1f}%")
    
    if usage['warnings']:
        print("\n⚠️  Warnings:")
        for warning in usage['warnings']:
            print(f"  - {warning}")
    
    if report['break_recommended']:
        print("\n💡 Suggestion: Take a break!")
    
    print("\n📋 Health Tips:")
    for tip in report['health_tips']:
        print(f"  - {tip}")


def main():
    """Main CLI loop."""
    print_header()
    
    # Get or create user ID
    user_id = input("Enter your user ID (or press Enter for 'demo_user'): ").strip()
    if not user_id:
        user_id = "demo_user"
    
    print(f"\n✓ Initializing Lexi AI for user: {user_id}")
    lexi = LexiAI(user_id)
    
    while True:
        print_menu()
        choice = input("Your choice (1-6): ").strip()
        
        if choice == '1':
            learn_preference(lexi)
        elif choice == '2':
            get_recommendations(lexi)
        elif choice == '3':
            combat_fatigue(lexi)
        elif choice == '4':
            view_persona(lexi)
        elif choice == '5':
            check_health(lexi)
        elif choice == '6':
            print("\nThank you for using Lexi AI!")
            print("Remember: You're in control of your decisions. 🎯")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting Lexi AI. Take care! 👋")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
