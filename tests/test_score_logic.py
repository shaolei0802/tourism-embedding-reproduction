"""Offline synthetic checks of original score functions, not research validation."""
import ast,json
from pathlib import Path
import numpy as np
root=Path(__file__).resolve().parents[1]
nb=json.loads((root/'notebooks/beijing_compare_2021_2025.ipynb').read_text())
source=''.join(nb['cells'][8]['source'])
ns={'np':np,'NODATA':-128,'VIEW':'pair','YEARS':[2021,2025]}
exec(compile('from __future__ import annotations\n'+source,'original_analysis_cell','exec'),ns)
x=np.zeros((2,64,2,2),dtype=np.int8);x[:,0,:,:]=100
x[:, :, 0, 0]=-128
inside=np.ones((2,2),bool);inside[1,1]=False
s=ns['score_years'](x,inside,0,0)
assert np.isnan(s[0,0]) and np.isnan(s[1,1])
assert np.allclose(s[np.isfinite(s)],0,atol=1e-6)
x[1,:,0,1]=0;x[1,1,0,1]=100
s=ns['score_years'](x,inside,0,0)
assert np.isclose(s[0,1],1,atol=1e-6)
assert np.isclose(s[1,0],0,atol=1e-6)
x[1,:,1,0]=-128
s=ns['score_years'](x,inside,0,0)
assert np.isnan(s[1,0])
print('PASS: identical vectors, orthogonal vectors, AOI mask, and missing-year masking. This is not empirical accuracy validation.')
