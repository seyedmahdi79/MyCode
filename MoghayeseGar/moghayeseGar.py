def compare(string1, string2):
    while string1 and string2:
     if ord(string1[0])-97<ord(string2[0])-97:
        string1=string1[1:]
        string1=string1[::-1]
        if string1:
           string2=string2[::-1]
     elif ord(string2[0])-97<ord(string1[0])-97:
         string2=string2[1:]
         string2=string2[::-1]
         if string2:
            string1=string1[::-1]
     elif ord(string2[0])-97==ord(string1[0])-97:
         string2=string2[1:]
         string1=string1[1:]
         if string1:
           string2=string2[::-1]
         if string2:
            string1=string1[::-1]
    if string1==string2=='':
        return 'Both strings are empty!'
    elif string1=='':
        return string2
    elif string2=='' :
        return string1












