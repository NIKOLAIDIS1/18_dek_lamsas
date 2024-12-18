import subprocess
import pandas as pd
import re
from concurrent.futures import ThreadPoolExecutor

# Load the data
latencies_series = pd.read_csv('open_ai_1000_request.csv')


print("---------------------------- ")
print("print full statics for ")
print("100 measuremnt both http2 hhtp2 in given url test  writen in specific file ")

print("---------------------------- ")
# Print out the average latencies
print(
    f"""
    HTTP/2 LATENCY : {latencies_series['http2'].mean()}
    HTTP/3 LATENCY : {latencies_series['http3'].mean()}
    """
)

# Calculate additional metrics for HTTP/2
http2_metrics = {
    'mean': latencies_series['http2'].mean(),
    'median': latencies_series['http2'].median(),
    'std_dev': latencies_series['http2'].std(),
    'min': latencies_series['http2'].min(),
    'max': latencies_series['http2'].max(),
    'percentile_25': latencies_series['http2'].quantile(0.25),
    'percentile_75': latencies_series['http2'].quantile(0.75),
}
print("---------------------------- ")
# Calculate additional metrics for HTTP/3
http3_metrics = {
    'mean': latencies_series['http3'].mean(),
    'median': latencies_series['http3'].median(),
    'std_dev': latencies_series['http3'].std(),
    'min': latencies_series['http3'].min(),
    'max': latencies_series['http3'].max(),
    'percentile_25': latencies_series['http3'].quantile(0.25),
    'percentile_75': latencies_series['http3'].quantile(0.75),
}

# Print detailed metrics for each protocol
print("\nHTTP/2 Detailed Metrics:")
for key, value in http2_metrics.items():
    print(f"{key.capitalize()}: {value}")

print("\nHTTP/3 Detailed Metrics:")
for key, value in http3_metrics.items():
    print(f"{key.capitalize()}: {value}")