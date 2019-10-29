#!/usr/bin/env python
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('stuff', nargs='+')
    args = parser.parse_args()
    print args.stuff

if __name__ == '__main__':
    main()