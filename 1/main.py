lines = open("input", "r").readlines()

current_batch = []
batches_sum = []
for line in lines:
    if line == "\n":
        batches_sum.append(sum(current_batch))
        current_batch = []
        continue
    current_batch.append(int(line[:-1]))
print(max(batches_sum))