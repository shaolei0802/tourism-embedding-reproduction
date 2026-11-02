# Reproduction guide

Remote data: OlmoEarth v1.3 Zarr store at Source Cooperative (`s3://olmoearth/olmoearth-v1-3-embeddings/embeddings.zarr`; HTTPS endpoint `https://data.source.coop`). Retained metadata reports Zarr v3, int8, shape `(9,128,1867776,98304)`, axes `(time,band,y,x)`, years 2017–2025 and chunks `(1,64,256,256)`. Primary comparison years: 2021 and 2025.

## Environment
Use Python 3.12 and the versions recorded in each run archive's environment/metadata. One Hainan run lists NumPy 2.5.4, Zarr 3.4.2, obstore 0.12.1, Matplotlib 3.11.2, pyproj 3.8.0, rasterio 1.4.3 and Shapely 2.2.0. A separate run may list different versions; inspect each archive.

## Re-run
1. Ensure access to the remote Source Cooperative archive.
2. Open the case-specific notebook and execute from top to bottom in its own kernel.
3. Keep the four conditions separate. Preserve signed-square dequantization, normalization, parity logic and zero-norm exclusion.
4. Compare dimensions only on identical valid pixels.
5. Export score rasters, masks, arrays, logs, environment freeze, run metadata and checksums.
6. Compare outputs against the consolidated CSV in results/.

The original run archives are stored outside this GitHub folder due their size and third-party data redistribution review. No new remote run was performed during package assembly. These sensitivity statistics do not establish accuracy, causal effects or governance effectiveness.