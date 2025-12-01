class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price 

    def discount_price(self):
        return self.sticker_price * 0.90

class Sport(Car): 
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.sport_wheels = "N"
        self.sport_engine = "N"
        self.sport_interior = "N"
     
    def price_with_options(self):
        updated_price = self.discount_price()

        if self.sport_wheels == "Y":
            updated_price = updated_price + 1000.00
        
        if self.sport_engine == "Y":
            updated_price = updated_price + 3000.00

        if self.sport_interior == "Y":
            updated_price = updated_price + 2000.00

        return updated_price

class Luxury(Sport):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.sport_wheels = "N"
        self.sport_engine = "N"
        self.sport_interior = "N"
        self.GPS = "N"
        self.self_driving = "N"

    def price_with_options(self):
        updated_price = self.discount_price()

        if self.sport_wheels == "Y":
            updated_price = updated_price + 1000.00
        
        if self.sport_engine == "Y":
            updated_price = updated_price + 3000.00

        if self.sport_interior == "Y":
            updated_price = updated_price + 2000.00

        if self.GPS == "Y":
            updated_price = updated_price + 5000.00

        if self.self_driving == "Y":
            updated_price = updated_price + 10000.00

        return updated_price
       


car1 = Sport('Test make', 'Test model', 15000)
car1.sport_wheels = "Y"
car1.sport_engine = "N"
car1.sport_interior = "Y"

car2 = Luxury('Fancy', 'Example', 200000)
car2.sport_wheels = "Y"
car2.sport_engine = "Y"
car2.sport_interior = "Y"
car2.GPS = "Y"
car2.self_driving = "Y"

print(car2.make)
print(car2.model)
print(car2.sticker_price)
print(car2.price_with_options())
