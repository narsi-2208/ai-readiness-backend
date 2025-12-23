"""
Consistency Engine v2 (Upgraded)
--------------------------------
Purpose:
- Detect logical contradictions and misalignments in AI readiness assessments
- Generate dynamic, explainable observations
- Add risk + baseline insights so observations are never empty
- Serve as a deterministic layer before optional LLM explanation
"""

from typing import Dict, List


# ============================================================
# 1. Capability Mapping
# ============================================================

CAPABILITIES = {
    "ai_ambition": ["Q1", "Q8", "Q15"],
    "strategy": ["Q1", "Q2", "Q3", "Q14"],
    "data": ["Q4", "Q5"],
    "cloud": ["Q6"],
    "automation": ["Q10", "Q11"],
    "people": ["Q9", "Q12", "Q15"],
    "leadership": ["Q14"],
    "foundation": ["Q4", "Q5", "Q6", "Q10", "Q11"],
}


# ============================================================
# 2. Utility Functions
# ============================================================

def average(scores: Dict[str, int], questions: List[str]) -> float:
    values = [scores.get(q, 0) for q in questions if q in scores]
    return round(sum(values) / len(values), 2) if values else 0.0


def compute_signals(scores: Dict[str, int]) -> Dict[str, float]:
    return {name: average(scores, qs) for name, qs in CAPABILITIES.items()}


# ============================================================
# 3. Contradiction Rules (UNCHANGED)
# ============================================================

def generate_flags(signals: Dict[str, float]) -> Dict[str, bool]:
    return {
        "high_ambition_low_foundation": (
            signals["ai_ambition"] >= 4 and signals["foundation"] <= 2
        ),
        "low_ambition_low_foundation": (
            signals["ai_ambition"] <= 2 and signals["foundation"] <= 2
        ),
        "high_ambition_high_foundation": (
            signals["ai_ambition"] >= 4 and signals["foundation"] >= 3
        ),
        "data_cloud_mismatch": (
            abs(signals["data"] - signals["cloud"]) >= 2
        ),
        "people_ahead_of_automation": (
            signals["people"] >= 4 and signals["automation"] <= 2
        ),
        "automation_ahead_of_people": (
            signals["automation"] >= 4 and signals["people"] <= 2
        ),
        "ambition_exceeds_leadership": (
            signals["ai_ambition"] >= 4 and signals["leadership"] <= 2
        ),
    }


# ============================================================
# 4. Observation Library
# ============================================================

OBSERVATION_LIBRARY = {
    "high_ambition_low_foundation": {
        "severity": "high",
        "message": (
            "Strong AI ambition and urgency are not currently supported by "
            "data, cloud, or process foundations, increasing execution risk."
        ),
    },
    "low_ambition_low_foundation": {
        "severity": "medium",
        "message": (
            "AI ambition and urgency are low while foundational capabilities "
            "remain weak. Awareness-building and readiness investments are needed."
        ),
    },
    "high_ambition_high_foundation": {
        "severity": "low",
        "message": (
            "AI ambition is well aligned with foundational readiness, positioning "
            "the organization for scalable AI adoption."
        ),
    },
    "data_cloud_mismatch": {
        "severity": "medium",
        "message": (
            "Data maturity and cloud readiness are advancing at different rates, "
            "which may slow AI deployment."
        ),
    },
    "people_ahead_of_automation": {
        "severity": "medium",
        "message": (
            "Workforce readiness exceeds automation maturity, indicating untapped "
            "execution potential."
        ),
    },
    "automation_ahead_of_people": {
        "severity": "medium",
        "message": (
            "Automation maturity exceeds workforce readiness, which may limit "
            "adoption and value realization."
        ),
    },
    "ambition_exceeds_leadership": {
        "severity": "medium",
        "message": (
            "AI ambition appears stronger than leadership commitment, which may "
            "slow decision-making and execution."
        ),
    },
}


# ============================================================
# 5. Public API — Consistency Engine v2 (FIXED)
# ============================================================

def run_consistency_engine_v2(
    scores: Dict[str, int],
    category: str = "Unknown",
    industry: str = "Unknown"
) -> List[dict]:

    signals = compute_signals(scores)
    flags = generate_flags(signals)

    observations: List[dict] = []

    # ------------------------------------------------
    # 1️⃣ CONTRADICTIONS (highest priority)
    # ------------------------------------------------
    for flag, active in flags.items():
        if active and flag in OBSERVATION_LIBRARY:
            tpl = OBSERVATION_LIBRARY[flag]
            observations.append({
                "type": flag,
                "severity": tpl["severity"],
                "message": tpl["message"],
                "signals": signals
            })

    if observations:
        return observations

    # ------------------------------------------------
    # 2️⃣ SCORE-BASED RISK OBSERVATIONS
    # ------------------------------------------------
    if scores.get("Q4", 5) <= 2 or scores.get("Q5", 5) <= 2:
        observations.append({
            "type": "data_risk",
            "severity": "medium",
            "message": (
                "Data infrastructure and quality are currently weak, which may "
                "limit the effectiveness of AI models."
            ),
        })

    if scores.get("Q6", 5) <= 2:
        observations.append({
            "type": "cloud_risk",
            "severity": "medium",
            "message": (
                "Cloud readiness is limited, potentially constraining scalability "
                "and deployment of AI workloads."
            ),
        })

    if scores.get("Q7", 5) <= 2:
        observations.append({
            "type": "use_case_clarity_risk",
            "severity": "medium",
            "message": (
                "AI use-case clarity is low, increasing the risk of unfocused or "
                "low-impact AI initiatives."
            ),
        })

    if observations:
        return observations

    # ------------------------------------------------
    # 3️⃣ BASELINE MATURITY (fallback)
    # ------------------------------------------------
    return [{
        "type": "baseline_maturity",
        "severity": "low",
        "message": (
            f"As an organization in the **{category}** stage within the "
            f"{industry} industry, AI readiness is progressing steadily. "
            "No major contradictions are present, but targeted improvements "
            "will be required to scale AI initiatives."
        ),
        "signals": signals
    }]


# ============================================================
# 6. Local Test
# ============================================================

if __name__ == "__main__":
    example_scores = {
        "Q1": 1,
        "Q4": 1,
        "Q5": 3,
        "Q6": 2,
        "Q7": 1,
        "Q8": 2,
        "Q15": 4,
    }

    from pprint import pprint
    pprint(run_consistency_engine_v2(
        example_scores,
        category="AI Aspirant",
        industry="Technology / IT Services"
    ))
