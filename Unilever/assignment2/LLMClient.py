import os
from langchain_core.language_models import BaseChatModel

class LLMClient:
    def __init__(self, provider: str, model_name: str, temperature: float=0.2):
        self.llm: BaseChatModel | None = None

        if provider == "google":
            from google import genai
            from google.api_core import retry
            from langchain_google_genai import ChatGoogleGenerativeAI

            is_retriable = lambda e: (isinstance(e, genai.errors.APIError) and e.code in {429, 503})

            genai.models.Models.generate_content = retry.Retry(
                predicate=is_retriable)(genai.models.Models.generate_content)

            self.llm = ChatGoogleGenerativeAI(model=model_name,
                                              temperature=temperature,
                                              api_key=os.getenv("GOOGLE_API_KEY"))
        elif provider == "openai":
            from langchain.chat_models import ChatOpenAI
            self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)
        elif provider == "ollama":
            from langchain_community.chat_models import ChatOllama
            self.llm = ChatOllama(model=model_name, temperature=temperature, base_url="http://localhost:11434")
        elif provider == "groq":
            from langchain_groq import ChatGroq
            groq_api_key = os.getenv("GROQ_API_KEY")
            if not groq_api_key:
                raise ValueError("GROQ_API_KEY environment variable not set.")
            self.llm = ChatGroq(model_name=model_name, temperature=temperature, groq_api_key=groq_api_key)
        else:
            raise ValueError("Unsupported provider")

    def invoke(self, prompt: str):
        if self.llm:
            return self.llm.invoke(prompt)
        else:
            raise RuntimeError("LLM client not initialized.")