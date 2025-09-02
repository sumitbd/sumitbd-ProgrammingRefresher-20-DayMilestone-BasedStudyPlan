class DuplicateDetector:
    def __init__(self, array):
        self.array = array

    # HashMap (dictionary)
    def detect_with_hashmap(self):
        freq = {}
        duplicates = []
        for num in self.array:
            if num in freq:
                freq[num] += 1
                if freq[num] == 2:
                    duplicates.append(num)
            else:
                freq[num] = 1
        return duplicates

    # Set
    def detect_with_set(self):
        seen = set()
        duplicates = set()
        for num in self.array:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)
        return  list(duplicates)


# Main program
if __name__ == "__main__":
    data = [1, 2, 3, 4, 2, 5, 6, 3, 1, 7,8,8,1,2]

    detector = DuplicateDetector(data)

    print("Original data:", data)
    print("Duplicates (HashMap):", detector.detect_with_hashmap())
    print("Duplicates (Set):", detector.detect_with_set())
