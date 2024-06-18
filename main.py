import os

from fastapi import FastAPI, HTTPException
from langchain_core.runnables import RunnableSequence
from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

app = FastAPI()


class TextToSummarize(BaseModel):
    text: str


os.environ["LANGCHAIN_TRACING_V2"] = "true"
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
prompt_template = """Write a concise summary of the following:
"{text}"
CONCISE SUMMARY:"""
prompt = PromptTemplate.from_template(prompt_template)
sequence = RunnableSequence(prompt | llm)


@app.post("/summarize")
async def summarize(text_to_summarize: TextToSummarize):
    try:
        input_data = {"text": text_to_summarize.text}
        result = sequence.invoke(input_data)
        summary = result["output_text"]
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
