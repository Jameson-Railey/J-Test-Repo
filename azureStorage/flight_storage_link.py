from azure.core.credentials import AzureNamedKeyCredential
from azure.data.tables import TableServiceClient

import pandas as pd
from datetime import datetime

# Pandas
stub_data = pd.read_csv(r"C:\Users\50573636\Documents\Stub Data\Stub Data.csv")

# Azure Table Storage
credential = AzureNamedKeyCredential("stubbedflightdata", "F0/tvG4LCoyIR01m63C678Pkgtjg2BoGGIt9Xwroyj8SgyZltqtWQ7KA/8xDCau/uY8uyYa+TJbi+ASt6jfzwQ==")

service = TableServiceClient(endpoint="https://stubbedflightdata.table.core.windows.net", credential=credential)

# SAMPLE CODE 

# for i in range(len(stub_data)):

#     my_entity = {
#         u'PartitionKey': 1,
#         u'RowKey': i,
#         u'Printer ID': stub_data['Printer ID'].loc[0].tolist(),
#         u'Sheets Printed': stub_data['Sheets Printed'].loc[0].tolist()
#     }

#     entity = table_client.create_entity(entity=my_entity)

my_entity = {
    u'PartitionKey': 1,
    u'RowKey': 2,
    u'PrinterID': 3,
    u'SheetsPrinted': 4
}

table_name = "testTable"
table_client = service.get_table_client(table_name=table_name)

#entity = table_client.create_entity(entity=my_entity)

# print(int(stub_data['Printer ID'].loc[0]))
# print(int(stub_data['Sheets Printed'].loc[0]))

