import pickle

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

# 1. Load the original image file in read-binary ('rb') mode
# (Replace 'shelly.png' with your actual source image filename)
with open('Shelly(1).png', 'rb') as f:
    raw_bytes = f.read()

# 2. Generate the RLE compression tuple-list
compressed_data = rle_encode(raw_bytes)

# 3. Save the tuple-list into "Shelly(1).rle" using write-binary ('wb') mode
with open('Shelly(1).rle', 'wb') as f:
    pickle.dump(compressed_data, f)

print("Successfully compressed and saved to Shelly(1).rle")
