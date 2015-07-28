from functools import reduce

product = lambda l: reduce(lambda x, y: x*y, l, 1)

text = open('p011.txt').read().replace(' ', '').replace('\n', '')
array = [int(text[2*i:2*(i+1)]) for i in range(len(text)//2)]
width = int(len(array)**0.5)

horizontal = {product(array[i:i+4]) for i in range(len(array)) if i%width <= width-4}
vertical = {product([array[i+n*width] for n in range(4)]) for i in range(len(array)) if i//width <= width-4}
ldiagonal = {product([array[i+n*(width+1)] for n in range(4)]) for i in range(len(array)) if i%width <= width-4 and i//width <= width-4}
rdiagonal = {product([array[i+n*(width-1)] for n in range(4)]) for i in range(len(array)) if i%width >= 3 and i//width <= width-4}

print(max(horizontal | vertical | ldiagonal | rdiagonal))
