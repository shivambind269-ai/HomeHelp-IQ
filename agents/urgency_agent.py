def get_urgency(issue):

    priorities = {
        "Air Conditioner": "Medium",
        "Plumbing": "High",
        "Electrical": "Critical"
    }

    return priorities.get(
        issue,
        "Low"
    )