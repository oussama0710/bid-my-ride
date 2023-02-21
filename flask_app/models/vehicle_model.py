from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DB
class Vehicle:
    def __init__(self,data):
        self.id=data["id"]
        self.admin_id=data["admin_id"]
        self.product_type=data["product_type"]
        self.mileage=data["mileage"]
        self.age=data["age"]
        self.transmission=data["transmission"]
        self.fuel_type=data["fuel_type"]
        self.power=data["power"]
        self.seats=data["seats"]
        self.vehicle_name=data["vehicle_name"]
        self.description=data["description"]
        self.photos=data["photos"]
        self.start_price=data["start_price"]
        self.auction_start_date=data["auction_start_date"]
        self.auction_last_date=data["auction_last_date"]
        self.created_at=data["created_at"]
        self.uptated_at=data["uptated_at"]
    @classmethod
    def save_vehicle(cls,data):
        query="""
        INSERT INTO vehicles (admin_id,prodect_type,mileage,age,transmission,fuel_type,power,seats,vehicle_name,
        description,photos,start_price,auction_start_date,auction_last_date)
        VALUES (%(admin_id)s,%(prodect_type)s,%(mileage)s,%(age)s,%(transmission)s,%(fuel_type)s,%(power)s,%(seats)s,%(vehicle_name)s
        ,%(description)s,%(photos)s,%(start_price)s,%(auction_start_date)s,%(auction_last_date)s) ; 
        """
        return connectToMySQL(DB).query_db(query,data)
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM vehicles WHERE product_type=%(prodect_type)s AND make=%(make)s AND price=%(start_price)s
        ORDER BY start_price %(order)s ;
        """
        return connectToMySQL(DB).query_db(query)
    @classmethod
    def delete(cls, data):
        query = """DELETE FROM vehicles WHERE id = %(id)s;"""
        return connectToMySQL(DB).query_db(query,data)
    

