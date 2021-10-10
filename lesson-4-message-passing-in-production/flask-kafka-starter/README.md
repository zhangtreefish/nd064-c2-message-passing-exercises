# Flask Starter
This is a bare-bones Flask application that showcases how simple it can be to set up a REST API. It also serves as a starter template for users to begin experimenting with writing their own REST API endpoints.

Flask applications can look very different depending on how they are structured and implemented. This application is built to have the minimum number of dependencies to run.
### Setting up Kafka
https://kafka.apache.org/quickstart
`bin/kafka-topics.sh --create --topic orders --partitions 2  --replication-factor 1 --bootstrap-server localhost:9092` //if replication-factor set to 2: Error while executing topic command : Replication factor: 2 larger than available brokers: 1.
## Running the app inside conda env:
1. Install Flask: `conda list` `pip3 install Flask kafka-python`
or `pip3 install -r requirements.txt` `conda list`
2. Run the app: `flask run` or `python3 app.py`
3. On a browser check GET: http://127.0.0.1:5000/health

The application should be available at `localhost:5000`.

### start consumer at kafka_2.13-3.0.0/:
`bin/kafka-console-consumer.sh --topic orders --from-beginning --bootstrap-server localhost:9092`

## References
https://blog.bitsrc.io/vs-codes-rest-client-plugin-is-all-you-need-to-make-api-calls-e9e95fcfd85a
"ImportError: attempted relative import with no known parent package": https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
