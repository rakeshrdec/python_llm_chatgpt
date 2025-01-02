import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
# from langchain.community.chat_models import ChatOpenAI

OPENAI_API_KEY = "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"
# Upload PDF FIle
st.header("My First ChatB0t")


with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a PDF file and start asking Questi0ns", type="pdf")


# Extract the text
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text+=page.extract_text()
        # st.write(text)

    # Break Text In to Chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=150,    # Using so that can't miss meaning full sentences even after 1000 chunk size
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    # st.write(chunks)

    # Now For Generating Vectors (Embeddings) :- We will use OpenAi
    #Genrate Embedding
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    # Create Vector Store  -- FAISS(Facebook AI Symmentocs)
    vector_store = FAISS.from_texts(chunks,embeddings)
    # embediing - (OPEN AI)
    # initilizing FAISS for us
    # store chunks and embedding the same

    # GET USER QUESTIONS
    user_question = st.text_input("Type Your Question Here")

    # DO SIMILARITY SEARCH
    if user_question:
        match = vector_store.similarity_search(user_question)
        # A = user_question
        # B = vectore DB -> vector_store
        # Now Comapre A & B for Question match
        st.write(match)

        llm = ChatOpenAI(
            openai_api_key = OPENAI_API_KEY,
            temprature = 0,
            max_tokens = 1000,
            model_name = "gpt-3.5-turbo"
        )
        # OUT PUT RESULT
        # chain ->take the question, get the relevant document, pass it to LLM, generate the output
        chain = load_qa_chain(llm, chain_type='stuff')
        response = chain.run(input_document = match , question = user_question)
        st.write(response)











