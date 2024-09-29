from tortoise import run_async
from tortoise import Tortoise


#  creating db
async def init():
    await Tortoise.init(db_url='sqlite://db.mysql',
                        modules={'models': ['models']})
    await Tortoise.generate_schemas()

run_async(init())
