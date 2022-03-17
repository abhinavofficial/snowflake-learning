from snowflake import connector


def sfconnect():
    cnx = connector.connect(
        account='EZ73197.europe-west2.gcp',
        user='AKUMARGCP',
        password='Sharanya@61',
        warehouse='COMPUTE_WH',
        database='DEMO_DB',
        schema='PUBLIC'
    )
    return cnx
