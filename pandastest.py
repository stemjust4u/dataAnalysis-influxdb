import pandas as pd
from influxdb_client import InfluxDBClient

url = 'http://192.168.254.89:8086'
token = 'root:root'
org = ''
bucket = 'esp2nred'

with InfluxDBClient(url=url, token=token, org=org) as client:
    query_api = client.query_api()
    tables = query_api.query('from(bucket: "esp2nred") |> range(start: -1h) |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")')
    #tables = client.query_api().query(query, org=org)
    #for table in tables:
    #    for record in table.records:
    #        print(record)
    df = pd.DataFrame(client.query_api().query_data_frame('from(bucket: "esp2nred") |> range(start: -1h) |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")'))
    print(df)