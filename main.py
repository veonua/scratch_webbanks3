import boto3
import streamlit as st
from io import BytesIO

session = boto3.Session(
    aws_access_key_id=st.secrets["ACCESS_KEY_ID"],
    aws_secret_access_key=st.secrets["SECRET_ACCESS_KEY"],
    region_name="us-east-1"
)
s3 = session.client("s3")

##############################################################################
st.title("Upload File to Webbank")
file = st.file_uploader("Upload File", type=["xlsx", "xls", "csv"])
if file is not None:
    bytes_data = file.getvalue()
    st.write("Uploading file to S3 ...")
    s3.upload_fileobj(BytesIO(bytes_data), "wb-partner-files", "Scratchpay/"+file.name)
    st.write(f"✅ {file.name} uploaded to S3")


# if False or st.button("Test download"):
#     # download file from s3
#     st.write("Downloading file from S3")
#     res = s3.download_file("wb-shared-files", "Scratchpay/test.txt", "test.txt")
#     st.write("File Downloaded from S3")