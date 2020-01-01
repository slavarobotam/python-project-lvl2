#!/usr/bin/env python3

from gendiff.engine import gendiff, parser


def main():
    args = parser.parse_args()
    gendiff(args)


if __name__ == '__main__':
    main()
