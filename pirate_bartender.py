import random

def drink_preferences():
    """ drink_preferences
    Asks customer what their drink preferences are based on dictionary of
    questions. Customer will answer as 'y' or 'n'. Answers will be stored in
    new dictionary as Boolean value. Function returns dictionary of answers.
    """
    questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
    }
    
    # Create loop that asks questions.
    """
    while there is a key in the dictionary, ask the value as a question 
    change the answer to the question to True or False
    put the answer in a new dictionary called answers with the same key
    as questions and the True or False as the value 
    
    if strong is yes, set answers(strong - True)
    """
    
    
    # Error check for 'y' or 'n'.
    # Save answers in 'answers' dictionary as Booleans.
    ## Example: 'strong': True
    
    # return answers

def drink_construct():
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
    
    # Loop through 'answers' dictionary
    # If the attribute is True in answers, grab random value in ingredients
    ## dictionary and add to drink list
    
    # Sample random code, ingredients is a dictionary, need to access values:
    ## drink.append((random.choice(ingredients)))
    
    return drink
    
    drink_preferences()