
def my_functy(string):
    wordie = string.split()
    wordie.reverse()
    pass

my_string = input()
my_words = my_string.split()
my_words.reverse()
my_results = ' '.join(my_words)
print(my_results)