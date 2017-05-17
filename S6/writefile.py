output = open('./example2.txt', 'r+')
with open('./example.txt', 'r') as input:
  for line in input:
    output.write(line)
input.close()
output.close()