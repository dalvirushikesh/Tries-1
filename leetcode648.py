# Time Complexity =  O(mL + nK) where
    # m = number of words in the dictionary
    # L = average length of words in dictionary
    # n = number of words in the sentence
    # K = average length of words in the sentence
#Space Complexity = O(mL+nK)

class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie = Trie()
        words = sentence.split(" ")

        # Insert dictionary words into the Trie
        for word in dict:
            trie.insert(word)

        root = trie.getRoot()
        res = ""

        for word in words:
            temp = root
            replaceStr = ""
            flag = False

            for char in word:
                replaceStr += char

                # If there is no path in Trie, keep original word
                if temp.children[ord(char) - ord('a')] is None:
                    res += word + " "
                    flag = True
                    break

                temp = temp.children[ord(char) - ord('a')]

                # If a valid prefix is found, replace the word
                if temp.isword:
                    res += replaceStr + " "
                    flag = True
                    break

            if not temp.isword and not flag:
                res += word + " "

        return res.strip()


class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = [None] * 26
        self.isword = False


class Trie:
    def __init__(self):
        self.root = TrieNode(" ")

    def getRoot(self):
        return self.root

    def insert(self, word):
        temp = self.root
        for char in word:
            if temp.children[ord(char) - ord('a')] is None:
                temp.children[ord(char) - ord('a')] = TrieNode(char)
            temp = temp.children[ord(char) - ord('a')]
        temp.isword = True
