def is_valid(s: str) -> bool:
    balanced = 0
    
    for bracket in s:
        if bracket == "(":
            balanced += 1
        elif bracket == ")":
            balanced -= 1

        if balanced < 0:
            return False
    return balanced == 0