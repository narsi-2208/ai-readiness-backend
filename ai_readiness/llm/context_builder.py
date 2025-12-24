def build_llm_context(assessment, scores, observations):
    return {
        "overall_score": float(assessment.capped_score),
        "category": assessment.category,

        "question_scores": scores,

        "observed_risks": observations,

        "industry": assessment.industry,
        "prioritized_use_case": assessment.prioritized_use_case
    }
