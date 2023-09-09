from influxdb_client import InfluxDBClient

url = 'http://192.168.254.89:8086'
token = 'root:root'
org = ''
bucket = 'esp2nred'

with InfluxDBClient(url=url, token=token, org=org) as client:
    query_api = client.query_api()

    tables = query_api.query('from(bucket: "esp2nred") |> range(start: -1d)')

    for table in tables:
        for record in table.records:
            print(str(record["_time"]) + " - " + record.get_measurement()
                  + " " + record.get_field() + "=" + str(record.get_value()))
