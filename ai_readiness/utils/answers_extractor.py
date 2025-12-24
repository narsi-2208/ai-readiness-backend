def extract_question_scores(assessment) -> dict:
    """
    Extract numeric answers only.
    Output example:
    {
        "Q1": 5,
        "Q2": 3,
        ...
    }
    """
    scores = {}

    for ans in assessment.answers.all():
        if ans.numeric_value is not None:
            scores[ans.question_id] = ans.numeric_value

    return scores
