"""Temp file cleaner: find temp/cache files, size report, dry-run delete."""
import argparse
import os
import sys

PATTERNS = (".tmp", ".temp", ".cache", ".bak", ".swp", "~")


def is_temp(name):
    low = name.lower()
    return low.endswith(PATTERNS) or low.startswith("~")


def scan(root):
    found = []
    for dirpath, _dirs, names in os.walk(root):
        for name in names:
            if is_temp(name):
                path = os.path.join(dirpath, name)
                try:
                    found.append((path, os.path.getsize(path)))
                except OSError:
                    continue
    return found


def main(argv=None):
    p = argparse.ArgumentParser(description="Find temp/cache files; dry-run delete by default.")
    p.add_argument("--path", required=True)
    p.add_argument("--apply", action="store_true")
    args = p.parse_args(argv)
    found = scan(args.path)
    total = sum(s for _p, s in found)
    for path, size in sorted(found):
        if args.apply:
            os.remove(path)
            print(f"deleted: {path} ({size} bytes)")
        else:
            print(f"would-delete: {path} ({size} bytes)")
    print(f"Found {len(found)} temp file(s), {total} bytes total.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
