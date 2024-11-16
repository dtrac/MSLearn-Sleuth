#import pytest

print( "Hello, Contosoville!" )
# This is a comment that won't be interpreted as a command.

# Associate variable town with the value "Contosoville"
town = "Contosoville"

# Print a message about the secret location
print( "The town I am looking for is " + town )

# Define a power (function) to chant a phrase
def chant( phrase ):
    # Glue three copies together and print it as a message
    print( phrase + phrase + phrase )

# Invoke the power to chant on the phrase "Contosoville!"
chant( "Contosoville!" )

""" Ensure that the value passed in the letter parameter is lowercase by calling .lower(). In this case, the letter passed in is a, so .lower() will keep it as a.
Use the ord() function to convert the letter a to its ASCII code, 97. Save the code value 97 in the letter_code variable.
Add a shift_amount value of 2 to the letter_code value of 97 to get the new number value: 99. Store the value 99 in the decoded_letter_code variable.
Use the chr() function to decode the number value 99 into a character to get c. (The chr() function simply does the opposite of the ord() function.) Store the decoded value c in the decoded_letter variable.
Return the decoded_letter value: c. """

# Define a function to find the truth by shifting the letter by the specified amount
def lasso_letter( letter, shift_amount ):
    # Invoke the ord function to translate the letter to its ASCII code 
    # Save the code to the letter_code variable
    letter_code = ord(letter.lower())
    
    # The ASCII number representation of lowercase letter 'a'
    a_ascii = ord('a')

    # The number of letters in the alphabet
    alphabet_size = 26

    # The formula to calculate the ASCII number for the decoded letter
    # Take into account looping around the alphabet
    true_letter_code = a_ascii + (((letter_code - a_ascii) + shift_amount) % alphabet_size)

    # Convert the ASCII number to the character or letter
    decoded_letter = chr(true_letter_code)

    # Send the decoded letter back
    return decoded_letter

#print(lasso_letter('a',3))

# Test case 1: Shift letter 'a' by 3, expected output: 'd'
def test_lasso_letter_shift_3():
    assert lasso_letter('a', 3) == 'd'

print(lasso_letter('p', -2))

# Define a function to find the truth in a secret message
# Shift the letters in a word by a specified amount to discover the hidden word
def lasso_word( word, shift_amount ):

    # This variable is updated each time another letter is decoded
    decoded_word = ""

    # This for loop iterates through each letter in the word parameter
    for letter in word:
        # The lasso_letter() function is invoked with each letter and the shift amount
        # The result (the decoded letter) is stored in a variable called decoded_letter
        decoded_letter = lasso_letter(letter, shift_amount)

        # The decoded_letter value is added to the end of the decoded_word value
        decoded_word = decoded_word + decoded_letter

    # The decoded_word is sent back to the line of code that invoked this function
    return decoded_word

# Try to decode the word "terra"
print( "Shifting terra by 13 gives: \n" + lasso_word( "terra", 13 ) )


print( "Shifting Ncevy by 13 gives: \n" + lasso_word( "Ncevy", 13 ) )
print( "Shifting gpvsui by 25 gives: \n" + lasso_word( "gpvsui", 25 ) )
print( "Shifting ugflgkg by -18 gives: \n" + lasso_word( "ugflgkg", -18 ) )
print( "Shifting wjmmf by -1 gives: \n" + lasso_word( "wjmmf", -1 ) )