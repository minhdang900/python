# asterisk in function call
def single_asterisk(*args):
    print('>>output', args)

def double_asterisk(**args):
    print('>>output',args)

def combine_asterisk(*t, **d):
    print('>>output',t, d)