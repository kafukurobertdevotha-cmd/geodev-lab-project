# **Spatial relationship and analysis**

**Week 4 deliverable.** GeoDv Lab Africa, Cohort One.
Author: Devotha Kafuku

Run one spatial operation relevant to my question

---
## **My question**

*Which settlement in Nyamagana sit in low-lying areas near rivers within 60m from river banks?*

## 1. CRS system check 

All layered were reprojected to UTM zone from EPSG:4326 to EPSG: 32736 UTM36s

**Working CRS:** EPSG:32736

## 2. My expectaction

After perfoming the spatial operation analysis based to my question (buffer & Intersection), I expect to have few features in the buffer zone compared to the total features found in my wards boudaries (Area of study)

## 3. Spatial operation as per my question

### 1. Buffer

My question need to buffer 60m from the edge of river banks

| Location | Area before buffer | Buffered area |
|---|---|---|
| Boundary | 7.441km2 | 0.623km2 |

*The buffered area is 8.37% of total boundary area*

### 2. Intersection

The intersection were done for settlement extent and buildings wthin my study area
**why** building?

*The settlement extent data of my area of study, building count is general (can not change even if we intersect the building count remain), I decided to building data to confirm.*

| Data | Total count | Total intersected | % of intersection |
|---|---|---|---|
| Settlement extent (building area) | 5.896km2 | 0.605km2 | 10.26 |
| Buildings | 17184 | 1720 | 10.0 |

**Note** The settlement extents data and buildings data have the same values. So, to use settlement extent (build-up area) is acceptable but this is valid for the settlement extent lied on built-up area and not other features.

## 4. The four quality checks

| Check | Results | Action taken |
|---|---|---|
| Does the output sit where I expected? | Yes | Accepted |
| Howm many rows? Does that match your expectaction from step 2? | Yes | Discussed in step 3 |
| Is features valid, is there any feature to use as verification manual? | Yes | The location of bridge which i know |
| Is there any feature with nothing means the operation did not full work? | No | The operation were fully works |


## 5. Settlement extent map after spatial operation analysis

![Study Area map](settlement_wards_map.png)

