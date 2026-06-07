class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = defaultdict(list)
        for string in strs:
            alphabet_list = [0] * 26
            for letter in string:
                alphabet_list[ord(letter) - ord('a')] += 1
            result_dict[tuple(alphabet_list)].append(string)
        return list(result_dict.values())

        