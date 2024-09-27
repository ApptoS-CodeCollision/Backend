### Welcome to ApptoS

There are few steps to initiate our backend

1. pip install -r requirements.txt
2. pip show langchain_community and find out the path of langchain_community
3. cd {PATH}/langchain_community/vectorstores, vi faiss.py
4. modify add_texts functions (add embeddings to return)

python -m uvicorn main:app --reload --host=0.0.0.0 --port=4000
python -m uvicorn main:app --reload --port=4000

export PATH="/home/poqopo/.local/bin:$PATH"
