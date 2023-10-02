class RailFence: #splits in half and scrambles the letters by alternating which one is inserted into the ciphertext 
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, rails=3):
        self.rails = rails

    def valid_phrase(self, phrase):
        ''' Checks if a string contains only lowercase letters and spaces. '''
        phrase = phrase.replace(' ', '')
        return phrase.isalpha() and phrase.islower()

    def encrypt(self, plaintext):
        ''' Scrambles a phrase; assumes lowercase and no punctuation. '''
        msgLength = len(plaintext)
        
        evenChars = ""
        oddChars = ""
        for i in range(msgLength):
            if i % 2 == 0:
                evenChars = evenChars + plaintext[i]
            else:
                oddChars = oddChars + plaintext[i]
        ciphertext = oddChars + evenChars
        return ciphertext
    def decrypt(self, ciphertext):
        ''' Converts a phrase back; assumes lowercase and no punctuation. '''
        halfLength = len(ciphertext) // 2
        halfLength
        oddText = ciphertext[:halfLength]  # from the beginning, up to the halfway point
        evenText = ciphertext[halfLength:] # from the halfway point, all the way to the end
        #print(evenText)
        #print(oddText)
        plaintext = ''
        for i in range(halfLength):
            plaintext += evenText[i] + oddText[i]
        if len(evenText) > len(oddText):
            plaintext += evenText[-1]

        return plaintext
    
#if __name__ == '__main__':
    #rail_fence = RailFence(rails=3)
    #phrase = "Pumpkin Cold Foam Chai Tea Latte"
    #print("Original phrase:", phrase)
    #encrypted = rail_fence.encrypt(phrase)
    #print("Encrypted:", encrypted)
    #decrypted = rail_fence.decrypt(encrypted)
    #print("Decrypted:", decrypted)
    
class Substitution: # take a parameter for the key
    def __init__(self, key):
        self.key = key

    def removePasswordDupes(password):
        newPassword = ''
        for ch in password:
            if ch not in newPassword:
                newPassword = newPassword + ch
        return newPassword

    def removeAlphabetDupes(alphabet, password):    
        '''
        Removes the duplicates in the alphabet
        '''
        newAlphabet = ''
        for ch in alphabet:
            if ch not in password:
                newAlphabet = newAlphabet + ch
        return newAlphabet
    
    def generateKeyFromPassword(key):
        """Creates a 5 x 5 grid from the given key"""
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' #alphabet without J
        key = key.upper() 
        key = Substitution.removePasswordDupes(key) #removes password duplicates function
        splitChr = key[-1] #finds the last letter in key
        splitIdx = alphabet.find(splitChr) #finds the last letter of the key in the alphabet
        afterStr = Substitution.removeAlphabetDupes(alphabet[splitIdx+1:], key) #removes alphabet duplicates of letters before the key
        beforeStr = Substitution.removeAlphabetDupes(alphabet[:splitIdx], key) #removes alphabet duplicates of letters after the key
        toReturn = key + beforeStr + afterStr #combines the key, the letters before, and the letters after in that order
        toReturn = toReturn.replace(' ', '') #removes spaces from key
        #separates letters into groups of five
        print(toReturn[0:5])
        print(toReturn[5:10])
        print(toReturn[10:15])
        print(toReturn[15:20])
        print(toReturn[20:25])
        

    def encrypt(self, key):
        ciphertext = ''
        for ch in key.lower():
            if ch == ' ':                           # Our version of CSC leaves spaces as spaces
                ciphertext = ciphertext + ' '
            else:
                num = ord(ch) - ord('a')            # Converts this letter a-z to a number 0-25
                num = num + key                     # Shift the number by the key value
                num = num % 26                      # Wrap back around to the alphabet numbers 0-25
                num = num + ord('a')                # Convert back to an ASCII letter
                ciphertext = ciphertext + chr(num)  # Add to the ciphertext
    def decrypt(self,ciphertext):
        alphabet = "abcdefghijklmnopqrstuvwxyz "
        decryptedtext = ""
        for ch in ciphertext:
            idx = self.key.find(ch.lower())
            decryptedtext = decryptedtext + alphabet[idx]
        return decryptedtext
    
#if __name__ == '__main__':
    #subbing = Substitution(key=3)
    #phrase = "Pumpkin Cold Foam Chai Tea Latte"
    #encrypted = subbing.encrypt(phrase)
    #print("Encrypted:", encrypted)
    #decrypted = subbing.decrypt(encrypted)
    #print("Decrypted:", decrypted)

class Playfair:

    def removePasswordDupes(password):
        '''Removes the duplicates in the password'''
        newPassword = ''
        for ch in password:
            if ch not in newPassword:
                newPassword = newPassword + ch
        return newPassword

    def removeAlphabetDupes(alphabet, password):    
        '''Removes the duplicates in the alphabet'''
        newAlphabet = ''
        for ch in alphabet:
            if ch not in password:
                newAlphabet = newAlphabet + ch
        return newAlphabet
    
    def generateKeyFromPassword(key):
        """Creates a 5 x 5 grid from the given key"""
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' #alphabet without J
        key = key.upper() 
        key = Playfair.removePasswordDupes(key) 
        splitChr = key[-1] #finds the last letter in key
        splitIdx = alphabet.find(splitChr)
        afterStr = Playfair.removeAlphabetDupes(alphabet[splitIdx+1:], key) 
        beforeStr = Playfair.removeAlphabetDupes(alphabet[:splitIdx], key) 
        toReturn = key + beforeStr + afterStr 
        toReturn = toReturn.replace(' ', '') 
        #separates letters into groups of five
        return(toReturn[0:5]
            ,toReturn[5:10]
            ,toReturn[10:15]
            ,toReturn[15:20]
            ,toReturn[20:25])


    def FindDuplicates(keyword):
        '''Locates the duplicates and puts a Q in between them'''
        keyword = keyword.upper()
        keyword = keyword.replace(" ", "") 
        keyword = keyword.replace('J', 'I')
        dupesRemoved = ""
        
        while i < len(keyword):   
            ch0 = keyword[i]
            ch1 = keyword[i + 1]
        
        if ch0 == ch1:
            ch1 = 'Q'
            i = i + 1
            
        else:
            i = i + 2
            
        duplicatesRemoved += ch0 + ch1   
        
        keyword = dupesRemoved
        
        if len(keyword) % 2 == 0: 
            print("")
            
        else:      
            keyword = keyword + 'Q'
            print("")
                
        return([keyword[i:i+2] for i in range(0, len(keyword), 2)])

    def splitTwos(keyword):
        """Splits the string into pairs without adding any 'X' at any point."""
        for i in range(0, len(keyword), 2):
            return(keyword[i:i+1])
        
    def gridLocation(self, letter, grid):
        letter = letter.upper()
        # Use self.grid to access the grid
        indices = ((row_idx, col_idx)
                   for row_idx, row in enumerate(grid)
                   for col_idx, letter in enumerate(row)
                   if letter == letter)
        location = next(indices, None)
        return location
        
    def getPairs(keyword, grid):
        letter1 = Playfair.gridLocation(keyword[0]) #first letter in pair
        letter2 = Playfair.gridLocation(keyword[1])  #second letter
        return grid[letter1][letter2]
    
    def letterRight(x, grid):
        """Shifts ones column to the right in the grid. It will wrap to the other side
        if reaches the end of the grid."""
        original = Playfair.gridLocation(x, grid)
        row = original[0]
        col = original[1]
        
        if col + 1 > 4:
            col = -1
            
        info = [row, col + 1]
    
    #return getLetter(info, grid)
 
    def letterLeft(x, grid):
        """Shifts one columns to the left in the grid. It will wrap to the other side
        if reaches the end of the grid."""
        original = Playfair.gridLocation(x, grid)
        row = original[0]
        col = original[1]
        
        if col - 1 < 0:
            col = 5
            
        info = [row, col - 1]
        
        return Playfair.getPairs(info,grid)
                    
    def letterDown(x, grid):
        """Shifts one row down in the grid. It will wrap to the other side
        if reaches the end of the grid."""   
        original = Playfair.gridLocation(x, grid)
        row = original[0]
        col = original[1]
        
        if row + 1 > 4:
            row = -1
        info = [row + 1, col]
        
        return Playfair.getPairs(info, grid)

    def letterUp(x, grid):
        """Shifts one row up in the grid. It will wrap to the other side
        if reaches the end of the grid.""" 
        original = Playfair.gridLocation(x, grid)
        row = original[0]
        col = original[1]
        
        if row - 1 < 0:
            row = 5
        info = [row -1, col]
        
        return Playfair.getPairs(info, grid)
    def encryption(password, keyword): 
        """Takes in a password and word, encrypting the password using the Playfair Cipher using the 
       keyword to encrypt into a grid"""
        grid = Playfair.generateKeyFromPassword(password) 
        plaintext = Playfair.splitTwos(keyword)        
        ciphertext = ''  
    
        for letters in plaintext:
            first = letters[0]
            second = letters[1]
            
            info1 = Playfair.gridLocation(first, grid)
            info2 = Playfair.gridLocation(second, grid)
            
            row1 = info1[0]
            row2 = info2[0]
            
            col1 = info1[1]
            col2 = info2[1]
            newFirst = ''
            newSecond = ''
            if row1 == row2: 
                newFirst = Playfair.letterRight(first, grid)
                newSecond = Playfair.letterRight(second, grid)
            elif col1 == col2:
                newFirst = Playfair.letterDown(first, grid)
                newSecond = Playfair.letterDown(second, grid)
            else:
                news = Playfair.rectangle(first, second, grid)
                newFirst = news[0]
                newSecond = news[1]
            ciphertext += newFirst + newSecond

    def decryption(password, ciphertext):
        """Takes in an encrypted code from the Playfair Cipher and the keyword, and then returns the 
        decrypted password."""
        grid = Playfair.generateKeyFromPassword(password)
        ciphertext = Playfair.splitTwos(ciphertext)
        plaintext = ''
        
        for letters in ciphertext:
            first = letters[0]
            second = letters[1]
            
            info1 = Playfair.gridLocation(first, grid)
            info2 = Playfair.gridLocation(second, grid)
            
            row1 = info1[0]
            row2 = info2[0]
            
            col1 = info1[1]
            col2 = info2[1]
            newFirst = ''
            newSecond = ''
            if row1 == row2:
                newFirst = Playfair.letterLeft(first, grid)
                newSecond = Playfair.letterLeft(second, grid)
            elif col1 == col2:
                newFirst = Playfair.letterUp(first, grid)
                newSecond = Playfair.letterUp(second, grid)
            else:
                news = Playfair.rectangle(first, second, grid)
                newFirst = news[0]
                newSecond = news[1]
            plaintext += newFirst + newSecond 

        return plaintext.replace('X', '')
    def rectangle(first, second, grid):
        """Takes two locations on the grid and then switches the columns of each location with each other.
        The locations stay in the same row."""
        o1 = Playfair.gridLocation(first, grid)
        o2 = Playfair.gridLocation(second, grid)
        
        row1 = o1[0]
        row2 = o2[0]
        
        col1 = o1[1]
        col2 = o2[1]
        
        new1 = [row1, col2]
        new2 = [row2, col1]
        
        return [Playfair.getPairs(new1, grid), Playfair.getPairs(new2, grid)]

if __name__ == '__main__':
    play = Playfair(key=3)
    phrase = "Pumpkin Cold Foam Chai Tea Latte"
    encrypted = play.encrypt(phrase)
    print("Encrypted:", encrypted)
    decrypted = play.decrypt(encrypted)
    print("Decrypted:", decrypted)
