my_dict={'key1': 'value1', 'key2': 'value2', 'key3':'value3'}
value1= my_dict['key1']

dict_keys=my_dict.keys() #return a list of all the keys in the dictionary
dict_valuse=my_dict.values() #return a list of all the values in the dictionary

get_value=my_dict.get('key4')
dict_item=my_dict['key4']
print(get_value) # print "None"
print(dict_item) # print