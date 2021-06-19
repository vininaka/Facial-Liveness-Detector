def question_bank(index):
    questions = [
                "Sorria",
                "Pisque os olhos",
                "Bravo",
                "Vire a face para direita",
                "Vire a face para esquerda"]
    return questions[index]

def challenge_result(question, out_model,blinks_up):
    if question == "Sorria":
        if len(out_model["emotion"]) == 0:
            challenge = "fail"
        elif out_model["emotion"][0] == "happy": 
            challenge = "pass"
        else:
            challenge = "fail"
    
    elif question == "Bravo":
        if len(out_model["emotion"]) == 0:
            challenge = "fail"
        elif out_model["emotion"][0] == "angry": 
            challenge = "pass"
        else:
            challenge = "fail"

    elif question == "Vire a face para direita":
        if len(out_model["orientation"]) == 0:
            challenge = "fail"
        elif out_model["orientation"][0] == "right": 
            challenge = "pass"
        else:
            challenge = "fail"

    elif question == "Vire a face para esquerda":
        if len(out_model["orientation"]) == 0:
            challenge = "fail"
        elif out_model["orientation"][0] == "left": 
            challenge = "pass"
        else:
            challenge = "fail"

    elif question == "Pisque os olhos":
        if blinks_up == 1: 
            challenge = "pass"
        else:
            challenge = "fail"

    return challenge