import json
alphabet=[symb for symb in 'abcdefghijklmnopqrstuvwxyz']
let2int={let:i for i,let in enumerate(alphabet)}
int2let={i:let for i,let in enumerate(alphabet)}
vocab={'let2int':let2int,'int2let':int2let}

with open ('vocab/vocab.json','w') as out:
    json.dump(vocab,out)

