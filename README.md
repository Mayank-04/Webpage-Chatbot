# 🧠 WebPage Q&A Chatbot

A lightweight chatbot that answers **only based on the content of a specific webpage** using **Groq's Compound-Beta-Mini** and **Meta's LLaMA 3.2** models. Hosted on **Streamlit**, this chatbot provides fast, focused answers with minimal hallucination.

---

## 🚀 Features

- ✅ Dynamic webpage scraping and content indexing
- ✅ Accurate question answering grounded in webpage content only
- ⚡ Powered by **Groq Compound-Beta-Mini**
- 🦙 Utilizes **Meta LLaMA 3.2**
- 🌐 Interactive UI via **Streamlit**
- 🧠 Uses embeddings + retrieval to ensure relevance
- 🛡️ Hallucination-resistant — answers only what the page says

---

## 🏗️ Architecture

    A[User Input] --> B[Streamlit UI]
    B --> C[Webpage Scraper & Cleaner]
    C --> D[Text Chunking & Embedding]
    D --> E[Vector Store (FAISS or Chroma)]
    E --> F[Retriever]
    F --> G[LLaMA 3.2 via Groq]
    G --> H[Answer Displayed in UI]

---
⚙️ Installation

1. Clone the repository
   ```
   git clone https://github.com/Mayank-04/Webpage-Chatbot
   cd webpage-chatbot

3. Set up a virtual environment (recommended)
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

5. Install dependencies
   ```
   pip install -r requirements.txt

7. Set up your .env file
   Create a .env file in the root directory and add your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here

🧪 Usage

Run the chatbot locally:
```
streamlit run app.py
```
1.Enter the URL of a webpage.
2.Ask a question about that page.
3.The chatbot will only respond using that page’s content.

🧠 Models

This chatbot uses:
• Groq Compound-Beta-Mini for fast inference
• Meta’s LLaMA 3.2 for high-quality reasoning

Models are accessed via the Groq Cloud API.
