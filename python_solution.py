class Solution:
    """
    Group anagrams together from a given array of strings

    Example:

    Input: ["eat", "tea", "tan", "ate", "nat", "bat"]

    Output:
    [
        ["ate","eat","tea"], ["nat","tan"], ["bat"]
    ]
    """
    def groupAnagrams(self, array):

        anagram_dict = {};

        for i in array:
            word = ''.join(sorted(i))
            if word in anagram_dict.keys():
                anagram_dict[word].append(i)
            else:
                anagram_dict[word] = [i]
        return [value for value in anagram_dict.values()]
