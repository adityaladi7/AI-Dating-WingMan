def build_opener_prompt(name, age, interests, match_interests, tone):
    return f"""
    You are a witty, respectful AI dating assistant.

    User Info:
    Name: {name}
    Age: {age}
    Interests: {interests}

    Match Info:
    Interests: {match_interests}

    Write a {tone.lower()} and personalized opening message to break the ice.
    """
