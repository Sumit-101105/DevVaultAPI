from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

snippet_db = {
    "1": {
        "id": "1",
        "title": "BS",
        "language": "cpp",
        "code": "Plz wait code is being updated ! ",
        "description": " Method : divide & conquere",
    },
    "2": {
        "id": "2",
        "title": "merge sort",
        "language": "cpp",
        "code": "Plz wait code is being updated ! ",
        "description": " Method : divide & conquere",
    },
    "3": {
        "id": "3",
        "title": "Quick sort",
        "language": "cpp",
        "code": "Plz wait code is being updated ! ",
        "description": " Method : divide & conquere",
    },
}

app = FastAPI()


class Snippet_db(BaseModel):
    id: str
    title: str
    language: str
    code: str
    description: str | None = None


@app.get("/snippet_db/{snippet_db_id}", response_model=Snippet_db)
async def get_snippet_db(snippet_db_id: str):
    if snippet_db_id not in snippet_db:
        raise HTTPException(status_code=404, detail="Snippet_db does not exists")
    return snippet_db[snippet_db_id]


@app.get("/snippet_db")
async def get_all_snippet_db():
    return snippet_db


@app.get("/snippet_db/")
async def get_snippet_dbs(search: str | None = None):
    if search:
        search_lower = search.lower()
        return {
            id: data
            for id, data in snippet_db.items()
            if search_lower in data["title"].lower()
            or search_lower in data["language"].lower()
            or search_lower in data["id"].lower()
        }
    return snippet_db


@app.post("/snippet_db/")
async def post_snippet_db(item: Snippet_db):
    if item.id in snippet_db:
        raise HTTPException(status_code=409, detail="This id is already taken")
    snippet_db[item.id] = item.model_dump()
    return item


@app.delete("/snippet_db/{snippet_db_id}")
async def del_snippet_db(
    snippet_db_id: str,
):
    if snippet_db_id not in snippet_db:
        raise HTTPException(status_code=404, detail="snippet_db not found")
    del snippet_db[snippet_db_id]
    return {"ok": True}


@app.put("/snippet_db/{snippet_db_id}", response_model= Snippet_db)
async def put_snippet_db(snippet_db_id : str, snippet_db : Snippet_db):
    stored_snippet_db = snippet_db[snippet_db_id]
    stored_model = Snippet_db(**stored_snippet_db)
    update_data = snippet_db.model_dump(exclude_unset=True)
    updated_snippet_db= stored_model.model_copy(updated=update_data)
    Snippet_db[snippet_db_id] = updated_snippet_db
    return updated_snippet_db
