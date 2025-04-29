from langchain.tools import Tool


VALID_NAMES = {"Ash", "Misty", "Brock", "Jessie", "James"}

def validate_and_extract_names(input_question: str) -> str:
    print("DEBUG: ", f"\nvalidate_and_extract_names received input: {input_question}\n\n")
    found_names = [name for name in VALID_NAMES if name in input_question]
    if len(found_names) != 2:
        return "Incorrect question"
    print("DEBUG: ", f"Found names in input question: {found_names}\n\n")
    return ",".join(found_names)


extract_names_tool = Tool(
    name="validate_and_extract_names",
    description="Validate question and extract two Pokémon human names",
    func=validate_and_extract_names,
)