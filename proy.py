def recursive_find_match(i, j, pattern, pattern_track):

    if pattern[i] == pattern[j]:
        pattern_track.append(i+1)
        return {"append":pattern_track, "i": i+1, "j": j+1}
    elif pattern[i] != pattern[j] and i == 0:
        pattern_track.append(i)
        return {"append":pattern_track, "i": i, "j": j+1}

    else:
        i = pattern_track[i-1]
        return recursive_find_match(i, j, pattern, pattern_track)

def kmp(str_, pattern):

    len_str = len(str_)
    len_pattern = len(pattern)
    pattern_track = []

    if len_pattern == 0:
        return
    elif len_pattern == 1:
        pattern_track = [0]
    else:   
        pattern_track = [0]
        i = 0
        j = 1

        while j < len_pattern:
            data = recursive_find_match(i, j, pattern, pattern_track)

            i = data["i"]
            j = data["j"]
            pattern_track = data["append"]

    index_str = 0
    index_pattern = 0
    match_from = -1

    while index_str < len_str:
        if index_pattern == len_pattern:
            break
        if str_[index_str] == pattern[index_pattern]:
            if index_pattern == 0:
                match_from = index_str

            index_pattern += 1
            index_str += 1
        else:
            if index_pattern == 0:
                index_str += 1
            else:
                index_pattern = pattern_track[index_pattern-1]
                match_from = index_str - index_pattern
    from time import time
    start =time()
    recursive_find_match()
    end=time()-start
    print(end)