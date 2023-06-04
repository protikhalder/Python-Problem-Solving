alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


plaintext_input = input("Enter a String to Encrypt: ")
input_length = len(plaintext_input)

shift_input = int(input("Enter the key value:"))

print(input_length)


output = ""

for i in range(input_length):
    char = plaintext_input[i]
    location_of_string = alphabets.find(char)
    new_location = (location_of_string+shift_input)%26

    output = output + alphabets[new_location]
print(output)
