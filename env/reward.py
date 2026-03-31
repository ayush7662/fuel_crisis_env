def compute_reward(grade):
    return{
        "score": grade["score"],
        "breakdown": {
            "total": grade["score"]
        }
    }