# Figure 3 provenance and rights audit

Retained Hainan tile logs in the supplied Applied Geography supplementary archive contain direct requests to Esri's World_Imagery/WMTS endpoint. Two Wayback release IDs occur: 56102 and 63116. The 56102 release is identified in Esri's official wayback-core documentation as World Imagery (Wayback 2023-12-07). The release date is a basemap publication date, not the capture date of each image. The final Figure 3 composition's exact selected release, fallback behavior for failed tile requests, underlying capture dates/providers and publication permission remain to be confirmed from the compositor/tile manifest and Esri terms.

The analytical layers are separate: 2025 Sentinel-2 L2A items accessed through Microsoft Planetary Computer, author-derived NDWI/SCL functional-context masks, and author-generated disagreement candidates. These are analytical proxies, not official planning or cadastral boundaries.

No raw Esri tile imagery is committed to this repository. Do not assign a specific satellite provider or capture date without Wayback metadata lookup for the exact coordinates, zoom and selected release. Confirm Esri's current publication/reuse terms and required attribution before journal submission.

Official Esri technical reference: https://github.com/Esri/wayback-core