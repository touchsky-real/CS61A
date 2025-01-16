def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branches),"branches must be tree"
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) <1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n<=1:
        return tree(n)
    else:
        left,right = fib_tree(n-2),fib_tree (n-1)
        return tree(label(left)+label(right),[left,right])

def count_leaves(t):
    """Count the leaves of a tree"""
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])

def leaves(tree):
    """Return a list containing the leaf labels of tree"""
    if is_leaf(tree):
        return [label(tree)]
    else:
        # return sum(List of leaf labels for each branch,[])
        return sum([leaves(b) for b in branches(tree)],[])


def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented"""
    if is_leaf(t):
        return tree(label(t)+1)
    else:
        return tree(label(t),[increment_leaves(b) for b in branches(t)])


# def increment(t):
#     """Return a tree like t but with all labels incremented"""
#     if is_leaf(t)
#         return tree(label(t)+1)
#     else:
#         return tree(label(t)+1,[increment(b) for b in branches(tree)])

def increment(t):
    """Return a tree like t but with all labels incremented
    Same as the above verson code"""
    return tree(label(t)+1,[increment(b) for b in branches(tree)])

def print_tree(t, indent=0):
    print("   "*indent+str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)

def print_sums(t,so_far):
    """Print sums of the labels from root label to leaves"""
    so_far = so_far + label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b,so_far)

