output_file = open("Updated.txt","w")
input_file = open("Repeated.txt","r")
lines_seen_so_far = set()
print("Eliminating duplicate lines")
for line in input_file:
  if line not in lines_seen_so_far:
    output_file.write(line)
    lines_seen_so_far.add(line)

output_file.close() 
input_file.close ()  