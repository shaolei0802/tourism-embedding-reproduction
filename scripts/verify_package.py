"""Offline checks of archived inputs; does not test live cloud availability."""
from pathlib import Path
import json,hashlib,ast,csv,sys
ROOT=Path(__file__).resolve().parents[1]
def main():
    errors=[];count=0
    for line in (ROOT/'SHA256SUMS.txt').read_text().splitlines():
        digest,relative=line.split('  ',1);p=ROOT/relative
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=digest:errors.append(f'Checksum mismatch: {relative}')
        count+=1
    cases=json.loads((ROOT/'metadata/cases.json').read_text())
    for case,cfg in cases.items():
        nb=json.loads((ROOT/f'notebooks/{case}_compare_2021_2025.ipynb').read_text())
        ns={};exec(''.join(nb['cells'][4]['source']),ns)
        geo=json.loads((ROOT/f'aois/{case}.geojson').read_text())
        if geo['features'][0]['geometry']['coordinates']!=ns['AOI']:errors.append(f'AOI mismatch: {case}')
        for key in ['AOI','YEARS','VIEW','EMBEDDING_DIMS','STORE_URL','STORE_ENDPOINT']:
            if ns[key]!=cfg[key]:errors.append(f'Config mismatch: {case} {key}')
        for cell in nb['cells']:
            if cell['cell_type']=='code':
                text=''.join(cell['source'])
                if not text.lstrip().startswith('%pip'):ast.parse(text)
    print(json.dumps({'files_checked':count,'errors':errors,'cloud_rerun_performed':False},indent=2))
    return bool(errors)
if __name__=='__main__':sys.exit(main())
