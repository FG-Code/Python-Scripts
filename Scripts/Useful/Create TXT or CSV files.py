var = ['1','2','3']


with open('content.csv', 'w') as f:
    for v in var:
        f.write(v + '\n')

f.close()

with open('content.txt', 'w') as f:
    for v in var:
        f.write(v + '\n')

f.close()
