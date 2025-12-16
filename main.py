import random

separator = "-"
separator_qty = 47
allowed_elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ELEMENTS = 4
limitations = {"position": 0, "value": "0"}
ending_text = "Correct, you've guessed the right number"
greeting = "Hi there!"
description = """I've generated a random 4 digit number for you.
    Let's play a bulls and cows game."""
command = "Enter a number: "


def generate_separator(separator: str, n: int) -> str:
    """Returns a string consisting of n separators."""
    return separator*n


def generate_list(elements: list, element_qty: int) -> list:
    """Returns a list containing randomly generated elements.
    """
    input = []
    for element in range(element_qty):
        element = random.choice(elements)
        input.append(str(element))
    return input


def check_input(input: list, elements: list,
                element_qty: int, limits: dict) -> str:
    """Checks if the input meets the specified conditions:
    number of elements, unique values, limitations and allowed elements.
    Returns str with error message or is empty if the input is validated. 
    """
    # input does not have required number of elements
    if len(input) != element_qty:
        return f"Your input must contain exactly {element_qty} characters."
    
    # input does not have unique values
    elif len(set(input)) != element_qty:
        return "All characters in your input must be unique."
    
    # input contains restricted value at specified position 
    elif input[limits.get("position")] == limits.get("value"):
        return f"""{limits.get("value")} is not allowed 
at position {limits.get("position")+1}.
"""
    
    # input is not subset of allowed elements
    elif not(set(input) <= set([str(element) for element in elements])):
        return f"""Your input includes invalid characters. 
Only these characters are allowed: {elements}.
"""
   
   # all validation passed
    else:
        return ""


def find_bulls(user_input: list, program_input: list, element_qty: int) -> int:
    """Iterates through the list user_input, comparing it with program_input.
    If any element of user_input is at the same position
    as in the list program_input, it counts it as a bull
    """
    bull_qty = 0
    for i in range(element_qty):
        if user_input[i] == program_input[i]:
            bull_qty += 1
    return bull_qty


def find_cows(user_input: list, program_input: list, element_qty: int) -> int:
    """Iterates through the user_input, comparing it with program_input.
    If any element of user_input is present in the list program_input,
    it counts it as a cow.
    """
    cow_qty = 0
    for i in range(element_qty):
        if user_input[i] in program_input:
            cow_qty += 1
    return cow_qty


if __name__ == "__main__":
    print(greeting)
    print(generate_separator(separator, separator_qty))
    print(description)
    print(generate_separator(separator, separator_qty))

    # generates list of elements and validates it
    while True:
        generated_list = generate_list(allowed_elements, ELEMENTS)        
        error = check_input(generated_list, allowed_elements, ELEMENTS, limitations)
        if len(error) == 0:
            break

    print(command)
    print(generate_separator(separator, separator_qty))

    attempt_qty = 0
    your_bull_qty = 0

    # the main game loop
    while your_bull_qty < ELEMENTS:
        #  the user input is stored in the variable guess in the list format
        guess = list(input())
        attempt_qty +=1

        # user input format is validated
        error = check_input(guess, allowed_elements, ELEMENTS, limitations)
        if len(error) == 0:
            
            # the function searching for bulls runs
            your_bull_qty = find_bulls(guess, generated_list, ELEMENTS)
            if your_bull_qty == ELEMENTS:
                break
            elif your_bull_qty == 1:
                format_bulls = "bull"      
            else:
                format_bulls = "bulls"

            # the function searching for cows runs
            your_cow_qty = find_cows(guess, generated_list, ELEMENTS) - your_bull_qty
            if your_cow_qty == 1:
                format_cows = "cow"
            else:
                format_cows = "cows"
            
            print(f"{your_bull_qty} {format_bulls}, {your_cow_qty} {format_cows}")
            print(generate_separator(separator, separator_qty))
            
        else:
            # error message if the user's input is not validated
            print(error)
            print(generate_separator(separator, separator_qty))

    # print success message
    print(ending_text)
    
    if attempt_qty == 1:
        format_attempts = "guess"
    else:
        format_attempts = "guesses"
    print(f"in {attempt_qty} {format_attempts}!")
    print(generate_separator(separator, separator_qty))
    print("That's amazing!")