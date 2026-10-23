Building an App to bridge tokens using hyperlane
## Offline demo and current scope

 The repository had a readme but no implementation. The offline demo calculates a synthetic bridge quote with an explicitly fictional fee. This explicitly labeled demo is a local prototype; it does not
 contact external services, use credentials, or persist data between executions.
 Requires Python 3.10+ and optionally Make. From this repository root:

 ```sh
 make demo
 python3 demo.py --help
 # Pass options: make demo ARGS="--help"
 ```

 The root Dockerfile runs this offline demo only. With Docker running:

 ```sh
 docker build -t bridging-tokens:demo .
 docker run --rm bridging-tokens:demo
 ```

 Docker's first build needs access to the Python base image registry.


## Concrete remaining work

- [ ] Select actual source/destination chains, assets, and bridge protocol; document trust assumptions.
- [ ] Implement network-aware quoting, allowance handling, transaction submission, and finality tracking.
- [ ] Test failed transfers, refunds, decimal conversion, and replay protection on test networks.
