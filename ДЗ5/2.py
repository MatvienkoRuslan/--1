with open("file_1.txt") as fp:
    tmp=[]
    for stri in fp.readlines():
        ls=len(stri)
        stri=stri[0:ls-1]
        v=eval(stri)
        tmp.append(stri+"="+str(v))
with open("file_1.txt","w") as fo:
    for s in tmp:
        fo.write(s+"\n")