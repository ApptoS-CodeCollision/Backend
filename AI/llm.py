from langchain_openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

openai = OpenAI()

embeddings = OpenAIEmbeddings()

template = """You are a helpful assistant with expertise in extracting the most relevant information from any given context.
Based on the context provided, analyze it to find the answer and respond accordingly, aligned with the role defined.
Context: {context}

Question: {question}

Answer:"""

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=template,
)

# 5. Function to generate an answer using the retrieved documents
def generate_answer(question, retrieved_docs):
    # Combine the content of the retrieved documents into a single context string
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])
    
    # Prepare the prompt with context and question
    final_prompt = prompt.format(context=context, question=question)
    print(final_prompt)

    # Using the chat completion endpoint for GPT-4
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": final_prompt}
        ],
        temperature=0.7,
        max_tokens=512
    )
    return response