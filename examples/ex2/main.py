from Manufaktur import process
from Manufaktur import dir
from Manufaktur import json
import os
import shutil

xs = process.wone_to_many("./input", dir.list_dir)
copyDir = lambda x: dir.copy_dir("./input/" + x, "./output/" + x)
process.producer_consumer(xs, copyDir)

# ys = list(range(4, 20))
# makeDir = lambda x: dir.create_dir("./input/test" + str(x))
# process.many_to_many(ys, makeDir)

x = json.str_to_json('{"foo":"bar"}')
print(type(x))
y = json.json_to_str(x)
print(y)
