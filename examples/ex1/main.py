from Manufaktur import process
from Manufaktur import dir

f = dir.list_dir
xs = process.one_to_many(".", f)
ys = process.many_to_many(xs, print)

f = dir.list_dir
zs = process.one_to_many("..", f)
print("-" * 40)
print(zs)
print("-" * 40)


def print2(x):
    print(x)
    return x


pp = lambda x: x


process.producer_consumer(zs, pp)
