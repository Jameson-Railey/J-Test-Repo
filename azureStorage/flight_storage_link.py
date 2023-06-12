from azure.core.credentials import AzureNamedKeyCredential
from azure.data.tables import TableServiceClient

import pandas as pd

credential = AzureNamedKeyCredential("stubbedflightdata", "F0/tvG4LCoyIR01m63C678Pkgtjg2BoGGIt9Xwroyj8SgyZltqtWQ7KA/8xDCau/uY8uyYa+TJbi+ASt6jfzwQ==")

service = TableServiceClient(endpoint="https://stubbedflightdata.table.core.windows.net", credential=credential)

table_name = "testTable"
table_client = service.delete_table(table_name=table_name)

# stub_data = pd.read_csv(r"C:\Users\50573636\Documents\Stub Data")
# stub_data.head()