def z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название Ресторана {self.restaurant_name}, кухня: {self.cuisine_type}")

        def open_restaurant(self):
                print("Ресторан сейчас открыт.")

    newRestaurant = Restaurant("Lowdawe","французская")
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название Ресторана {self.restaurant_name}, кухня: {self.cuisine_type}")

    restaurant1 = Restaurant("dgbdrb", "Итальянская")
    restaurant2 = Restaurant("Фравпивя", "Немецкая")
    restaurant3 = Restaurant("вапивапи", "Домашняя")

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

def z3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating=0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"Название Ресторана {self.restaurant_name}, кухня: {self.cuisine_type} Рейтинг: {self.rating}")

        def update_rating(self, new_rating):
                print(f"Изначальный рейтинг ресторана {self.rating}")
                self.rating = new_rating
                print(f"Рейтинг ресторана был обновлен {self.rating}")
                print(f"Новый, обновленный рейтинг ресторана: {self.rating}")

    restaurant = Restaurant("Lowdawe", "французская", "5")




    new_rating = input("Введите новый рейтинг для ресторана: ")
    restaurant.update_rating(new_rating)
z1()
z2()
z3()