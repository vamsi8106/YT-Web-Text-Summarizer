# LangChain-Summarize-Text-From-YouTube-or-Website-Ollama
This project is a Streamlit app that summarizes content from YouTube videos or websites using the local Ollama language model (LLM). The app uses LangChain to load and summarize content, leveraging Ollama for local LLM inference.   

## Requirements

Before running the application, make sure you have the following software installed:

1. **Python**: Python 3.10.
2. **Conda**: Package and environment management system.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/vamsi8106/YT-Web-Text-Summarizer.git
2. **Create and Activate a Conda Environment**

   ```bash
   conda create --n ollama_env python=3.10
   ```
   ```bash
   conda activate ollama_env
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt     
4. **Set Up Ollama**
   ```bash
   ollama pull llama3
   
5. **Run the Streamlit App**
   ```bash
   streamlit run app.py
