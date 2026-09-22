# Data preperation

**Week 3 deliverable.** GeoDv Lab Africa, Cohort One.
Author: Devotha Kafuku

What I reprojected, what I clipped, what I checked and what I fixed.

---

## 1. Coordinate system decision

**Working CRS:** EPSG:32736

**Why this one: The coordinate system changed from geographical coordinate to projected because I want to measure distance, area, so the projected one (EPSG:32736) is in meter and under the area of study zone UTM36s.

| Dataset | CRS as downloaded | CRS projected | Operation |
|---|---|---|---|
| Boundary | EPSG:4326 | EPSG:32736 | Reprojected |
|Settlement extent | EPSG:4326 | EPSG:32736 | Reprojected |
| Waterway | EPSG:4326| EPSG:32736 | Reprojected |
| Elevation | EPSG:4326 | EPSG:32736 | Reprojected |

## 2. Clipping to the study area

- **Boundary used:** Mbugani-Mirongo-Pamba boundary

### Settlement extent data
-**Features before clipping:** 667240
-**Features after clipping:** 4

### Waterway data
#### rivers

- **Features before clipping:** 3
- **Features after clipping:** 3

No change observed 

#### streams
- **Feature before clipping:** 8
- **Features after clipping:** 2

## 3. The five quality checks

| Check | Results | Action taken |
|---|---|---|
| Is the CRS what i think it is? | Yes | No action taken |
| Are there nulls in the fields I need | No | No action needed |
| Are there dubplicate features? | No | No action needed |
| Is the geometry valid? | Yes | Accepted |
| Does coverage span the whole study area? | Yes | Accepted |

## 4. Problem found, and what I did

**Problem: Accuracy of Land Area of study**

The geometry downloaded from Hummaritarian website (published 2018) indicate large land area compared to the land area published during 2022 census.

**Solution (what i did)**

I proceed with the downloaded one for learning purpose while looking for the published one from the Tanzania responsible authority.

## 5. The analysis-ready output

- **File:** "D:\GeoDev\My-project\Data\Processed\Boundary\mbugani_mirongo_pamba_utm36S.gpkg"
- **Format:** Geopackage
- **CRS:** EPSG:32736 UTM36s
- **Features:** 3, polygon
- **Columns:** ET_ID (integer64), ADM0_EN (text), ADM0_SW (text), AADM0_PCODE (text), ADM1_EN (text), ADM2_EN (text), ADM2_PCODE (text), ADM3_3EN (text), ADM_PCODE (text)
- **Produced by:** "manually in QGIS"


**File:** "D:\GeoDev\My-project\Data\Processed\Settlement\settlement_mbgn_mirong_utm36s.gpkg"
- **Format:** Geopackage
- **CRS:** EPSG:32736 UTM36s
- **Features:** 4, line
- **Columns:** OBJECTID (integer64), country (text), iso3 (text), building_count (interger64), building_area (Decimal), type (text), probability (Decimal), Date (text), source (text), mgrs_code (text)
- **Produced by:** "manually in QGIS"


**File:** "D:\GeoDev\My-project\Data\Processed\Waterway\water_river_mbugn_mirong_pamba_utm32S_clipped.gpkg"
- **Format:** Geopackage
- **CRS:** EPSG:32736 UTM36s
- **Features:** 3, line
- **Columns:** full_id (text), osm_id (text), osm_type (text), waterway (text), tunnel (text), layer (text), name (text)
- **Produced by:** "manually in QGIS"


**File:** "D:\GeoDev\My-project\Data\Processed\Waterway\water_stream_mbugn_mirong_pamba_utm32S_clipped.gpkg"
- **Format:** Geopackage
- **CRS:** EPSG:32736 UTM36s
- **Features:** 2, line
- **Columns:** full_id (text), osm_id (text), osm_type (text), waterway (text), tunnel (text), layer (text)
- **Produced by:** "manually in QGIS"

**File:** "D:\GeoDev\My-project\Data\Processed\Elevation\STRM_dem_projec_utm36s_clipped.tiff"
- **Format:** tiff file
- **CRS:** EPSG:32736 UTM36s
- **Produced by:** "manually in QGIS"

## CRS and preparation
- All source layers arrived in EPSG:4326
- Study area: mbugani_mirongo_pamba, extracted from humdata.org (tza_admbnda_adm3)
- All layers reprojected to EPSG:32736 and clipped to the study area
- Area check: mbugani_mirongo_pamba 7.4km2, different with published figure
- Working files in data/processed/, raw files untouched

---

**Status"** Week 3 complete: Coordinate systems and preparing data


