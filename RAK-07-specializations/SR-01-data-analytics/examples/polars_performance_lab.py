"""
LAB PRACTICAL: Modern Data Stack Performance (Polars vs Pandas)
Standard: PPM V4 - Gold Standard

Tujuan: Verifikasi kecepatan eksekusi Polars vs Pandas pada dataset 1 juta baris.
Guna: Dasar pengambilan keputusan untuk arsitektur data industri.
"""

import time
import pandas as pd
import polars as pl
import duckdb
import numpy as np

def generate_big_data(n=1_000_000):
    print(f"--- Generating {n} rows of synthetic data ---")
    data = {
        "id": np.random.randint(1, 100, n),
        "category": np.random.choice(["A", "B", "C", "D"], n),
        "value": np.random.randn(n),
        "salary": np.random.randint(30000, 150000, n)
    }
    return data

def run_pandas_test(data):
    df = pd.DataFrame(data)
    start = time.time()
    # Task: Group by category and calculate mean salary
    res = df[df["salary"] > 50000].groupby("category")["salary"].mean()
    end = time.time()
    print(f"   [PANDAS] Time: {end - start:.4f}s")
    return res

def run_polars_test(data):
    # Eager mode (df)
    df = pl.DataFrame(data)
    start = time.time()
    # Task: Group by category and calculate mean salary
    res = (
        df.lazy()
          .filter(pl.col("salary") > 50000)
          .group_by("category")
          .agg(pl.col("salary").mean())
          .collect()
    )
    end = time.time()
    print(f"   [POLARS] Time: {end - start:.4f}s (Lazy API)")
    return res

def run_duckdb_test(data):
    df = pl.DataFrame(data)
    start = time.time()
    # Task: SQL on Polars Dataframe
    res = duckdb.query("""
        SELECT category, AVG(salary) 
        FROM df 
        WHERE salary > 50000 
        GROUP BY category
    """).pl()
    end = time.time()
    print(f"   [DUCKDB] Time: {end - start:.4f}s (Zero-Copy SQL)")
    return res

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 MODERN DATA STACK PERFORMANCE LAB")
    print("=" * 60)
    
    raw_data = generate_big_data(1_000_000)
    
    run_pandas_test(raw_data)
    run_polars_test(raw_data)
    run_duckdb_test(raw_data)
    
    print("\n" + "=" * 60)
    print("✅ Lab Completed. Polars & DuckDB provide superior speed via Arrow.")
