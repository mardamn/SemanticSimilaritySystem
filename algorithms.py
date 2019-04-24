from difflib import SequenceMatcher
from pyjarowinkler import distance
from fuzzywuzzy import fuzz
import Levenshtein as lev
from algorithm import DL
from  algorithm import LCS
from  algorithm import LCSubstring
import pickle

def Ratcliff_Obershelp(a, b):
    return SequenceMatcher(None, a, b).ratio() *100

def Damerau_Levenshtein(X,Y):

    damerau = DL.dameraulevenshtein(X,Y)
    lens=len(X) + len(Y)
    return ((lens - damerau) / (lens)) *100
    # return damerau.distance(X, Y)

def Levenshtein(X,Y):
    return lev.ratio(X, Y)*100

def Jaro_Winkler(X,Y):
    return distance.get_jaro_distance(X, Y, winkler=True, scaling=0.1)*100

def Jaro(X,Y):
    return distance.get_jaro_distance(X, Y, winkler=False, scaling=0.1)*100

def Fuzzy(X,Y):
    return  fuzz.token_set_ratio(X, Y)

def LCSeq(X,Y):
    return LCS.LCSsimilarity(X,Y)

def LCStr(X,Y):
    return LCSubstring.LCSubStr(X,Y)

def NeuralNetwork(X,Y):
    filename = 'modelweb.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    list = []
    list.append(Jaro(X,Y))
    list.append(Jaro_Winkler(X,Y))
    list.append(Levenshtein(X,Y))
    list.append(Ratcliff_Obershelp(X, Y))
    list.append(Fuzzy(X,Y))
    list.append(Damerau_Levenshtein(X,Y))
    list.append(LCStr(X,Y))
    list.append(LCSeq(X,Y))

    result = loaded_model.predict([list])
    print(result)
    if(int(result[0])==0):
        return "ns"
    if (int(result[0]) == 1):
        return "s"



