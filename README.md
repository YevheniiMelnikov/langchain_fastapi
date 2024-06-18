## FastAPI Text Summarizer
### Setup

#### Create a virtual environment:

```bash
python -m venv env
```
```bash
source env/bin/activate  
```
#### On Windows use: 
```bash 
env\Scripts\activate
 ```
#### Install dependencies:

```bash
pip install fastapi uvicorn langchain
```

#### Set up following env variables:
- LANGCHAIN_API_KEY
- OPENAI_API_KEY

#### Run the application:
```bash
uvicorn main:app --reload
```
#### Test the endpoint:

Send a POST request to http://127.0.0.1:8000/summarize with a JSON body containing the text to be summarized.