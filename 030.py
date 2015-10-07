print(sum(filter(lambda x: x == sum(map(lambda x: int(x)**5, str(x))), range(10, 6*9**5+1))))
