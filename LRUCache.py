class cacheNode(object):

    def __init__(self, key, value):

        self.key = key
        self.value = value
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cacheMap = {}
        self.capacity = capacity  
        self.cacheHead = cacheNode( 0, 0 ) # dummy head
        self.cacheTail = None


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cacheMap:
            return -1

        cacheEntry = self.cacheMap[ key ]
        self.move2head( cacheEntry, exists=True )

        return cacheEntry.value
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cacheMap:
            self.cacheMap[ key ].value = value
            self.move2head( self.cacheMap[ key ], exists=True )            
            return

        if len(self.cacheMap) == self.capacity:
            remove_key = self.remove_last()
            self.cacheMap.pop( remove_key, None )


        new_cacheEntry = cacheNode( key, value )
        self.move2head( new_cacheEntry, exists=False )
        self.cacheMap[ key ] = new_cacheEntry



    def move2head(self, cache_node, exists):

        if cache_node == self.cacheHead.next:
            return

        if self.cacheTail is None and cache_node.next is None:
            self.cacheTail = cache_node
        elif self.cacheTail == cache_node:
            self.cacheTail = self.cacheTail.prev

        if exists:
            cache_node.prev.next = cache_node.next
            if cache_node.next is not None:
                cache_node.next.prev = cache_node.prev

        cache_node.next = self.cacheHead.next
        if self.cacheHead.next is not None:
            self.cacheHead.next.prev = cache_node
        self.cacheHead.next = cache_node
        cache_node.prev = self.cacheHead


    def remove_last(self):

        if self.cacheTail is None:
            return

        remove_key = self.cacheTail.key
        new_tail_node = self.cacheTail.prev  
        del self.cacheTail
        new_tail_node.next = None
        
        self.cacheTail = None if new_tail_node == self.cacheHead else new_tail_node

        return remove_key


if __name__ == '__main__':

    cache = LRUCache(1)
    cache.put(2, 1)
    print( cache.get(2) )         # returns 1
    cache.put(3, 2)    # evicts key 2
    print( cache.get(2) )       # returns -1 (not found)
    print(cache.get(3))       # returns -1 (not found)
    print(cache.get(3))       # returns 3
    print(cache.get(4))      # returns 4
    



