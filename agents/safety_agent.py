def safety_advice(category):

    tips = {
        "Air Conditioner":
        "Switch off power before inspection.",

        "Electrical":
        "Avoid touching exposed wires.",

        "Plumbing":
        "Turn off water supply."
    }

    return tips.get(
        category,
        "Follow general safety precautions."
    )