import os, json
from flask import request


BLOCKCHAIN_DIR = 'records/'

def search():

    results = []
    if request.method == 'POST':
        id = request.form.get('search')

        with open(BLOCKCHAIN_DIR + id) as f:
            block = json.load(f)
            res = json.dumps(block, indent = 4, sort_keys=True)

            print(f'Block {id}: {res}')
            results.append({'block': id, 'results': res})

    return results

        #print(json.dumps(block, indent = 4, sort_keys=True))



if __name__ == '__main__':
    main()
