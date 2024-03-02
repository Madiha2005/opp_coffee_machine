def get_user_input():
    switch_a = input("Is switch A enabled? (y/n): ").lower() == 'y'
    if switch_a != "y":
        print("Please enter y/n:")
    switch_b = input("Is switch B enabled? (y/n): ").lower() == 'y'
    if switch_b != "y":
        print("Please enter y/n:")
    slider_value = int(input("What is the value of the numeric slider? (0-100): "))

    return switch_a, switch_b, slider_value

def generate_beverage(switch_a, switch_b, slider_value):

    if switch_a and switch_b:
        if slider_value <= 17:
            return "Juice, Apple, Frozen"
        elif 18 <= slider_value <= 39:
            return "GreenTea, lemon, Cold"
        elif 40 <= slider_value <= 99:
            return "Juice, Apple, Hot"
        elif slider_value == 100:
            return "GreenTea, lemon, Boiling"
    elif switch_a:
        if 1 <= slider_value <= 17:
            return "Juice, Apple, Cold"
        elif 18 <= slider_value <= 39:
            return "Juice, Apple, Warm"
        elif 40 <= slider_value <= 99:
            return "Juice, Apple, Hot"
        elif slider_value == 100:
            return "Juice, Apple, Boiling"
    elif switch_b:
        if 1 <= slider_value <= 17:
            return "Coke, Regular, Frozen"
        elif 18 <= slider_value <= 39:
            return "Coke, Regular, Warm"
        elif 40 <= slider_value <= 99:
            return "Coke, Regular, Hot"
        elif slider_value == 100:
            return "Coke, Regular, Boiling"
    else:
        return "Unknown Beverage"

def run_replicator():
    switch_a, switch_b, slider_value = get_user_input()
    result = generate_beverage(switch_a, switch_b, slider_value)
    print(f"Result: {result}")

if __name__ == "__main__":
    run_replicator()

