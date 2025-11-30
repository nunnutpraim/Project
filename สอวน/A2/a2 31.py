def is_valid_pair(a, b):
    return (a == 'A' and b == 'T') or \
           (a == 'T' and b == 'A') or \
           (a == 'C' and b == 'G') or \
           (a == 'G' and b == 'C')

n = int(input())
chrom1 = input().split()
chrom2 = input().split()
k = int(input())

for _ in range(k):
    line = input().split()
    chrom_no = int(line[0])
    pos = int(line[1])
    new_gene = line[2]

    if chrom_no == 1:
        chrom1[pos] = new_gene
    else:
        chrom2[pos] = new_gene

wrong_count = 0
for a, b in zip(chrom1, chrom2):
    if not is_valid_pair(a, b):
        wrong_count += 1

print(" ".join(chrom1))
print(" ".join(chrom2))
print(wrong_count)