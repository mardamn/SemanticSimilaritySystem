def jaro_similarity(s, t):
        s_len = len(s)
        t_len = len(t)

        if s_len == 0 and t_len == 0:
            return 1

        match_distance = (max(s_len, t_len) // 2) - 1

        s_matches = [False] * s_len
        t_matches = [False] * t_len

        matches = 0
        transpositions = 0

        for i in range(s_len):
            start = max(0, i - match_distance)
            end = min(i + match_distance + 1, t_len)

            for j in range(start, end):
                if t_matches[j]:
                    continue
                if s[i] != t[j]:
                    continue
                s_matches[i] = True
                t_matches[j] = True
                matches += 1
                break

        if matches == 0:
            return 0

        k = 0
        for i in range(s_len):
            if not s_matches[i]:
                continue
            while not t_matches[k]:
                k += 1
            if s[i] != t[k]:
                transpositions += 1
            k += 1

        return ((matches / s_len) +
                (matches / t_len) +
                ((matches - transpositions / 2) / matches)) / 3


def jaro_winkler_similarity(s1, s2, p=0.1, max_l=None):

    jaro_sim = jaro_similarity(s1, s2)

    max_l = max_l if max_l else len(s1)

    l = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            print(s1[i])
            l += 1
        else:
            break
        if l == max_l:
            break
    l= min(l, 4)

    return ((jaro_sim + (l * p * (1 - jaro_sim)))*100)/100
