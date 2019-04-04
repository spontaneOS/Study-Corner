# Unpacking list in variables
p = (10, 20)
a, b = p
print(a, b)
print("----------------------------------------------------------------------------------------")
# Nested unpacking
data = ['AMD', 100, 26, (2019, 4, 1)]
symbol, num, price, date = data
print("{} of {} at price {} on day {} of month {} in year {}.".format(num, symbol, price, date[2], date[1], date[0]))
print("----------------------------------------------------------------------------------------")
# Unpacking works on strings too
s = "Hello"
a, b, c, d, e = s
print(a, b, c, d, e)
print("----------------------------------------------------------------------------------------")
# Unpacking Elements from Iterables of Arbitrary Length
# You need to unpack N elements from an iterable, but the iterable may be longer than N elements, causing a “too many values to unpack” exception.
def drop_first_last(grades):
    first, second, *last = grades
    return (sum(last)/len(last))
print(drop_first_last((10, 100, 200, 300, 20)))
print("----------------------------------------------------------------------------------------")
records = [('a', 1, 2), ('b', 4, 5, 6)]
for tag, *args in records:
    if len(args) > 2:
        print("Tag : ", tag)
print("----------------------------------------------------------------------------------------")
data = ['AMD', 100, 26, (2019, 4, 1)]
symbol, *_, (year, *_) = data
print(symbol, year)
print("----------------------------------------------------------------------------------------")
# You want to keep a limited history of the last few items seen during iteration or during some other kind of processing.
from collections import deque
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


