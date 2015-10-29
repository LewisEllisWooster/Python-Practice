name = raw_input("Enter file:")
handle = open(name)
lst=[]
dict_lst={}
for line in handle:
    if line.startswith("From "):
        lst.append(line.strip().split()[5].split(":")[0])
    else:
        continue
for i in lst:
    dict_lst[i]=dict_lst.get(i,0)+1
    #list comprehension with dictionaries
for k,v in sorted([(k,v) for k,v in dict_lst.items()]):
    print k, v
