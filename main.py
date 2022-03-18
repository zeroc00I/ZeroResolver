#!/bin/python3
import json, optparse, redis
from output_result import output_result

def menu():
    parser = optparse.OptionParser()
    parser.add_option('-t', '--threads', dest="threads", help='100')
    parser.add_option('-r', '--resolvers', dest="resolvers_list", help='resolvers.txt')
    parser.add_option('-d', '--domains', dest="domains_list", help='domains.txt')
    parser.add_option('-m', '--maxtimeout', dest="max_time_out", help='2 (time in seconds)')
    parser.add_option('-v', '--verbose', dest="verbose_output", action="store_true", default=False, help='-v [Will output results with ERROR status')


    options, args = parser.parse_args()

    if not options.domains_list:
        print("[-] You should set --domains (-d) parameter with your wordlist")
        exit()

    if not options.resolvers_list:
        print("[-] You should set --resolvers (-r) parameter with your wordlist")
        exit()

    globals().update(locals())



def main():
    menu()

    nameservers_file = open(options.resolvers_list,"r")
    domains_file = open(options.domains_list,"r")
    
    nameservers = nameservers_file.read().splitlines()
    domains = domains_file.read().splitlines()
    nameservers_file.close()
    domains_file.close()

    list_to_resolve = list()

    for domain in domains:
        domain = domain.rstrip()

        for nameserver in nameservers:

            list_to_resolve.append([domain,nameserver])
            print(list_to_resolve)
            
    output_result(
    list_to_resolve
    )
    

if __name__== "__main__":
    main()