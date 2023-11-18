from PIL import Image

def hide_message(image_path, message, output_path):
 
    img = Image.open(image_path)
    pixels = list(img.getdata())
    binary_message = ''.join(format(ord(char), '08b') for char in message)

   
    index = 0
    for i in range(len(pixels)):
        pixel = list(pixels[i])
        for j in range(3): 
            
            if index < len(binary_message):
                pixel[j] = pixel[j] & ~1 | int(binary_message[index])
                index += 1
        pixels[i] = tuple(pixel)

   
    new_img = Image.new(img.mode, img.size)
    new_img.putdata(pixels)
    new_img.save(output_path)

def extract_message(image_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    binary_message = ''
    for pixel in pixels:
        for value in pixel:
            binary_message += str(value & 1)

  
    message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))

    return message

image_path = '/home/amul/Documents/stegnography/Untitled.jpeg'
message_to_hide = 'hello i am amul this side!'
output_image_path = '/home/amul/Documents/stegnography/output_image.png'


hide_message(image_path, message_to_hide, output_image_path)


extracted_message = extract_message(output_image_path)
print("Extracted Message:", extracted_message)
