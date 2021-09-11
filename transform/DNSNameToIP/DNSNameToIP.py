# input : maltego.DNSName
# output: maltego.DNSName
import socket
import datetime
import netaddr
from lib.basicTransform import BasicTransform

class MainTransform(BasicTransform):
    
    transform_name='transformR.DNSNameToIP.BySocket'
    display_name='To IP [transformR.BySocket]'

    def doTransform(self):
        print("[*] Performing Transform DNSNameToIP")
        for sourceDNSName in self.entities.copy():
            run_date=datetime.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]+datetime.datetime.now().astimezone().strftime(" %z")
            try:
                ipResult = socket.getaddrinfo(sourceDNSName['fqdn'], None)
            except socket.gaierror:
                print("[!] Can't find the IP address of {}".format(sourceDNSName['fqdn']))
            generatedIP = {}
            
            for ipInfo in ipResult:
                ip = ipInfo[4][0]
                if ip in generatedIP:
                    if generatedIP[ip]['sourceDNSName'] != sourceDNSName:
                        self.links.append(self.objectFactory.generateLink(
                            sourceDNSName['EntityID'],generatedIP[ip]['EntityID'],maltego_link_transform_name=self.transform_name,maltego_link_transform_display_name=self.display_name,maltego_link_transform_run_date=run_date))
                else:
                    print("[+] {} --> {}".format(sourceDNSName['fqdn'],ip))
                    if ipInfo[0] == 2: # ipv4
                        newEntity = self.objectFactory.generateEntity("maltego.IPv4Address")
                        newEntity['ipv4-address']=ip
                    elif ipInfo[0] == 10:# ipv6
                        newEntity = self.objectFactory.generateEntity("maltego.IPv6Address")
                        newEntity['ipv6-address']=ip
                    newEntity['ipaddress.internal'] = netaddr.IPAddress(ip).is_private()
                    generatedIP[ip]={'EntityID':newEntity['EntityID'],'sourceDNSName':sourceDNSName}
                    self.entities.append(newEntity)
                    self.links.append(self.objectFactory.generateLink(
                        sourceDNSName['EntityID'],newEntity['EntityID'],maltego_link_transform_name=self.transform_name,maltego_link_transform_display_name=self.display_name,maltego_link_transform_run_date=run_date))
        print("[+] Transform DNSNameToIP Finished")