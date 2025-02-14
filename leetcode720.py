#Time Complexity = O(nlogn)
#Space Complexity = O(n)
class Solution:
    def longestWord(self, words: List[str]) -> str:
    # Sort words first lexicographically and then by length
        words.sort()
        
        wordset, longest_word = set([""]), ""

        for word in words:
            if word[:-1] in wordset:  # Check if the prefix exists
                wordset.add(word)
                if len(word) > len(longest_word):
                    longest_word = word

        return longest_word

# Tries solution
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True  # Mark end of word

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Step 1: Insert all words into the Trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        # Step 2: Perform DFS to find the longest valid word
        longest_word = ""
        stack = [(trie.root, "")]  # (node, current_word)

        while stack:
            node, word = stack.pop()

            # Update longest_word if a valid longer word is found
            if len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word):
                longest_word = word

            # Iterate through children in sorted order (ensuring lexicographical order)
            for c in sorted(node.children.keys()):
                if node.children[c].endOfWord:
                    stack.append((node.children[c], word + c))

        return longest_word



