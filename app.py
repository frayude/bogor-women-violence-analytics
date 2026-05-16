import streamlit as st
from utils.analysis import (load_data, 
                            preprocess_data,
                            get_total_kasus,
                            get_kasus_per_tahun,
                            get_kasus_per_kecamatan,
                            get_kasus_per_jenis,
                            get_kasus_per_status,
                            get_kasus_penanganan
                            )

# data
df = load_data()
df = preprocess_data(df)
total_kasus = get_total_kasus(df)
kasus_pertahun = get_kasus_per_tahun(df)

# for metric
high_cases = kasus_pertahun.max()
low_cases = kasus_pertahun.min()

year_max = kasus_pertahun.idxmax()
year_min = kasus_pertahun.idxmin()

st.title("Violence Against Women in Bogor (2017-2022) Dashboard")
st.divider()

# Overview & Metrics
st.header("Overview")

col1, col2, col3 = st.columns(3)
col1.metric("Total number of cases", total_kasus)
col2.metric(f"High Cases in {year_max}", high_cases)
col3.metric(f"Low Cases in {year_min}", low_cases)

st.subheader("Yearly trend analysis")
st.line_chart(kasus_pertahun)
st.subheader("Summary")
# st.markdown("none")