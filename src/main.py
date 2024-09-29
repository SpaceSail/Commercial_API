from datetime import datetime

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from starlette.responses import JSONResponse

from models import order


morning = datetime.now().replace(hour=7, minute=0)
night = datetime.now().replace(hour=23, minute=0, second=0)
app = FastAPI()

register_tortoise(
    app=app,
    db_url='sqlite://db.mysql',
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)

# bblank page
@app.get("/")
async def root():
    return {"Hello": "World"}

# making an order
@app.post("/order")
async def make_order(animal_name: str, room_number: int,
                     breed: str, dogsitter: str):
    # checking the time
    if morning > datetime.now() or night < datetime.now():
        return JSONResponse(status_code=200, content={"message": "Please make"
                                                                 "sure that "
                                                                 "order time "
                                                                 "is not "
                                                                 "earlier "
                                                                 "than 07.00 "
                                                                 "and not "
                                                                 "later than "
                                                                 "23.00"})
    else:
        # formatting time and date according to docs
        date = datetime.today().strftime('%Y-%m-%d')
        time = datetime.now().replace(minute=0).strftime('%H:%M') if (
                datetime.now() < datetime.now().replace(minute=30)) \
            else datetime.now().replace(minute=0).strftime('%H:%M')
        # create db record
        await order.create(animal_name=animal_name,
                           room_number=room_number,
                           breed_name=breed,
                           dogsitter_name=dogsitter,
                           added=date,
                           time_added=time)
        return JSONResponse(status_code=200, content={"message": "order "
                                                                 "created"})


@app.get("/{date}")
# getting the list of all orders
async def read_order(date: str):
    response = await order.filter(added=date)
    return response
