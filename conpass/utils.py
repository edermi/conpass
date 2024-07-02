import dns.resolver

from datetime import datetime, timedelta, timezone


def win_timestamp_to_datetime(ts):
    us = (ts - 116444736000000000) // 10
    return (datetime(1970, 1, 1) + timedelta(microseconds=us)).replace(tzinfo=timezone.utc)

def get_list_from_file(file):
    with open(file, 'r') as f:
        lines = [line.rstrip() for line in f]
    return lines

def get_PDC(domain):
    record_name = f"_ldap._tcp.pdc._msdcs.{domain}"  # Full SRV record name specific for AD DC
    try:
        # Query the SRV records
        answers = dns.resolver.resolve(record_name, 'SRV')
        if answers:
            first_record = answers[0]
            target_fqdn = first_record.target.to_text().rstrip('.')
            # Resolve the FQDN to get the IP address
            ip_addresses = dns.resolver.resolve(target_fqdn, 'A')  # Assume IPv4
            return (target_fqdn, ip_addresses[0].to_text())
    except dns.resolver.NoAnswer:
        print(f"No SRV records found for {record_name}")
    except dns.resolver.NXDOMAIN:
        print(f"Domain name {domain} does not exist")
    except dns.resolver.Timeout:
        print("Timeout querying the DNS server")
    except dns.exception.DNSException as e:
        print(f"DNS query failed: {e}")
    
    return None

