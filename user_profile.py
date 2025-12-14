def detect_experience_level(user_input: str) -> str:
    keywords = {
        "beginner": ["what is", "explain", "simple", "basic"],
        "intermediate": ["how does", "difference", "compare", "use case"],
        "advanced": ["internals", "optimize", "complexity", "architecture"]
    }

    text = user_input.lower()
    for level, words in keywords.items():
        if any(word in text for word in words):
            return level

    return "intermediate"  # default
