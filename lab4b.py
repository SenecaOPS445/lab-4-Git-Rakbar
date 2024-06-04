#!/usr/bin/env python3

# #s1 = {'Prime', 'Ix', 'Secundus', 'Caladan'}
# #s2 = {1, 2, 3, 4, 5}
# #s3 = {4, 5, 6, 7, 8}
# set1 = set(range(1,10))
# set2 = set(range(5,15))


# def join_sets(s1, s2):
#     # join_sets will return a set that contains every value from both s1 and s2
#     return (s1.union(s2))
        
# def match_sets(s1, s2):
#     # match_sets will return a set that contains all values found in both s1 and s2
#     return (s1.intersection(s2))


# def diff_sets(s1, s2):
#     # diff_sets will return a set that contains all different values which are not shared between the sets
#     return (s1.symmetric_difference(s2))



# if __name__ == '__main__':
# #    set1 = set(range(1,10))
# #    set2 = set(range(5,15))
#     print('set1: ', set1)
#     print('set2: ', set2)
#     print('join: ', join_sets(set1, set2))
#     print('match: ', match_sets(set1, set2))
# print('diff: ', diff_sets(set1, set2))



#!/usr/bin/env python3

def join_lists(l1, l2):
    # join_lists will return a list that contains every value from both l1 and l2
    return list(set(l1) | (set(l2)))

def match_lists(l1, l2):
    # match_lists will return a list that contains all values found in both l1 and l2
    return list(set(l1) & (set(l2)))

def diff_lists(l1, l2):
    # diff_lists will return a list that contains all different values, which are not shared between the lists
    return list(set(l1) ^ (set(l2)))

if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))