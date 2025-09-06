from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend domain
origins = [
    "https://nextgenerationmart.com",  # Next Generation Mart
    "https://nxtgenmart.com",  # Next Generation Mart
    "https://lingaaannela.github.io/nxt-gen-aio",  # GitHub Pages
    "http://localhost:4200"            # optional, for local dev
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI on AWS EC2!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


# health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}
