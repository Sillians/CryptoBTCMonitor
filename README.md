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



### Start and Connect to the Database from the command line
- You can run it in local dev mode from `sh start-postgres.sh` or connect with dev.
- #### Connect to the <db> from the command line
    - psql postgres
    - CREATE ROLE <db> WITH LOGIN PASSWORD <'db-password'>;
    - ALTER ROLE dbUser CREATEDB;
    - psql postgres -U <db>;
    - CREATE DATABASE <databasename>;
    - GRANT ALL PRIVILEGES ON DATABASE <databasename> TO <db>;
    - postgres-> \list
    - postgres-> \dt



### Commands

`docker compose -f compose.yaml up -d`
`docker compose up --build`

- tear down the volumes
`docker compose down -v`



### REMOVE

DROP DATABASE bitcoinmonitor WITH (FORCE);


DROP SCHEMA IF EXISTS bitcoin;
DROP TABLE IF EXISTS bitcoin.exchange;


CREATE TABLE bitcoin.exchange
(
    id VARCHAR(50),
    name VARCHAR(50),
    rank INT,
    percentTotalVolume NUMERIC(8, 5),
    volumeUsd NUMERIC(18, 5),
    tradingPairs INT,
    socket BOOLEAN,
    exchangeUrl VARCHAR(50),
    updated_unix_millis BIGINT,
    updated_utc TIMESTAMP
)

SELECT * FROM bitcoin.exchange;