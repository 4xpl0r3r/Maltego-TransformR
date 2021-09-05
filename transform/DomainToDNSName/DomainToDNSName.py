# input : maltego.Domain
# output: maltego.DNSName
import argparse
import requests
import re
import datetime
from lib.basicTransform import BasicTransform

class MainTransform(BasicTransform):
    # crt.sh
    # make use of https certs to find out subdomains
    def doTransform(self):
        print("[*] Performing Transform with crt.sh")
        transform_name='transformR.DomainToDNSName.ByCrtsh'
        display_name='To DNS Name [transformR.ByCrtsh]'
        iSession = requests.session()
        iSession.headers['User-Agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73'
        for sourceDomain in self.entities.copy():
            run_date=datetime.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]+datetime.datetime.now().astimezone().strftime(" %z")
            httpRes = iSession.get('https://crt.sh',params={
                'q':sourceDomain['fqdn']
            })
            httpRes.raise_for_status()
            subdomains = set(re.findall(r'(?:[\da-zA-z\-]+\.)+'+re.escape(sourceDomain['fqdn']),httpRes.text,re.I))
            print("[+] Found {} subdomains for {}".format(len(subdomains),sourceDomain['fqdn']))
            for subdomain in subdomains:
                newEntity = self.objectFactory.generateEntity("maltego.DNSName")
                newEntity['fqdn']=subdomain
                self.entities.append(newEntity)
                self.links.append(self.objectFactory.generateLink(sourceDomain['EntityID'],newEntity['EntityID'],
                maltego_link_transform_name=transform_name,maltego_link_transform_display_name=display_name,maltego_link_transform_run_date=run_date))
        print("[+] Transform with crt.sh Finished")