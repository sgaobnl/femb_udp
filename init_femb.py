#!/usr/bin/env python33

#specify which version of the board used here
from femb_config_35t import FEMB_CONFIG

femb_config = FEMB_CONFIG()

print "START CONFIG"
femb_config.initBoard()
print "END CONFIG"
