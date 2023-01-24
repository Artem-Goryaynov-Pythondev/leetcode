def lengthOfLongestSubstring(s: str) -> int:
    a = 0
    i = 0
    lengths = []
    accumulator = []
    while i != len(s):
        if accumulator.__contains__(s[i]):
            lengths.append(len(accumulator))
            print(accumulator)
            accumulator = []
            a += 1
            i = 0
            i = i + a
            continue
        else:
            accumulator.append(s[i])
            i += 1
    lengths.append(len(accumulator))
    a = sorted(lengths)

    return a[-1]
assert lengthOfLongestSubstring("dvdf") == 3
assert lengthOfLongestSubstring("ababc") == 3
assert lengthOfLongestSubstring("eabcdefgabcdefgh") == 8 #ab
assert lengthOfLongestSubstring("aaaabb") == 2 #ab
assert lengthOfLongestSubstring("abcab") == 3 #abc
assert lengthOfLongestSubstring("abcabcbb") == 3 #abc
assert lengthOfLongestSubstring("hfuoirbaspdyutowokzxjkhroquisdafoije") == 12 #fsdoaktjp

