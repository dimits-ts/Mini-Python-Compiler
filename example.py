#! /usr/bin/env python
#A miniPython example

import a_module.submodule as name1, a_module2.submodule2 as name2
from another_module import member1 as name3, member2 as name4

def func(param1, param2 = 3, param3 = "hello"):
	int1 = 1 + 2 * 3 - 4 ** 5 / 6 + 7 % 8
    if not int1 > 5 and param3 == "hello":
        int1 -= (1 + 2) * 3 - 4 ** (5 / (6 + 7)) % 8
    int2 = len(max(1, 'a', "b")) + id2[id1.func1(arg1, arg2)]
    assert int1, int2
    func(param1, param2 + 5, ["hi", 'hello'])
    print "the string 'compilers' has length", len("compilers")
	return int1 / 3

while true:
    my_int = func(1, "hello", name3)
    for x in name4:
        if x > 3 or false:
            print x, None

int_array = [1, 2, 3]
int_array[0 + 1 * 2] = 10
print int_array
