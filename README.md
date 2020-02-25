# WIP: freilanz - CLI Freelancing Suite

## Developer Set Up

```bash
python3 setup.py install
lanz init
```

## CLI Commands

```bash
lanz init

lanz scaffold

lanz start
Usage: lanz start [OPTIONS]
Options:
  -ago, --ago TEXT    If you started already you can present the clock. Values
                      10m 15m 20m 30m 1h
  -o, --open          Tell ftpm to open the directory with your IDE
  -m, --message TEXT  Message to save with starting job
  -s, --service TEXT  Your service short_name, defaults to the first entry of
                      config services
  -a, --account TEXT  Your service short_name, defaults to the first entry of
                      config services
  -p, --project TEXT  Your service short_name, defaults to the first entry of
                      config services
  --help              Show this message and exit.

lanz stop
Usage: lanz stop [OPTIONS]
Options:
  -m, --message TEXT  Message to save with starting job
  -s, --service TEXT  Your service short_name, defaults to the first entry of
                      config services
  -a, --account TEXT  Your service short_name, defaults to the first entry of
                      config services
  -p, --project TEXT  Your service short_name, defaults to the first entry of
                      config services
  --help              Show this message and exit.

lanz status

```
