dict1={'a':1,'b':2}
dict2={'b':3,'c':4}
merge_dict=dict1.copy()
merged_dict.update(dict2)
print("merged Dictionary (using update()):",merged_dict)
dict1={'a':1,'b':2}
dict2={'b':3,'c':4}
merged_dict={**dict1,**dict2}
print("merged dictionary (using dictionary unpacking):",merged_dict)

