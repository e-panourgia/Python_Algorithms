import sre_yield
import sys
import csv
import string

class GameInstance: # Grouping my data!
    g_completion = {}
    g_tomes = {}
    g_incompleted = []
    regex_words = {}
    g_completed_regexs = {} # It helps me for the final output!

    def __init__(self, g_completion, g_tomes, g_incompleted, regex_words, g_completed_regexs):  
        self.g_completion = {key:g_completion[key] for key in g_completion.keys()} 
        self.g_tomes = {key:g_tomes[key] for key in g_tomes.keys()}
        self.g_incompleted = [item for item in g_incompleted]
        self.regex_words = {key:regex_words[key] for key in regex_words.keys()}
        self.g_completed_regexs = {key:g_completed_regexs[key] for key in g_completed_regexs.keys()}

"""
Input : filename, a csv file contains the strature of crossword puzzle.
Output : g_completion, a dictionary contains as key word of crossword puzzle and as value the dots of word.
         g_tomes, a dictionary conatins as key word of crossword puzzle and as value a dictionary with key 
         intersection word of crossword puzzle and value the intersection point.          
"""
def getData1(filename):
    g_completion = {}
    g_tomes = {}

    with open(filename) as file:
        reader = csv.reader(file)
        for line in reader:
            id = line[0]
            g_completion[id] = line[1]
            tomes = line[2:]
            total_temnetai = int(len(tomes)/2)
            for tomi_index in range(total_temnetai):
                if not id in g_tomes:
                    g_tomes[id] = {} # Initialize
                g_tomes[id][tomes[tomi_index * (2)]] = tomes[tomi_index * 2 + 1] # dictionary of dictionary
    return g_completion, g_tomes


""""
Input : filename, a txt file contains the regex'es
Output : regex_words, a dictionary contains as key regex 
and as value a list that conatins the words generated from this regex
"""
def getData2(filename):
    regex_words = {}
    with open(filename) as file:
        reader = csv.reader(file)
        for line in reader:
            regex_word = line[0]
            regex_words[regex_word] = []
            generated_words = sre_yield.AllStrings(regex_word, max_count=5,charset=string.ascii_uppercase)
            for j in range(generated_words.length):
                regex_words[regex_word].append(generated_words.get_item(j))
            regex_words[regex_word] = list(dict.fromkeys(regex_words[regex_word])) # Remove duplicates
    return regex_words


"""
Input : g_completion, a dictionary contains as key word of crossword puzzle and as value the dots of word
        regex_words, a dictionary contains as key regex and as value a list of words witch gerenerated from the regex
        g_completed_regexs, a dictionary contains as key word of crossword puzzle and as value the completed regex(e.g. HA+)
Output : g_incompleted, a list contains incompleted words of crossword puzzle  
"""
def checkCompleted(g_completion, regex_words, g_completed_regexs):
    g_incompleted = []
    for id in g_completion:
        if "." in g_completion[id]:
            g_incompleted.append(id)
        else: # The word is completed, we have to remove it's regex
            completed_string = g_completion[id]
            for regex_word in regex_words: # Remove the corresponding regex word
                if completed_string in regex_words[regex_word]:
                    del regex_words[regex_word]
                    g_completed_regexs[id] = regex_word
                    break                        
    return g_incompleted, regex_words, g_completed_regexs

"""
Input : game_instance, an object that contains : 
        g_completion, a dictionary contains as key word of crossword puzzle and as value the dots of word. 
        g_tomes, a dictionary conatins as key word of crossword puzzle and as value a dictionary with key 
        intersection word of crossword puzzle and value the intersection point.  
        g_incompleted, a list contains incompleted words of crossword puzzle
        regex_words, a dictionary contains as key regex 
        and as value a list that conatins the words generated from this regex
        g_completed_regexs, a dictionary contains as key word of crossword puzzle(e.g. 3) and as value the completed regex (e.g. (HA+)) 
        ~
        word_id, a word of crossword puzzle
Output : word_id, g_completed_regexs , generated regex per line(e.g. 1 HA+ HAAA) 
"""
def DFS(game_instance, word_id = '-1'):
    if word_id == '-1': # If we are at initial state
        word_id = game_instance.g_incompleted[0]
    geitones = game_instance.g_tomes[word_id]
    word = game_instance.g_completion[word_id]
    
    found = False
    for regex in game_instance.regex_words:
        generated_words = game_instance.regex_words[regex]
        for generated_word in generated_words:            
            if len(generated_word) == len(word): # First stage check, length
                
                # Begin second stage check, tomes
                found = True
                for i, letter in enumerate(word):
                    if letter != '.' and letter != generated_word[i]:
                        found = False
                        break # We didn't found it
                # End of second stage check
                if found: # We know that we found the word
                    child_instance = GameInstance(game_instance.g_completion, game_instance.g_tomes, game_instance.g_incompleted, game_instance.regex_words, game_instance.g_completed_regexs)
                    child_instance.g_completion[word_id] = generated_word # Replace dots with the actual word
                    child_instance.g_completed_regexs[word_id] = regex

                    # Find the neighboors and replace the characters 
                    next_word_id = -1
                    geitones = [geitonas for geitonas in geitones if geitonas in child_instance.g_incompleted]
                    for neighboor_id in geitones:
                        next_word_id = neighboor_id
                        letter_index = child_instance.g_tomes[neighboor_id][word_id]
                        letter_to_add = generated_word[int(letter_index)]
                        neighboor_letter_index = child_instance.g_tomes[word_id][neighboor_id]
                        neighboor_string = child_instance.g_completion[neighboor_id]
                        letters = list(neighboor_string)
                        letters[int(neighboor_letter_index)] = letter_to_add
                        child_instance.g_completion[neighboor_id] = "".join(letters)
                    child_instance.g_incompleted = [w_id for w_id in child_instance.g_incompleted if w_id != word_id] # Delete word id
                    child_instance.regex_words = {key:child_instance.regex_words[key] for key in child_instance.regex_words if key != regex} # Delete the regex
                    if len(child_instance.g_incompleted) == 0: # Finished!
                        sorted_keys = child_instance.g_tomes.keys()
                        sorted_keys = sorted([int(key) for key in sorted_keys])
                        for i in sorted_keys:
                            print(str(i) + " " + child_instance.g_completed_regexs[str(i)] + " " + child_instance.g_completion[str(i)])
                        exit()
                    # The case doesn't exit geitonas!
                    if len(geitones) == 0:
                        neighboor_id = '-1'
                    result = DFS(child_instance, neighboor_id) # We have to check if it returned true or false
                        
                    # End of find neighboors
    if not found:
        # Not, return back
        return False    
    

data1_filename = sys.argv[1]
data2_filename = sys.argv[2]

# Filling data structures
g_completion, g_tomes = getData1(data1_filename)
regex_words = getData2(data2_filename)
g_incompleted, regex_words, g_completed_regexs = checkCompleted(g_completion, regex_words, {})
# Fillig initial object contains all data stractures I use 
initial_game_instance = GameInstance(g_completion, g_tomes, g_incompleted, regex_words, g_completed_regexs)
DFS(initial_game_instance, '-1') # Calling the main method solving the problem!