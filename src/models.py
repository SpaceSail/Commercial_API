from tortoise.models import Model
from tortoise import fields

# db scheme
class Order(Model):
    id = fields.IntField(pk=True)
    animal_name = fields.CharField(max_length=255)
    room_number = fields.IntField(max_length=3)
    breed_name = fields.CharField(max_length=255)
    time = fields.DatetimeField(auto_now=True)
    dogsitter_name = fields.CharField(max_length=255)
    added = fields.CharField(max_length=255)
    time_added = fields.CharField(max_length=255)

    def __str__(self):
        return self.animal_name


order = Order()
