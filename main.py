import uuid
import time
import fastapi

id = str(uuid.uuid4())
app = fastapi.FastAPI()


@app.get("/")
def index():
    return id


@app.get("/s")
def s():
    return str(int(time.time()))
