def rle_encode(data):
    if not data:
        return []
    encoding = []
    prev_char = data[0]
    count = 1
    for char in data[1:]:
        if char == prev_char:
            count += 1
        else:
            encoding.append((prev_char, count))
            prev_char = char
            count = 1
    encoding.append((prev_char, count))
    return encoding

def rle_decode(encoded_data):
    decoded = []
    for char, count in encoded_data:
        decoded.extend([char] * count)
    # Convert back to a bytearray or list depending on your input type
    return bytearray(decoded) 

# --- ENCODING AN IMAGE FILE ---
# 1. Read the raw bytes of the image
with open('Shelly(1).png', 'rb') as f:
    raw_bytes = f.read()

# 2. Run your encoder function
compressed_data = rle_encode(raw_bytes)

# --- DECODING BACK TO AN IMAGE FILE ---
# 3. Run your decoder function
decompressed_bytes = rle_decode(compressed_data)

# 4. Save the bytes back out as an image
with open('restored_image.png', 'wb') as f:
    f.write(decompressed_bytes)
