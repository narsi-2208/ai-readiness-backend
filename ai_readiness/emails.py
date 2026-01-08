from .graph_email import send_graph_email


def send_assessment_emails(assessment):
    # Email to user
    user_subject = "Your AI Readiness Assessment Results"
    user_body = f"""
        Hi {assessment.person_name or "there"},

        Thank you for completing the AI Readiness Assessment.

        Summary:
        • AI Readiness Score: {assessment.capped_score}%
        • Category: {assessment.category}
        • Industry: {assessment.industry}

        Our team at Forgebyte will review your inputs and reach out with next steps.

        Regards,
        Forgebyte Team
        Assist@forgebyte.ai
        """

    send_graph_email(
        to_email=assessment.email,
        subject=user_subject,
        body_text=user_body,
    )

    # Email to internal team
    internal_subject = f"New AI Readiness Submission — {assessment.company_name}"
    internal_body = f"""
        New assessment submitted.
        
        Client:
        Name: {assessment.person_name}
        Company: {assessment.company_name}
        Email: {assessment.email}
        Industry: {assessment.industry}
        
        Scores:
        Raw: {assessment.raw_score}%
        Capped: {assessment.capped_score}%
        Category: {assessment.category}
        
        Use case:
        {assessment.prioritized_use_case}
        """

    send_graph_email(
        to_email="assist@forgebyte.ai",
        subject=internal_subject,
        body_text=internal_body,
    )
