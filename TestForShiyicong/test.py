import gc
import sys

print(sys.version)
print(gc.is_tracked(1))
print(gc.is_tracked("nihao"))
print(gc.is_tracked([]))
