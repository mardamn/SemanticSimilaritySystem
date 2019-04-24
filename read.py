import results
import time
def clear_text(a):
    a = a.lower()
    a = a.replace("\n", "")
    a = a.replace(" ", "")
    a = a.replace(".", "")
    a = a.replace("?", "")
    a = a.replace("!", "")
    a = a.replace("\"", "")
    a = a.replace(":", "")
    a = a.replace(",", "")
    a = a.replace("-", "")
    a = a.replace(" ", "")
    a = a.replace("|", "")

    return a



with open("news/cemiyyet.txt","r") as file:
    same = []
    cemiyyet=[[]]
    i=0
    for ln in file:
        if ln.startswith("#"):
            num=int(ln[1:(int(ln[0:6].find(':')))])
            if(i==num):
                a=ln[int(ln[0:6].find(':'))+1:]
                # a = clear_text(a)
                a = a.replace("\n", "")
                same.append(a)
            elif(i!=num):
                cemiyyet.insert(i,same)
                i=num
                same = []
                a = ln[int(ln[0:6].find(':')) + 1:]
                # a=clear_text(a)
                a = a.replace("\n", "")
                same.append(a)

    cemiyyet.insert(i, same)


with open("news/hadise.txt","r") as file:
    same = []
    hadise = [[]]
    i = 0
    for ln in file:
        if ln.startswith("#"):
            num = int(ln[1:(int(ln[0:6].find(':')))])
            if (i == num):
                a = ln[int(ln[0:6].find(':')) + 1:]
                # a = clear_text(a)
                a = a.replace("\n", "")
                same.append(a)
            elif (i != num):
                hadise.insert(i, same)
                i = num
                same = []
                a = ln[int(ln[0:6].find(':')) + 1:]
                # a=clear_text(a)
                a = a.replace("\n", "")
                same.append(a)

    hadise.insert(i, same)



with open("news/idman.txt","r") as file:
    same = []
    idman = [[]]
    i = 0
    for ln in file:
        if ln.startswith("#"):
            num = int(ln[1:(int(ln[0:6].find(':')))])
            if (i == num):
                a = ln[int(ln[0:6].find(':')) + 1:]
                # a = clear_text(a)
                a = a.replace("\n", "")
                same.append(a)
            elif (i != num):
                idman.insert(i, same)
                i = num
                same = []
                a = ln[int(ln[0:6].find(':')) + 1:]
                # a=clear_text(a)
                a = a.replace("\n", "")
                same.append(a)

    idman.insert(i, same)


with open("news/medeniyyet.txt","r") as file:
    same = []
    medeniyyet = [[]]
    i = 0
    for ln in file:
        if ln.startswith("#"):
            num = int(ln[1:(int(ln[0:6].find(':')))])
            if (i == num):
                a = ln[int(ln[0:6].find(':')) + 1:]
                # a = clear_text(a)
                a = a.replace("\n", "")
                same.append(a)
            elif (i != num):
                medeniyyet.insert(i, same)
                i = num
                same = []
                a = ln[int(ln[0:6].find(':')) + 1:]
                # a=clear_text(a)
                a = a.replace("\n", "")
                same.append(a)

    medeniyyet.insert(i, same)


with open("news/siyaset.txt","r") as file:
    same = []
    siyaset = [[]]
    i = 0
    for ln in file:
        if ln.startswith("#"):
            num = int(ln[1:(int(ln[0:6].find(':')))])
            if (i == num):
                a = ln[int(ln[0:6].find(':')) + 1:]
                # a = clear_text(a)
                a = a.replace("\n", "")
                same.append(a)
            elif (i != num):
                siyaset.insert(i, same)
                i = num
                same = []
                a = ln[int(ln[0:6].find(':')) + 1:]
                # a=clear_text(a)
                a = a.replace("\n", "")
                same.append(a)

    siyaset.insert(i, same)


with open("news/texnologiya.txt","r") as file:
    same = []
    texnologiya = [[]]
    i = 0
    for ln in file:
        if ln.startswith("#"):
            num = int(ln[1:(int(ln[0:6].find(':')))])
            if (i == num):
                a = ln[int(ln[0:6].find(':')) + 1:]
                # a = clear_text(a)
                a = a.replace("\n", "")
                same.append(a)
            elif (i != num):
                texnologiya.insert(i, same)
                i = num
                same = []
                a = ln[int(ln[0:6].find(':')) + 1:]
                # a=clear_text(a)
                a = a.replace("\n", "")
                same.append(a)

    texnologiya.insert(i, same)



with open("news/iqtisadiyyat.txt","r") as file:
    same = []
    iqtisadiyyat = [[]]
    i = 0
    for ln in file:
        if ln.startswith("#"):
            num = int(ln[1:(int(ln[0:6].find(':')))])
            if (i == num):
                a = ln[int(ln[0:6].find(':')) + 1:]
                # a = clear_text(a)
                a = a.replace("\n", "")
                same.append(a)
            elif (i != num):
                iqtisadiyyat.insert(i, same)
                i = num
                same = []
                a = ln[int(ln[0:6].find(':')) + 1:]
                # a=clear_text(a)
                a = a.replace("\n", "")
                same.append(a)

    iqtisadiyyat.insert(i, same)




with open("news/maraqli.txt","r") as file:
    same = []
    maraqli = [[]]
    i = 0
    for ln in file:
        if ln.startswith("#"):
            num = int(ln[1:(int(ln[0:6].find(':')))])
            if (i == num):
                a = ln[int(ln[0:6].find(':')) + 1:]
                # a = clear_text(a)
                a = a.replace("\n", "")
                same.append(a)
            elif (i != num):
                maraqli.insert(i, same)
                i = num
                same = []
                a = ln[int(ln[0:6].find(':')) + 1:]
                # a=clear_text(a)
                a = a.replace("\n", "")
                same.append(a)

    maraqli.insert(i, same)
k=0
for i in range(cemiyyet.__len__()):
    for j in range(cemiyyet[i].__len__()):
        k=k+1
        print("cemiyyet: ", i, "-", j, ":", cemiyyet[i][j])
print(k)
k=0
for i in range(hadise.__len__()):
    for j in range(hadise[i].__len__()):
        k=k+1
        print("hadise: ", i, "-", j, ":", hadise[i][j])
print(k)
k=0
for i in range(idman.__len__()):
    for j in range(idman[i].__len__()):
        k=k+1

        print("idman: ", i, "-", j, ":", idman[i][j])
print(k)
k=0
for i in range(medeniyyet.__len__()):
    for j in range(medeniyyet[i].__len__()):
        k=k+1

        print("medeniyyet: ", i, "-", j, ":", medeniyyet[i][j])
print(k)
k=0
for i in range(siyaset.__len__()):
    for j in range(siyaset[i].__len__()):
        k=k+1

        print("siyaset: ", i, "-", j, ":", siyaset[i][j])
print(k)
k=0
for i in range(texnologiya.__len__()):
    for j in range(texnologiya[i].__len__()):
        k=k+1

        print("texnologiya: ", i, "-", j, ":", texnologiya[i][j])
print(k)
k=0
for i in range(iqtisadiyyat.__len__()):
    for j in range(iqtisadiyyat[i].__len__()):
        k=k+1

        print("iqtisadiyyat: ", i, "-", j, ":", iqtisadiyyat[i][j])
print(k)
k=0
for i in range(maraqli.__len__()):
    for j in range(maraqli[i].__len__()):
        k=k+1

        print("maraqli: ", i, "-", j, ":", maraqli[i][j])
print(k)
k=0

#JARO
start=time.time()
results.jaro_result(cemiyyet,"cemiyyet",idman)
results.jaro_result(hadise,"hadise",idman)
results.jaro_result(idman,"idman",maraqli)
results.jaro_result(iqtisadiyyat,"iqtisadiyyat",idman)
results.jaro_result(maraqli,"maraqli",idman)
results.jaro_result(medeniyyet,"medeniyyet",idman)
results.jaro_result(siyaset,"siyaset",idman)
results.jaro_result(texnologiya,"texnologiya",idman)
end = time.time()
print("jaro:",end-start)


# JARO WINKLER
start=time.time()
results.jaro_wikler_result(cemiyyet,"cemiyyet",idman)
results.jaro_wikler_result(hadise,"hadise",idman)
results.jaro_wikler_result(idman,"idman",maraqli)
results.jaro_wikler_result(iqtisadiyyat,"iqtisadiyyat",idman)
results.jaro_wikler_result(maraqli,"maraqli",idman)
results.jaro_wikler_result(medeniyyet,"medeniyyet",idman)
results.jaro_wikler_result(siyaset,"siyaset",idman)
results.jaro_wikler_result(texnologiya,"texnologiya",idman)
end = time.time()
print("jaro-winkler:",end-start)

# LEVENSHTEIN
start=time.time()
results.levenshtein_result(cemiyyet,"cemiyyet",idman)
results.levenshtein_result(hadise,"hadise",idman)
results.levenshtein_result(idman,"idman",maraqli)
results.levenshtein_result(iqtisadiyyat,"iqtisadiyyat",idman)
results.levenshtein_result(maraqli,"maraqli",idman)
results.levenshtein_result(medeniyyet,"medeniyyet",idman)
results.levenshtein_result(siyaset,"siyaset",idman)
results.levenshtein_result(texnologiya,"texnologiya",idman)
end = time.time()
print("levenshtein: ",end-start)

# fuzzy
start=time.time()
results.fuzzy_result(cemiyyet,"cemiyyet",idman)
results.fuzzy_result(hadise,"hadise",idman)
results.fuzzy_result(idman,"idman",maraqli)
results.fuzzy_result(iqtisadiyyat,"iqtisadiyyat",idman)
results.fuzzy_result(maraqli,"maraqli",idman)
results.fuzzy_result(medeniyyet,"medeniyyet",idman)
results.fuzzy_result(siyaset,"siyaset",idman)
results.fuzzy_result(texnologiya,"texnologiya",idman)
end = time.time()
print("fuzzy: ",end-start)

#RO
start=time.time()
results.ratcliff_obershelp_result(cemiyyet,"cemiyyet",idman)
results.ratcliff_obershelp_result(hadise,"hadise",idman)
results.ratcliff_obershelp_result(idman,"idman",maraqli)
results.ratcliff_obershelp_result(iqtisadiyyat,"iqtisadiyyat",idman)
results.ratcliff_obershelp_result(maraqli,"maraqli",idman)
results.ratcliff_obershelp_result(medeniyyet,"medeniyyet",idman)
results.ratcliff_obershelp_result(siyaset,"siyaset",idman)
results.ratcliff_obershelp_result(texnologiya,"texnologiya",idman)
end = time.time()
print("ratcliff_obershelp: ",end-start)

# DL
start=time.time()
results.damerau_levenshtein_result(cemiyyet,"cemiyyet",idman)
results.damerau_levenshtein_result(hadise,"hadise",idman)
results.damerau_levenshtein_result(idman,"idman",maraqli)
results.damerau_levenshtein_result(iqtisadiyyat,"iqtisadiyyat",idman)
results.damerau_levenshtein_result(maraqli,"maraqli",idman)
results.damerau_levenshtein_result(medeniyyet,"medeniyyet",idman)
results.damerau_levenshtein_result(siyaset,"siyaset",idman)
results.damerau_levenshtein_result(texnologiya,"texnologiya",idman)
end = time.time()
print("damerau_levenshtein: ",end-start)
#
# LC-subsequence
start=time.time()
results.longest_common_subsequence_result(cemiyyet,"cemiyyet",idman)
results.longest_common_subsequence_result(hadise,"hadise",idman)
results.longest_common_subsequence_result(idman,"idman",maraqli)
results.longest_common_subsequence_result(iqtisadiyyat,"iqtisadiyyat",idman)
results.longest_common_subsequence_result(maraqli,"maraqli",idman)
results.longest_common_subsequence_result(medeniyyet,"medeniyyet",idman)
results.longest_common_subsequence_result(siyaset,"siyaset",idman)
results.longest_common_subsequence_result(texnologiya,"texnologiya",idman)
end = time.time()
print("LC-subsequence: ",end-start)


#LC-substring
start=time.time()
results.longest_common_substring_result(cemiyyet,"cemiyyet",idman)
results.longest_common_substring_result(hadise,"hadise",idman)
results.longest_common_substring_result(idman,"idman",maraqli)
results.longest_common_substring_result(iqtisadiyyat,"iqtisadiyyat",idman)
results.longest_common_substring_result(maraqli,"maraqli",idman)
results.longest_common_substring_result(medeniyyet,"medeniyyet",idman)
results.longest_common_substring_result(siyaset,"siyaset",idman)
results.longest_common_substring_result(texnologiya,"texnologiya",idman)
end = time.time()
print("LC-substring: ",end-start)
