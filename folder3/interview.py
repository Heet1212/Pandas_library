ip = {"a":1, "b":5, "c":{"a":3,"c":-5,"d":{"a":1,"b":3}}}
#op = {"a":5,"b":8,"c":-5,"d":0}


def got_value():
    for key, value in ip.items():
       ip[key].append(value)
        
    

for keyke, value in ip.items():

    if type(value)!='int':

