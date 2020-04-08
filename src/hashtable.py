# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"<{self.key}, {self.value}>"


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        # Hashmod the key to find the bucket
        index = self._hash_mod(key)
       #  Check if a pair already exists in the bucket
        if self.storage[index] is not None:
            # pair exists, set current pair to head.next, then new pair to head
            head = LinkedPair(key, value)
            head.next = self.storage[index]
            # set new pair to head
            self.storage[index] = head

        else:
            self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        index = self._hash_mod(key)
        # Check if key matches the first item at the index
        # If it does:
        if self.storage[index].key == key:
            # Set the first item in the LL to found item's "next" node
            self.storage[index] = self.storage[index].next
            return
        # If it doesnt:
        else:
            prev_node = self.storage[index]
            #  Traverse the LL one-by-one until you find the item, then set the node before it to point to the node after it
            while prev_node is not None and prev_node.next is not None:
                current_node = prev_node.next
                if current_node.key == key:
                    if current_node.next is not None:
                        prev_node.next = current_node.next
                        return
                    #  If it's the last item, set the item before it to point to "None"
                    else:
                        prev_node.next = None

                prev_node = prev_node.next

    def retrieve(self, key):
        index = self._hash_mod(key)
        if self.storage[index] is None:
            return None
        else:
            if self.storage[index].key == key:
                return self.storage[index].value
            else:
                node = self.storage[index]
                while node.next is not None:
                    node = node.next
                    if node.key == key:
                        return node.value

    def resize(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity

        for bucket_item in self.storage:
            # move everything to new storage
            if bucket_item is not None:
                node = bucket_item
                new_index = self._hash_mod(node.key)
                new_storage[new_index] = LinkedPair(node.key, node.value)
                while node.next is not None:
                    node = node.next
                    new_index = self._hash_mod(node.key)
                    if new_storage[new_index] is not None:
                        head = LinkedPair(node.key, node.value)
                        head.next = new_storage[new_index]
                        new_storage[new_index] = head
                    else:
                        new_storage[new_index] = LinkedPair(
                            node.key, node.value)

        self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print(ht.storage)

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
