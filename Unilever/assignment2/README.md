# Interview: System Setup Instructions

Welcome to the interview setup packet. Please follow these steps to configure your environment:

1. Gemin API Key  
    - Add the Gemini API key in your `.env` file located in the project root 
    - If you haven't received the API key, please contact your interviewer.

2. Install Dependencies  
    - Run the following command to install all necessary packages:
      ```
      pip install -r requirements.txt
      ```

3. Test the Setup  
    - Run `gemini_setup.py`:
      ```
      python gemini_setup.py
      ```
    - Run `pokemon_api.py` to verify that the API integration is working:
      ```
      python tools/pokemon_api.py
      ```

4. Agent Building Framework  
    - Set up your environment using your favorite agent building framework.  
    - Update the `requirements.txt` file to include any new dependencies required by your framework.

If you encounter any issues during setup, please reach out to your interviewer for guidance.

Good luck with your setup!



## Project Structure
```bash
/assignment2/
│
├── LLMClient.py
├── main.py
├── .env
├── requirements.txt
│
├── prompts/
│   ├── prompt_loader.py
│   ├── name_extraction.txt
│   └── pokemon_extraction.txt
│
├── tools/
│   ├── name_extraction.py
│   ├── transcript_parser.py
│   ├── weight_fetcher.py
│   ├── pokemon_api.py
│   └── csv_generator.py
│
├── kb/
│   ├── pokemon_transcript.txt
```

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

## Run
```bash
export GOOGLE_API_KEY="your-api-key-here"
```
or
```bash
export GROQ_API_KEY="your-api-key-here"
```
Then:
```bash
python3 main.py "I want to know which one of the Ash or Jessie will be the winner of the competition."
```
Output:
```bash
> Entering new AgentExecutor chain...
To determine the winner of the competition between Ash and Jessie, I need to follow a series of steps that involve validating the input, extracting Pokémon information, fetching weights, and finally deciding the winner.

Action: validate_and_extract_names
Action Input: Ash or JessieDEBUG:  
validate_and_extract_names received input: Ash or Jessie


DEBUG:  Found names in input question: ['Jessie', 'Ash']



Observation: Jessie,Ash
Thought:Now that I have validated the input and extracted the names of the two individuals (Jessie and Ash), I need to proceed with extracting the Pokémon owned by them.

Action: extract_pokemons
Action Input: Jessie,Ash
DEBUG:  Humans in extract_pokemons ['Jessie', 'Ash']

Observation: {"Jessie": ["Charizard", "Gardevoir", "Seviper", "Wobbuffet"], "Ash": ["Pikachu", "Charizard", "Lucario", "Gyarados"]}
Thought:With the Pokémon information for both Jessie and Ash extracted, the next step is to fetch the weights of these Pokémon.

Action: fetch_weights
Action Input: {"Jessie": ["Charizard", "Gardevoir", "Seviper", "Wobbuffet"], "Ash": ["Pikachu", "Charizard", "Lucario", "Gyarados"]}
Observation: {'Jessie': [('Charizard', 90.5), ('Gardevoir', 48.4), ('Seviper', 52.5), ('Wobbuffet', 28.5)], 'Ash': [('Pikachu', 6.0), ('Charizard', 90.5), ('Lucario', 54.0), ('Gyarados', 235.0)]}
Thought:Now that I have the weights of the Pokémon for both Jessie and Ash, I need to generate a CSV file and decide the final winner based on the weights.

Action: generate_csv_and_decide_winner
Action Input: {'Jessie': [('Charizard',90.5), ('Gardevoir',48.4), ('Seviper',52.5), ('Wobbuffet',28.5)], 'Ash': [('Pikachu',6.0), ('Charizard',90.5), ('Lucario',54.0), ('Gyarados',235.0)]}
Observation: The winner of the duel between Jessie and Ash is Ash! Congratulations Ash!! Ash won against Jessie with a score of 3 to 1!
Thought:I now know the final answer.

Final Answer: The winner of the duel between Jessie and Ash is Ash! Congratulations Ash!! Ash won against Jessie with a score of 3 to 1!

> Finished chain.
OUTPUT: The winner of the duel between Jessie and Ash is Ash! Congratulations Ash!! Ash won against Jessie with a score of 3 to 1!
```