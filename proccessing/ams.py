import math
import random
import numpy as np

def AMS_second_moment(stream, k):
    """
    Calculate the estimated second moment (F2) using the AMS (Alon-Matias-Szegedy) algorithm.

    :param stream: The input stream of items.
    :param k: Number of random samples (hash functions).
    :return: Estimated second moment (F2).
    """
    # Initialize counters
    counters = [0] * k

    # Random hash functions (+1 or -1)
    hash_functions = [random.choice([-1, 1]) for _ in range(k)]

    # Process each item in the stream
    for item in stream:
        # Generate random hash values for the item
        hashes = [random.choice(hash_functions) for _ in range(k)]

        # Update counters
        for i in range(k):
            counters[i] += hashes[i]

    # Compute the estimate of F2
    squared_counters = [count ** 2 for count in counters]
    estimated_F2 = np.median(squared_counters)

    return estimated_F2

# Example usage:
if __name__ == "__main__":
    stream = [1, 2, 3, 1, 2, 1, 3, 4, 5, 1, 10, 20, 30, 11, 13, 15, 17, 1, 4, 5]
    k = 5  # Number of random samples

    # Calculate the estimated second moment (F2)
    estimated_F2 = AMS_second_moment(stream, k)
    
    # Compare with the real value (mean of the stream)
    real_value = sum(stream) / len(stream)
    
    # Print results
    print("Estimated second moment (F2):", math.sqrt(estimated_F2))
    print("Real value (mean):", real_value)

