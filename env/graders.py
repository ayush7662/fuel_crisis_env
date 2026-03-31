def grade(state, action):
    requests = state["requests"]
    fuel = state["fuel_available"]
    alloc = action.allocations

    score = 0.0

    if alloc.get("hospital",0) >= 0.7 * requests["hospital"]:
        score += 0.3

    if sum(alloc.values()) <= fuel:
        score += 0.3

    if alloc.get("public", 0 ) > 0:
        score += 0.2

    return{
        "score" : min(score, 1.0),
        "done": True
    }
        
