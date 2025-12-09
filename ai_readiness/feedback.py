from .scoring import get_category

LABELS = {
    "business_fit": "Business Fit",
    "leadership": "Leadership",
    "workforce": "Workforce",
    "data": "Data",
    "adoption": "Adoption",
}

DETAILS = {
    "Foundational": "(0–39%) You are in early stage. Focus on data quality, basic automation and leadership alignment.",
    "Emerging": "(40–59%) Awareness exists. Fill key gaps before scaling AI.",
    "AI-Ready": "(60–79%) Strong base. Start scaling AI initiatives with measurable ROI.",
    "Transforming": "(80–100%) AI becoming strategic. Focus on governance, talent and innovation.",
}

def generate_feedback(dim_scores, overall):
    category = get_category(overall)

    sorted_dims = sorted(dim_scores.items(), key=lambda x: x[1], reverse=True)
    best_key, best_val = sorted_dims[0]
    worst_key, worst_val = sorted_dims[-1]

    best = LABELS[best_key]
    worst = LABELS[worst_key]

    return {
        "category": category,
        "summary": f"Your AI Readiness Index is {overall}%, placing you in the **{category}** category.",
        "profile": f"Your strongest capability is **{best} ({best_val})**, while the biggest bottleneck is **{worst} ({worst_val})**.",
        "category_detail": DETAILS[category],
        "recommended_actions": [
            f"Leverage your strong area: **{best}**.",
            f"Prioritize improvement in **{worst}**.",
            "Identify top 2–3 ROI-focused AI use cases.",
            "Develop internal AI talent and literacy.",
            "Create short-term pilots and long-term roadmap."
        ]
    }
