import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain.llms import Ollama


# 1. Configuration for Streamlit App
def configure_app():
    st.set_page_config(page_title="LangChain: Summarize Text From YT or Website (Ollama)", page_icon="🦜")
    st.title("🦜 LangChain: Summarize Text From YT or Website (Ollama)")
    st.sidebar.title("Settings")


# 2. Input Section for URL
def get_url_input():
    st.subheader("Enter the URL to Summarize")
    generic_url = st.text_input("URL", label_visibility="collapsed", placeholder="Enter YouTube or Website URL")
    return generic_url


# 3. Input Validation
def validate_input(generic_url):
    if not generic_url.strip():
        st.error("Please provide a URL to get started.")
        return False
    elif not validators.url(generic_url):
        st.error("Invalid URL. It must be a valid YouTube or website URL.")
        return False
    return True


# 4. Load Content from URL (YouTube or Website)
def load_content(generic_url):
    try:
        if "youtube.com" in generic_url:
            loader = YoutubeLoader.from_youtube_url(generic_url, add_video_info=True)
        else:
            loader = UnstructuredURLLoader(
                urls=[generic_url],
                ssl_verify=False,
                headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
            )
        docs = loader.load()
        return docs
    except Exception as e:
        st.error(f"An error occurred while loading content: {e}")
        return None


# 5. Summarize Content using Ollama
def summarize_content(docs, llm, prompt_template):
    try:
        chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt_template)
        summary = chain.invoke(docs)
        return summary
    except Exception as e:
        st.error(f"An error occurred during summarization: {e}")
        return None


# 6. Main Summarization Logic
def run_summarization():
    configure_app()

    # Local Ollama Model
    llm = Ollama(model="llama3", base_url="http://localhost:11434")

    # Prompt template for summarization
    prompt_template = PromptTemplate(
        template="""
        Provide a summary of the following content in 300 words:
        Content: {text}
        """, 
        input_variables=["text"]
    )

    # Get URL Input
    generic_url = get_url_input()

    if st.button("Summarize Content"):
        if validate_input(generic_url):
            with st.spinner("Loading content..."):
                docs = load_content(generic_url)
                if docs:
                    with st.spinner("Summarizing content..."):
                        summary = summarize_content(docs, llm, prompt_template)
                        if summary:
                            st.success("Summary:")
                            st.write(summary)


# 7. Footer and Additional Info
def add_footer():
    st.sidebar.markdown("---")
    st.sidebar.info("Powered by [LangChain](https://github.com/hwchase17/langchain) and [Ollama](https://ollama.com/).")


# Run the app
if __name__ == "__main__":
    run_summarization()
    add_footer()
