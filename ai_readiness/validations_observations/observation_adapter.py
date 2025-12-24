def adapt_observations_for_llm(observations: list) -> list:
    """
    Converts observation objects into short factual statements
    suitable for LLM grounding.
    """

    return [
        obs["message"]
        for obs in observations
        if obs.get("severity") in ("medium", "high")
    ]
