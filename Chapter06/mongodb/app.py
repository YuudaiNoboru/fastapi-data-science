from bson import ObjectId, errors
from fastapi import Depends, FastAPI, HTTPException, Query, status
from motor.motor_asyncio import AsyncIOMotorDatabase

from Chapter06.mongodb.database import get_databese
from Chapter06.mongodb.models import (
    CommentCreate,
    Post,
    PostCreate,
    PostParticialUpdate
)

app = FastAPI()

async def pagination(skip: int = Query(0, ge=0),
                    limit: int = Query(10, ge=0),
                    ) -> tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)

async def get_object_id(id: str) -> ObjectId:
    try:
        return ObjectId(id)
    except (errors.InvalidBSON, TypeError):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

async def get_post_or_404(
        id: ObjectId = Depends(get_object_id),
        database: AsyncIOMotorDatabase = Depends(get_databese)
        ) -> Post:
    raw_post = await database["posts"].find_one({"_id": id})
    if raw_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return Post(**raw_post)

@app.get("/posts", response_model=list[Post])
async def list_post(
    pagination: tuple[int, int] = Depends(pagination),
    database: AsyncIOMotorDatabase = Depends(get_databese)
    ) -> list[Post]:
    skip, limit = pagination
    query = database["posts"].find({}, skip=skip, limit=limit)
    result = [Post(**raw_post) async for raw_post in query]
    return result

@app.get("/posts/{id}", response_model=Post)
async def get_post(post: Post = Depends(get_post_or_404)) -> Post:
    return post

@app.post("/posts", response_model=Post, status_code=status.HTTP_201_CREATED)
async def create_post(
    post_create: PostCreate, database: AsyncIOMotorDatabase = Depends(get_databese)
    ) -> Post:
    post = Post(**post_create.model_dump())
    await database["posts"].insert_one(post.model_dump(by_alias=True))
    post = await get_post_or_404(post.id, database)

    return post

@app.patch("/posts/{id}", response_model=Post)
async def update_post(
    post_update: PostParticialUpdate,
    post: Post = Depends(get_post_or_404),
    database: AsyncIOMotorDatabase = Depends(get_databese)
    ) -> Post:
    await database["posts"].update_one(
        {"_id": post.id}, {"$set": post_update.model_dump(exclude_unset=True)}
    )
    post = await get_post_or_404(post.id, database)

    return post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post: Post = Depends(get_post_or_404),
                      database: AsyncIOMotorDatabase = Depends(get_databese)
                      ):
    await database["posts"].delete_post({"_id": post.id})

@app.post("/posts/{id}/comments", response_model=Post, status_code=status.HTTP_201_CREATED)
async def create_comment(
    comment: CommentCreate,
    post: Post = Depends(get_post_or_404),
    database: AsyncIOMotorDatabase = Depends(get_databese)
    ) -> Post:
    await database["posts"].update_one(
        {"_id": post.id}, {"$push": {"comments": comment.model_dump()}}
    )

    post = await get_post_or_404(post.id, database)

    return post