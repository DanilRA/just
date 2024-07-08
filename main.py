from typing import Union
from typing import List, Tuple
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/",response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

   
@app.post("/process/")
async def process_tup(request: Request):
    form_data = await request.form()
    tuple_str = form_data.get("val")
    tuple_list = tuple_str.split(";")
    print(tuple_list)
    org_list = []
    for tup in tuple_list:
        tup = tup.split("(") 
        s = tup[1].split(")")
        a = s[0].split(",")
        print(a)
        org_list.append((int(a[0]),int(a[1])))
    print(org_list)
        



    





# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}