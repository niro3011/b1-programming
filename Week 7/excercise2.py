import re
import logging
from datetime import datetime
from collections import Counter

# Setup logging
log_filename = f"analysis_audit_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

LOG_PATTERN = re.compile(
    r'(?P<ip>[\d\.]+) - - \[(?P<timestamp>[^\]]+)\] '
    r'"(?P<method>\w+) (?P<url>[^\s]+) HTTP/[\d\.]+" '
    r'(?P<status>\d+) (?P<size>\d+|-)'
)

# Storage for analysis
total_requests = 0
unique_ips = set()
http_methods = Counter()
urls = Counter()
hourly_traffic = Counter()
errors = []
failed_logins = {}
forbidden_access = []
security_incidents = []


def parse_log_line(line):
    match = LOG_PATTERN.match(line.strip())
    if not match:
        return None
    
    data = match.groupdict()
    data['status'] = int(data['status'])

    try:
        dt = datetime.strptime(data['timestamp'], '%d/%b/%Y:%H:%M:%S %z')
        data['hour'] = dt.strftime('%Y-%m-%d %H:00')
    except:
        data['hour'] = None
    
    return data


def analyze_log_entry(entry):
    global total_requests
    
    total_requests += 1
    unique_ips.add(entry['ip'])
    http_methods[entry['method']] += 1
    urls[entry['url']] += 1
    
    if entry['hour']:
        hourly_traffic[entry['hour']] += 1

    if entry['status'] >= 400:
        errors.append(entry)

    check_security(entry)


def check_security(entry):
    ip = entry['ip']
    status = entry['status']
    url = entry['url']

    if status == 401:
        if ip not in failed_logins:
            failed_logins[ip] = []
        failed_logins[ip].append(entry)
        logger.warning(f"Failed login from {ip}")

    if status == 403:
        forbidden_access.append(entry)
        logger.warning(f"Forbidden access from {ip} to {url}")

    sql_patterns = ['union', 'select', 'insert', 'delete', 'drop', "' or '", '" or "']
    if any(pattern in url.lower() for pattern in sql_patterns):
        security_incidents.append({
            'type': 'SQL Injection',
            'ip': ip,
            'url': url,
            'timestamp': entry['timestamp']
        })
        logger.warning(f"SQL injection attempt from {ip}")


def detect_brute_force():
    for ip, attempts in failed_logins.items():
        if len(attempts) >= 5:
            security_incidents.append({
                'type': 'Brute Force',
                'ip': ip,
                'attempts': len(attempts)
            })
            logger.warning(f"Brute force attack from {ip} - {len(attempts)} attempts")


def process_log_file(filename):
    logger.info(f"Processing file: {filename}")
    
    try:
        with open(filename, 'r') as f:
            line_num = 0
            parsed = 0
            
            for line in f:
                line_num += 1
                
                try:
                    entry = parse_log_line(line)
                    if entry:
                        analyze_log_entry(entry)
                        parsed += 1
                    else:
                        logger.debug(f"Could not parse line {line_num}")
                
                except Exception as e:
                    logger.error(f"Error on line {line_num}: {e}")
            
            logger.info(f"Processed {line_num} lines, parsed {parsed} entries")
    
    except FileNotFoundError:
        logger.error(f"File not found: {filename}")
        print(f"Error: {filename} not found")
    except Exception as e:
        logger.error(f"Error reading file: {e}")
        print(f"Error processing file: {e}")


def generate_summary_report():
    """Generate summary report."""
    with open('summary_report.txt', 'w') as f:
        f.write("WEB SERVER LOG ANALYSIS SUMMARY\n")
        f.write("=" * 60 + "\n\n")
        
        f.write(f"Total Requests: {total_requests:,}\n")
        f.write(f"Unique Visitors: {len(unique_ips):,}\n\n")
        
        f.write("HTTP Methods:\n")
        for method, count in http_methods.most_common():
            f.write(f"  {method}: {count:,}\n")
        
        f.write("\nTop 10 URLs:\n")
        for url, count in urls.most_common(10):
            f.write(f"  {count:,} - {url}\n")
        
        f.write("\nPeak Traffic Hours:\n")
        for hour, count in hourly_traffic.most_common(5):
            f.write(f"  {hour}: {count:,} requests\n")
        
        f.write("\nSecurity Summary:\n")
        f.write(f"  Security Incidents: {len(security_incidents)}\n")
        f.write(f"  Failed Logins: {sum(len(v) for v in failed_logins.values())}\n")
        f.write(f"  Forbidden Access: {len(forbidden_access)}\n")
    
    logger.info("Summary report generated")


def generate_security_report():
    """Generate security incidents report."""
    with open('security_incidents.txt', 'w') as f:
        f.write("SECURITY INCIDENTS REPORT\n")
        f.write("=" * 60 + "\n\n")

        brute_force = [i for i in security_incidents if i['type'] == 'Brute Force']
        if brute_force:
            f.write("Brute Force Attacks:\n")
            for incident in brute_force:
                f.write(f"  IP: {incident['ip']} - {incident['attempts']} attempts\n")
            f.write("\n")

        sql_attacks = [i for i in security_incidents if i['type'] == 'SQL Injection']
        if sql_attacks:
            f.write("SQL Injection Attempts:\n")
            for incident in sql_attacks:
                f.write(f"  {incident['timestamp']} - {incident['ip']}\n")
                f.write(f"    URL: {incident['url']}\n")
            f.write("\n")
        
        f.write("Failed Login Attempts by IP:\n")
        for ip, attempts in sorted(failed_logins.items(), key=lambda x: len(x[1]), reverse=True):
            f.write(f"  {ip}: {len(attempts)} attempts\n")
    
    logger.info("Security report generated")


def generate_error_report():
    """Generate error log report."""
    with open('error_log.txt', 'w') as f:
        f.write("HTTP ERRORS (4xx and 5xx)\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Total Errors: {len(errors)}\n\n")

        by_status = {}
        for error in errors:
            status = error['status']
            if status not in by_status:
                by_status[status] = []
            by_status[status].append(error)
        
        for status in sorted(by_status.keys()):
            error_list = by_status[status]
            f.write(f"\nStatus {status} ({len(error_list)} errors):\n")
            for error in error_list[:20]:  # Show first 20
                f.write(f"  {error['timestamp']} - {error['ip']} - {error['url']}\n")
            if len(error_list) > 20:
                f.write(f"  ... and {len(error_list) - 20} more\n")
    
    logger.info("Error report generated")


def main():
    """Main function."""
    print("Web Server Log Analyzer")
    print("=" * 60)

    log_file = "logfile.txt"
    
    process_log_file(log_file)
    
    if total_requests > 0:
        print(f"\nAnalyzed {total_requests:,} requests")

        detect_brute_force()

        print("Generating reports...")
        generate_summary_report()
        generate_security_report()
        generate_error_report()
        
        print("\nReports generated:")
        print("  - summary_report.txt")
        print("  - security_incidents.txt")
        print("  - error_log.txt")
        print(f"  - {log_filename}")
        print("\nDone!")
    else:
        print("\nNo log entries processed.")


if __name__ == "__main__":
    main()