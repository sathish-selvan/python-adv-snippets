from timeit import repeat
from operator import methodcaller

names : list[str] = ['saathish', 'nithish', 'ranjith']
starts_with_s : methodcaller = methodcaller("startswith","s")

warm_up: str = """
for i in range(3):
    ...
"""

method_caller_test: str = """
filter(starts_with_s,names)
"""

lambda_test: str = """
filter(lambda x: x.startswith('s'), names)
"""

warm_up_time : float = min(repeat(stmt=warm_up))
method_caller_test_time :  float = min(repeat(method_caller_test, globals=globals()))
lambda_test_time :  float = min(repeat(lambda_test, globals=globals()))

print(f"{method_caller_test_time =:.3f}")
print(f"{lambda_test_time =:.3f}")