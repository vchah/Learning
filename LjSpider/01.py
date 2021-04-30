import re


size = '754.4平'
size2 = '74平'

print('pipline Size',re.findall(r'(\d+(\.\d+)?)', size)[0][0])
Size= float(re.findall(r'(\d+(\.\d+)?)', size)[0][0])
print(Size)