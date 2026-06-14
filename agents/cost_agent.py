def estimate_cost(category):

    costs = {
        "Air Conditioner": "₹1000 - ₹5000",
        "Electrical": "₹500 - ₹3000",
        "Plumbing": "₹300 - ₹2000"
    }

    return costs.get(
        category,
        "Cost Unknown"
    )