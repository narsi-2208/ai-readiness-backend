from rest_framework import serializers
from .models import Assessment, Answer
from .questions_config import QUESTIONS
from .scoring import compute_dimension_scores, compute_overall_score
from .feedback import generate_feedback



# index config for fast lookup
QUESTION_INDEX = {q["id"]: q for q in QUESTIONS}


class AssessmentCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    answers = serializers.DictField()  # {"A1": "...", "B4": 7, ...}

    def validate(self, data):
        answers = data.get("answers", {})
        if not answers:
            raise serializers.ValidationError("Answers field cannot be empty")

        # validate every answer against config rules
        for qid, value in answers.items():
            if qid not in QUESTION_INDEX:
                raise serializers.ValidationError(f"Invalid question ID: {qid}")

            q = QUESTION_INDEX[qid]
            q_type = q.get("type")

            # Validate based on type
            if q_type == "rating":
                if not isinstance(value, (int, float)):
                    raise serializers.ValidationError(f"{qid} must be a number between 1 and 10")
                if value < 1 or value > 10:
                    raise serializers.ValidationError(f"{qid} must be between 1–10")

            elif q_type == "single_choice":
                if value not in q["options"]:
                    raise serializers.ValidationError(f"{qid} must be one of: {q['options']}")

            elif q_type == "multi_choice":
                if not isinstance(value, list):
                    raise serializers.ValidationError(f"{qid} must be a list of options")
                for item in value:
                    if item not in q["options"]:
                        raise serializers.ValidationError(f"{qid} contains invalid option: {item}")

            # text type has no restrictions

        return data


    def create(self, validated_data):
        email = validated_data["email"]
        answers = validated_data["answers"]

        # 1️⃣ Create Assessment row first (email only)
        assessment = Assessment.objects.create(email=email)

        # 2️⃣ Create Answer rows (store every question)
        for qid, value in answers.items():
            q = QUESTION_INDEX[qid]
            Answer.objects.create(
                assessment=assessment,
                question_id=qid,
                section=q["section"],
                question_text=q["label"],
                answer_type=q["type"],
                raw_value=value,
            )

        # 3️⃣ Calculate scores by dimensions
        dim_scores = compute_dimension_scores(answers)

        # 4️⃣ Total score & category
        overall = compute_overall_score(dim_scores)

        # 5️⃣ Generate feedback text & recommendations
        feedback = generate_feedback(dim_scores, overall)

        # 6️⃣ Save scores + feedback in Assessment record
        assessment.overall_score = overall
        assessment.category = feedback["category"]
        assessment.dimension_scores = dim_scores
        assessment.feedback_summary = feedback["summary"]
        assessment.feedback_profile = feedback["profile"]
        assessment.feedback_category_detail = feedback["category_detail"]
        assessment.feedback_recommended_actions = feedback["recommended_actions"]
        assessment.save()

        return assessment
