from langchain_openai import ChatOpenAI
from agent.prompt import SYSTEM_PROMPT
from agent.tools import search_tool

llm = ChatOpenAI(model="gpt-4o", temperature=0)

def solve(question: str) -> str:
    search_result = search_tool.run(question)

    response = llm.invoke(
        SYSTEM_PROMPT +
        f"\nQuestion: {question}\nContext: {search_result}"
    )

    return response.content.strip()
