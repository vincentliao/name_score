
import re

expr = re.compile(r'"([A-Z]+)"')
name_list = expr.findall(open('names.txt', 'r').read())
name_order_by_alphabet = sorted(name_list)

base = ord('A')
total_sum = 0
for idx, name in enumerate(name_order_by_alphabet):
	total_sum += (sum([ord(x)-base+1 for x in name]) * (idx+1))

print total_sum
