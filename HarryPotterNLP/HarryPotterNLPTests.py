from HarryPotterNLP import *
import unittest

class TestAssignment5(unittest.TestCase):

    def testcreateUnigramDictionary(self):
        wordDict = createUnigramDictionary('HP1.txt')
        self.assertEqual(2, wordDict['opened'])

    def testcreateUnigramDictionary2(self):
        wordDict = createUnigramDictionary('HP1.txt')
        self.assertEqual(14, wordDict['so'])

    def testcreateUnigramDictionary3(self):
        wordDict = createUnigramDictionary('HP1.txt')
        self.assertEqual(29, wordDict['you'])

    def testcreateUnigramDictionary4(self):
        wordDict = createUnigramDictionary('HP1.txt')
        self.assertEqual(16, wordDict['this'])

    def testcreateUnigramDictionary5(self):
        wordDict = createUnigramDictionary('HP1.txt')
        self.assertEqual(26, wordDict['mcgonagall'])

    def testcreateUnigramDictionary6(self):
        wordDict = createUnigramDictionary('HP1.txt')
        self.assertEqual(False, '#' in wordDict)



    def testimportWords(self):
        words = importWords('HP1.txt')
        self.assertEqual("'you", words[0])

    def testimportWords2(self):
        words = importWords('testText.txt')
        self.assertEqual("are", words[0])        
 


    def testreadFileLine(self):
        wordList = readFileLine('HP1.txt')
        self.assertEqual('Mr.', wordList[0])

    def testreadFileLine2(self):
        wordList2 = readFileLine('HPChar.txt')
        self.assertEqual('Harry', wordList2[0])



    def testcreateDictionary(self):
        self.assertEqual({'a' : 2, 'b': 1}, createDictionary(['a', 'b', 'a']))




    def testcreateWordList(self):
        self.assertEqual(['apple', 'oranges'], createWordList(['apple!', '?oranges']))

    def testcreateWordList2(self):
        self.assertEqual(['man', 'hour'], createWordList(["man's", "hours'"]))




    def testremoveAllPunctuation(self):
        self.assertEqual('haggis', removeAllPunctuation('haggis,', [',']))

    def testremoveAllPunctuation2(self):
        self.assertEqual('haggis', removeAllPunctuation('haggis,', [',', ':']))

    def testremoveAllPunctuation3(self):
        self.assertEqual('haggis,', removeAllPunctuation('haggis,', [':']))

    def testremoveAllPunctuation4(self):
        self.assertEqual('haggis', removeAllPunctuation('hag,gis', [',']))

    def testremoveAllPunctuation5(self):
        self.assertEqual('haggis', removeAllPunctuation('hag\gis', ['\\']))

    def testremoveAllPunctuation6(self):
        self.assertEqual('haggis', removeAllPunctuation("hag'gis", ['\'']))

    def testremoveAllPunctuation7(self):
        self.assertEqual('haggis', removeAllPunctuation('hag"gis', ['"']))
        


    def testwriteDictToFile(self):
        writeDictToFile({'a': 2, 'b': 3}, 'writeToDictUnitTest.txt')
        f = open('writeToDictUnitTest.txt')
        lines = f.readlines()
        self.assertEqual('a : 2\n', lines[0])

    def testwriteDictToFile2(self):
        writeDictToFile({'a': 2, 'b': 3}, 'writeToDictUnitTest.txt')
        f = open('writeToDictUnitTest.txt')
        lines = f.readlines()
        self.assertEqual('b : 3\n', lines[1])




    def testreformatDictionary(self):
        self.assertEqual('assert : 5', reformatDictionary(('assert', 5)))
       



    def testignoreNames(self):
        ignoreNames('HP1.txt', 'HPChar.txt')
        f = open('HPMinusNames.txt')
        lines = f.readlines()
        words = []
        for line in lines:
            words.extend(line.split())
        self.assertEqual('#', words[3])




    def testreplaceNameWithHash(self):
        self.assertEqual(['#', 'and', '#', 'went', 'up', 'the', 'hill'], replaceNameWithHash(['John', 'Jack', 'Jill'], ['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill']))




    def testgetBigramFreqFromFile(self):
        documentBigramDictionary = getBigramFreqFromFile('HP1.txt')
        self.assertEqual(6, documentBigramDictionary['they were'])

    def testgetBigramFreqFromFile2(self):
        documentBigramDictionary = getBigramFreqFromFile('HP1.txt')
        self.assertEqual(None, documentBigramDictionary.get('Harry Potter'))

    def testgetBigramFreqFromFile3(self):
        documentBigramDictionary = getBigramFreqFromFile('HP1.txt')
        self.assertEqual(None, documentBigramDictionary.get('unDursleyish as'))

    def testgetBigramFreqFromFile4(self):
        documentBigramDictionary = getBigramFreqFromFile('HP1.txt')
        self.assertEqual(1, documentBigramDictionary['drills he'])




    def testgetSentences(self):
        self.assertEqual(['Do we have any sugar', 'Yes we do', 'Thank you and farewell'], getSentences('getSentenceTest.txt'))




    def testremoveDotAfterMr(self):
        self.assertEqual('Mr and Mrs Jones and Mrs Smith', removeDotAfterMr('Mr. and Mrs. Jones and Mrs. Smith'))




    def testsentenceCleansing(self):
        self.assertEqual(['Do we have any sugar', 'Yes we do', 'Thank you and farewell'], sentenceCleansing(['', 'Do we have any sugar ', '\nYes we do', '', 'Thank you and farewell']))




    def testremoveEmptyStrings(self):
        self.assertEqual(['Do we have any sugar', 'Yes we do'], removeEmptyStrings(['', 'Do we have any sugar', 'Yes we do', '']))




    def testremoveSpacesAndReturns(self):
        self.assertEqual(['Do we have any sugar', 'Yes we do', 'Thank you and farewell'], removeSpacesAndReturns(['Do we have any sugar ', '\nYes we do ', ' Thank you and farewell\n']))  





    def testignoreNamesInSentence(self):
        self.assertEqual('# and # Churchill', ignoreNamesInSentence('Harry and Lord Churchill', 'HPChar.txt'))




    def testrecombineSentence(self):
        self.assertEqual('a and b and c', recombineSentence(['a', 'and', 'b', 'and', 'c']))




    def testamalgamateBigramDictionary(self):
        newDictionary = amalgamateBigramDictionary('this is a test', {'this is': 1, 'a test': 3, 'a man': 4})
        self.assertEqual(2, newDictionary['this is'])

    def testamalgamateBigramDictionary2(self):
        newDictionary = amalgamateBigramDictionary('this is a test', {'this is': 1, 'a test': 3, 'a man': 4})
        self.assertEqual(4, newDictionary['a man'])

    def testamalgamateBigramDictionary3(self):
        newDictionary = amalgamateBigramDictionary('this is a test', {'this is': 1, 'a test': 3, 'a man': 4})
        self.assertEqual(1, newDictionary['is a'])





    def testgetBigramFreqFromSentence(self):
        dictionary = getBigramFreqFromSentence('This is a test, this is only a test, a test should not be concerning')
        self.assertEqual(3, dictionary['a test'])

    def testgetBigramFreqFromSentence2(self):
        dictionary = getBigramFreqFromSentence('This is a test, this is only a test, a test should not be concerning')
        self.assertEqual(set(['this is','is a','test a', 'test this', 'test should', 'a test','is only', 'only a','should not', 'not be', 'be concerning']), set(dictionary.viewkeys()))





    def testcreateBigrams(self):
        self.assertEqual(['a man', 'man and', 'and a', 'a pan'], createBigrams(['a', 'man', 'and', 'a', 'pan']))

    def testcreateBigrams2(self):
        self.assertEqual(['by what'], createBigrams(['by', 'what', '#', 'said']))




    def testcreateContingency(self):
        filename = 'HP1.txt'
        self.populateBigramDictionary(filename)
        self.populateUnigramDictionary(filename)
        self.assertEqual([[0, 1-0],[1-0, (3875-(0 + (1-0) + (1-0)))]], createContingency('bathroom crept', 'bigramFrequencies.txt', 'unigramFrequenciesMinusNames.txt'))

    def testcreateContingency2(self):
        filename = 'HP1.txt'
        self.populateBigramDictionary(filename)
        self.populateUnigramDictionary(filename)
        self.assertEqual([[3, 8-3],[204-3, (3875-(3 + (8-3) + (204 - 3)))]], createContingency('Last The', 'bigramFrequencies.txt', 'unigramFrequenciesMinusNames.txt'))

    def testcreateContingency3(self):
        filename = 'HP1.txt'
        self.populateBigramDictionary(filename)
        self.populateUnigramDictionary(filename)
        self.assertEqual([[3, 204-3],[8-3, (3875-(3 + (8-3) + (204 - 3)))]], createContingency('The Last', 'bigramFrequencies.txt', 'unigramFrequenciesMinusNames.txt'))




    def testcontingencyValidation(self):
        self.assertEqual(None, contingencyValidation('a b', 'bigramFrequencies.txt', 'unigramFrequenciesMinusNames.txt'))




    def testsplitBigram(self):
        self.assertEqual(('oh', 'no'), splitBigram('oh no'))




    def testwordOneAndTwo(self):
        bigramLines = self.populateBigramDictionary('testText.txt')
        self.assertEqual(3, wordOneAndTwo('my', 'name', bigramLines))

    def testwordOneAndTwo2(self):
        bigramLines = self.populateBigramDictionary('testText.txt')
        self.assertEqual(0, wordOneAndTwo('is', 'Harry', bigramLines))

    def testwordOneAndTwo3(self):
        bigramLines = self.populateBigramDictionary('HP1.txt')
        self.assertEqual(0, wordOneAndTwo('bathroom', 'crept', bigramLines))

    def testwordOneAndTwo4(self):
        bigramLines = self.populateBigramDictionary('HP1.txt')
        self.assertEqual(3, wordOneAndTwo('last', 'the', bigramLines))

    def testwordOneAndTwo5(self):
        bigramLines = self.populateBigramDictionary('HP1.txt')
        self.assertEqual(wordOneAndTwo('i', 'know', bigramLines), wordOneAndTwo('know', 'i', bigramLines))





    def testopenFileWrite(self):
        self.assertEqual(True, openFileWrite('unitTestEmpty.txt'))

    def testopenFileWrite2(self):
        self.assertEqual(False, openFileWrite('/test/test.txt'))




    def testoneWordFrequency(self):
        unigramLines = self.populateUnigramDictionary('HP1.txt')
        self.assertEqual(32, oneWordFrequency('all', unigramLines))

    def testoneWordFrequency2(self):
        unigramLines = self.populateUnigramDictionary('HP1.txt')
        self.assertEqual(0, oneWordFrequency('Harry', unigramLines))
 



    def testtotalFrequency(self):
        bigramLines = self.populateBigramDictionary('HP1.txt')
        self.assertEqual(3875, totalFrequency(bigramLines))

    def testtotalFrequency2(self):
        bigramLines = self.populateBigramDictionary('testText.txt')
        self.assertEqual(12, totalFrequency(bigramLines))




    def testprobStart(self):
        self.assertEqual(3.0/349, probStart('this', 'HP1.txt'))

    def testprobStart2(self):
        self.assertEqual(50.0/349, probStart('he', 'HP1.txt'))

    def testprobStart3(self):
        self.assertEqual(0/349, probStart('Harry', 'HP1.txt'))




    def testcleanSentencesForProbability(self):
        sentencesRaw = getSentences('HP1.txt')
        cleanSentences = cleanSentencesForProbability(sentencesRaw)
        self.assertEqual('and # of number four privet drive were proud to say that they were perfectly normal thank you very much', cleanSentences[0])

    def testcleanSentencesForProbability2(self):
        sentencesRaw = getSentences('testTextForProbability.txt')
        cleanSentences = cleanSentencesForProbability(sentencesRaw)
        self.assertEqual('this is #', cleanSentences[3])




    def testfirstWordProbability(self):
        sentencesRaw = getSentences('testTextForProbability.txt')
        cleanSentences = cleanSentencesForProbability(sentencesRaw)
        self.assertEqual(0.5, firstWordProbability('This', cleanSentences))

    def testfirstWordProbability2(self):
        sentencesRaw = getSentences('testTextForProbability.txt')
        cleanSentences = cleanSentencesForProbability(sentencesRaw)
        self.assertEqual(0, firstWordProbability('Harry', cleanSentences))

    def testfirstWordProbability3(self):
        sentencesRaw = getSentences('testTextForProbability.txt')
        cleanSentences = cleanSentencesForProbability(sentencesRaw)
        self.assertEqual(0.25, firstWordProbability('hello', cleanSentences))




    def testwriteProbStart(self):
        f = open('writeProbStart.txt', 'w')
        f.write('')
        f.close()
        writeProbStart('man', 3, 'writeProbStart.txt')
        f1 = open('writeProbStart.txt', 'r')
        linesRaw = f1.read()
        self.assertEqual(True, linesRaw.find('man 3') > -1)

    def testwriteProbStart2(self):
        f = open('writeProbStart2.txt', 'w')
        f.write('')
        f.close()
        writeProbStart('man', 3, 'writeProbStart2.txt')
        writeProbStart('pan', 5, 'writeProbStart2.txt')
        f1 = open('writeProbStart2.txt', 'r')
        linesRaw = f1.read()
        self.assertEqual(True, linesRaw.find('pan 5') > -1)

    def testwriteProbStart3(self):
        f = open('writeProbStart3.txt', 'w')
        f.write('')
        f.close()
        writeProbStart('man', 3, 'writeProbStart3.txt')
        writeProbStart('pan', 5, 'writeProbStart3.txt')
        writeProbStart('man', 3, 'writeProbStart3.txt')
        f1 = open('writeProbStart3.txt', 'r')
        lines = f1.readlines()
        self.assertEqual('pan 5\n', lines[-1])





    def testgetLinesFromFile(self):
        wordList3 = getLinesFromFile('HPChar.txt')
        self.assertEqual('Harry Potter', wordList3[0])

 


    def testopenFile(self):
        self.assertEqual(True, openFile('HP1.txt'))

    def testopenFile2(self):
        self.assertEqual(False, openFile('HP.txt'))




    def testprintErrorStatement(self):
        pass
        #Can't test print statement




    def testbigramFormat(self):
        self.assertEqual(True, bigramFormat('one two'))

    def testbigramFormat2(self):
        self.assertEqual(False, bigramFormat('one two three'))

    def testbigramFormat3(self):
        self.assertEqual(False, bigramFormat('one'))

    def testbigramFormat4(self):
        self.assertEqual(False, bigramFormat('one '))

    def testbigramFormat5(self):
        self.assertEqual(False, bigramFormat(' one'))

    def testbigramFormat6(self):
        self.assertEqual(True, bigramFormat(' one two'))


    

    def populateBigramDictionary(self, sourceFileName):
        """
        File -> List[String,...]
        Given a file, returns a list of bigrams
        """
        sourceFile = sourceFileName
        bigramDictionary = getBigramFreqFromFile(sourceFile)
        writeDictToFile(bigramDictionary, 'bigramFrequencies.txt')
        bigramLines = getLinesFromFile('bigramFrequencies.txt')
        return bigramLines

    def populateUnigramDictionary(self, sourceFileName):
        """
        File -> List[String,...]
        Given a file, returns a list of unigrams
        """
        sourceFile = sourceFileName
        cleanFile = ignoreNames(sourceFile, 'HPChar.txt')
        newDictionary = createUnigramDictionary('HPMinusNames.txt')
        writeDictToFile(newDictionary, 'unigramFrequenciesMinusNames.txt')
        unigramLines = getLinesFromFile('unigramFrequenciesMinusNames.txt')
        return unigramLines


unittest.main()
