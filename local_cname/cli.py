#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import argparse
import socket
import time
from pathlib import Path

from clickclick import Action, info


def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument('from')
    # parser.add_argument('to')
    # parser.add_argument('file')
    # args = parser.parse_args()

    hosts_file = Path('/etc/hosts')

    with hosts_file.open() as fd:
        old_contents = fd.read()

    backup_file = hosts_file.with_suffix('.local-cname-backup')
    with backup_file.open('w') as fd:
        fd.write(old_contents)    

    try:
        while True:
            entries = []
            cname_file = Path('/etc/cnames')
            with cname_file.open() as fd:
                for line in fd:
                    (cnameFrom,cnameTo) = line.strip().split('=')
                    print('resoving:' + cnameTo)
                    with Action('Resolving {} ..'.format(cnameTo)):
                        results = socket.getaddrinfo(cnameTo, 80, type=socket.SOCK_STREAM)
                        for result in results:
                            family, type, proto, canonname, sockaddr = result
                            if family in (socket.AF_INET, socket.AF_INET6):
                                ip = sockaddr[0]
                                entries.append((cnameFrom, ip))

            info('Current entries:')
            for hostname, ip in entries:
                info('{} -> {}'.format(hostname, ip))

            with Action('Writing {} ..'.format(hosts_file)):
                with hosts_file.open('w') as fd:
                    fd.write(old_contents)
                    fd.write('#### Start of entries generated by local-cnames\n')
                    for hostname, ip in entries:
                        fd.write('{} {}\n'.format(ip, hostname))

            time.sleep(60)
    except KeyboardInterrupt:
        # ignore, do not print stacktrace
        pass
    finally:
        backup_file.rename(hosts_file)
