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


### Setting up Local Postgres with Docker Compose

Helpful Resources:

- [Frictionless Local Postgres with Docker Compose](https://github.com/asaikali/docker-compose-postgres/blob/master/README.md)
- [Postgres, PgAdmin docker compose file](https://github.com/asaikali/docker-compose-postgres/blob/master/docker-compose.yml)
- [How to automatically setup pgAdmin with a Docker database](https://event-driven.io/en/automatically_connect_pgadmin_to_database/)
- [Getting a postgres instance with pgadmin4 🐘 and docker-compose](https://gist.github.com/diegoquintanav/a3c046f016f4887ba8e74859dcb560a7)
- [Creating and filling a Postgres DB with Docker compose](https://levelup.gitconnected.com/creating-and-filling-a-postgres-db-with-docker-compose-e1607f6f882f)
- https://gist.github.com/onjin/2dd3cc52ef79069de1faa2dfd456c945?permalink_comment_id=2961048


1. checkout the code.
2. run `postgres` and `pgAdmin` using `docker-compose up`.
3. Using a browser go to `localhost:8080` and explore the pgAdmin console. There should be one database `bitcoinmonitor`. pgAdmin will not ask for any passwords.
4. The docker compose file uses a `server.json` file, with details of the server connection, to avoid having to enter the connection settings. pgAdmin will import the `.json` file into its configuration the first time it starts.

#### Command to Create and start containers
- `docker compose -f <docker-compose.yaml> up -d` or `docker compose up --build`

#### Command to stop containers and removes containers, networks, volumes, and images created by up
- `docker compose down -v`
















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




