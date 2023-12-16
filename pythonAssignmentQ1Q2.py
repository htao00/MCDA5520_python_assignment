
###### Question 1 ######
def stack(list, op, el=None):
    if op == 'add' and el != None:
        nlist = [el]
        nlist.extend(list)
        list = nlist
    elif op == 'remove':
        del list[0]
    else:
        print('operation not supported')
    return list

def queue(list, op, el=None):
    if op == 'add' and el != None:
        list.append(el)
    elif op == 'remove':
        del list[0]
    else:
        print('operation not supported')
    return list


###### Question 2 ######
import pandas as pd
df = pd.read_csv('titles.csv')
df['vowels'] = df['title'].str.count(r'[aeiouAEIOU]')
print(df)
