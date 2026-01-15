from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Create an instance of our application
app = FastAPI()



posts: list[dict] = [
    {
        "id" : 1,
        "author" : "Hamza Ahmed",
        "title" : "FastAPI Blog Project",
        "content" : "This ...",
        "date_posted" : "January 2026",

    },
    {
        "id" : 2,
        "author" : "Nabeeha Ahmed",
        "title" : "Ewe Move",
        "content" : "That ...",
        "date_posted" : "January 2026",

    },
]


# Create a home route for the API 
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f'<h1>{posts[0]['title']}</h1>'

# API endpoint for snippets 
@app.get("/api/posts")
def get_posts():
    return posts