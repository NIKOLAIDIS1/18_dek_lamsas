# README: HTTP/2 vs HTTP/3 Latency Analysis Project

## Overview
This project evaluates and compares the latency of HTTP/2 and HTTP/3 protocols under different network conditions. It includes tools for measuring response times, statistical analysis, and visualizing performance data. The project also supports network simulation to test protocol behavior under constrained environments like high latency, packet loss, and limited bandwidth.

---

## Features
1. **Latency Measurement:**
   - Repeated requests to a given URL using HTTP/2 and HTTP/3.
   - Uses cURL through Docker to ensure compatibility with experimental HTTP/3 implementations.

2. **Statistical Analysis:**
   - Calculates detailed metrics like mean, median, standard deviation, min, max, and percentiles.
   - Provides insights into the relative performance of both protocols.

3. **Network Simulation:**
   - Simulates weak and unstable network conditions (e.g., 50ms delay, 10% packet loss, 1 Mbps bandwidth).
   - Tests protocol resilience and performance consistency.

4. **Visualization Tools:**
   - Generates histograms and box plots to visualize latency distribution.
   - Displays comparative data trends for HTTP/2 and HTTP/3.

5. **Data Export:**
   - Saves raw and processed data to CSV files for further analysis.

---

## Prerequisites
- **Python 3.6+**
- **Docker** (for executing cURL commands)
- **Python Libraries:** pandas, matplotlib, re, subprocess, concurrent.futures

---

## Usage
### 1. Running Basic Latency Tests
To measure and compare latency:
1. Configure the number of measurements in the script.
2. Set the target URL (default: `https://openai.com`).
3. Execute the script:
   ```bash
   python HTTP2_vs_HTTP3_Latency_Benchmark.py
   ```

### 2. Network Simulation
To simulate a weak network environment:
1. Ensure `tc` (Traffic Control) is available on your machine.
2. Run the network simulation setup script:
   ```bash
   python Simulated_Weak_Network_Instability_Benchmark.py
   ```
3. The script will:
   - Introduce 50ms delay, 10% packet loss, and 1 Mbps bandwidth.
   - Reset network settings after testing.

### 3. Visualization
To generate visual comparisons of latency:
1. Use the `Network_Latency_Graph_Analyzer.py` script:
   ```bash
   python Network_Latency_Graph_Analyzer.py
   ```
2. View box plots and histograms comparing HTTP/2 and HTTP/3 performance.

---

## File Descriptions
### Code Files
1. **`HTTP2_vs_HTTP3_Latency_Benchmark.py`**: Measures and compares HTTP/2 and HTTP/3 latencies.
2. **`Simulated_Weak_Network_Instability_Benchmark.py`**: Simulates network constraints to test protocol resilience.
3. **`Network_Latency_Graph_Analyzer.py`**: Visualizes latency data using box plots and histograms.
4. **`Statistics_by_N_Measurements_of_Latency.py`**: Provides detailed statistical analysis based on N latency measurements.
5. **`Network_Latency_Breakdown.py`**: Outputs detailed timing metrics (DNS lookup, connect, TLS handshake, etc.) for HTTP/2 and HTTP/3.

### Data Files
- **`open_ai_1000_request.csv`**: Example dataset with latency measurements for HTTP/2 and HTTP/3.

---

## Methodology
1. **Measurement:**
   - Requests are sent using Dockerized cURL with HTTP/2 and HTTP/3 protocols.
   - Response times are parsed and saved.

2. **Analysis:**
   - Statistical metrics are computed using Pandas.
   - Outliers and anomalies are identified for further investigation.

3. **Visualization:**
   - Data is visualized using Matplotlib for comparative analysis.

---

## Results
### Key Findings
- HTTP/3 demonstrates lower latency under high packet loss and unstable network conditions due to its QUIC protocol.
- HTTP/2 performs comparably in stable environments but suffers from head-of-line blocking in weak networks.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
This project is inspired by modern advancements in HTTP protocols and leverages Docker for HTTP/3 support. Special thanks to contributors and open-source libraries.



# 18_dek_lamsas

This project is a comprehensive benchmarking and analysis tool designed to evaluate the performance of HTTP/2 and HTTP/3 protocols under various network conditions. By leveraging Docker containers and advanced Python libraries, the tool automates the process of executing multiple HTTP requests, capturing detailed latency metrics, and generating insightful statistical summaries.
Key Features:

    Automated Benchmarking:
        Executes HTTP/2 and HTTP/3 requests using curl within Docker containers.
        Supports configurable measurements and parallel execution for performance evaluation.

    Detailed Metrics Extraction:
        Measures DNS lookup time, connection time, TLS handshake time, transfer start time, and total request time.
        Parses and stores latency results for in-depth analysis.

    Statistical Analysis:
        Computes average, median, standard deviation, and percentile-based latencies for both HTTP/2 and HTTP/3.
        Visualizes performance trends using Python libraries like pandas and matplotlib.

    Network Simulation:
        Simulates real-world network conditions (e.g., latency, packet loss) using Linux traffic control (tc) utilities.
        Tests protocol performance under constrained bandwidth, high latency, and packet loss scenarios.

    Exportable Results:
        Saves latency data and statistical summaries to CSV files for further analysis or reporting.
        Ensures reproducibility of results with minimal setup.

Use Cases:

    Compare HTTP/2 and HTTP/3 performance across diverse network environments.
    Evaluate protocol efficiency for latency-sensitive applications.
    Generate reports for academic research, development insights, or optimization studies.

Requirements:

    Docker installed and configured on the system.
    Python 3.x with necessary libraries (pandas, matplotlib, etc.).
    Basic familiarity with Linux and Docker commands.
