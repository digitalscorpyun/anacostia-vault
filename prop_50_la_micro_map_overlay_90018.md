---
id: 20251028090500
title: prop_50_la_micro_map_overlay_90018
category: civic_ops
style: CodeRitual
path: civic_ops/prop50_la_micro_map_90018
created: 2025-10-28
updated: 2025-10-28
status: draft
priority: high
summary: Zip-level overlay to show how Prop 50 changes congressional lines around 90018, Baldwin Hills, Inglewood, and Leimert Park/Africatown.
longform_summary: Visual receipt pack to rebut/sustain claims about Black-influence fragmentation in South LA under Prop 50. Produces side-by-side PNGs (current vs. Prop 50) with 90018 highlighted and neighborhood/city borders overlaid.
tags:
  - civic
  - california
  - prop50
  - redistricting
  - los_angeles
  - mapping
  - elections
cssclasses:
  - tyrian-purple
  - sacred-tech
synapses: []
key_themes:
  - representation
  - black_political_power
  - maps
  - data_viz
bias_analysis: |
  Maps inherently frame reality; this overlay centers Black political continuity against redistricting fragmentation claims.
grok_ctx_reflection: |
  Cartography as resistance—these boundaries aren't just lines but circuits of community power.
quotes: []
adinkra: nkyinkyim
linked_notes: []
aliases:
  - prop50_90018_overlay
---

## Purpose

Make a **receipts-first** micro‑map centered on **ZIP 90018** that overlays:

- Current **U.S. House** district(s) (2022–present)
    
- **Prop 50** proposed congressional district(s) for 2026–2030
    
- **City boundary: Inglewood** (Place polygon)
    
- **Neighborhood polygons:** Baldwin Hills & Leimert Park/Africatown (local boundary sources)
    
- **90018 ZCTA** outline & centroid label
    

Goal: Show at a glance whether Black hubs are **split or preserved**.

## Output

- `maps/prop50_la_90018_current.png`
    
- `maps/prop50_la_90018_prop50.png`
    
- `maps/prop50_la_90018_side_by_side.png` (optional composite)
    

## Data You’ll Need (drop into `assets/shapes/prop50_la/`)

> Use authoritative, public files; keep filenames as‑is for the script below.

1. **ZCTA (ZIP Code Tabulation Areas), California** — `tl_2024_06_zcta520.shp`
    
2. **Cities/Places, California** — `tl_2024_06_place.shp` (for Inglewood boundary)
    
3. **Neighborhoods (Baldwin Hills, Leimert Park/Africatown)** — LA GeoHub neighborhood GeoJSON (export to `la_neighborhoods.geojson`).
    
4. **Current U.S. Congressional Districts (118th)** — `tl_2024_us_cd118.shp` (filter to CA)
    
5. **Prop 50 Proposed Congressional Plan (SoCal)** — `prop50_congress_socal.geojson` (official release or mirrored GeoJSON). If statewide, name it `prop50_congress_ca.geojson`.
    

> Put everything under: `C:\Users\digitalscorpyun\sankofa_temple\Anacostia\assets\shapes\prop50_la\`

## Map Window (approx.)

South LA focus, tweak if needed:

- **lat:** 33.94 → 34.08
    
- **lon:** −118.38 → −118.25
    

## Runbook (Windows)

```powershell
# 1) Create env
py -m venv %ANACOSTIA_DEV%\venvs\mapops && ^
%ANACOSTIA_DEV%\venvs\mapops\Scripts\activate && ^
pip install --upgrade pip && ^
pip install geopandas shapely pyogrio matplotlib pillow

# 2) Run
python C:\Users\digitalscorpyun\sankofa_temple\Anacostia\civic_ops\scripts\render_prop50_la_90018.py
```

## Python (save as `civic_ops/scripts/render_prop50_la_90018.py`)

```python
import os
from pathlib import Path
import geopandas as gpd
from shapely.geometry import box
import matplotlib.pyplot as plt

VAULT = Path(r"C:\Users\digitalscorpyun\sankofa_temple\Anacostia")
SHAPES = VAULT/"assets"/"shapes"/"prop50_la"
OUTDIR = VAULT/"maps"
OUTDIR.mkdir(parents=True, exist_ok=True)

# --- Load data ---
zcta = gpd.read_file(SHAPES/"tl_2024_06_zcta520.shp").to_crs(4326)
places = gpd.read_file(SHAPES/"tl_2024_06_place.shp").to_crs(4326)
hoods = gpd.read_file(SHAPES/"la_neighborhoods.geojson").to_crs(4326)
cd118 = gpd.read_file(SHAPES/"tl_2024_us_cd118.shp").to_crs(4326)

# Prop 50 shape may be statewide or SoCal-only
try:
    prop50 = gpd.read_file(SHAPES/"prop50_congress_ca.geojson").to_crs(4326)
except Exception:
    prop50 = gpd.read_file(SHAPES/"prop50_congress_socal.geojson").to_crs(4326)

# --- Focus window ---
xmin, ymin, xmax, ymax = (-118.38, 33.94, -118.25, 34.08)
window = box(xmin, ymin, xmax, ymax)

# --- Filter layers ---
# 90018 ZCTA
z90018 = zcta[zcta['ZCTA5CE20'] == '90018']

# LA neighborhoods of interest (case-insensitive contains)
sel_names = {"baldwin hills", "leimert park", "africa town", "africatown"}
hoods['__name_low'] = hoods.iloc[:, hoods.columns.str.contains('name', case=False)].astype(str).apply(lambda s: s.str.lower())
# If multiple name columns exist, create a unified name field
hoods['name_any'] = hoods.apply(lambda r: next((str(r[c]).lower() for c in hoods.columns if 'name' in c.lower() and isinstance(r[c], str)), ''), axis=1)
hoods_sel = hoods[hoods['name_any'].apply(lambda n: any(k in n for k in sel_names))]

# Inglewood city boundary
inglewood = places[places['NAME'].str.lower() == 'inglewood']

# Crop everything to window (for speed and clean plot)
clip = lambda gdf: gpd.clip(gdf, gpd.GeoSeries([window], crs=4326))
cd118_w = clip(cd118[cd118['STATEFP'] == '06'])
prop50_w = clip(prop50)
inglewood_w = clip(inglewood)
hoods_w = clip(hoods_sel)
zcta_w = clip(zcta)
z90018_w = clip(z90018)

# --- Styling helpers ---
def plot_frame(ax, title):
    ax.set_title(title, loc='left', fontsize=12, weight='bold')
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.axis('off')

# --- CURRENT MAP ---
fig1, ax1 = plt.subplots(figsize=(8,8), dpi=200)
cd118_w.boundary.plot(ax=ax1, linewidth=1.2)
inglewood_w.boundary.plot(ax=ax1, linewidth=1.2, linestyle='--')
hoods_w.boundary.plot(ax=ax1, linewidth=1.0, linestyle=':')
zcta_w.boundary.plot(ax=ax1, linewidth=0.5)
z90018_w.boundary.plot(ax=ax1, linewidth=2.0)

# Labels
if not z90018_w.empty:
    c = z90018_w.geometry.iloc[0].centroid
    ax1.text(c.x, c.y, '90018', fontsize=10, weight='bold')

plot_frame(ax1, 'Current Congressional (118th) with 90018, Inglewood, Baldwin Hills/Leimert')
fig1.tight_layout()
fig1.savefig(OUTDIR/"prop50_la_90018_current.png")

# --- PROP 50 MAP ---
fig2, ax2 = plt.subplots(figsize=(8,8), dpi=200)
prop50_w.boundary.plot(ax=ax2, linewidth=1.2)
inglewood_w.boundary.plot(ax=ax2, linewidth=1.2, linestyle='--')
hoods_w.boundary.plot(ax=ax2, linewidth=1.0, linestyle=':')
zcta_w.boundary.plot(ax=ax2, linewidth=0.5)
z90018_w.boundary.plot(ax=ax2, linewidth=2.0)

if not z90018_w.empty:
    c = z90018_w.geometry.iloc[0].centroid
    ax2.text(c.x, c.y, '90018', fontsize=10, weight='bold')

plot_frame(ax2, 'Prop 50 Proposed Congressional (2026–2030) with 90018, Inglewood, Baldwin Hills/Leimert')
fig2.tight_layout()
fig2.savefig(OUTDIR/"prop50_la_90018_prop50.png")

print("Wrote:", OUTDIR/"prop50_la_90018_current.png")
print("Wrote:", OUTDIR/"prop50_la_90018_prop50.png")
```

## Legend (reading guide)

- **Thick square** = **90018 ZCTA**
    
- **Solid line** = Congressional district boundary (current or Prop 50)
    
- **Dashed line** = **Inglewood city** boundary
    
- **Dotted line** = **Neighborhoods** (Baldwin Hills, Leimert/Africatown)
    

## Receipts Checklist (for debate)

- Screenshot both PNGs and mark whether **90018** and **named neighborhoods** are **split across multiple seats** or remain within a single seat.
    
- Note **any shift** in which district number covers 90018 (e.g., CA‑37 → CA‑## under Prop 50).
    
- Point out that this is **U.S. House only**; city/county/LAUSD lines are **unchanged**.
    

## Troubleshooting

- If neighborhood polygons don’t load, verify LA GeoHub field names include a **name** column; adjust the `name_any` logic accordingly.
    
- If Prop 50 file is statewide, the script will handle it; if SoCal only, make sure the filename matches.
    
- For missing fonts on Windows, install a font that supports bold; matplotlib will fall back automatically.
    

## One‑line Sting (for socials)

Prop 50 tweaks **Congress**, not **Crenshaw**—here’s the line-dance over 90018.

Done. I dropped a Vault-ready note to the canvas with:

- strict YAML frontmatter + canonical paths
    
- a receipts-first runbook
    
- a Python script (GeoPandas) that outputs:
    
    - `maps/prop50_la_90018_current.png`
        
    - `maps/prop50_la_90018_prop50.png`
        

You just need to place the shapefiles/geojsons in `Anacostia/assets/shapes/prop50_la/` using the exact names shown. Run the two PowerShell lines in the note and you’ll get side-by-side receipts for 90018, Baldwin Hills, Leimert/Africatown, and Inglewood.

Want me to also prep a quick QGIS version (no code) and a social-ready composite with labels/arrows?