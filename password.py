# python3 code
# CoE 135 - Random Password
# ===================================

import string
import random

# ===== Generates password of length 5 ====
def create():
	chars = string.ascii_letters + string.digits;
	return ''.join(random.choice(chars) for _ in range(5));


# ===================================
# Code and info gotten from these websites:
# https://www.practicepython.org/solution/2014/06/06/16-password-generator-solutions.html
# ===================================
