def first_word(sentence):
    firstword = sentence[0:sentence.find(" ")]
    return firstword

def second_word(sentence):
    secondword1 = sentence[sentence.find(" ") + 1:]
    secondword2 = secondword1[0:secondword1.find(" ")]
    x = secondword1.find(" ")
    if x == -1:
        return secondword1
    else:
        return secondword2

    
def last_word(sentence):
    word = ""
    index = 0
    while index < len(sentence):
        if sentence[index - 1] == " ":
            word = ""
        word = sentence[index:len(sentence)]
        y = word.find(" ")
        if y == -1:
            return word
        index += 1

### I DID IT!!! WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO





    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))

###Solution
#def find_word(str, whatth): whatth is how we designate what word we want. counter goes up each blank, when counter = whatth, break.
    #index = 0
    #word = ""
    #counter = 0
    #while index < len(str):
    	#if str[index] == " ":  checks if we hit a blank.
    	    #counter += 1  adds 1 to counter, this is counting words since once we hit a blank, it adds 1.
    	    #if counter == whatth: if counter (words) = whatth, break. whatth is used to designate the word we want.
    	        #break
    	    #word = "" sets word to blank when this loop runs. This loop runs when str index = " ". We only get here if index is blank and counter != whatth.
    	#else:
    	    #word += str[index]
    	#index += 1 moves us through, letter by letter
    #return word
 
#def first_word(mjono):
    #return find_word(mjono, 1) Mjono = sentence, 1 = whatth
 
#def second_word(mjono):
    #return find_word(mjono, 2)
 
#def last_word(mjono):
    #return find_word(mjono, 0)

#sentence = "once upon a time there was a programmer"
#print(first_word(sentence)) sentence passes in to function first_word(MJONO)
#print(second_word(sentence))
#print(last_word(sentence))
