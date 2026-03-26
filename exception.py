# Step 1: Define a custom exception
class TextTooShortError(Exception):
    pass

# Step 2: Function to check text length
def check_text_length(text):
    if len(text) < 10:
        raise TextTooShortError("Text must be at least 10 characters long.")
    else:
        print("Text is accepted:", text)

# Step 3: Get user input and check
try:
    user_input = input("Enter some text (at least 10 characters): ")
    check_text_length(user_input)

except TextTooShortError as e :
    print("Error:",e)
