def find_longest(string):
    spl = string.split(" ")
    longest = 0
    for word in spl:
        if len(word) > longest:
            longest = len(word)
    return longest

find_longest("The quick white fox jumped around the massive dog")   # 7
find_longest("Take me to tinseltown with you")                      # 10
find_longest("Sausage chops")                                       # 7
find_longest("Wind your body and wiggle your belly")                # 6
find_longest("Lets all go on holiday")                              # 7