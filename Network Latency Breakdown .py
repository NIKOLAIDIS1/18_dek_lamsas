
# pThis script is efficient and outputs all required details 
# for a quick comparison of HTTP/2 and HTTP/3 performance.
import subprocess
import re

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

   




def parse_curl_output(curl_output: str) -> dict:
    """Parses detailed timing information from curl output."""

# Initialize an empty dictionary for metrics
    metrics = {}


    metrics["DNS lookup"] = re.search(r"DNS lookup: ([\d.]+) seconds", curl_output)
    metrics["Connect"] = re.search(r"Connect: ([\d.]+) seconds", curl_output)
    metrics["TLS handshake"] = re.search(r"TLS handshake: ([\d.]+) seconds", curl_output)
    metrics["Start transfer"] = re.search(r"Start transfer: ([\d.]+) seconds", curl_output)
    metrics["Total time"] = re.search(r"Total time: ([\d.]+) seconds", curl_output)
    return {key: float(match.group(1)) if match else None for key, match in metrics.items()}

def run_measurement(url: str):

    print("-----------------")

    print("This script is efficient and outputs all required details ")
    print("for a quick comparison of HTTP/2 and HTTP/3 performance.")

    print("-----------------")

    print("DNS lookup  >>>> Time spent performing the DNS lookup.")
    print("                                                ")
    print ("Connect  >>>>> pTime spent establishing a connection to the server ")
    print("                                                ")
    print ("TLS handshake  >>>>> Time taken to negotiate and secure the connection with TLS (SSL) encryption. ")
    print("                                                ")
    
    print ("Start transfer >>>>> Time when the first byte of the response is received. ")
    print("                                                ")
    print ("Total time   >>>>> Time when the entire response (including the data transfer) is received. ")
#%{time_namelookup}: Time spent performing the DNS lookup.
#%{time_connect}: Time spent establishing a connection to the server.
#%{time_appconnect}: Time spent completing the TLS handshake (if applicable).
#%{time_starttransfer}: Time until the first byte is received from the server.
#%{time_total}: Total time for the request to complete.)








    # Measure HTTP/2
    print("HTTP/2 Results:")
    http2_output = make_http2_call(url)
    if http2_output:
        http2_metrics = parse_curl_output(http2_output)
        for key, value in http2_metrics.items():
            print(f"{key}: {value} seconds")
    else:
        print("HTTP/2 measurement failed.")
    print("-----------------")
    print("\nHTTP/3 Results:")
    # Measure HTTP/3
    http3_output = make_http3_call(url)
    if http3_output:
        http3_metrics = parse_curl_output(http3_output)
        for key, value in http3_metrics.items():
            print(f"{key}: {value} seconds")
    else:
        print("HTTP/3 measurement failed.")

# URL to test
test_url = 'https://openai.com'

# Run the single measurement
run_measurement(test_url)
