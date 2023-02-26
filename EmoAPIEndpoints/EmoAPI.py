from fastapi import FastAPI
from fastapi import Query
from fastapi.middleware.cors import CORSMiddleware

from transformers import RobertaTokenizerFast, TFRobertaForSequenceClassification, pipeline

tokenizer = RobertaTokenizerFast.from_pretrained("arpanghoshal/EmoRoBERTa")
model = TFRobertaForSequenceClassification.from_pretrained("arpanghoshal/EmoRoBERTa", from_pt = True)

emotion = pipeline('sentiment-analysis', 
                    model=model, tokenizer=tokenizer)



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/text")
async def getSentiment(data:str = Query(...)):
    return pipeline(data)