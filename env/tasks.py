
def easy():
    return{
        "fuel_available": 1000,
        "requests":{
            "hospital": 300,
            "transport": 300,
            "public": 200
        }, 
        "urgency": "low"
    }

def medium():
    return{
        "fuel_available": 700,
        "requests":{
            "hospital": 400,
            "transport": 400,
            "public": 400
        },
        "urgency": "medium"
    }

def hard():
    return{
        "fuel_available": 500,
        "requests":{
            "hospital": 500,
            "transport": 400,
            "public": 300

        },
        "urgency": "high"
    }

TASKS= {
    "easy": easy,
    "medium": medium,
    "hard": hard
}