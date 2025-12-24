from .scoring import get_category

# ----------------------------------
# Industry → Example Mapping
# ----------------------------------
INDUSTRY_EXAMPLES = {
    "Healthcare & HealthTech": (
        "Healthcare (drug discovery acceleration, clinical decision support)"
    ),
    "Pharma / Med Devices": (
        "Pharma (clinical trials optimization, adverse event detection)"
    ),
    "Retail & E-commerce": (
        "Retail (hyper-personalized customer experiences, demand forecasting)"
    ),
    "Banking & Financial Services": (
        "Banking (fraud detection, credit risk modeling)"
    ),
    "Insurance": (
        "Insurance (automated claims processing, risk scoring)"
    ),
    "Technology / IT Services": (
        "Technology services (AI copilots, intelligent service automation)"
    ),
    "Manufacturing": (
        "Manufacturing (predictive maintenance, quality inspection)"
    ),
    "Transport & Logistics": (
        "Logistics (route optimization, predictive fleet maintenance)"
    ),
    "Energy & Utilities": (
        "Energy (load forecasting, asset optimization)"
    ),
    "Media / Entertainment / Telecom": (
        "Media & Telecom (content recommendation, churn prediction)"
    ),
    "Education / EdTech": (
        "Education (adaptive learning, student performance analytics)"
    ),
    "Government / Public Sector": (
        "Public sector (process automation, citizen service optimization)"
    ),
}


def get_industry_example(industry: str) -> str:
    return INDUSTRY_EXAMPLES.get(
        industry,
        "multiple industries (AI-driven optimization and automation use cases)"
    )


# ----------------------------------
# Bucket Narratives
# ----------------------------------
BUCKET_TEXT = {
    "AI Aspirant": {
        "range": "40% to 55%",
        "title": "AI Aspirant: The Foundational Stage",
        "description": (
            "You are actively identifying AI's potential but are strategically focused on building the core "
            "prerequisites: data consistency, cloud foundation, and cross-functional alignment.\n\n"
            "We Understand:\n"
            "Organizations at this stage need assurance. They need a clear path that moves them from "
            "'Maybe' to 'Must-Have.'\n\n"
            "Forgebyte's Partnership Approach:\n"
            "We start by de-risking your investment with a Focused Discovery & Readiness POC and deliver "
            "a rapid pilot to prove value quickly and create a reliable 12-month AI Blueprint.\n\n"
            "Ready to establish a confident, clear foundation?\n"
            "Contact our partnership team at Assist@forgebyte.com to start your discovery."
        ),
    },

    "AI Explorer": {
        "range": "56% to 65%",
        "title": "AI Explorer: The Proof-of-Value Phase",
        "description": (
            "You have successfully run initial AI experiments or POCs, validating the technology’s "
            "potential. Your challenge now is scaling these isolated successes across the organization.\n\n"
            "We Understand:\n"
            "The risk of 'Pilot Purgatory'—where promising ideas never reach production.\n\n"
            "Forgebyte's Partnership Approach:\n"
            "We specialize in engineering the transition from POC to industrialized AI solutions, "
            "implementing robust MLOps, data governance, and team enablement.\n\n"
            "Ready to turn pilots into scalable business assets?\n"
            "Contact Assist@forgebyte.com to discuss your transition."
        ),
    },

    "AI Adopter": {
        "range": "66% to 80%",
        "title": "AI Adopter: The Transformation Phase",
        "description": (
            "You possess mature technical infrastructure and AI is already integrated into core business "
            "units. You are now ready to leverage advanced capabilities like Generative AI for competitive "
            "advantage.\n\n"
            "We Understand:\n"
            "At this level, success depends on optimization, responsible governance, and differentiation.\n\n"
            "Forgebyte's Partnership Approach:\n"
            "We go beyond basic implementation. Leveraging our cross-industry expertise—ranging from "
            "{industry_example}—we introduce state-of-the-art models and architectures. "
            "We act as your long-term innovation lab, optimizing cost-to-serve and proactively maintaining "
            "your AI governance framework for sustained, responsible growth.\n\n"
            "Ready to future-proof your leadership position?\n"
            "Engage our innovation team at Assist@forgebyte.com for a strategy session."
        ),
    },
}


# ----------------------------------
# Narrative Generator
# ----------------------------------
def generate_narrative(assessment, raw_pct: float, capped_pct: float) -> str:
    category = get_category(capped_pct)
    bucket = BUCKET_TEXT.get(category, {})

    industry_example = get_industry_example(assessment.industry)

    description = bucket.get("description", "").format(
        industry_example=industry_example
    )

    narrative = (
        f"AI readiness score: {capped_pct:.2f}%.\n\n"
        f"{bucket.get('title', '')}\n\n"
        f"{description}"
    )

    return narrative






