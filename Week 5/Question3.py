

import gzip
from datetime import datetime
from collections import Counter
import shlex
import re

# Regex for timestamp inside brackets
time_re = re.compile(r"\[([^\]]+)\]")

def parse_timestamp(s):
    return datetime.strptime(s, "%d/%b/%Y:%H:%M:%S %z")

def parse_line_fields(line):
    lexer = shlex.shlex(line, posix=True)
    lexer.whitespace_split = True
    lexer.commenters = ''
    return list(lexer)

counts = Counter()

logfile = "apache_logs_may2024.gz"

with gzip.open(logfile, "rt", encoding="utf-8", errors="replace") as f:
    for lineno, line in enumerate(f, 1):
        line = line.strip()
        if not line:
            continue

        # Extract timestamp
        m = time_re.search(line)
        if not m:
            continue
        time_str = m.group(1)
        dt = parse_timestamp(time_str)

        # Split remaining fields
        fields = parse_line_fields(line)
        

        req_parts = fields[6].split()
        if len(req_parts) != 3:
            continue
        method, url, protocol = req_parts

        if method != "GET":
            continue
        counts["method_get"] += 1

        if not url.startswith("/tamil/"):
            continue
        counts["url_tamil"] += 1

print()
print("Filter counts:")
for k, v in counts.items():
    print(f"{k:>15}: {v}")
