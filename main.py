# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 11:22 PM
# @Author  : Zhixin Piao 
# @Email   : piaozhx@shanghaitech.edu.cn

import argparse
import os
import socket


def get_args():
    parser = argparse.ArgumentParser(description='Docker Manager')
    parser.add_argument('--username', default='', type=str, help='username')
    parser.add_argument('--uid', default=0, type=int, help='uid')
    args = parser.parse_args()

    return args


def main():
    args = get_args()
    hostname = socket.gethostname()

    if args.username == '' or args.uid == 0:
        print('wrong format!!!!')
        return

    container_name = "%s.%s" % (args.username, hostname)
    container_port = args.uid + 21000
    each_user_port_num = 10
    port_range_str = '%d-%d' % (30000 + each_user_port_num * args.uid, 30000 + each_user_port_num * (args.uid + 1) - 1)

    os.system("nvidia-docker run "
              "--name %s "
              "--shm-size=16G "
              "-v /home/%s:/home/%s "
              "-v /new_disk1:/new_disk1 "
              "-v /new_disk2:/new_disk2 "
              "-v /ssd:/ssd "
              "-h %s "
              "-d "
              "-p %s:%s "
              "-p %d:22  "
              "deepo_plus /usr/sbin/sshd -D" % (container_name, args.username, args.username, container_name, port_range_str, port_range_str, container_port))


if __name__ == '__main__':
    main()