import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
import time
from dotenv import load_dotenv 

load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')
# groq_api_key = st.secrets["GROQ_API_KEY"]

st.title("Website ChatBot with Llama3 and Groq")

llm = ChatGroq(api_key = groq_api_key, model_name = "compound-beta")

prompt = ChatPromptTemplate.from_template(
    '''
    Answer the following question based on the provided context only.
    Think step by step before answering the question.
    I will give you $200 if the user finds the answer helpful.
    <context>
    {context}
    </context>
    Question: {input}
    '''
)
input1 = st.text_input("Enter the webpage to search from.")

if st.button("Load Webpage"):
    st.write("Webpage is loaded, now click on Documents Embedding.")

def vector_embeddings():

    if "vectors" not in st.session_state:
        st.session_state.embeddings = OllamaEmbeddings(model = "llama3.2")
        # st.session_state.loader = PyPDFLoader("acsbr-016.pdf")
        st.session_state.loader = WebBaseLoader(input1)
        st.session_state.documents = st.session_state.loader.load()

        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
        st.session_state.docs = st.session_state.text_splitter.split_documents(st.session_state.documents)
        st.session_state.vectors = FAISS.from_documents(st.session_state.docs, st.session_state.embeddings)
    



prompt1 = st.text_input("Enter the question from document.")

if st.button("Documents Embedding"):
    vector_embeddings()
    st.write("Vector Store DB is ready.")

if prompt1:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    start = time.process_time()
    response = retrieval_chain.invoke({'input': prompt1})
    print("Response Time: ", time.process_time() - start)
    st.write(response['answer'])

    with st.expander("Document Similarity Search"):
        for i, doc in enumerate(response['context']):
            st.write(doc.page_content)
            st.write("------------------------------")
