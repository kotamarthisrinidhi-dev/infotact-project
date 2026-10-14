import pandas as pd
import streamlit as st
import snowflake.connector


def load_analytics_data():
    conn = snowflake.connector.connect(
        account=st.secrets["snowflake"]["ACCOUNT"],
        user=st.secrets["snowflake"]["USER"],
        password=st.secrets["snowflake"]["PASSWORD"],
        warehouse=st.secrets["snowflake"]["WAREHOUSE"],
        database="ATMOSYNC",
        schema="RAW",
    )

    try:
        query = """
            SELECT *
            FROM ATMOSYNC.RAW.MICROCLIMATE_ANALYTICS
            ORDER BY DATE
        """
        return pd.read_sql(query, conn)
    finally:
        conn.close()