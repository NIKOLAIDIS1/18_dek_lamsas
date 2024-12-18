import subprocess
import pandas as pd
import re
from concurrent.futures import ThreadPoolExecutor
from time import time

interface = "wlp2s0"

#--------------------------------------------------------------


def setup_network_simulation(interface: str):
    """
    Configure network simulation using `tc` to add latency, bandwidth limits, and packet loss.
    """
    try:
        # Check if a qdisc exists on the interface
        check_qdisc = subprocess.run(
            f"tc qdisc show dev {interface}",
            shell=True, text=True, capture_output=True, check=True
        )
        
        if "noqueue" not in check_qdisc.stdout and check_qdisc.stdout.strip():
            # Delete any existing qdisc
            subprocess.run(
                f"sudo tc qdisc del dev {interface} root",
                shell=True, check=True
            )
            print(f"Existing qdisc on {interface} removed.")
        else:
            print(f"No active qdisc on {interface}, skipping removal.")
            # # Apply new network simulation settings: 50ms delay, 10% packet loss, and 1 Mbps bandwidth limit
        # Add latency, packet loss, and bandwidth limits---
        subprocess.run(
            f"sudo tc qdisc add dev {interface} root netem delay 50ms loss 10% rate 1mbit",
            shell=True, check=True
        )
        print(f"Network simulation configured on {interface}: 50ms delay, 10% loss, 1Mbps bandwidth.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to set up network simulation: {e.stderr}")
#----------------------------------------------------
# After adding the netem rule
check_simulation = subprocess.run(
    f"tc qdisc show dev {interface}",
    shell=True, text=True, capture_output=True, check=True
)
print(f"Current qdisc configuration:\n{check_simulation.stdout}")

#------------------------------------------------------
def reset_network_simulation(interface: str):
    """
    Reset the network interface to its default state by removing `tc` configurations.
    """
    try:
        subprocess.run(
            f"sudo tc qdisc del dev {interface} root",
            shell=True, check=True
        )
        print(f"Network simulation reset on {interface}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to reset network simulation on {interface}: {e.stderr}")


#--------------------------------------------------------
def make_http2_call(url: str) -> str:
    docker_command = (
        'docker run -it --rm ymuski/curl-http3 curl --http2 -o /dev/null '
        '-w "DNS lookup: %{time_namelookup} seconds\n'
        'Connect: %{time_connect} seconds\n'
        'TLS handshake: %{time_appconnect} seconds\n'
        'Start transfer: %{time_starttransfer} seconds\n'
        'Total time: %{time_total} seconds\n" '
        f'{url}'
    )

    try:
        result = subprocess.run(docker_command, shell=True, text=True, capture_output=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"HTTP/2 command failed: {e.stderr}")
        return None


def make_http3_call(url: str) -> str:
    docker_command = (
        'docker run -it --rm ymuski/curl-http3 curl --http3 -o /dev/null '
        '-w "DNS lookup: %{time_namelookup} seconds\n'
        'Connect: %{time_connect} seconds\n'
        'TLS handshake: %{time_appconnect} seconds\n'
        'Start transfer: %{time_starttransfer} seconds\n'
        'Total time: %{time_total} seconds\n" '
        f'{url}'
    )

    try:
        result = subprocess.run(docker_command, shell=True, text=True, capture_output=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"HTTP/3 command failed: {e.stderr}")
        return None


def get_total_time_from_curl_output(curl_output: str) -> float:
    match = re.search(r"Total time: (\d+\.\d+)", curl_output)
    if match:
        return float(match.group(1))
    else:
        raise Exception("Failed to parse curl output.")


def run_benchmark(url: str, iterations: int = 1) -> dict:
    latencies = {'http2': [], 'http3': []}

    for _ in range(iterations):
        curl_output_http3 = make_http3_call(url)
        curl_output_http2 = make_http2_call(url)

        if curl_output_http3 and curl_output_http2:
            total_time_http3 = get_total_time_from_curl_output(curl_output_http3)
            total_time_http2 = get_total_time_from_curl_output(curl_output_http2)

            if total_time_http3 and total_time_http2:
                latencies['http3'].append(total_time_http3)
                latencies['http2'].append(total_time_http2)
        else:
            print("Skipped iteration due to missing curl output.")

    return latencies


# Interface and URL to test
interface = "wlp2s0"  # Replace with your network interface name
url = 'https://openai.com'

# Set up network simulation
setup_network_simulation(interface)

try:
    # Run the benchmark
    latencies = run_benchmark(url)

    # Create a DataFrame to analyze the results
    latencies_series = pd.DataFrame(latencies)

    # Print out the average latencies
    print(
        f"""
        HTTP/2 LATENCY : {latencies_series['http2'].mean()}
        HTTP/3 LATENCY : {latencies_series['http3'].mean()}
        """
    )

    # Save the results to a CSV file
    output_file = f'/tmp/http2-vs-http3_{int(time())}.csv'
    latencies_series.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")

finally:
    # Reset the network simulation
    reset_network_simulation(interface)
