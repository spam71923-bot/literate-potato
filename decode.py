import pickle

def rle_decode(encoded_data):
    decoded = []
    for char, count in encoded_data:
        decoded.extend([char] * count)
    return bytearray(decoded)

# 1. Load the compressed .rle structural data
with open('Shelly(1).rle', 'rb') as f:
    loaded_data = pickle.load(f)

# 2. Decompress back into raw bytes
restored_bytes = rle_decode(loaded_data)

# 3. Write back out as a visible image file
with open('Shelly_restored.png', 'wb') as f:
    f.write(restored_bytes)
