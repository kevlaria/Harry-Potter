Harry-Potter
============
There are three main components of this assignment

1. You are given the first chapter of the first Harry Potter - ’HP1.txt’ 
The first thing is to read in each line from the file and compute the frequency of the each individual word. The unigrams and their frequencies should be stored in one file called unigramDict.txt. The file format should read like this. ‘of : 45’. 

The slightly tricky aspect to this part is to get rid of all the punctuation and just count words. 
Make a function called createUnigramDictionary(fileName) which reads in a file and creates a dictionary that given a word will return the frequency of the word.

To aid in removing punctuation marks which would mess this analysis up, please also write a function called removeAllPunctuation(string, disallowedCharacters), which takes in a string and a list of disallowed characters. It just removes all the disallowed characters from the string so that counting the words becomes easier. Also, in this particular text since we have a bunch of ‘Mr.’ and ‘Mrs.’, please remove all of them during this analysis as well.

Finally, in order to store the frequencies into a file, write a small utility function called writeDictToFile(dictionary, filename) that goes through key-value pairs in a given dictionary and writes them out to the provided filename in the form ‘key : value’. For instance if your dictionary contains ’abc’:123 then the file will basically just have one line saying ‘abc : 123’. Call this file unigramFrequencies.txt

2. Note the result of your unigram frequency analysis. A fair number of them will be proper nouns. This is less than useful since in theory the end goal is to understand patterns in the language. Now use the other file provided to you called ‘HPChar.txt’ which just has a bunch of Harry Potter characters with most of the principal characters and a few random ones thrown in there for fun. Figure out how you can use that file to help elminate the proper nouns and thereby get a cleaner analysis of the unigram frequencies.

Write a function called ignoreNames(mainfilename, characterfilename) that takes in a main file and a characters file and goes through and basically writes out another file, in this case let us call it ‘HPMinusNames.txt’ by throwing in the special character # anytime we have the name of a person. There are a couple of subtle things about a person’s name that I want you to discover and figure out how to handle.

Once ‘HPMinusNames.txt’ has been created, pass that file back through the unigram dictionary creator that you have in part 1 and obtain a cleaner result. Save that into a file unigramFrequeniciesMinusNames.txt

3. The second task is to now start looking at bigrams, and computing their frequencies. A bigram is just a two word sequence. So for instance a document like ‘This is a test. This is only a test. A test should not be concerning’, has the following bigrams:

  This is: 2,
  is a: 1,
  a test: 3,
  is only: 1,
  only a: 1,
  should not : 1,
  not be : 1,  
  be concerning : 1. 
  
Compute the bigram frequencies for all the pairs in the Harry Potter file. Remember that you break the bigram at the end of sentences.

The first step here is to write a function that given a file returns a list of the sentences in the file. Write getSentences(fileName) that takes in a fileName and parses the file returning a list of sentences.

Given the sentences, first clean up the sentences (remove things like quotes, exclama- tions etc and ignore names) using previously written functions and then write a function to produce bigram frequencies. In this problem make sure bigrams involving a person’s name all get ignored. Specifically write getBigramFreqFromSentence(sentence) which takes in sentence and returns a dictionary with bigrams and their frequencies. This function is allowed to call (in fact it has to) the functions you wrote to remove punctuation.

You might also find it useful to write another function called ignoreNamesInSentence(string, characterfilename), which goes through a sentence and just strips out all the names.

As a specific example ‘John and I decided to go have a beer, a pizza and brownies with Tracy’ should generate the following bigrams: ‘{and I, I decided, decided to, to go, go have, have a, a beer, beer a, a pizza, pizza and, and brownies, brownies with}’

Now using the 2 functions written above, write a third function called getBigramFreqFromFile(filename) which takes in a filename and returns a dictionary of bigram frequencies.

Since we do want to later access this information, store these bigram frequencies in another file called bigramFrequencies.txt. Of course, you are allowed to use the function that you wrote earlier that takes in a dictionary and just dumps that information in a file. So for instance a line in this file would read something like - ‘in this : 34’ meaning that we have seen the occurence of either ‘in this’ 34 times.

4. Finally, assemble the contingency matrix for any bigram. The contingency matrix basically tries to give you the frequecy of the bigram and of the individual words in the bigram. A contingency matrix is of the form shown below
      of ¬of 
most  4  24 
¬most 55 10000

where ¬ indicates the not operator.

• The bigram ‘most of’ occurs a grand total of 4 times in the text
• The word ‘most’ occurs a total of 28 times. Only 4 of those times it occurs alongside ‘of’
• The word ‘of’ shows up 59 times. 4 of those times it occurs alongside ‘of’
• There are a total of 10,000 bigrams that do not have the word ‘of’ or the word ‘most’ in them.

Write a function called createContingency(bigram, bigramfilename) which returns the 2x2 matrix for any bigram that is provided using the information about bigram frequencies from a provided file. As we have seen in previous assignments, the easiest way to represent this would be to just use a list of lists representation for the matrix. For this function, make sure you do some level of error checking to make sure that it is indeed a bigram that is being passed to you. That is, make sure that it has 2 words in it.

Note that the bigram frequencies file has all the information you need to construct this contingency matrix for any bigram. To make this matrix you just have to parse that one file and should not have to go back to the original Harry Potter text.
