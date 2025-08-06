import gzip
from collections import defaultdict
from datetime import datetime

def parse_line(line):
    """
    Parse a log line into its fields.
    """
    parts = []
    current = ''
    in_quote = False
    i = 0
    while i < len(line):
        c = line[i]
        if c == '"':
            if in_quote and i + 1 < len(line) and line[i+1] == '"':
                current += '"'
                i += 1
            else:
                in_quote = not in_quote
        elif c == ' ' and not in_quote:
            if current:
                parts.append(current)
                current = ''
        else:
            current += c
        i += 1
    if current:
        parts.append(current)
    return parts

def parse_request(request_field):
    """
    Split the request into method, URL, protocol.
    """
    try:
        method, url, protocol = request_field.strip().split(' ')
    except:
        return None, None, None
    return method, url, protocol

# Counter per IP
ip_totals = defaultdict(int)

# Open the gzipped log file
with gzip.open("apache_logs_may2024.gz", "rt", encoding="utf-8", errors="replace") as f:
    for line in f:
        fields = parse_line(line)
        if len(fields) < 12:
            continue

        ip = fields[0]
        time_field = fields[3].lstrip('[')
        request_field = fields[5]
        status = fields[6]
        size = fields[7]

        # Parse timestamp
        try:
            dt = datetime.strptime(time_field, "%d/%b/%Y:%H:%M:%S")
        except:
            continue

        # Filter date
        if dt.strftime("%Y-%m-%d") != "2024-05-06":
            continue

        # Parse request
        method, url, protocol = parse_request(request_field)
        if url is None:
            continue

        # Filter URL
        if not url.startswith("/carnatic/"):
            continue

        # Filter status
        try:
            status_int = int(status)
            if not (200 <= status_int < 300):
                continue
        except:
            continue

        # Parse size
        try:
            size_int = int(size)
        except:
            continue

        # Aggregate by IP
        ip_totals[ip] += size_int

# Find the IP with the max download
if ip_totals:
    top_ip = max(ip_totals, key=ip_totals.get)
    total_bytes = ip_totals[top_ip]
    print(f"Top IP: {top_ip}")
    print(f"Total bytes downloaded: {total_bytes}")
else:
    print("No matching records found.")
