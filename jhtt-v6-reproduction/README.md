# JHTT v6 Reproduction Materials

This folder supplements, and does not replace, the repository's earlier exploratory v0.1.0 materials. It contains the Beijing and Hainan parity-correction and embedding-dimensionality sensitivity notebooks, consolidated results, and run-provenance documentation supporting the JHTT manuscript revision.

## Four analytical conditions per destination

- 64D, without parity correction
- 64D, with parity correction
- 128D, without parity correction
- 128D, with parity correction

The 64D condition uses the first 64 components of the stored 128-component representation; it is not a separately trained model. Spatial rankings are compared on common valid-pixel support. The reported metrics are numerical sensitivity diagnostics rather than independent measures of change-detection accuracy.

## Evidence included

- `notebooks/`: Original v2 experiment notebooks.
- `results/`: Consolidated CSV results covering eight destination–configuration comparisons (Beijing: n = 40,946; Hainan: n = 483,597).
- `provenance/`: Run-provenance register and Figure 3 imagery-source and rights audit.

Large raw run archives are retained separately in the author-held JHTT v6.2 internal reproduction package and are not included in this public repository. No third-party Esri imagery tiles are redistributed. The existing repository release v0.1.0 predates the JHTT-specific reproduction materials and should not be treated as their version-matched release. A dedicated release and persistent archival DOI for these materials remain pending.

See `REPRODUCTION_GUIDE.md` for the software environment, upstream data source, run-archive mapping, reproduction instructions, and methodological limitations.
