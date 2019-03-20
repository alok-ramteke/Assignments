import multiprocessing 


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


def square(numbers, result, square_sum): 
    """ 
    function to square a given list 
    """
    for idx, num in enumerate(numbers): 
        result[idx] = num * num 

    square_sum.value = sum(result) 

    print("Result(process p1): {}".format(result[:])) 

    print("Sum of squares(process p1): {}".format(square_sum.value)) 

if __name__ == "__main__": 

    numbers = [1,2,3,4] 

    result = multiprocessing.Array('i', 4) 
 
    square_sum = multiprocessing.Value('i') 

    p1 = multiprocessing.Process(target=square, args=(numbers, result, square_sum)) 

    p1.start() 

    p1.join() 

    print("Result(main program): {}".format(result[:])) 

    print("Sum of squares(main program): {}".format(square_sum.value))
