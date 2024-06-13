import hashlib
import math


class BloomFilter:
    def __init__(self, items_count, false_positive_probability):
        """
        Initialize BloomFilter with given parameters.

        :param items_count: Expected number of items to be added to the filter.
        :param false_positive_probability: Desired false positive probability.
        """
        self.false_positive_probability = false_positive_probability
        self.size = self.get_size(items_count, false_positive_probability)
        self.hash_count = self.get_hash_count(self.size, items_count)
        self.bit_array = [0] * self.size  # Initialize bit array with zeros

    def add(self, item):
        """
        Add an item to the BloomFilter.

        :param item: The item to add.
        """
        for i in range(self.hash_count):
            digest = self.hash(item, i) % self.size
            self.bit_array[digest] = 1

    def check(self, item):
        """
        Check if an item may be present in the BloomFilter.

        :param item: The item to check.
        :return: True if the item may be present (possibly), False if it's definitely not present.
        """
        for i in range(self.hash_count):
            digest = self.hash(item, i) % self.size
            if self.bit_array[digest] == 0:
                return False  # Definitely not present
        return True  # Possibly present

    def hash(self, item_list, i):
        """
        Generate a hashed value for the given item.

        :param item_list: List of items to hash.
        :param i: Index of the hash function.
        :return: Hashed integer value.
        """
        item_str = ''.join(str(e) for e in item_list)

        # Incorporate index i into the hashing input to ensure uniqueness per i
        unique_input = f"{item_str}-{i}"

        # Create hash object
        hash_obj = hashlib.md5(unique_input.encode())

        # Return the resulting integer hash
        return int(hash_obj.hexdigest(), 16)

    @classmethod
    def get_size(cls, n, p):
        """
        Calculate the size of the bit array (m) for the BloomFilter.

        :param n: Expected number of items.
        :param p: False positive probability.
        :return: Size of the bit array (m).
        """
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    @classmethod
    def get_hash_count(cls, m, n):
        """
        Calculate the number of hash functions (k) for the BloomFilter.

        :param m: Size of the bit array.
        :param n: Expected number of items.
        :return: Number of hash functions (k).
        """
        k = (m / n) * math.log(2)
        return int(k)


# Example usage
if __name__ == "__main__":
    import util.util as util

    # Assume we are working with a random person and their family members
    person = util.pick_random_person()
    array = person.family

    items_count = len(person.family)  # Assume we expect to hold len(person.family) items
    false_positive_probability = 0.05  # Desired false positive probability

    # Create a BloomFilter instance
    bloom = BloomFilter(items_count, false_positive_probability)

    # Adding items from the array to the Bloom filter
    for item in array:
        bloom.add(item)

    # Check if the first item in the person's family is possibly in the array
    test_item = person.family[0]
    if bloom.check(test_item):
        print(f"'{test_item}' is possibly in the array")
    else:
        print(f"'{test_item}' is definitely not in the array")

    # Check a specific test_item not in the person's family
    test_item = "ce14d3da-17c6-4c4b-9701-98ec69166794"
    if bloom.check(test_item):
        print(f"'{test_item}' is possibly in the array")
    else:
        print(f"'{test_item}' is definitely not in the array")

