# temp-file-cleaner

Find temp/cache files by extension pattern (`.tmp`, `.temp`, `.cache`,
`.bak`, `.swp`, `~` files), report count and total size, and delete only
with `--apply`. Dry-run is the default, so nothing is removed by accident.

## How to run

```bash
python3 main.py --path ./some-folder
python3 main.py --path ./some-folder --apply
```

## Example output (sample from test fixture data)

```text
would-delete: ./some-folder/a.tmp (5 bytes)
would-delete: ./some-folder/b.bak (3 bytes)
Found 2 temp file(s), 8 bytes total.
```

Standard library only. No network access.
