                  
import random

def greeting ():
    print(
        "Welcome to your very own Random Trip Generator!"
        )
    print(
        "If you have the cash then we got your plan! "
        )
greeting()


def random_destination():
    destination_list=["Guatamala", "Hondorus", "New York City", "California"]
    location=True
    while location == True:
        rand_dest_choice=random.choice(destination_list)
        location_choice = input(f'Would you like to go to {rand_dest_choice}? Choose y or n?')
        if location_choice== "y":
            location=False 
            return rand_dest_choice
        elif location_choice== "n":
            destination_list.remove(rand_dest_choice)
             
            
def random_restaurant():
    restaurant_list=["Mama Lucia's", "Applegate Market", "Irie Eats", "Sushimi Mimi's"]
    eat_time=True
    while eat_time == True:
        rand_rest_choice=random.choice(restaurant_list)
        rest_choice = input(f'Would you like to go to {rand_rest_choice}? Choose y or n?')
        if rest_choice== "y":
            eat_time=False
            return rand_rest_choice
        elif rest_choice== "n":
            restaurant_list.remove(rand_rest_choice)
            
def random_transportation():
    transportation_list=["Car", "Subway", "Boat", "Plane"]
    transport=True
    while transport == True:
        rand_transport_choice=random.choice(transportation_list)
        choice = input(f'Would you like to go by {rand_transport_choice}? Choose y or n?')
        if choice== "y":
            transport=False
            return rand_transport_choice
        elif choice== "n":
            transportation_list.remove(rand_transport_choice)
            
def random_entertainment():
    entertainment_list=["golfing", "scuba diving", "swimming w/ sharks", "siteseeing"]
    fun=True
    while fun == True:
        rand_entertainment_choice=random.choice(entertainment_list)
        entertainment_choice = input(f'Would you like to go {rand_entertainment_choice}? Choose y or n?')
        if entertainment_choice== "y":
            fun=False
            return rand_entertainment_choice
        elif entertainment_choice== "n":
            entertainment_list.remove(rand_entertainment_choice) 
       
def confirm_random_choices():
    confirmation=True
    while confirmation==True:
        print(f'You have selected {destination} as your destination.') 
        print(f'You will eat some delicious food at {restaurant}.') 
        print(f'You will arrive by {transportation}.')
        print(f'You will have a ball while {entertainment}.')
        confirmed_choice=input(print("Do you want to move forward with these choices? Type y or n."))
        if confirmed_choice=="y":
            confirmation=False
            print("You're going to have an amazing trip! Can't wait to hear all about it.")
                
        elif confirmed_choice=="n":
            change_destination=input(print(f'Is it the destination of {destination} that you want to change? y or n?'))
            if change_destination == "y":
                random_destination()
            elif change_destination== "n":
                change_restaurant=input(print(f'Is it the restaurant that you want to change? y or n?'))
                if change_restaurant=="y":
                    random_restaurant()
                elif change_restaurant=="n":
                    change_entertainment=input(print(f'Is it the entertainment that you want to change? y or n?'))
                    if change_entertainment=="y":
                        random_entertainment()
                    elif change_entertainment=="n":
                        change_transportation=input(print(f"So it's the transportation you want to change. Correct? y or n?"))
                        if change_transportation=="y":
                            random_transportation()
                        elif change_transportation=="n":
                            print("I'm not sure what you want anymore. Let's start over!")
                            confirmation=False

# def confirm_dest():
#     user_choice()
#     print(f' Would you like to go to {user_choice()}?')
    
# confirm_dest()

destination=random_destination()  
print(destination) 

restaurant= random_restaurant()
print(restaurant)

transportation=random_transportation()
print(transportation)
 
entertainment= random_entertainment()
print(entertainment)
   
confirmation=confirm_random_choices()

   
# while choice=="n":
    
#         del rand_choice
#         continue
#     print("No worries, I have other options left")
    

# user_choice ()


