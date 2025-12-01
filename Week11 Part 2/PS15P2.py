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

car1 = Sport('Test make', 'Test model', 15000)
car1.sport_wheels = "Y"
car1.sport_engine = "N"
car1.sport_interior = "Y"

print(car1.make)
print(car1.model)
print(car1.sticker_price)
print(car1.price_with_options())
