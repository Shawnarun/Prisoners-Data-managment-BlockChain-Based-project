import json
import os
import hashlib

BLOCKCHAIN_DIR = 'records/'

def get_hash(prev_block):
    with open(BLOCKCHAIN_DIR + prev_block, 'rb') as f:
        content = f.read()
    return hashlib.md5(content).hexdigest()

def check_intergrity():
    files = sorted(os.listdir(BLOCKCHAIN_DIR), key=lambda x: int(x))

    results = []

    for file in files[1:]:
        with open(BLOCKCHAIN_DIR + file) as f:
            block = json.load(f)

        prev_hash = block.get('prev_block').get('hash')
        prev_filename = block.get('prev_block').get('filename')

        actual_hash = get_hash(prev_filename)

        if prev_hash == actual_hash:
            res = 'ok'
        else:
            res = 'Something was changed'

        print(f'Block {prev_filename}: {res}')
        results.append({'block': prev_filename, 'results': res})
    return results


def write_block(id, name, dob, nic, address, bio, cad, pd, fd, ed, rd):

    blocks_count = len(os.listdir(BLOCKCHAIN_DIR))
    prev_block = str(blocks_count)
    data = {

                    "ID":id,
                    "Name":name,
                    "D.O.B":dob,
                    "NIC": nic,
                    "Address": address,
                    "Bio": bio,
                    "CriminalActivityDetails": cad,
                    "PunishmentDetails": pd,
                    "FamilyDetails":fd,
                    "EntryDate": ed,
                    "Release Date": rd,
        "prev_block": {
            "hash": get_hash(prev_block),
            "filename": prev_block
        }
    }

    current_block = BLOCKCHAIN_DIR + str(blocks_count + 1)

    with open(current_block, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.write('\n')


def main():
    #write_block(caseid='002', name='Michale', age='40', height='6ft', weight='50kg', other='Rape')
    check_intergrity()

if __name__ == '__main__':
    main()
