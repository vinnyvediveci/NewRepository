import re

string = "Peter Piper picked a pack of pickled peppers"

pattern = re.compile("[pP]\w*r(?=\s)")

print(re.findall(pattern, string))


#
#
#
#
#
#
#