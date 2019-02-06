#!/usr/bin/python3

# Fix nhc.conf on warewulf nodes without having to create a separate
# node image just because the primary ethernet interface or the
# infiniband speed is different.

# First, the HCA type -> speed table. Add to this when new hardware arrives!
hca2speed = { 'MT4099': 56,
              'MT25418': 40,
              'MT4115': 56,
              'MT26428': 40,
              'MT26438': 40,
              'MT4119': 100 }

import subprocess
from pathlib import Path
import tempfile
import os
import re
import sys

# First lookup the primary ethernet interface. Take the interface used
# for the default route.
dev = None
ipr = subprocess.check_output(["ip", "r"])
for line in ipr.splitlines():
    w = line.split()
    if w[0] == b'default':
        dev = w[4].decode('utf-8')
        break

# Then check the IB adapter model. Pick the first adapter where any of
# the ports is in linkup state.
hca = None
p = Path("/sys/class/infiniband")
if p.is_dir():
    for x in p.iterdir():
        if hca != None:
            break
        for y in (x / 'ports').iterdir():
            with (y / 'phys_state').open() as f:
                state = f.read().split()[1]
                if state == 'LinkUp':
                    with (x / 'hca_type').open() as f2:
                        hca = f2.read().strip()
                        break

# Finally read the nhc.conf format file given as the 1st cmdline
# argument, replace the eth device and IB speeds
infile = Path(sys.argv[1])
with infile.open() as inf:
    with tempfile.NamedTemporaryFile(mode='w', delete=False, dir=str(infile.parent)) as of:
        for line in inf.readlines():
            if dev != None:
                l = re.sub(r'check_hw_eth .*', r'check_hw_eth ' + dev, line)
            else:
                l = line
            if hca != None and (hca in hca2speed):
                l = re.sub(r'check_hw_ib .*', r'check_hw_ib {}'.format(hca2speed[hca]), l)
            of.write(l)
        os.replace(of.name, str(infile))

