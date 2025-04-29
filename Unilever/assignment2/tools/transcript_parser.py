from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import Tool
from pathlib import Path
import os
import json
from prompts.prompt_loader import load_prompt
from LLMClient import LLMClient


TRANSCRIPT_FILE = Path(str(Path(__file__).parent.parent / "kb" / "pokemon_transcript.txt"))
prompt_template = load_prompt(str(Path(__file__).parent.parent / "prompts" / "pokemon_extraction.txt"))


# llm = LLMClient(provider="google",
#                 model_name="gemini-2.0-flash",
#                 temperature=0.2)
llm = LLMClient(provider="groq",
                model_name="meta-llama/llama-4-scout-17b-16e-instruct",
                temperature=0.2)

def extract_pokemon_for_human(human: str, dialogue: str) -> list:
    prompt = prompt_template.format(human=human, dialogue=dialogue)
    response = llm.invoke(prompt)
    try:
        pokemons = eval(response.content.strip())
        if isinstance(pokemons, list):
            return pokemons
        else:
            return []
    except Exception as e:
        print(f"Failed to parse for {human}: {response.content} - Error: {e}")
        return []

def extract_pokemons(human_names: str) -> str:
    humans = human_names.split(",")
    pokemons = {humans[0]: [], humans[1]: []}
    
    transcript = TRANSCRIPT_FILE.read_text()

    print("\nDEBUG: ","Humans in extract_pokemons", humans)
    for human in humans:
        found_pokemons = extract_pokemon_for_human(human, transcript)
        pokemons[human] = found_pokemons

    return json.dumps(pokemons)


extract_pokemons_tool = Tool(
    name="extract_pokemons",
    description="Extract Pokémon owned by two given humans from the full transcript using Gemini.",
    func=extract_pokemons,
)