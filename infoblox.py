#!/usr/bin/env python

import infoblox, sys, os

#Check to see if command line included enough arguments.

'''

if (len(sys.argv) < 3):

    print "Usage: createHost.py <fqdn> <network CIDR>"

    quit()

'''

 

 

#Assign command line arguments to named variables

#fqdn = sys.argv[1] + '.test.local'

#network = sys.argv[2]

 

fqdn = os.environ['vmName'] + '.test.local'

#network = os.environ['IPAMNetwork']

network = '192.168.10.0/24'

 

#Setup connection object for Infoblox

iba_api = infoblox.Infoblox('192.168.10.1', 'admin', 'infoblox', '1.6', 'default', 'default', False)

try:

    #Create new host record with supplied network and fqdn arguments

    ip = iba_api.create_host_record(network, fqdn)

    print 'domainName=test.local'

    print 'DnsServerList=8.8.8.8'

    print 'nicDnsServerList_0=8.8.8.8'

    print 'nicGateway_0=192.168.10.254'

    print 'nicNetmask_0=255.255.255.0'

    print "nicCount=1"

    print "nicIP_0=" + ip

    print 'hwClockUTC=true'

    print 'timeZone=Canada/Eastern'

    print 'osHostname=%s' % os.environ['vmName']

except Exception as e:

    print e