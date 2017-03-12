import random

valid  = {"yes":True, "y":True, "no":False, "n":False}
drink_response = {"strong":False, "salty":False, "bitter":False, "sweet":False, "fruity":False}
    
def drink_preferences():
    """ drink_preferences
    Asks customer what their drink preferences are based on dictionary of
    questions. Customer will answer as 'y' or 'n'. Answers will be stored in
    new dictionary as Boolean value. Function returns dictionary of answers.
    """
    questions = {
    "strong": "Do ye like yer drinks strong? (y/n) ",
    "salty": "Do ye like it with a salty tang? (y/n) ",
    "bitter": "Are ye a lubber who likes it bitter? (y/n) ",
    "sweet": "Would ye like a bit of sweetness with yer poison? (y/n) ",
    "fruity": "Are ye one for a fruity finish? (y/n) ",
    }
    
    strong = input(questions["strong"])
    salty = input(questions["salty"])
    bitter = input(questions["bitter"])
    sweet = input(questions["sweet"])
    fruity = input(questions["fruity"])
    
    if salty in valid:
        drink_response["salty"] = valid[salty]
    if bitter in valid:
        drink_response["bitter"] = valid[bitter]
    if strong in valid:
        drink_response["strong"] = valid[strong]
    if fruity in valid:
        drink_response["fruity"] = valid[fruity]
    if sweet in valid:
        drink_response["sweet"] = valid[sweet]
    
    return drink_response

def drink_construct(responses):
    """ drink_construct
    Takes in 'answers' dictionary as parameter. Create empty list for drink.
    For every True in answers dictionary, find random ingredient associated
    with drink preference and add to empty list. Return drink.
    """
    
    ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
    }
    
    drink = []
    
    if responses["salty"] == True:
        drink.append(random.choice(ingredients["salty"]))
    if responses["bitter"] == True:
        drink.append(random.choice(ingredients["bitter"]))
    if responses["strong"] == True:
        drink.append(random.choice(ingredients["strong"]))
    if responses["fruity"] == True:
        drink.append(random.choice(ingredients["fruity"]))
    if responses["sweet"] == True:
        drink.append(random.choice(ingredients["sweet"]))
        
    return drink
    
if __name__ == "__main__":
    drink_preferences()
    print(drink_construct(drink_response))