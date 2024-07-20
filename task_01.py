"""
Додати метод delete для видалення пар ключ-значення таблиці HashTable , яка реалізована в конспекті.
"""


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] in self.table:
            for pair in self.table[key_hash]:
                if pair == key_value:
                    del self.table[key_hash]
                    print(f"Key: value '{key}: {value}' deleted")
                else: 
                    print(f" {key}: {value} not found")

    def __str__(self):
        result = []
        for i, bucket in enumerate(self.table):
            if bucket:
                result.append(f"Bucket {i}: " + ", ".join(f"{key}: {value}" for key, value in bucket))
            else:
                result.append(f"Bucket {i}: Empty")
        return "\n".join(result)

    
if __name__ == "__main__":
    H = HashTable(5)
    H.insert("apple", 10)
    H.insert("orange", 20)
    H.insert("banana", 30)

    print(H.get("apple"))   # Виведе: 10
    print(H.get("orange"))  # Виведе: 20
    print(H.get("banana"))  # Виведе: 30
    print(H)

    H.delete("orange", 30)
    print(H)

