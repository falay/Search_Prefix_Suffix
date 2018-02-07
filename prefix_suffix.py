class TrieNode(object):

    def __init__(self, substr=""):

        self.substr = substr
        self.children = {}
        self.isWord = False


class Trie:

    def __init__(self):

        self.root = TrieNode( "" )


    def insert(self, string):

        current_node = self.root

        for i in range( len(string) ):
            if string[i] not in current_node.children:
                current_node.children[ string[i] ] = TrieNode( string[:i+1] )
            current_node = current_node.children[ string[i] ]
        
        current_node.isWord = True


    def start_with(self, prefix):

        current_node = self.root
        
        for i in range( len(prefix) ):
            current_node = current_node.children.get( prefix[i], None )
            if current_node is None:
                return None

        return current_node 


    def fitSuffix(self, word, suffix):

        if len(word) >= len(suffix):
            return word[ len(word)-len(suffix): ] == suffix
        return False


    def suffixFinder(self, target_node, suffix, possible_words):

        if target_node is None:
            return

        if target_node.isWord and self.fitSuffix( target_node.substr, suffix ):
            possible_words.append( target_node.substr )

        for char, child in target_node.children.items():
            self.suffixFinder( child, suffix, possible_words )




class WordFilter:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = Trie()
        self.weight_map = {}

        for i in range( len(words) ):
            self.weight_map[ words[i] ] = i
            self.trie.insert( words[i] )



    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        current_node = self.trie.start_with( prefix )
        if current_node is None:
            return -1

        possible_words = []
        self.trie.suffixFinder( current_node, suffix, possible_words )
        possible_weights = [ self.weight_map[word] for word in possible_words if word in self.weight_map ]

        return max( possible_weights ) if len(possible_weights) > 0 else -1




if __name__ == '__main__':

    w = WordFilter(["apple"])
    
    print( w.f( "a", "e" ) )




