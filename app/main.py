from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings


# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"] # allow all origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World pushing out to ubuntu"}

# before using datsbases
# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "pizza tastes awesome", "id": 2}]

# def find_post(id):
#   for p in my_posts:
#     if p['id'] == id:
#       return p
    

# def find_post_index(id):
#   for i, p in enumerate(my_posts):
#     if p['id'] == id:
#       return i

# # Using postges to connect to database instead of sqlalchemy
# while True:
#   try:
#       conn = psycopg2.connect()
#       cursor = conn.cursor()
#       print("Database connection was successful")
#       break
    
#   except Exception as error:
#     print("Database connection failed")
#     print("The error was ", error)
#     time.sleep(2)
    

# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "pizza tastes awesome", "id": 2}]

# def find_post(id):
#   for p in my_posts:
#     if p['id'] == id:
#       return p
    

# def find_post_index(id):
#   for i, p in enumerate(my_posts):
#     if p['id'] == id:
#       return i

# # dependency for session
# def get_db():
#   db = SessionLocal()
#   try:
#     yield db
#   finally:
#     db.close

# @app.post("/posts")
# def create_posts(payload: dict = Body(...)): # converts everything in endpoint body into a python dictionary
#   print(payload)
#   # return {"data": "Successfull created posts"}
#   return {"new_post": f"title {payload['title']} content: {payload['content']}"}

# @app.get("/posts")
# def get_posts():
#   cursor.execute(""" SELECT * FROM posts """)
#   posts = cursor.fetchall()
#   return {"data": posts}

# # To implement pydantic
# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post: Post): # pydantic model automatically extracts the data from frontend
#   # print(post)
#   # print(post.dict()) # converts the pydatic model into python dictionary
#   post_dict = post.dict()
#   post_dict['id'] = randrange(0, 1000000)
#   my_posts.append(post_dict)
#   return {"data": post_dict}

# @app.get("/posts/latest") # for API structure, ensure this path is not the last one
# def get_latest_post(): 
#   post = my_posts[len(my_posts)-1]
#   return {"detail": post}

 
# @app.get("/posts/{id}") # provide path id for a single post
# def get_post(id: int): # automatically validates user input as integer
#   post = find_post(id)
#   if not post:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
#     # returns above instead of null from database
#   return {"post_detail": post}

 
# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#   index = find_post_index(id)
#   if index == None:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exit")
#   my_posts.pop(index)
#   return Response(status_code=status.HTTP_204_NO_CONTENT)  
 
# @app.put("/posts/{id}")
# def update_post(id: int, post: Post):
#   index = find_post_index(id)
#   if index == None:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exit")
#   post_dict = post.dict()
#   post_dict['id'] = id
#   my_posts[index] = post_dict
#   return {'data': post_dict}

  
  
# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, 
#           {"title": "favorite foods", "content": "Chicken Nuggets and Fufu", "id": 2}
#           ]

# def find_post(id):
#   for p in my_posts:
#     if p["id"] == id:
#       return p

# def find_index_post(id):
#   for i, p in enumerate(my_posts):
#     if p['id'] == id:
#       return i


# # @app.get("/")
# # def root():
# #     return {"message": "Welcome to my first API!!!"}

# # Testing session
# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#   posts = db.query(models.Post).all() # runs sql
#   return {"data": posts}

  # post_dict = post.dict()
  # post_dict['id'] = randrange(0, 10000000)
  # my_posts.append(post_dict)
  # print(post)
  # print(post.dict())
  # return {"message": "Updated Post created successfully"}
  # return {"new_post": f"{hotels['title']} : {hotels['content']}"}
  # return {"data": post_dict}
# title: str, content str, category, boolean

 