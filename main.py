from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

# Create an instance of our application
app = FastAPI()

# Initialise a templates object and set the dir to the templates dir we created
templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id" : 1,
        "author" : "Hamza Ahmed",
        "title" : "Hamza's Post",
        "content" : "This ...",
        "date_posted" : "January 2026",

    },
    {
        "id" : 2,
        "author" : "Nabeeha Ahmed",
        "title" : "Nabeeha's post",
        "content" : "That ...",
        "date_posted" : "January 2026",

    },
]


# Create a home route for the API 
@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request : Request):
    
    return templates.TemplateResponse(
        request,
        "home.html",
        # Context Dictionary 
        {
            "posts" : posts,
            "title" : "Home",
        },
        
        )

# API endpoint for snippets 
@app.get("/api/posts")
def get_posts():
    return posts


