from .questions_config import QUESTIONS

DIMENSIONS = ["business_fit", "leadership", "workforce", "data", "adoption"]

# map answer text to score (for single_choice)
CHOICE_SCORES = {
    "Fully structured": 10,
    "Partially structured": 6,
    "Mostly unstructured": 3,

    "Yes": 9,
    "No": 3,
    "Planning": 6,
    "Pilot / Limited": 7,
    "Pilot / POC": 7,
    "Experimenting": 7,

    "On-prem": 5,
    "Cloud": 9,
    "Hybrid": 8,

    "Strong team": 9,
    "Basic knowledge": 7,
    "Exploring": 5,
    "None": 2,

    "Immediate": 10,
    "Within 3 months": 8,
    "Within 6–12 months": 6,
    "Just exploring": 4,
}

def score_multi_choice(answer_list, options):
    if not answer_list:
        return 0
    ratio = min(len(answer_list), len(options)) / len(options)
    return ratio * 10

def compute_dimension_scores(answers: dict):
    totals = {d: 0.0 for d in DIMENSIONS}
    weights = {d: 0.0 for d in DIMENSIONS}
    Q = {q["id"]: q for q in QUESTIONS}

    for qid, value in answers.items():
        q = Q.get(qid)
        if not q or "dimension" not in q:
            continue

        dimension = q["dimension"]
        weight = q.get("weight", 1.0)
        q_type = q["type"]
        score = None

        if q_type == "rating":
            score = float(value)
            if q.get("invert"):
                score = 11 - score

        elif q_type == "single_choice":
            score = CHOICE_SCORES.get(value, 0)

        elif q_type == "multi_choice":
            score = score_multi_choice(value, q["options"])

        if score is not None:
            totals[dimension] += score * weight
            weights[dimension] += weight

    result = {}
    for d in DIMENSIONS:
        result[d] = round(totals[d] / weights[d], 1) if weights[d] else 0

    return result

def compute_overall_score(dim_scores: dict):
    if not dim_scores:
        return 0
    avg = sum(dim_scores.values()) / len(dim_scores)
    return round(avg * 10, 1)

def get_category(score):
    if score < 40:
        return "Foundational"
    elif score < 60:
        return "Emerging"
    elif score < 80:
        return "AI-Ready"
    else:
        return "Transforming"
