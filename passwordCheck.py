# %%
import re 

# %%
def checkPassword(password: str) -> str or bool:
    # regex to check for
    # * capital Letters
    # * Number
    # * letter
    # * special character
    # * password of length 8 or more 

    wordRegex = r'\D+'
    numberRegex = r'\d+'
    specialRegex = r'\W+'
    capitalRegex = r'[A-Z]+'
    fullMatchRegex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*'#'?&])[A-Za-z\d@$!#%*?&]{8,}$"

    # Matches each regex to see if it fits
    wordMatch = re.findall(wordRegex, password)
    numberMatch = re.findall(numberRegex, password)
    specialMatch = re.findall(specialRegex, password)
    capitalMatch = re.findall(capitalRegex, password)
    fullMatch = re.findall(fullMatchRegex, password)

    # check for any output produce by the regex 
    # if so it returns true otherwise it returns false
    wordMatch = False if wordMatch == [] else True
    numberMatch = False if numberMatch == [] else True
    specialMatch = False if specialMatch == [] else True
    capitalMatch = False if capitalMatch == [] else True
    fullMatch = False if fullMatch == [] else True

    regexList = [wordMatch, numberMatch, specialMatch, capitalMatch]
    if fullMatch == True:
        return "Very Strong"
    
    # Counts how many passes the password 
    # has been to match 
    matchCounter = 0
    for i in regexList:
        if i == True:
            matchCounter += 1

    # Assigns the password levels 
    # depending on how many passes it has achieved
    if matchCounter >= 3 and len(password) >= 8:
        return "Strong"
    elif matchCounter > 2 or len(password) >= 8:  
        return "Medium"
    elif matchCounter <= 2:
        return "Weak"

    
# %%
