# xrange() in Python 2:
# xrange() returns an iterator (an xrange object) instead of a list. It generates each number on-the-fly as you loop through it, without storing the entire sequence in memory.
# This makes xrange() more memory-efficient, especially for large ranges.
# You cannot directly index or slice xrange() because it doesn't produce a list.
# Example usage:

# range() in Python 3:
# In Python 3, range() was optimized to work like xrange() from Python 2, producing a range object that generates numbers on demand.
# xrange() was removed in Python 3, and range() now behaves as a memory-efficient generator.
# This means in Python 3, you can use range() for both small and large sequences without memory issues.