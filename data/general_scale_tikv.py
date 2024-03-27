#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def generate_tikv_template(ips: list):

    tikv_str = """
    - host: {ip_address}
    ssh_port: 22
    port: 20160
    status_port: 20180
    deploy_dir: /chj/app/tidb/deploy/tikv-20160
    data_dir: /chj/app/tidb/data/tikv-20160
    log_dir: /chj/app/tidb/deploy/tikv-20160/log
    arch: amd64
    os: linux
    """

    for ip in ips:
        print(tikv_str.format(ip_address=ip))


if __name__ == "__main__":
    ips = [
        "172.21.84.138",
        "172.21.84.141",
        "172.21.84.137",
        "172.21.84.146",
        "172.21.84.139",
        "172.21.84.145",
        "172.21.84.142",
        "172.21.84.144",
        "172.21.84.140",
        "172.21.84.143",
    ]
    generate_tikv_template(ips)
