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
