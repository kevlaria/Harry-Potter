# Kevin Lee, Shijia Lu

import sys

def main():
    """
    None -> Various
    Creates requirements for parts 1, 2 & 3.
    Parts 4 & 5 need to be run at the function level.
    """
    
    sourceFile = 'HP1.txt'
    dictionary = createUnigramDictionary(sourceFile)
    writeDictToFile(dictionary, 'unigramFrequencies.txt')
    
    cleanFile = ignoreNames(sourceFile, 'HPChar.txt')
    
    newDictionary = createUnigramDictionary('HPMinusNames.txt')
    writeDictToFile(newDictionary, 'unigramFrequenciesMinusNames.txt')

    bigramDictionary = getBigramFreqFromFile(sourceFile)
    writeDictToFile(bigramDictionary, 'bigramFrequencies.txt')

    
## Structure of file:
# Part 1
# Part 2
# Part 3
# Part 4
# Part 5
# Bottom level file-opening functions and error handling

####

# Part 1

def createUnigramDictionary(fileName):
    """
    File -> Dict{string: int}
    Reads in a file, and creates a dictionary of word : frequency in file
    """

    words = importWords(fileName)
    while '#' in words:
        words.remove('#')
    wordDict = createDictionary(words)
    return wordDict

def importWords(filename):
    """
    File -> list[string,...]
    Takes a file and converts text in the file into a list of words
    """
    wordsRaw = readFileLine(filename)
    words = createWordList(wordsRaw)
    words.sort()
    return words

def readFileLine(filename):
    """
    File -> List[String, ...]
    Reads in a file and creates a list of all the lines in the file. All '\n's are stripped.
    """
    lines = getLinesFromFile(filename)
    wordsRaw = []
    for line in lines:
        wordsRaw.extend(line.split())
    return wordsRaw

def createDictionary(words):
    """
    List[String,...] -> Dict{string: int}
    Takes in a list of words and returns a dictionary of the word : frequency
    """
    wordDict = {}
    for word in words:
        wordDict[word] = wordDict.get(word, 0) + 1
    return wordDict

def createWordList(wordsRaw):
    """
    list[string,...] -> list[string,...]
    Takes in a list of words, removes disallowed characters, and returns a list of words without the disallowed characters
    """
    disallowedCharacters = ['-', 'mrs', 'mr', ';', ',', '.', '"', ':', '?', '/', '(', ')', '[', ']', '\\', '!', '@', '$', '%', '^', '&', '*', "'s", "s'"]
    words = []
    for wordRaw in wordsRaw:
        wordRaw = wordRaw.lower()
        word = removeAllPunctuation(wordRaw, disallowedCharacters)
        if not word == '':
            words.append(word)
    return words
    

def removeAllPunctuation(string, disallowedCharacters):
    """
    string, list[string,...] -> string
    Takes in a string and a list of disallowed characters, and removes the disallowed characters from the list
    """
    for disallowedCharacter in disallowedCharacters:
        string = string.replace(disallowedCharacter, '')
    return string

def writeDictToFile(dictionary, filename):
    """
    Dictionary{string : int} -> File
    Reads in a dictionary, creates a file with one line of the dictionary in each row in the format '<string> : <count>'
    """
    if not openFileWrite(filename):
        printErrorStatement(filename)
    else:
        output = open(filename, 'w')
        for i in range(len(dictionary)):
            dictEntry = dictionary.items()[i]
            outputEntry = reformatDictionary(dictEntry)
            output.write(outputEntry + '\n')
        output.close()

def reformatDictionary(tupleFormat):
    """
    tuple(string, int) -> string
    Reads in a single entry of a dictionary (in the tuple format), and returns a string in the format '<word> : <frequency>'
    """
    key = tupleFormat[0]
    value = str(tupleFormat[1])
    returnString = key +  ' : ' +  value
    return returnString


# Part 2


def ignoreNames(mainfilename, characterfilename):
    """
    File, file -> file
    Takes in a main file and a character file, and replaces character names with a #. Returns a file
    """
    # importing mainfilename
    words = readFileLine(mainfilename)

    # importing characterfilename
    names = readFileLine(characterfilename)

    cleanWords = replaceNameWithHash(names, words)
    
    outputFile = 'HPMinusNames.txt'
    if not openFileWrite(outputFile):
        printErrorStatement(outputFile)
    else:
        output = open(outputFile, 'w')
        for cleanWord in cleanWords:
            output.write(cleanWord + ' ')
        output.close()

def replaceNameWithHash(names, words):
    """
    List[String, ...], List[String,...] -> List[String,...]
    Takes a list of names, a list of words, and converts name into # in the list of words. Returns the cleaned up list of words.
    """
    for name in names:
        for i in range(len(words)):
            word = words[i]
            namePresence = word.find(name)
            if namePresence > -1:
                words[i] = '#'
    return words


# Part 3

def getBigramFreqFromFile(filename):
    """
    File -> Dictionary
    Takes in a file and returns a dictionary containing all the bigrams and their frequencies
    """
    documentBigramDictionary = {}
    sentences = getSentences(filename)
    for sentence in sentences:
        sentenceWithoutNames = ignoreNamesInSentence(sentence, 'HPChar.txt')
        documentBigramDictionary = amalgamateBigramDictionary(sentenceWithoutNames, documentBigramDictionary)
    return documentBigramDictionary

def getSentences(fileName):
    """
    File -> List[string,...]
    Takes in a file and returns a list of sentences. Sentences are split either on '.' or '?'
    """
    if not openFile(fileName):
        printErrorStatement(fileName)
    else:
        text = open(fileName, 'r')
        lines = text.read()
        text.close()
        lines = removeDotAfterMr(lines)
        sentencesSplitAtDot = lines.split('.')
        sentences = []
        for sentenceSplitAtDot in sentencesSplitAtDot:
            if '?' in sentenceSplitAtDot:
                sentencesSplitAtQuestion = sentenceSplitAtDot.split('?')
                for sentenceSplitAtQuestion in sentencesSplitAtQuestion:
                    sentences.append(sentenceSplitAtQuestion)
            else:
                sentences.append(sentenceSplitAtDot)
            cleanSentences = sentenceCleansing(sentences)

    return cleanSentences

def removeDotAfterMr(text):
    """
    String -> String
    Removes all '.' that follow 'Mr.' and 'Mrs.'
    """
    text = text.replace('Mrs.', 'Mrs')
    text = text.replace('Mr.', 'Mr')
    return text

def sentenceCleansing(sentences):
    """
    List[String,...] -> List[String,...]
    Removes all elements with empty strings, all instances of '\n', and excess spaces
    """
    cleanSentences = removeEmptyStrings(sentences)
    cleanSentences = removeSpacesAndReturns(cleanSentences)
    return cleanSentences

def removeEmptyStrings(sentences):
    """
    List[String,...] -> List[String,...]
    Removes all elements with empty strings
    """
    while '' in sentences:
        sentences.remove('')
    return sentences

def removeSpacesAndReturns(sentences):
    """
    List[String,...] -> List[String,...]
    Removes all '\n' and strips sentences of excess whitespaces
    """
    cleanSentences = []
    for sentence in sentences:
        cleanerSentence = sentence.strip()
        cleanestSentence = cleanerSentence.replace('\n',' ')
        cleanSentences.append(cleanestSentence)
    return cleanSentences

def ignoreNamesInSentence(string, characterfilename):
    """
    string, file -> string
    Function goes through a sentence and strips out all the names present in characterfilename
    """

    names = readFileLine(characterfilename)
    
    # Strip out names and return #
    words = string.split()
    cleanedWords = replaceNameWithHash(names, words)

    # Re-combine sentence
    cleanSentence = recombineSentence(cleanedWords)
    
    return cleanSentence

def recombineSentence(words):
    """
    List[string,...] -> string
    Takes in a list of words and recombines them into a sentence (in the form of a string)
    """
    cleanSentence = ''
    for i in range(len(words)):
        cleanSentence = cleanSentence + ' ' + words[i]
    
    cleanSentence = cleanSentence.strip()
    return cleanSentence

def amalgamateBigramDictionary(sentence, documentBigramDictionary):
    """
    String, Dict{string:int}
    For a given sentence, find out the bigram frequencies within the sentence, and update the document bigram dictionary
    """

    sentenceBigramDictionary = getBigramFreqFromSentence(sentence)
    for bigram in sentenceBigramDictionary:
            bigramInSentenceCount = sentenceBigramDictionary[bigram]
            documentBigramDictionary[bigram] = documentBigramDictionary.get(bigram, 0) + bigramInSentenceCount
    return documentBigramDictionary


def getBigramFreqFromSentence(sentence):
    """
    String -> Dict{string: int}
    Takes in a sentence, and returns a dictionary with bigrams and their frequencies
    """
    words = sentence.split()
    cleanWords = createWordList(words)
    bigrams = createBigrams(cleanWords)
    bigramDictionary = createDictionary(bigrams)
    return bigramDictionary

def createBigrams(words):
    """
    List[string,...], List(String)
    Takes in a list of words, and create a list of bigram strings (each string in the format '<word1> <word2>'). Excludes any bigrams that contain the element '#'
    """
    bigramList = []
    for i in range(len(words)):
        if i + 1 < len(words):
            bigramString = ''
            bigramString = words[i] + ' ' +  words[(i+1)]
            if not '#' in bigramString:
                bigramList.append(bigramString)
    return bigramList


# Part 4

def createContingency(bigram, bigramFilename, unigramFilename):
    """
    String, File, File -> List[List[Int]]
    This takes in a bigram (just a string) and a bigramFilename and a unigramfilename and computes
the contingency matrix. This function returns a list of lists. The first list is the first row of the matrix. The second list is the second row of the matrix.
    """
    contingencyValidation(bigram, bigramFilename, unigramFilename)
    bigramTuple = splitBigram(bigram)
    wordOne = bigramTuple[0]
    wordTwo = bigramTuple[1]
    bigramLines = getLinesFromFile(bigramFilename)
    unigramLines = getLinesFromFile(unigramFilename)
    
    wordOneAndTwoValue = wordOneAndTwo(wordOne, wordTwo, bigramLines)
    wordOneAndNotTwoValue = oneWordFrequency(wordOne, unigramLines) - wordOneAndTwoValue
    wordTwoAndNotOneValue = oneWordFrequency(wordTwo, unigramLines) - wordOneAndTwoValue
    notOneAndNotTwoValue = totalFrequency(bigramLines) - wordOneAndTwoValue - wordOneAndNotTwoValue - wordTwoAndNotOneValue
    lineOneMatrix = [wordOneAndTwoValue, wordOneAndNotTwoValue]
    lineTwoMatrix = [wordTwoAndNotOneValue, notOneAndNotTwoValue]
    
    contingencyMatrix = [lineOneMatrix, lineTwoMatrix]
    return contingencyMatrix

def contingencyValidation(bigram, bigramFilename, unigramFilename):
    """
    String, File, File -> None
    Input validation for the createContingency functions. Program exits if a) bigram isn't in the right format OR b) bigramFilename doesn't exist OR c) unigramFilename doesn't exist). Otherwise nothing happens.
    """

    if not bigramFormat(bigram):
        print 'The bigram is not in the format "<word1> <word2>". Please try again.'
        sys.exit(0)
    if not openFile(bigramFilename):
        printErrorStatement(bigramFilename)
    if not openFile(unigramFilename):
        printErrorStatement(unigramFilename)

def splitBigram(bigram):
    """
    string, tuple(string, string)
    Given a bigram, splits it into a tuple of two separate words
    """
    bigram = bigram.lower()
    bigramSplit =  bigram.split()
    wordOne = bigramSplit[0]
    wordTwo = bigramSplit[1]
    return (wordOne, wordTwo)


def wordOneAndTwo(wordOne, wordTwo, bigramLines):
    """
    string, string, list[string,...]
    Takes two words, and looks up the frequency for the two words (both for wordOne, wordTwo and for wordTwo, wordOne).
    """
    wordOneWordTwoBigram = wordOne + ' ' + wordTwo
    wordTwoWordOneBigram = wordTwo + ' ' + wordOne
    bigramCombinations = (wordOneWordTwoBigram, wordTwoWordOneBigram)
    bigramCount = 0
    for line in bigramLines:
        bigramAndCount = line.split(' : ')
        bigramFromBigramLines = bigramAndCount[0].strip()
        countFromBigramLines = int(bigramAndCount[1].strip())
        for bigram in bigramCombinations:
            if bigram == bigramFromBigramLines:
                bigramCount = bigramCount + countFromBigramLines
    return bigramCount

def oneWordFrequency(word, unigramLines):
    """
    string, list[string,...] -> Int
    For a given word, returns the word frequency based on unigramLines
    """
    frequency = 0
    for line in unigramLines:
        line = line.split(' : ')
        unigramWord = line[0].strip()
        unigramValue = int(line[1].strip())
        if word == unigramWord:
            frequency = unigramValue
    return frequency

        
def totalFrequency(unigramLines):
    """
    List[String,...], int
    Returns the total number of words based on the unigram file
    """
    totalfrequency = 0
    for line in unigramLines:
        line = line.split(' : ')
        frequency = int(line[1].strip())
        totalfrequency += frequency
    return totalfrequency


# Part 5

def probStart(startString, filename):
    """
    string, file -> integer
    Given a start string (just one word) and a filename, compute the probability that a sentence begins with that startstring. So split your file into sentences. Count the number of times that the sentence begins with the word provided as startString. Return the probability as a number between
0 and 1. 
    """
    sentencesRaw = getSentences(filename)
    cleanSentences = cleanSentencesForProbability(sentencesRaw)
    firstWordProbabilityValue = firstWordProbability(startString, cleanSentences)
    writeProbStart(startString, firstWordProbabilityValue, 'commonStartingWords.txt')
    return firstWordProbabilityValue

def cleanSentencesForProbability(sentencesRaw):
    """
    list[string,...] -> list[string,...]
    Given a raw sentence, remove the names and remove unwanted punctuation. Return a list of clean sentences
    """
    cleanSentences = []
    for sentence in sentencesRaw:
        sentenceWithoutNames = ignoreNamesInSentence(sentence, 'HPChar.txt')
        words = sentenceWithoutNames.split()
        cleanWords = createWordList(words)
        cleanSentence = recombineSentence(cleanWords)
        cleanSentences.append(cleanSentence)
    return cleanSentences

def firstWordProbability(startString, cleanSentences):
    """
    string, list[string,...] -> int
    Given a string and a list of sentences, calculate the probability that the startString starts a sentence
    """
    numberOfSentences = len(cleanSentences)
    count = 0
    startString = startString.lower()
    for sentence in cleanSentences:
        words = sentence.split()
        firstWord = words[0]
        if startString == firstWord:
            count += 1
    probability = float(count) / numberOfSentences
    return probability

def writeProbStart(startString, firstWordProbabilityValue, outputFile):
    """
    string, integer, string -> File
    Takes a string and its probability as a starting word, populates the output file. Each time writeProbStart is run, a new entry is added, unless there is already an existing entry for the word.
    """

    if not openFile(outputFile):
        createFile = open(outputFile, 'w')
        createFile.close()
    lines = getLinesFromFile(outputFile)
    allWords = []
    for line in lines:
        words = line.split()
        allWords.extend(words)
    if not startString in allWords:
        outputText = startString.lower() + ' ' +  str(firstWordProbabilityValue)
        output = open(outputFile, 'a')
        output.write(outputText + '\n')
        output.close()


# Bottom level file-opening functions and error handling

def getLinesFromFile(filename):
    """
    File -> List[String,..]
    Given a file, return the contents of the file as lists of strings. Uses readlines (ie strips out /n)
    """
    if not openFile(filename):
        printErrorStatement(filename)
    else:
        text = open(filename, 'r')
        lines = []
        for line in text:
            lines.append(line.rstrip())
        text.close()
        return lines

def openFile(filename):
    """
    File -> Boolean
    Tries to open file. Returns false if there is an IO error, otherwise returns true
    """

    try:
        text = open(filename, 'r')
        text.close()
        return True
    except IOError:
        return False

def openFileWrite(filename):
    """
    File -> Boolean
    Attempts to open file for writing. Returns False if it fails
    """
    try:
        text = open(filename, 'w')
        text.close()
        return True
    except IOError:
        return False

def printErrorStatement(filename):
    """
    String -> None
    Prints an error message (if file cannot be opened), and exits program
    """
    print 'Unable to open file "' + filename + '". Please try again.'
    sys.exit(0)

def bigramFormat(bigram):
    """
    String -> boolean
    Takes a string, returns true only if it contains two words (separated by a space). 
    """
    if len(bigram.split()) != 2:
        return False
    else: 
        return True

    

if __name__ == "__main__":
    main()
