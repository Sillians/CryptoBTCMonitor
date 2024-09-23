# CryptoBTCMonitor




### Exchanges

The `/exchanges` endpoint of [CoinCap](https://docs.coincap.io/) offers an understanding into the where cryptocurrency is being exchanged and offers high-level information on those exchanges. CoinCap strives to provide transparency in the recency of our exchange data. For that purpose you will find an "updated" key for each exchange. 

Details into the coin pairs and volume;
`api.coincap.io/v2/exchanges`

#### Response Data

| Key                | Description                       |
| ------------------ | --------------------------------- |
| id                 | unique identifier for exchange    |
| name               | proper name of exchange           |
| rank               | rank is in ascending order - this number is directly associated with the total exchange volume whereas the highest volume exchange receives rank 1    |
| percentTotalVolume | the amount of daily volume a single exchange transacts in relation to total daily volume of all exchanges     |
| volumeUsd          | daily volume represented in USD    |
| tradingPairs       | number of trading pairs (or markets) offered by exchange    |
| socket             | true/false, true = trade socket available, false = trade socket unavailable  |
| exchangeUrl        | website to exchange                |
| updated            | UNIX timestamp (milliseconds) since information was received from this exchange   |



### Commands

`docker compose -f compose.yaml up -d`

