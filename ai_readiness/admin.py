from django.contrib import admin
from .models import Assessment, Answer


# Inline to display answers inside the Assessment page
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    readonly_fields = ("question_id", "section", "question_text", "answer_type", "raw_value")
    can_delete = False


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ("email", "category", "overall_score", "created_at")
    search_fields = ("email", "category")
    list_filter = ("category", "created_at")
    readonly_fields = (
        "email",
        "overall_score",
        "category",
        "dimension_scores",
        "feedback_summary",
        "feedback_profile",
        "feedback_category_detail",
        "feedback_recommended_actions",
        "created_at",
        "updated_at",
    )
    inlines = [AnswerInline]

    fieldsets = (
        ("Lead / Client Info", {
            "fields": ("email",)
        }),
        ("AI Readiness Score & Category", {
            "fields": ("overall_score", "category", "dimension_scores")
        }),
        ("Narrative Insights", {
            "fields": (
                "feedback_summary",
                "feedback_profile",
                "feedback_category_detail",
                "feedback_recommended_actions",
            ),
        }),
        ("System Data", {
            "fields": ("created_at", "updated_at"),
        }),
    )


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("assessment", "question_id", "section", "answer_type")
    search_fields = ("assessment__email", "question_text", "section", "question_id")
    list_filter = ("section", "answer_type")
    readonly_fields = ("assessment", "question_id", "section", "question_text", "answer_type", "raw_value", "created_at")
