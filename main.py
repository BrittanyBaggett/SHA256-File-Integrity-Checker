import hashlib

def hashing_generator(file):
    with open(file, "rb") as f:
# hashlib.file_digest(fileobj, digest, /)
# Return a digest object that has been updated with contents of file object.
        digest = hashlib.file_digest(f, "sha256")
#hexdigest() : Returns the encoded data in hexadecimal format.
    return digest.hexdigest()

def compare_hash(value1, value2):
    if value1 == value2:
        print("Match: file unchanged")
    else:
        print("Mistmatch: file changed")

original_value = hashing_generator("text.txt")
print("Original value:", original_value)
new_value = hashing_generator("text_copy.txt")
print("New value:", new_value)
compare_hash(original_value, new_value)


