from typing import List, Dict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        Given a string s and a dictionary of strings wordDict, add spaces in s to
        construct a sentence where each word is a valid dictionary word. Return
        all such possible sentences in any order.

        Args:
            s (str): The input string to be segmented.
            wordDict (List[str]): The list of valid dictionary words.

        Returns:
            List[str]: A list of all possible sentences.
        """
        def dfs(memo: Dict[str, List[str]], chaine: str) -> List[str]:
            if chaine in memo:
                return memo[chaine]
            if not chaine:
                return [""]
            resultat = []
            for mot in motDict:
                if chaine.startswith(mot):
                    sous_resultat = dfs(memo, chaine[len(mot):])
                    for segment in sous_resultat:
                        resultat.append(mot + ("" if not segment else " ") + segment)
            memo[chaine] = resultat
            return resultat

        motDict = set(wordDict)
        return dfs({}, s)

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak("catsanddog", ["cat","cats","and","sand","dog"])) # ["cats and dog","cat sand dog"]
    print(sol.wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"])) # ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
    print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"])) # []
    print(sol.wordBreak("aaaaaaa", ["aaaa","aa","a"])) # ["a a a a a a a","aa a a a a a","a aa a a a a","aa aa a a a","a a aa a a a","a aa aa a a","aa a aa a a","a a a aa a a","aa aa aa a","a a aa aa a","a aa a aa a","a a a a aa a","aa a a aa a","a aa aa aa","aa aa aa a","a a a aa aa","a aa a aa","aa a aa aa","a a a a a a a"]
