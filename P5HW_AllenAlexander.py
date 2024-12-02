#Alexander Allen
#P5HW
#18Nov24
#Use functions to create a game with characters

#Import libraries
import random

def create_character():
    """
    Creates a game character by collecting attributes from the user.

    Returns:
        dict: A dictionary containing the character's attributes.
    """
    print("Create Your Game Character")
    name = input("Enter the character's name: ").strip()
    
    # Get numerical inputs and validate them
    health = int(input(f"Enter {name}'s health: "))
    strength = int(input(f"Enter {name}'s strength: "))
    speed = int(input(f"Enter {name}'s speed: "))
    sanity = int(input(f"Enter {name}'s sanity: "))
    investigation = int(input(f"Enter {name}'s investigation: "))
    
    # Create the character dictionary
    character = {
        "name": name,
        "health": health,
        "strength": strength,
        "speed": speed,
        "sanity": sanity,
        "investigation": investigation
    }
    
    return character

def display_character(character):
    
    for key, value in character.items():
        print(f"{key}: {value}")


#Battle between 2 characters        
def battle(attacker, defender):
    """
    Simulates a battle between an attacker and a defender.

    Parameters:
        attacker (dict): A dictionary representing the attacker with a 'strength' attribute.
        defender (dict): A dictionary representing the defender with a 'health' attribute.

    Returns:
        dict: The updated dictionary for the defender.
    """
    print(f"{attacker['name']} is attacking {defender['name']}!!!")
    # Ensure both dictionaries contain the necessary attributes
    if "strength" not in attacker or "health" not in defender:
        raise ValueError("Attacker must have 'strength', and defender must have 'health' attributes.")

    # Calculate damage (random value between 0 and attacker's strength)
    damage = random.randint(0, attacker["strength"])
    print(f"{attacker['name']} attacks {defender['name']} and deals {damage} damage!")

    # Reduce the defender's health
    defender["health"] = max(defender["health"] - damage, 0)  # Ensure health doesn't go below 0
    print(f"{defender['name']}'s health is now {defender['health']}.")

    return defender

# Example Usage
#if __name__ == "__main__":
 #   attacker = {
  #      "name": "Warrior",
   #     "strength": 15,
    #    "health": 100
    #}

    #defender = {
     #   "name": "Mage",
      #  "health": 50,
       # "strength": 8
    #}

    #updated_defender = battle(attacker, defender)
    #print("\nUpdated Defender:")
    #print(updated_defender)


#Define the main
def main():
    print("You Died")
    print("\n\n\n")
    #create two characters(more if neccacary)
    print("Create first character: ")
    char1 = create_character()
    print("\nCreate second character: ")
    char2 = create_character()
    print()

    #Display the created characters
    display_character(char1)
    print()
    display_character(char2)
    print()

    #Simulate a battle
    char2 = battle(char1, char2)

    display_character(char2)
    

#Call the main
if __name__ == "__main__":
    main()
    #character = create_character()
    #print("\nYour created character:")
    #print(character)
