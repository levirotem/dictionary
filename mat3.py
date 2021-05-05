
import json
import os
    
def readfile():
    chat= open("C:/Users/levir/matala3/noya.txt", encoding='utf-8')
    dictionar(chat)
    

def dictionar(chat:str): 
    dicid=dict()
    diction=dict()
    num=1
    lst=list()
    diction2=dict()
    linenum=1
    c_line=0
    metadata=dict()
    for line in chat:
        line=line.rstrip()
        start=line.find('-')
        end=line.find(':',start)        
        if end>0:    
            name=line[start+1:end]
            if name not in dicid:
                dicid[name]=num
                num=num+1
            diction['datetime']= line[0:15]
            diction['id']=dicid[name]
            tmp = line.split(':')
            diction['text'] = tmp[2].strip()
            # print(diction['text'])
            lst.append({ 'id' : str(diction['id']), 'date': diction['datetime'] , 'text': diction['text'].strip()})
        if c_line == linenum:
            # print(line)
            sta2=line.find('"')
            end2=line.find('"',sta2+1)
            metadata['chat_name']=line[sta2+1:end2]
            chat_name= metadata['chat_name']
            metadata['creation_date']=line[0:15]
            sta=line.find('+')
            metadata['creator']=line[sta+1:]
        if end<0 and '-' not in line : 
            diction['text']= (diction['text']+line).strip()
            lst.append(diction.copy())
        c_line += 1
    metadata['num_of_participants']=len(dicid)
    # print(dicid)
    diction2={'Massege':lst,'metadata':metadata}
    

    
#    json_string = json.dumps(lst2)
    son_string = json.dumps(diction2,indent=4, ensure_ascii=False)

    with open(os.path.join('C:/Users/levir/matala3',chat_name+".txt"), 'w',encoding='utf-8') as f:
        f.write(son_string)

readfile()