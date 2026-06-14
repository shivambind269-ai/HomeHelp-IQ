def detect_issue(text):
    text = text.lower()

    if "ac" in text:
        return "Air Conditioner"

    elif "fan" in text:
        return "Electrical"

    elif "leak" in text or "water" in text:
        return "Plumbing"

    return "General Maintenance"