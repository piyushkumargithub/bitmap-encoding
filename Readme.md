# Bitmap Index with Run-Length Encoding

## Overview
A **Bitmap Index** is a space-efficient data structure commonly used in **columnar storage** and **database indexing**. It represents categorical data as **bitmaps** (binary arrays), enabling fast query performance and compression.

### How It Works
1️. **Bitmap Creation**: Each unique value in a column gets its own binary array. If a row contains that value, the corresponding bit is `1`, otherwise `0`.
2️. **Run-Length Encoding (RLE)**: To compress storage, consecutive `0`s and `1`s are stored as `(count, value)` pairs.
3️. **Efficient Querying**: Boolean operations (AND, OR, NOT) allow fast filtering without scanning entire datasets.

### Example
#### Given Dataset:
| Index | Category |
|-------|----------|
| 0     | A        |
| 1     | B        |
| 2     | A        |
| 3     | C        |
| 4     | B        |

#### Bitmap Representation:
```
A: [1 0 1 0 0]
B: [0 1 0 0 1]
C: [0 0 0 1 0]
```

#### RLE Compression:
```
A: [(1,1), (1,0), (1,1), (2,0)]
B: [(1,0), (1,1), (2,0), (1,1)]
C: [(3,0), (1,1), (1,0)]
```

### Advantages
**Space Efficient** – Bitmap indexing reduces storage compared to raw data.  
**Fast Query Performance** – Boolean operations allow quick filtering.  
**Compression** – RLE significantly reduces bitmap size for sparse data.  

### Applications
🔹 **Columnar Databases** (e.g., Apache Parquet, Apache ORC)  
🔹 **Data Warehousing**  
🔹 **OLAP (Online Analytical Processing)**  
🔹 **Indexing for Big Data Analytics**  

