from fastapi.param_functions import Form
import tarantool
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from credentials import DATABASE_CREDENTIALS, HOSTNAME

database = DATABASE_CREDENTIALS.pop('database')

connection = tarantool.connect(**DATABASE_CREDENTIALS)
my_space = connection.space(database)

app = FastAPI()

templates = Jinja2Templates(directory="static/")


class Url(BaseModel):
    url: str


@app.get("/shortme")
async def shortme(request: Request):
    shortened = "Type a URL to resource"
    template = templates.TemplateResponse(
        "form.html", {"request": request, "shortened": shortened})
    return template


@app.post("/shortme")
async def shortme(request: Request, url: str = Form(...)):
    url_id = my_space.insert((None, url))[0][0]
    shortened = f"http://{HOSTNAME}/{url_id}"
    template = templates.TemplateResponse(
        'form.html', context={'request': request, 'result': shortened})
    return template


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
