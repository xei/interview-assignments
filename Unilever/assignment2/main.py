import sys
# from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from tools.name_extraction import extract_names_tool
from tools.transcript_parser import extract_pokemons_tool
from tools.weight_fetcher import fetch_weights_tool
from tools.csv_generator import generate_csv_and_decide_winner_tool
from LLMClient import LLMClient


# load_dotenv()

# llm = LLMClient(provider="google",
#                 model_name="gemini-2.0-flash",
#                 temperature=0.3)
llm = LLMClient(provider="groq",
                model_name="meta-llama/llama-4-scout-17b-16e-instruct",
                temperature=0.3)

tools = [
    extract_names_tool,
    extract_pokemons_tool,
    fetch_weights_tool,
    generate_csv_and_decide_winner_tool,
]

agent = initialize_agent(
    tools=tools,
    llm=llm.llm,
    # agent=AgentType.OPENAI_FUNCTIONS,  # OpenAI tool-calling agent style
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,    # Text-based tool reasoning
    verbose=True,
    handle_parsing_errors=True,
    # For OpenAI tool-calling style
    # agent_kwargs={
    #     "system_message": "You must always use the available tools to answer questions. Never answer directly without using tools.",
    # }
    # For Text-based Zero-shot reactive tool-calling style
    agent_kwargs={
        "system_message": (
            "You are a reasoning agent. "
            "You MUST always keep using tools until you have all the information needed. "
            "After each tool result, decide your next action. "
            "NEVER stop after one tool unless you are 100% sure the task is complete. "
            "ALWAYS explain your reasoning step by step."
        ),
    }
)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_question = sys.argv[1]
    else:
        user_question = input("Ask your Pokémon duel question: ")

    # print("DEBUG: ", user_question)
    try:
        output = agent.run(user_question)
        print("OUTPUT:", output)
    except Exception as e:
        print("ERROR:", e)