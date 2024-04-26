import random
import string

def generate_promo_code():
    # Define the characters allowed in the promo code
    characters = string.ascii_uppercase + string.digits
    
    # Define the length of the promo code
    code_length = 8
    
    # Generate a random promo code
    promo_code = ''.join(random.choices(characters, k=code_length))
    
    # Add a country code prefix (e.g., FR for France), Suppose generating promo codes for https://ma-codereduc.fr/
    promo_code = "FR-" + promo_code
    
    return promo_code

# Generate and print a sample promo code
print("Sample Promo Code for https://ma-codereduc.fr/:", generate_promo_code())
