#!/usr/local/bin/python3
from pprint import pprint
s1 = "dresen"
s2 = "spenden"

def lcs_mat(list1, list2):
    m = len(list1)
    n = len(list2)
    mat = [[0] * (n+1) for row in range(m+1)]
    for row in range(1, m+1):
        for col in range(1, n+1):
            if list1[row - 1] == list2[col - 1]:
            # if it's the same element, it's one longer than the LCS of the truncated lists
                mat[row][col] = mat[row - 1][col - 1] + 1
            else:
		# they're not the same, so it's the the maximum of the lengths of the LCSs of the two options (different list truncated in each case)
                mat[row][col] = max(mat[row][col - 1], mat[row - 1][col])
    return mat

def all_lcs(lcs_dict, mat, list1, list2, index1, index2):
    # if we've calculated it already, just return that
    if ((index1, index2) in lcs_dict): return lcs_dict[(index1, index2)]
    # otherwise, calculate it recursively
    if (index1 == 0) or (index2 == 0): # base case
	    return [[]]
    elif list1[index1 - 1] == list2[index2 - 1]:
	    # elements are equal! Add it to all LCSs that pass through these indices
	    lcs_dict[(index1, index2)] = [prevs + [list1[index1 - 1]] for prevs in all_lcs(lcs_dict, mat, list1, list2, index1 - 1, index2 - 1)]
	    return lcs_dict[(index1, index2)]
    else:
	    lcs_list = [] # set of sets of LCSs from here
	    # not the same, so follow longer path recursively
	    if mat[index1][index2 - 1] >= mat[index1 - 1][index2]:
		    before = all_lcs(lcs_dict, mat, list1, list2, index1, index2 - 1)
		    for series in before: # iterate through all those before
			    if not series in lcs_list: lcs_list.append(series) # and if it's not already been found, append to lcs_list
	    if mat[index1 - 1][index2] >= mat[index1][index2 - 1]:
		    before = all_lcs(lcs_dict, mat, list1, list2, index1 - 1, index2)
		    for series in before:
			    if not series in lcs_list: lcs_list.append(series)
	    lcs_dict[(index1, index2)] = lcs_list
	    return lcs_list


lcs = lcs_mat(s1,s2)
mapping = dict()
all_lcs(mapping, lcs, s1, s2, len(s1), len(s2))
pprint(mapping)
