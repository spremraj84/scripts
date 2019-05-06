import re
from collections import Counter



def log_parser(filename):
        hostregex = r'\w+\.\w+\.\w+'

        with open(filename) as f:
                logfile = f.read()
                hostnames = re.findall(hostregex,logfile)
                hostcount = Counter(hostnames)



                with open(outfile,'a') as out:
                        for host, count in hostcount.items():
                                out.write(str(host)+" " +str(count)+'\n')


if __name__ == '__main__':
        filename = raw_input()
        outfile = "records_access_log_00.txt"
        log_parser(filename)
