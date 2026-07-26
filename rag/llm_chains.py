from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from schemas.models import (
    RelevanceGrade,
    RewriteOutput,
    DecisionOutput,
    HallucinationGrade,
    HumanEscalation,
)
from prompts.relevance import RELEVANCE_PROMPT
from prompts.rewrite import REWRITE_PROMPT
from prompts.adjudication import ADJUDICATION_PROMPT
from prompts.hallucination import HALLUCINATION_PROMPT
from prompts.escalation import ESCALATION_PROMPT
from rag.llm_engine import get_llm_engine
from config.settings import LLM_MODEL_NAME

# Initialize the central core LLM instance using Groq (single shared factory)
print(f"🤖 Initializing central Groq Chat LLM engine ({LLM_MODEL_NAME}) in JSON Mode...")
llm = get_llm_engine()

# Set up native structural JSON mode chains using Pydantic parsers
relevance_chain = (
    ChatPromptTemplate.from_template(
        RELEVANCE_PROMPT
        + "\n\nReturn ONLY a valid JSON object matching this schema: {format_instructions}"
    )
    .partial(
        format_instructions=PydanticOutputParser(
            pydantic_object=RelevanceGrade
        ).get_format_instructions()
    )
    | llm.bind(response_format={"type": "json_object"})
    | PydanticOutputParser(pydantic_object=RelevanceGrade)
)

rewrite_chain = (
    ChatPromptTemplate.from_template(
        REWRITE_PROMPT
        + "\n\nReturn ONLY a valid JSON object matching this schema: {format_instructions}"
    )
    .partial(
        format_instructions=PydanticOutputParser(
            pydantic_object=RewriteOutput
        ).get_format_instructions()
    )
    | llm.bind(response_format={"type": "json_object"})
    | PydanticOutputParser(pydantic_object=RewriteOutput)
)

adjudicate_chain = (
    ChatPromptTemplate.from_template(
        ADJUDICATION_PROMPT
        + "\n\nReturn ONLY a valid JSON object matching this schema: {format_instructions}"
    )
    .partial(
        format_instructions=PydanticOutputParser(
            pydantic_object=DecisionOutput
        ).get_format_instructions()
    )
    | llm.bind(response_format={"type": "json_object"})
    | PydanticOutputParser(pydantic_object=DecisionOutput)
)

hallucination_chain = (
    ChatPromptTemplate.from_template(
        HALLUCINATION_PROMPT
        + "\n\nReturn ONLY a valid JSON object matching this schema: {format_instructions}"
    )
    .partial(
        format_instructions=PydanticOutputParser(
            pydantic_object=HallucinationGrade
        ).get_format_instructions()
    )
    | llm.bind(response_format={"type": "json_object"})
    | PydanticOutputParser(pydantic_object=HallucinationGrade)
)

escalate_chain = (
    ChatPromptTemplate.from_template(
        ESCALATION_PROMPT
        + "\n\nReturn ONLY a valid JSON object matching this schema: {format_instructions}"
    )
    .partial(
        format_instructions=PydanticOutputParser(
            pydantic_object=HumanEscalation
        ).get_format_instructions()
    )
    | llm.bind(response_format={"type": "json_object"})
    | PydanticOutputParser(pydantic_object=HumanEscalation)
)

print("✅ Anirudh Step 3 Updated: All LLM validation chains migrated safely to JSON Mode!")
