from peewee import *
from datetime import date

db = SqliteDatabase("laba.db")


class Transport(Model):
    id_transport = PrimaryKeyField()
    mark = TextField()
    registration_date = DateField()
    color = TextField()

    class Meta:
        database = db


class Receiver(Model):
    id_receiver = PrimaryKeyField()
    last_name = TextField()
    first_name = TextField()
    patronymic_name = TextField()
    date_of_birth = DateField()
    postal_code = TextField()
    city = TextField()
    street = TextField()
    house = TextField()
    apartment = TextField()
    phone_number = TextField()

    class Meta:
        database = db


class Order(Model):
    id_order = PrimaryKeyField()
    id_sender = IntegerField()
    id_receiver = IntegerField()
    order_date = DateField()
    delivery_date = DateField()
    delivery_price = FloatField()
    id_courier = IntegerField()
    id_transport = IntegerField()

    class Meta:
        database = db


db.create_tables([Transport, Receiver, Order])

transport_1 = Transport(mark="BMW", registration_date=date(2023, 6, 1), color="Black")
transport_1.save()

transport_2 = Transport(mark="Tesla", registration_date=date(2021, 8, 15), color="Red")
transport_2.save()

receiver_1 = Receiver(last_name="Ivanov", first_name="Ivan", patronymic_name="Ivanovich",
                      date_of_birth=date(1980, 10, 10), postal_code="101000", city="Saint Petersburg",
                      street="Nevsky Prospect", house="10", apartment="45", phone_number="89030001234")
receiver_1.save()

receiver_2 = Receiver(last_name="Petrov", first_name="Petr", patronymic_name="Petrovich",
                      date_of_birth=date(1990, 5, 25), postal_code="200020", city="Moscow",
                      street="Tverskaya", house="25", apartment="12", phone_number="89215556677")
receiver_2.save()

order_1 = Order(id_sender=2, id_receiver=1, order_date=date(2024, 11, 10),
                delivery_date=date(2024, 11, 12), delivery_price=150.75, id_courier=2, id_transport=1)
order_1.save()

order_2 = Order(id_sender=1, id_receiver=2, order_date=date(2024, 11, 13),
                delivery_date=date(2024, 11, 14), delivery_price=200.40, id_courier=2, id_transport=2)
order_2.save()