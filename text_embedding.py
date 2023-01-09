from sentence_transformers import SentenceTransformer
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

def text_embed(text):
    with torch.no_grad():
        try:
            embedded = model.encode(text, device=device).tolist()
            return embedded
        except Exception as e:
            return {"error ": e}