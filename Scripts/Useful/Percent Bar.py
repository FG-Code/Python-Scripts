
def multiple(m, n):

	a = range(n, (m * n)+1, n)
	
	print(*a)

m = 7
n = 8

multiple(m, n)

percent = int(input('percent;'))
def count_multiples(factor, maximum): 
    return maximum // factor
total = (count_multiples(5,percent))

end = 21 - total
start = total +1
bar = ''

for i in range(1, start):
    bar = bar + '-'

for i in range(1, end):
    bar = bar + '+'

print(percent)
print(bar)
