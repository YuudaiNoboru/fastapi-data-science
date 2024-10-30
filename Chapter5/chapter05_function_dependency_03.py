from fastapi import FastAPI, Depends, Query, HTTPException, status
from pydantic import BaseModel

class PostBase(BaseModel):
    content: str

class PostCreate(PostBase):
    pass

class PostRead(PostBase):
    id: int

class Post(PostBase):
    id: int
    nb_views: int = 0


class PostUpdate(BaseModel):
    title: str | None = None
    content: str | None = None

class DummyDatabase:
    posts: dict[int, Post] = {}

db = DummyDatabase()

app = FastAPI()

async def pagination(skip: int = Query(0, ge=0), limit: int = Query(10, ge=0)) -> tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)

async def get_post_or_404(id: int) -> Post:
    try:
        return db.posts[id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.get("/items")
async def list_items(p: tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}

@app.post("/posts/{id}")
async def get(post: Post = Depends(get_post_or_404)):
    return post

@app.patch("/posts/{id}")
async def update(post_update: PostUpdate, post: Post = Depends(get_post_or_404)):
    updated_post = post.model_copy(update=post_update.model_dump())
    db.posts[post.id] = updated_post
    return updated_post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(post: Post = Depends(get_post_or_404)):
    db.posts.pop(post.id)