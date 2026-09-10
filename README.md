### hi, i'm alina

onchain data, berlin. i read block explorers so you don't have to.

- the short version, with charts: [x.com/alinaschanz](https://x.com/alinaschanz)
- the long version: [alinaschanz.life](https://alinaschanz.life)

#### what is here

| repo | what it does |
| --- | --- |
| [onchain-notes](https://github.com/alinaschanz/onchain-notes) | the numbers i look at before posting anything: prices, base fee, fear & greed, tvl. one card, one screen. |
| [gasweek](https://github.com/alinaschanz/gasweek) | when is ethereum cheapest? base fee by hour of day over the last week, as a table and an svg, plus a daily dataset that fills itself. |
| [blobwatch](https://github.com/alinaschanz/blobwatch) | who bought ethereum's blob space in the last ten minutes and what they paid, by rollup. every name comes with a source, or from the chain itself. |
| [bigmoves](https://github.com/alinaschanz/bigmoves) | large stablecoin, weth and wbtc transfers in the last n blocks, with exchange and bridge labels. `--follow` keeps watching. |
| [stablepeg](https://github.com/alinaschanz/stablepeg) | are the stablecoins still a dollar? uniswap v3 spot and twap, a curve 3pool swap quote, coingecko next to it. |
| [lendrates](https://github.com/alinaschanz/lendrates) | what a dollar earns and what borrowing one costs on aave, spark, compound and the sky savings rate, all read at one block. |
| [ens-lookup](https://github.com/alinaschanz/ens-lookup) | ens names to addresses and back, text records included. pure python, keccak and all. |
| [netflows](https://github.com/alinaschanz/netflows) | which exchanges gained or lost stablecoins in the last hour. work in progress, the numbers are not quotable yet. |
| [gasweek-js](https://github.com/alinaschanz/gasweek-js) | gasweek for the browser and node: the same pages, interpolation and percentiles in typescript, zero dependencies. |
| [rpcprobe](https://github.com/alinaschanz/rpcprobe) | which public rpcs answer today and what they allow: log ranges, archive state, batches, the blob fee. the fallback lists in the other repos come from it. |

all of it: python 3.10+, standard library only, public json-rpc endpoints, no api keys
(the one typescript twin has no dependencies either). if a number in a post looks off, the
script that produced it is here. commits are signed.

two pieces small enough to be gists: [keccak-256 in plain python](https://gist.github.com/alinaschanz/d8faf7e1d6dfe129e9094c4c085790e6)
and [a uniswap v3 price and twap from one pool](https://gist.github.com/alinaschanz/92e7f3dd401362e802ecc7727332707e).

#### right now

<!-- live:start -->
- base fee on 2026-09-10: median 0.074 gwei, p90 0.203, cheapest hour 02:00 utc, priciest 15:00 utc
- last 3 days: medians from 0.056 to 0.074 gwei ([the dataset](https://github.com/alinaschanz/gasweek/blob/main/data/daily.csv))
- latest note: [week 37 in numbers: gas by the hour, nine pegs, and $429m that never left](https://alinaschanz.life/notes/2026-09-08-week-37-in-numbers.html) (2026-09-08)
<sub>refreshed 2026-09-10 00:53 utc by [refresh_readme.py](refresh_readme.py)</sub>
<!-- live:end -->

numbers, not calls. not financial advice.
