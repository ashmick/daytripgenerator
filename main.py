destinations= ["Aruba", "New York City", "California", "Hawaii"]
restaurants= ["Lima Bistro", "Cafe Neo", "Indian Bistro", "Tastee's Delights"]
transportations= ["bus", "train", "cab", "boat"]
entertainments= ["Snorkel with fish", "Hiking", "Escape Room", "Siteseeing"]

print("We're so happy that you chose us to help you plan your next trip. If you got the cash we have the plans! ")
    
for destination in destinations:
    answer_to_choice= input(print(f'The location we have chose for you is {destination}. Would you like that choice y/n? '))
    if answer_to_choice == "y":
        print ("Great choice I think you will love it there! Let's move on to your restaurant recommendations!")
        break
    elif answer_to_choice == "n":
        print ("No worries! We have a few other options for you! Let's try another one! ")
        continue
    
    
for restaurant in restaurants:
    answer_to_restaurant= input(print(f'The restaurant we have as an option is {restaurant}. Would you like that choice y/n? '))
    if answer_to_restaurant == "y":
        print ("Great choice again. I think the food is wonderful there. Let's move on to your transportation options!")
        break
    elif answer_to_restaurant == "n":
        print ("No worries! We have a few other options for you! Let's try another one! ")
        continue
    
for transportation in transportations:
    answer_to_transportation= input(print(f'The transportation option we suggest as an option is {transportation}. Would you like that choice y/n? '))
    if answer_to_transportation == "y":
        print ("Great choice again. The experience will be great. Let's move on to your entertainment options!")
        break
    elif answer_to_transportation == "n":
        print ("No worries! We have a few other options for you! Let's try another one! ")
        continue
    
    
for entertainment in entertainments:
    answer_to_entertainment= input(print(f'The transportation option we suggest as an option is {entertainment}. Would you like that choice y/n? '))
    if answer_to_entertainment == "y":
        print ("Great choice again. The fun you have will be amazing! Let's confirm your choices!")
        break
    elif answer_to_transportation == "n":
        print ("No worries! We have a few other options for you! Let's try another one! ")
        continue
    
    

    

    
    
    
            
            