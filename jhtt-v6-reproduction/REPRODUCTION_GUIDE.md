# Reproduction Guide

## 1. Data source and archive structure

The analyses use the OlmoEarth v1.3 embedding archive hosted by Source Cooperative.

- Zarr store: `s3://olmoearth/olmoearth-v1-3-embeddings/embeddings.zarr`
- HTTPS endpoint: `https://data.source.coop`
- Archive format: Zarr v3
- Data type: int8
- Array shape: `(9, 128, 1867776, 98304)`
- Dimension order: `(time, band, y, x)`
- Available years: 2017–2025
- Chunk shape: `(1, 64, 256, 256)`

The primary temporal comparison uses 2021 and 2025. The archive metadata and array structure should be checked against the upstream source before a new execution.

## 2. Software environment

Use Python 3.12 and inspect the environment metadata retained with each original run archive.

One Hainan run records the following software versions:

- NumPy 2.5.4
- Zarr 3.4.2
- obstore 0.12.1
- Matplotlib 3.11.2
- pyproj 3.8.0
- Rasterio 1.4.3
- Shapely 2.2.0

These versions describe the recorded Hainan run and should not be interpreted as a universally pinned environment for every Beijing and Hainan execution. Other runs may contain different package versions. Consult the corresponding environment metadata when reproducing a specific run.

## 3. Analytical configurations

Four analytical conditions are evaluated independently for each destination:

1. 64D without parity correction;
2. 64D with parity correction;
3. 128D without parity correction;
4. 128D with parity correction.

The 64D condition uses the first 64 components of the stored 128-component representation. It is not a separately trained embedding model.

The dimensionality and parity comparisons use common valid-pixel support to maintain a consistent spatial basis for comparison.

## 4. Reproduction procedure

1. Ensure access to the upstream Source Cooperative OlmoEarth v1.3 archive.
2. Open the corresponding destination-specific notebook:
   - `notebooks/beijing_parity_dimension_sensitivity_v2.ipynb`
   - `notebooks/hainan_parity_dimension_sensitivity_v2.ipynb`
3. Execute each notebook from top to bottom in its own Jupyter kernel.
4. Keep the four analytical conditions separate.
5. Preserve the original signed-square dequantization, normalization, parity-correction logic, and zero-norm exclusion implemented in the notebooks.
6. Apply the common valid-pixel mask when comparing dimensionality and parity configurations.
7. Export the resulting score rasters, masks, arrays, execution logs, environment information, run metadata, and checksums.
8. Compare the resulting numerical outputs with the consolidated results provided in `results/`.

The notebooks and original run-provenance records should be consulted for the implementation details and case-specific parameters. This guide does not substitute for those implementation records.

## 5. Run provenance and data availability

The public repository contains the experiment notebooks, consolidated numerical results, run-provenance register, and reproduction documentation.

The original large raw run archives are retained separately by the authors in the JHTT v6.2 internal reproduction package because of their size and third-party data redistribution considerations. They are not included in this public GitHub folder.

No new remote execution was performed during the assembly of this reproduction package. The reported sensitivity statistics are retained outputs from the documented runs.

No third-party Esri imagery tile payloads are redistributed. The Figure 3 imagery-source and publication-rights status is documented separately in `provenance/FIGURE3_PROVENANCE_AND_RIGHTS_AUDIT.md`.

## 6. Interpretation and limitations

The reported sensitivity statistics assess the numerical stability of spatial screening results under alternative embedding dimensionalities and parity-correction configurations.

They do not independently establish change-detection accuracy, causal effects, or tourism-governance effectiveness.

Reproduction from the public materials requires access to the upstream embedding archive and an appropriately configured software environment. Exact reproduction of the retained runs may additionally require access to the corresponding author-held run archives and their environment metadata.
