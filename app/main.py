from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

snippet = {
    "1" : {
        "id" : "1",
        "title" : "BS",
        "language" : "cpp",
        "code" : "Plz wait code is being updated ! ",
        "description" : " Method : divide & conquere"
        },
    "2" : {
        "id" : "2",
        "title" : "merge sort",
        "language" : "cpp",
        "code" : "Plz wait code is being updated ! ",
        "description" : " Method : divide & conquere"
        },
    "3" : {
        "id" : "3",
        "title" : "Quick sort",
        "language" : "cpp",
        "code" : "Plz wait code is being updated ! ",
        "description" : " Method : divide & conquere"
        }
    

}

app = FastAPI()
class item(BaseModel):
    id : str
    title : str
    language : str
    code : str
    description : str | None = None


@app.get("/snippet/{snippet_id}", response_model=item)
async def get_snippet(snippet_id : str ):
    if snippet_id not in snippet:
        raise HTTPException(status_code=404, detail="Snippet does not exists")
    return snippet[snippet_id]