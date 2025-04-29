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
export GROK_API_KEY="your-api-key-here"
```
Then:
```bash
python3 main.py "I want to know which one of the Ash or Jessie will be the winner of the competition."
```