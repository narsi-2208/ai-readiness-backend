REQUIRED_KEYS = {
    "executive_summary",
    "overall_assessment",
    "confidence_level",
    "recommended_strategy",
    "dimension_insights",
    "what_to_do_now",
    "what_to_delay_or_avoid",
    "phased_roadmap",
    "industry_considerations",
    "key_risks_and_tradeoffs",
    "success_metrics"
}

FORBIDDEN_TERMS = [
    "guaranteed",
    "100%",
    "no risk",
    "fully autonomous"
]

def validate_llm_output(output: dict):
    missing = REQUIRED_KEYS - output.keys()
    if missing:
        raise ValueError(f"Missing LLM keys: {missing}")

    text = str(output).lower()
    for term in FORBIDDEN_TERMS:
        if term in text:
            raise ValueError(f"Forbidden claim detected: {term}")
