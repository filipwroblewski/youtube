def reverse_words(s):
    arr = s.split()
    print(arr)
    arr.reverse()
    print(arr)
    return ' '.join(arr)


reverse_words("hello world!")	#"world! hello"
reverse_words("The greatest victory is that which requires no battle")	#battle no requires which that is victory greatest The
