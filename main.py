import uuid
import fastapi

id = str(uuid.uuid4())
app = fastapi.FastAPI()


@app.get("/")
def index():
    return id
