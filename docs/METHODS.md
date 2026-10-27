# Implemented method

Inputs are the two exact AOIs, years `[2021, 2025]`, `VIEW = pair`, and the first 64 stored dimensions. Source archive: OlmoEarth v1.3 embeddings, identified by exported TIFF metadata as store v2. The manuscript's full Appendix A gives the same boundaries and export provenance.

1. Read int8 embedding values on the archive's 10 m UTM grid, using 256-pixel-aligned windows.
2. Dequantize each component: `z = sign(q/127.5) * abs(q/127.5)**2`.
3. Estimate four mean vectors indexed by global row/column parity in each loaded regional window and year. Subtract each class mean's deviation from the four-class average. The sampler excludes first-component NODATA values; insufficient samples return zero offsets. Parameters: `PARITY_SAMPLE_CELLS = 16384`, `PARITY_MIN_PIXELS = 64`.
4. Normalize corrected vectors by `max(L2_norm, 1e-12)`.
5. Compute `distance = 1 - sum(u_2021 * u_2025)` per location.
6. Score only AOI pixels with valid vectors in both years. A vector whose 64 components all equal `-128` is missing. Other score locations remain NaN.

The parity estimate uses the loaded regional window, not only AOI pixels. Changing the AOI can change that window and correction; sensitivity has not been evaluated. This package intentionally preserves the supplied implementation rather than modifying its scientific assumptions.

The original code's archive grid transform is `(10, 0, 0, 0, -10, 9502720)`, width `98304`, height `1867776`. It uses `GRID_TRANSFORM * Affine.translation(x0, y0)` for each loaded window. New raster output uses that transform and EPSG:32600+zone; both included AOIs are in the northern hemisphere.

The notebook's plot range `[0, 0.5]` is a display range only. Scores beyond that range can occur and are retained in the raw score raster. No changed-area threshold is defined. Browser screenshots have a different palette and use 60% opacity in Beijing versus 100% in Hainan. Original browser exports are visualization evidence, not the new runner's numeric output.
