### Encoding ###
codes = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}

def encode(text):
  text_list = list(text)
  for i in range(len(text_list)):
    vowel_code = codes.get(text_list[i].lower())

    if vowel_code:
      text_list[i] = f'{vowel_code}'

  return "".join(text_list)


print(encode('Hello World'))
# Will output: H2ll4 W4rld

print(encode('I love Python programming'))
# Will output: 3 l4v2 pyth4n pr4gr1mm3ng


### Decoding ###
# Time complexity is lower when we access dictionary by keys rather than values;
# therefore we create a dictionary of reverse codes
codes_reverse = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}

def decode(text):
  text_list = list(text)
  for i in range(len(text_list)):
    vowel = codes_reverse.get(text_list[i])

    if vowel:
      text_list[i] = vowel

  return "".join(text_list)

print(decode('H2ll4 W4rld'))
# Will output: Hello World

print(decode('3 l4v2 Pyth4n pr4gr1mm3ng'))
# Will output: I love Python programming