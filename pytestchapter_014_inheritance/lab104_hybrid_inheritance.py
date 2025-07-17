"""
Hybrid Inheritance
Combination of single, multilevel, multiple, heirarchical inheritance
"""

class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(A,B):
    pass
class E(C):
    pass
