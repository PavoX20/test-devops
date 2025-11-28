from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI()


class MessageInput(BaseModel):
    message: str
    to: str

    from_: str = Field(None, alias="from")
    timeToLifeSec: int


@app.post("/DevOps")
async def devops_endpoint(
    item: MessageInput,

    x_parse_rest_api_key: str = Header(None, alias="X-Parse-REST-API-Key"),
    x_jwt_kwy: str = Header(None, alias="X-JWT-KWY")
):

    expected_key = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"
    if x_parse_rest_api_key != expected_key:
        raise HTTPException(status_code=401, detail="Invalid API Key")


    if not x_jwt_kwy:
        raise HTTPException(status_code=401, detail="Missing JWT")


    return {
        "message": f"Hello {item.to} your message will be send"
    }


@app.api_route("/DevOps", methods=["GET", "PUT", "DELETE", "PATCH"])
async def catch_all_methods():
    return JSONResponse(content="ERROR", status_code=405)