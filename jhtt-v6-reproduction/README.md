# JHTT v6 Reproduction Materials

This folder supplements, and does not replace, the repository's earlier exploratory 0.1.0 materials. It contains the Beijing and Hainan parity/dimensionality sensitivity notebooks, summary tables and run provenance notes for the JHTT manuscript revision.

## Four conditions per destination
- 64D, parity correction off
- 64D, parity correction on
- 128D, parity correction off
- 128D, parity correction on

The 64D condition is the first 64 components of the stored 128-component representation, not a separately trained model. Rankings are compared on common valid-pixel support. The metrics are numerical sensitivity diagnostics, not independent change-detection accuracy.

## Evidence included here
- notebooks/: original v2 experiment notebooks.
- results/: consolidated CSVs (eight comparisons; Beijing n=40,946; Hainan n=483,597).
- provenance/: run register and Figure 3 source audit.

Large raw run archives are retained separately in the author-held JHTT v6.2 package. No Esri imagery tile payloads are redistributed in this repository. The existing repository release v0.1.0 is not the v6 reproduction release. A version-matched release and DOI remain pending.

See REPRODUCTION_GUIDE.md for the environment, data source, run archive map and limitations.