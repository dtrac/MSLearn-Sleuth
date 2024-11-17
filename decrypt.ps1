# Define a function to shift a letter by the specified amount
function Lasso-Letter {
    param (
        [string]$letter,
        [int]$shiftAmount
    )

    # Convert the letter to lowercase and get its ASCII code
    $letterCode = [int][char]($letter.ToLower())

    # The ASCII code for lowercase 'a'
    $aAscii = [int][char]'a'

    # The number of letters in the alphabet
    $alphabetSize = 26

    # Calculate the ASCII code for the shifted letter
    $trueLetterCode = $aAscii + ((($letterCode - $aAscii) + $shiftAmount) % $alphabetSize)

    # Convert the ASCII code back to a character
    $decodedLetter = [char]$trueLetterCode

    # Return the decoded letter
    return $decodedLetter
}

# Test the function with letter 'a' shifted by 3 (expected output: 'd')
Write-Output (Lasso-Letter -letter 'a' -shiftAmount 3)

# Define a function to shift all letters in a word
function Lasso-Word {
    param (
        [string]$word,
        [int]$shiftAmount
    )

    # Initialize an empty string for the decoded word
    $decodedWord = ""

    # Loop through each letter in the word
    foreach ($letter in $word.ToCharArray()) {
        # Shift the letter and add it to the decoded word
        $decodedLetter = Lasso-Letter -letter $letter -shiftAmount $shiftAmount
        $decodedWord += $decodedLetter
    }

    # Return the decoded word
    return $decodedWord
}

# Test the Lasso-Word function with various examples
Write-Output "Shifting 'terra' by 13 gives: $(Lasso-Word -word 'terra' -shiftAmount 13)"
Write-Output "Shifting 'Ncevy' by 13 gives: $(Lasso-Word -word 'Ncevy' -shiftAmount 13)"
Write-Output "Shifting 'gpvsui' by 25 gives: $(Lasso-Word -word 'gpvsui' -shiftAmount 25)"
Write-Output "Shifting 'ugflgkg' by -18 gives: $(Lasso-Word -word 'ugflgkg' -shiftAmount -18)"
Write-Output "Shifting 'wjmmf' by -1 gives: $(Lasso-Word -word 'wjmmf' -shiftAmount -1)"
