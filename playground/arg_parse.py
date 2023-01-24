import argparse

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument("-t", "--tender", action="store_true", help="untuk memilih tender")
group.add_argument("-n", "--nontender", action="store_true", help="untuk memilih non tender")

parser.add_argument("url", type=str, help="Masukan URL untuk tender (example: 'https://eproc.esdm.go.id/eproc4/lelang') atau non-tender (example: 'https://eproc.esdm.go.id/eproc4/nontender').")
parser.add_argument("-l", "--log", action="store_true", help="Logging.")
parser.add_argument("-f", "--follow", action="store_true", help="Follow.")
parser.add_argument("-v", "--verbose", action="store_true", help="Verbose.")

args = parser.parse_args()

answer = '/'.join(args.url.split('/')[:-1]) if not args.url.split('/')[-1] else args.url 

if args.tender:
    print('tender')
    print(answer)

if args.nontender:
    print('nontender')
    print(answer)

if args.log:
    print('log')
    print(answer)
    
if args.follow:
    print('follow')
    print(answer)
    
if args.verbose:
    print('verbose')
    print(answer)
