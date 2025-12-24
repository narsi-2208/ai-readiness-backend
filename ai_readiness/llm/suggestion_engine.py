import json
from .prompt import SYSTEM_PROMPT, USER_PROMPT
from .context_builder import build_llm_context
from .industry_context import INDUSTRY_CONTEXT
from .llm_client import call_llm
from .validators import validate_output

def generate_ai_suggestions(assessment, observations):
    context = build_llm_context(assessment, observations)

    industry_notes = INDUSTRY_CONTEXT.get(
        assessment.industry, ["General enterprise constraints apply"]
    )
    context["industry_notes"] = industry_notes

    prompt = USER_PROMPT.format(
        context_json=json.dumps(context, indent=2)
    )

    output = call_llm(SYSTEM_PROMPT, prompt)
    validate_output(output)

    return output
