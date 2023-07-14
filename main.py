from fastapi import FastAPI, Path
app= FastAPI()

@app.get("/")
def home():
    return  {'Data': "Test"}


@app.get("/about")
def about():
    return {"Data": "About"}


        ##creating a path 
   

from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    price: float
    brand: Optional[str] = None
inventory = {}

class UpdateItem(BaseModel):
    name: Optional[str]= None
    price : Optional[float] =None
    brand: Optional[str]=None
        

@app.get("/get-item/{item_id}")
def get_item(item_id : int = Path(description="The ID of the item you would like to view. ", gt=0)):
    return inventory[item_id]


@app.post("/create-item")
def create_item(item_id:int, item:Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists,"}
    
    inventory[item_id]= {"name": item.name, "brand":item.brand, "price": item.price}
    ### accessing all the fields 
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item ID already exists,"}
    
    inventory[item_id]= {"name": item.name, "brand":item.brand, "price": item.price}
    ### accessing all the fields 
    return inventory[item_id]


