"""Execute selected original exported notebook definitions; never overwrite originals."""
from pathlib import Path
import argparse, json, sys, hashlib, platform, subprocess
from datetime import datetime, timezone
ROOT = Path(__file__).resolve().parents[1]

def load_namespace(case):
    notebook = ROOT / 'notebooks' / f'{case}_compare_2021_2025.ipynb'
    nb = json.loads(notebook.read_text(encoding='utf-8'))
    import matplotlib
    matplotlib.use('Agg')
    ns = {'__name__': '__main__'}
    # Original cells: inputs, GIS/imports, score functions, plot functions.
    # Install, network loading, analysis, and show cells are intentionally not executed here.
    for index in (4, 6, 8, 10):
        cell = nb['cells'][index]
        if cell['cell_type'] != 'code':
            raise ValueError('Notebook layout changed; review cell selection.')
        exec(compile(''.join(cell['source']), f'{notebook.name}:cell{index}', 'exec'), ns)
    return ns, notebook

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', choices=['beijing', 'hainan'], required=True)
    parser.add_argument('--output', type=Path, help='New, nonexistent directory (default timestamped outputs directory).')
    args = parser.parse_args()
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    target = args.output or ROOT / 'outputs' / f'{args.case}_{stamp}'
    target.mkdir(parents=True, exist_ok=False)
    ns, notebook = load_namespace(args.case)
    import numpy as np
    import rasterio
    import matplotlib.pyplot as plt
    print('Reading live cloud archive; this can take time and requires internet access.', flush=True)
    archive = ns['open_archive'](ns['STORE_URL'], ns['STORE_ENDPOINT'])
    data = ns['load_embeddings_for_aoi'](archive, ns['AOI'], ns['YEARS'], ns['EMBEDDING_DIMS'])
    results = ns['compare_years'](data)
    summaries=[]
    for result in results:
        aoi=result.aoi
        scores=result.scores.astype(np.float32)
        x0,y0,_,_=aoi.bounds
        transform=ns['GRID_TRANSFORM'] * ns['Affine'].translation(x0,y0)
        # Newly computed values, not values decoded from the browser RGBA export.
        path=target/f'{args.case}_distance_utm{aoi.zone}.tif'
        with rasterio.open(path,'w',driver='GTiff',height=scores.shape[0],width=scores.shape[1],count=1,dtype='float32',crs=f'EPSG:{32600+aoi.zone}',transform=transform,nodata=np.nan,compress='deflate') as dst:
            dst.write(scores,1)
            dst.update_tags(SOURCE_NOTEBOOK=notebook.name,YEARS=json.dumps(ns['YEARS']),EMBEDDING_DIMS=str(ns['EMBEDDING_DIMS']),PRODUCT='New notebook rerun distance values; not original browser values')
        valid_years=[int(np.sum(aoi.inside & ~np.all(vals==ns['NODATA'],axis=0))) for vals in aoi.embeddings]
        count=int(np.isfinite(scores).sum());total=int(aoi.inside.sum())
        s=scores[np.isfinite(scores)]
        summaries.append({'utm_zone':aoi.zone,'aoi_pixel_count':total,'valid_pixels_per_year':dict(zip(map(str,ns['YEARS']),valid_years)),'valid_pair_pixels':count,'valid_pair_fraction':count/total if total else None,'mean_distance':float(s.mean()) if count else None,'min_distance':float(s.min()) if count else None,'max_distance':float(s.max()) if count else None,'quantiles_05_50_95':np.quantile(s,[.05,.5,.95]).tolist() if count else None,'output':path.name})
    # Save the original notebook plotting function with its palette and range.
    original_show=plt.show
    plt.show=lambda:None
    try:
        ns['plot_results'](results)
        fig=plt.gcf()
        fig.savefig(target/f'{args.case}_notebook_plot.png',dpi=300,bbox_inches='tight')
        fig.savefig(target/f'{args.case}_notebook_plot.pdf',bbox_inches='tight')
        plt.close(fig)
    finally:
        plt.show=original_show
    record={'case':args.case,'rerun_utc':datetime.now(timezone.utc).isoformat(),'notebook_sha256':hashlib.sha256(notebook.read_bytes()).hexdigest(),'python':sys.version,'platform':platform.platform(),'source':{k:ns[k] for k in ['STORE_URL','STORE_ENDPOINT','AOI','YEARS','VIEW','EMBEDDING_DIMS']},'zones':summaries,'interpretation':'Descriptive embedding dissimilarity; no accuracy, tourism causation, or changed-area validation.'}
    (target/'run_metadata.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    env=subprocess.run([sys.executable,'-m','pip','freeze'],capture_output=True,text=True)
    (target/'environment_freeze.txt').write_text(env.stdout if env.returncode==0 else 'pip freeze failed; capture environment manually.\n',encoding='utf-8')
    print(f'Outputs: {target.resolve()}')
    print('A successful run is not proof of agreement with the browser or ground truth.')
if __name__=='__main__':
    main()
