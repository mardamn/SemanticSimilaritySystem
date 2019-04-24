from  algorithm import LCS
from  algorithm import LCSubstring
import algorithms
import time
import csv
from random import randrange, uniform


def jaro_result(all, name, ran):
    # with open('results/Jaro.csv', mode='w') as csv_file:
    fieldnames = ['name', 'num', 's1', 's2', 's3', 'r1', 'r2', 'r3', "t1", "t2", "t3", "t4", "t5", "t6"]
    #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #     writer.writeheader()

    for i in range(51):
        for j in range(all[i].__len__()):
            numbers = []
            times = []
            for k in range(all[i].__len__()):
                if (j != k):
                    start = time.time()
                    numbers.append(algorithms.Jaro(all[i][j], all[i][k]))
                    end = time.time()
                    times.append(end - start)
            for k in range(2):
                random1 = randrange(1, 50)
                random2 = randrange(0, 4)
                if (random1 == i):
                    random1 = randrange(1, 50)
                try:
                    start = time.time()
                    numbers.append(algorithms.Jaro(all[i][j], all[random1][random2]))
                    end = time.time()
                    times.append(end - start)
                except:
                    print("Ulvi bey:", random1, random2)

            random1 = randrange(1, 50)
            random2 = randrange(0, 3)
            try:
                start = time.time()
                numbers.append(algorithms.Jaro(all[i][j], ran[random1][random2]))
                end = time.time()
                times.append(end - start)
            except:
                print("Ulvi bey:", random1, random2)

            with open(r'results/Jaro.csv', 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                try:
                    writer.writerow({'name': name, 'num': i,
                                     's1': numbers[0], 's2': numbers[1], 's3': numbers[2],
                                     'r1': numbers[3], 'r2': numbers[4], 'r3': numbers[5],
                                     't1': times[0], 't2': times[1], 't3': times[2],
                                     't4': times[3], 't5': times[4], 't6': times[5]
                                     })

                except IndexError:
                    print(name)
                    print("Ulvi bey:", numbers)


def jaro_wikler_result(all, name, ran):
    # with open('results/Jaro_Winkler.csv', mode='w') as csv_file:
    fieldnames = ['name', 'num', 's1', 's2', 's3', 'r1', 'r2', 'r3', "t1", "t2", "t3", "t4", "t5", "t6"]
    #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #     writer.writeheader()

    for i in range(51):
        for j in range(all[i].__len__()):
            numbers = []
            times = []
            for k in range(all[i].__len__()):
                if (j != k):
                    start = time.time()
                    numbers.append(algorithms.Jaro_Winkler(all[i][j], all[i][k]))
                    end = time.time()
                    times.append(end - start)
            for k in range(2):
                random1 = randrange(1, 50)
                random2 = randrange(0, 4)
                if (random1 == i):
                    random1 = randrange(1, 50)
                try:
                    start = time.time()
                    numbers.append(algorithms.Jaro_Winkler(all[i][j], all[random1][random2]))
                    end = time.time()
                    times.append(end - start)
                except:
                    print("Ulvi bey:", random1, random2)

            random1 = randrange(1, 50)
            random2 = randrange(0, 3)
            try:
                start = time.time()
                numbers.append(algorithms.Jaro_Winkler(all[i][j], ran[random1][random2]))
                end = time.time()
                times.append(end - start)
            except:
                print("Ulvi bey:", random1, random2)

            with open(r'results/Jaro_Winkler.csv', 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                try:
                    writer.writerow({'name': name, 'num': i,
                                     's1': numbers[0], 's2': numbers[1], 's3': numbers[2],
                                     'r1': numbers[3], 'r2': numbers[4], 'r3': numbers[5],
                                     't1': times[0], 't2': times[1], 't3': times[2],
                                     't4': times[3], 't5': times[4], 't6': times[5]
                                     })

                except IndexError:
                    print(name)
                    print("Ulvi bey:", numbers)


def levenshtein_result(all, name, ran):
    # with open('results/Levenshtein.csv', mode='w') as csv_file:
    fieldnames = ['name', 'num', 's1', 's2', 's3', 'r1', 'r2', 'r3', "t1", "t2", "t3", "t4", "t5", "t6"]
    #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #     writer.writeheader()

    for i in range(51):
        for j in range(all[i].__len__()):
            numbers = []
            times = []
            for k in range(all[i].__len__()):
                if (j != k):
                    start = time.time()
                    numbers.append(algorithms.Levenshtein(all[i][j], all[i][k]))
                    end = time.time()
                    times.append(end - start)
            for k in range(2):
                random1 = randrange(1, 50)
                random2 = randrange(0, 4)
                if (random1 == i):
                    random1 = randrange(1, 50)
                try:
                    start = time.time()
                    numbers.append(algorithms.Levenshtein(all[i][j], all[random1][random2]))
                    end = time.time()
                    times.append(end - start)
                except:
                    print("Ulvi bey:", random1, random2)

            random1 = randrange(1, 50)
            random2 = randrange(0, 3)
            try:
                start = time.time()
                numbers.append(algorithms.Levenshtein(all[i][j], ran[random1][random2]))
                end = time.time()
                times.append(end - start)
            except:
                print("Ulvi bey:", random1, random2)

            with open(r'results/Levenshtein.csv', 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                try:
                    writer.writerow({'name': name, 'num': i,
                                     's1': numbers[0], 's2': numbers[1], 's3': numbers[2],
                                     'r1': numbers[3], 'r2': numbers[4], 'r3': numbers[5],
                                     't1': times[0], 't2': times[1], 't3': times[2],
                                     't4': times[3], 't5': times[4], 't6': times[5]
                                     })
                except IndexError:
                    print(name)
                    print("Ulvi bey:", numbers)


def damerau_levenshtein_result(all, name, ran):
    # with open('results/Damerau_Levenshtein.csv', mode='w') as csv_file:
    fieldnames = ['name', 'num', 's1', 's2', 's3', 'r1', 'r2', 'r3', "t1", "t2", "t3", "t4", "t5", "t6"]
    #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #     writer.writeheader()

    for i in range(51):
        for j in range(all[i].__len__()):
            numbers = []
            times = []
            for k in range(all[i].__len__()):
                if (j != k):
                    start = time.time()
                    numbers.append(algorithms.Damerau_Levenshtein(all[i][j], all[i][k]))
                    end = time.time()
                    times.append(end - start)
            for k in range(2):
                random1 = randrange(1, 50)
                random2 = randrange(0, 4)
                if (random1 == i):
                    random1 = randrange(1, 50)
                try:
                    start = time.time()
                    numbers.append(algorithms.Damerau_Levenshtein(all[i][j], all[random1][random2]))
                    end = time.time()
                    times.append(end - start)
                except:
                    print("Ulvi bey:", random1, random2)

            random1 = randrange(1, 50)
            random2 = randrange(0, 3)
            try:
                start = time.time()
                numbers.append(algorithms.Damerau_Levenshtein(all[i][j], ran[random1][random2]))
                end = time.time()
                times.append(end - start)
            except:
                print("Ulvi bey:", random1, random2)

            with open(r'results/Damerau_Levenshtein.csv', 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                try:
                    writer.writerow({'name': name, 'num': i,
                                     's1': numbers[0], 's2': numbers[1], 's3': numbers[2],
                                     'r1': numbers[3], 'r2': numbers[4], 'r3': numbers[5],
                                     't1': times[0], 't2': times[1], 't3': times[2],
                                     't4': times[3], 't5': times[4], 't6': times[5]
                                     })
                except IndexError:
                    print(name)
                    print("Ulvi bey:", numbers)


def ratcliff_obershelp_result(all, name, ran):
    # with open('results/Ratcliff_Obershelp.csv', mode='w') as csv_file:
    fieldnames = ['name', 'num', 's1', 's2', 's3', 'r1', 'r2', 'r3', "t1", "t2", "t3", "t4", "t5", "t6"]
    #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #     writer.writeheader()

    for i in range(51):
        for j in range(all[i].__len__()):
            numbers = []
            times = []
            for k in range(all[i].__len__()):
                if (j != k):
                    start = time.time()
                    numbers.append(algorithms.Ratcliff_Obershelp(all[i][j], all[i][k]))
                    end = time.time()
                    times.append(end - start)
            for k in range(2):
                random1 = randrange(1, 50)
                random2 = randrange(0, 4)
                if (random1 == i):
                    random1 = randrange(1, 50)
                try:
                    start = time.time()
                    numbers.append(algorithms.Ratcliff_Obershelp(all[i][j], all[random1][random2]))
                    end = time.time()
                    times.append(end - start)
                except:
                    print("Ulvi bey:", random1, random2)

            random1 = randrange(1, 50)
            random2 = randrange(0, 3)
            try:
                start = time.time()
                numbers.append(algorithms.Ratcliff_Obershelp(all[i][j], ran[random1][random2]))
                end = time.time()
                times.append(end - start)
            except:
                print("Ulvi bey:", random1, random2)

            with open(r'results/Ratcliff_Obershelp.csv', 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                try:
                    writer.writerow({'name': name, 'num': i,
                                     's1': numbers[0], 's2': numbers[1], 's3': numbers[2],
                                     'r1': numbers[3], 'r2': numbers[4], 'r3': numbers[5],
                                     't1': times[0], 't2': times[1], 't3': times[2],
                                     't4': times[3], 't5': times[4], 't6': times[5]
                                     })
                except IndexError:
                    print(name)
                    print("Ulvi bey:", numbers)


def longest_common_substring_result(all, name, ran):
    # with open('results/longest_common_substring.csv', mode='w') as csv_file:
    fieldnames = ['name', 'num', 's1', 's2', 's3', 'r1', 'r2', 'r3', "t1", "t2", "t3", "t4", "t5", "t6"]
    #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #     writer.writeheader()

    for i in range(51):
        for j in range(all[i].__len__()):
            numbers = []
            times = []
            for k in range(all[i].__len__()):
                if (j != k):
                    start = time.time()
                    numbers.append(LCSubstring.LCSubStr(all[i][j], all[i][k]))
                    end = time.time()
                    times.append(end - start)
            for k in range(2):
                random1 = randrange(1, 50)
                random2 = randrange(0, 4)
                if (random1 == i):
                    random1 = randrange(1, 50)
                try:
                    start = time.time()
                    numbers.append(LCSubstring.LCSubStr(all[i][j], all[random1][random2]))
                    end = time.time()
                    times.append(end - start)
                except:
                    print("Ulvi bey:", random1, random2)

            random1 = randrange(1, 50)
            random2 = randrange(0, 3)
            try:
                start = time.time()
                numbers.append(LCSubstring.LCSubStr(all[i][j], ran[random1][random2]))
                end = time.time()
                times.append(end - start)
            except:
                print("Ulvi bey:", random1, random2)

            with open(r'results/longest_common_substring.csv', 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                try:
                    writer.writerow({'name': name, 'num': i,
                                     's1': numbers[0], 's2': numbers[1], 's3': numbers[2],
                                     'r1': numbers[3], 'r2': numbers[4], 'r3': numbers[5],
                                     't1': times[0], 't2': times[1], 't3': times[2],
                                     't4': times[3], 't5': times[4], 't6': times[5]
                                     })
                except IndexError:
                    print(name)
                    print("Ulvi bey:", numbers)


def longest_common_subsequence_result(all, name, ran):
    # with open('results/longest_common_subsequence.csv', mode='w') as csv_file:
    fieldnames = ['name', 'num', 's1', 's2', 's3', 'r1', 'r2', 'r3', "t1", "t2", "t3", "t4", "t5", "t6"]
    #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #     writer.writeheader()

    for i in range(51):
        for j in range(all[i].__len__()):
            numbers = []
            times = []
            for k in range(all[i].__len__()):
                if (j != k):
                    start = time.time()
                    numbers.append(LCS.LCSsimilarity(all[i][j], all[i][k]))
                    end = time.time()
                    times.append(end - start)
            for k in range(2):
                random1 = randrange(1, 50)
                random2 = randrange(0, 4)
                if (random1 == i):
                    random1 = randrange(1, 50)
                try:
                    start = time.time()
                    numbers.append(LCS.LCSsimilarity(all[i][j], all[random1][random2]))
                    end = time.time()
                    times.append(end - start)
                except:
                    print("Ulvi bey:", random1, random2)

            random1 = randrange(1, 50)
            random2 = randrange(0, 3)
            try:
                start = time.time()
                numbers.append(LCS.LCSsimilarity(all[i][j], ran[random1][random2]))
                end = time.time()
                times.append(end - start)
            except:
                print("Ulvi bey:", random1, random2)

            with open(r'results/longest_common_subsequence.csv', 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                try:
                    writer.writerow({'name': name, 'num': i,
                                     's1': numbers[0], 's2': numbers[1], 's3': numbers[2],
                                     'r1': numbers[3], 'r2': numbers[4], 'r3': numbers[5],
                                     't1': times[0], 't2': times[1], 't3': times[2],
                                     't4': times[3], 't5': times[4], 't6': times[5]
                                     })
                except IndexError:
                    print(name)
                    print("Ulvi bey:", numbers)


def fuzzy_result(all, name, ran):
    # with open('results/fuzzy.csv', mode='w') as csv_file:
    fieldnames = ['name', 'num', 's1', 's2', 's3', 'r1', 'r2', 'r3', "t1", "t2", "t3", "t4", "t5", "t6"]
    #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #     writer.writeheader()

    for i in range(51):
        for j in range(all[i].__len__()):
            numbers = []
            times = []
            for k in range(all[i].__len__()):
                if (j != k):
                    start = time.time()
                    numbers.append(algorithms.Fuzzy(all[i][j], all[i][k]))
                    end = time.time()
                    times.append(end - start)
            for k in range(2):
                random1 = randrange(1, 50)
                random2 = randrange(0, 4)
                if (random1 == i):
                    random1 = randrange(1, 50)
                try:
                    start = time.time()
                    numbers.append(algorithms.Fuzzy(all[i][j], all[random1][random2]))
                    end = time.time()
                    times.append(end - start)
                except:
                    print("Ulvi bey:", random1, random2)

            random1 = randrange(1, 50)
            random2 = randrange(0, 3)
            try:
                start = time.time()
                numbers.append(algorithms.Fuzzy(all[i][j], ran[random1][random2]))
                end = time.time()
                times.append(end - start)
            except:
                print("Ulvi bey:", random1, random2)

            with open(r'results/fuzzy.csv', 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                try:
                    writer.writerow({'name': name, 'num': i,
                                     's1': numbers[0], 's2': numbers[1], 's3': numbers[2],
                                     'r1': numbers[3], 'r2': numbers[4], 'r3': numbers[5],
                                     't1': times[0], 't2': times[1], 't3': times[2],
                                     't4': times[3], 't5': times[4], 't6': times[5]
                                     })
                except IndexError:
                    print(name)
                    print("Ulvi bey:", numbers)
