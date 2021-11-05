import tarantool
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from credentials import DATABASE_CREDENTIALS, HOSTNAME

database = DATABASE_CREDENTIALS.pop('database')

connection = tarantool.connect(**DATABASE_CREDENTIALS)
my_space = connection.space(database)

app = FastAPI()


class Url(BaseModel):
    url: str


@app.post("/set")
def set_url(url: Url):
    url = url.url
    url_id = my_space.insert((None, url))[0][0]
    return {"shortened": f"http://{HOSTNAME}/{url_id}"}


@app.get("/{url_id}")
def get_url(url_id: str):
    url = my_space.select(int(url_id))[0][1]
    print(url)
    return RedirectResponse(url, status_code=308)
