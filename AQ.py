#!/usr/bin/env python

import sys
import executive

def main():
    checks=False
    if len(sys.argv)>1:
        if sys.argv[1] == "-verify":
            checks=True
    executive.run(checks)


if __name__ == "__main__":
    main()
