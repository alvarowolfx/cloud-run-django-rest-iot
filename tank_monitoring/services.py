import os
import json
from datetime import datetime
from google.cloud import bigquery

from .settings import DATASET_ID, TABLE_NAME, PROJECT_ID

client = bigquery.Client()

schema = [
    bigquery.SchemaField("device_id", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("data", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("time", "TIMESTAMP", mode="REQUIRED"),
]


class DeviceTelemetry():

    def save(self, device_id, data):
        full_dataset_name = "{}.{}".format(PROJECT_ID, DATASET_ID)
        dataset = bigquery.Dataset(full_dataset_name)
        dataset = client.create_dataset(dataset, exists_ok=True)

        full_table_name = "{}.{}.{}".format(PROJECT_ID, DATASET_ID, TABLE_NAME)
        table = bigquery.Table(full_table_name, schema=schema)
        table = client.create_table(table, exists_ok=True)

        rows_to_insert = [
            (
                device_id,
                json.dumps(data),
                datetime.now(tz=None)
            )
        ]
        client.insert_rows(table, rows_to_insert)

    def query_historical_data(self, device_id, start, end, fields):
        def map_field(field):
            return "avg(CAST(JSON_EXTRACT(d.data,'$.{field}') as float64)) as {field}".format(field=field)

        query_fields = ', '.join(map(map_field, fields))
        query = """
            SELECT
                TIMESTAMP_TRUNC(d.time, HOUR) time,
                {query_fields}
            FROM
                `{project_id}.{dataset_id}.{table_name}` d
            where 
                d.time between '{start}' and '{end}'
                and d.device_id = '{device_id}'
            GROUP BY
                time
            ORDER BY
                time
        """.format(
            start=start,
            end=end,
            query_fields=query_fields,
            project_id=PROJECT_ID,
            dataset_id=DATASET_ID,
            table_name=TABLE_NAME,
            device_id=device_id)

        query_job = client.query(query)
        rows = query_job.result()
        return list(rows)
