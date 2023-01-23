file_descriptors = []
for x in range(2000):
    file_descriptors.append(open('data.txt', 'w')) 