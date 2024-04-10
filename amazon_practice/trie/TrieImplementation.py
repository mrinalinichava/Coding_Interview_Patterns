class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def get(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def reverse(self, node=None, word='', results=None):
        if results is None:
            results = []
            node = self.root
        if node.is_end_of_word:
            results.append(word[::-1])  # Reverse the word before adding
        for char, next_node in node.children.items():
            self.reverse(next_node, word + char, results)
        return results

# Example usage:
prefix_tree = PrefixTree()
words = ["hello", "world", "help", "held", "halt"]
for w in words:
    prefix_tree.add(w)

print("Get 'hello':", prefix_tree.get("hello"))  # True
print("Get 'world':", prefix_tree.get("world"))  # True
print("Get 'worlds':", prefix_tree.get("worlds"))  # False
print("Get 'help':", prefix_tree.get("help"))  # True

print("All words in reverse:")
print(prefix_tree.reverse())  # ['olleh', 'dlrow', 'pleh', 'dleH', 'tlah']
