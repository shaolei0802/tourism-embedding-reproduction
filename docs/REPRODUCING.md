# Reproduction workflow

## 1. Inspect archived evidence without network access

Run `python scripts/verify_package.py` from the repository root. The script uses the Python standard library to verify all listed checksums, notebook syntax, and AOI/configuration consistency. If you edit a file, checksum verification will intentionally fail until you document the change and regenerate the checksum list. Original bytes are separately recorded in `metadata/original_files.json`.

Open the TIFFs in a GIS and use their embedded CRS. They are 8-bit RGBA visualizations with padding around the AOI. Do not compute distance means, change thresholds, or changed areas from RGB values or from all nontransparent pixels. Use the GeoJSON polygons to display the analysis boundary.

The Hainan heatmap side panel has a conflicting area label; exported coordinates define the actual approximately 48.36 km² AOI. The latest 2025 Hainan monthly screenshot has no loading message but retains vertical texture over water. Screenshot month labels are not a complete record of satellite acquisition dates. Matching-month display is a visual cross-check, not independent reference validation.

## 2. Install a new environment

The `requirements.txt` lower bounds for numpy/zarr follow the exported notebook. Other versions are not pinned. A Python 3.10+ virtual environment is suggested because the export uses modern type syntax. The historical environment is unknown; successful installation is not a claim of a tested historical lockfile.

```bash
python -m venv .venv
# Activate the environment for your operating system (see README).
python -m pip install -r requirements.txt
python tests/test_score_logic.py
```

## 3. Read the live archive and compute new outputs

```bash
python scripts/reproduce.py --case beijing
python scripts/reproduce.py --case hainan
```

The script executes the input, import/GIS, analysis, and plotting definitions from the original notebooks. It skips their install and runtime cells and invokes the same load/compare functions explicitly. The two cases occupy a single UTM zone each. A new output folder is required for every run.

Each completed case produces:

| Output | Meaning |
|---|---|
| `*_distance_utmXX.tif` | Newly computed float32, one-band cosine distances with NaN NODATA |
| `*_notebook_plot.png` | Newly computed notebook visualization saved at 300 dpi |
| `*_notebook_plot.pdf` | PDF plot with raster data layer and vector annotations where supported |
| `run_metadata.json` | AOI/year/dimension settings, source endpoint, time, hashes, valid fractions, and score summaries |
| `environment_freeze.txt` | Versions from the actual successful rerun environment |

These do not reconstruct the exact browser basemap screenshot. Their numerical values have not been compared against a browser raw score layer. Saving at 300 dpi does not increase the spatial resolution of the original 10 m data.

## 4. Review and retain results

Inspect the AOI alignment, NODATA areas, valid pair fraction, raw score distribution, and raster CRS. A nonzero valid fraction does not establish full regional coverage. Archive the outputs, the source notebooks, the exact commit, and `environment_freeze.txt` together. If the archive is mutable, preserve a local source subset or upstream provenance identifiers where available and permitted; the present package contains no source embedding snapshot.

To share successful outputs, attach a dedicated ZIP to a GitHub Release. `outputs/` is ignored by default to prevent accidentally committing large or partial runs. Add a dated status entry to `metadata/verification_report.json` only after the run succeeds. Keep the initial assembly status in release history.

## 5. Troubleshooting

- Missing module: verify the intended virtual environment is active; install requirements with that environment's `python -m pip`.
- Network / source access error: check access to `https://data.source.coop`; do not substitute unrecorded data or treat an error as zero change.
- Year unavailable / no valid pair: source availability or coverage may differ. Retain the error and run date; do not replace absent pixels with zeros.
- Zarr/API incompatibility: record exact versions and source error. Review upstream documentation before changing the exported code, retain an unmodified original, and describe any patch. On zarr 3.3+, upstream documents a small-read optimization using `array.sharding_coalesce_max_gap_bytes = 0`; it is not silently added by this runner.
- Memory constraints: do not silently shrink an AOI or alter dimensions. Record any separately labeled sensitivity analysis.

## 6. Interpretation

No step above supplies independent labels, a confusion matrix, positional error estimates, or tourism attribution. Statistical summaries are descriptive of embedding dissimilarity, not detection accuracy. A rigorously validated paper would require a separately designed reference assessment.

## Coverage update checked 27 October 2026

The upstream dataset page now reports completed global coverage for 2021–2025. This supersedes the initial-release 2023–2025 global-coverage description; it does not replace an AOI-specific valid-pair measurement. The source archive is not frozen in this package.
