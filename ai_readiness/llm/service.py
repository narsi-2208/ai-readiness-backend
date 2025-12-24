import json
from .prompt import SYSTEM_PROMPT, USER_PROMPT
from .context_builder import build_llm_context
from .llm_client import call_llm
from .validators import validate_llm_output


def generate_llm_suggestions(assessment, scores, observations):
    context = build_llm_context(assessment, scores, observations)

    prompt = USER_PROMPT.format(
        context_json=json.dumps(context, indent=2)
    )

    output = call_llm(SYSTEM_PROMPT, prompt)
    validate_llm_output(output)

    return output
