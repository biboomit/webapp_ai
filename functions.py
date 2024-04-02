from google.cloud import bigquery
from google.oauth2 import service_account

def queryBigQuery(query):
    credentials = service_account.Credentials.from_service_account_file(
        'key.json', scopes=["https://www.googleapis.com/auth/cloud-platform","https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/bigquery"],
    )
    client = bigquery.Client(credentials=credentials, project=credentials.project_id,)
    query_job = client.query(query)
    df = query_job.to_dataframe()
    return df


def get_data():
    query = "SELECT * FROM `lafise-boomit.Dashboard.Dashboard_v3` "
    bx_data = queryBigQuery(query)
    return bx_data