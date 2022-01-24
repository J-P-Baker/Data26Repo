"""

fish-market, fish-market-mon, fish-market-tues

create a csv, contains all averages for each fish species

store back in s3, data-eng-resources python/

"""
import boto3
import pandas as pd
import io

s3_client = boto3.client("s3")
s3_resource = boto3.resource("s3")

b_name = "data-eng-resources"
k_name = "python/fish"
s_name = "Data26/Test/"
f_name = "JacobB-fish-market.csv"


# get all keys with fish in them
def get_keys(bucket_name, prefix):
    bucket_contents = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

    keys = []

    for object in bucket_contents["Contents"]:
        keys.append(object["Key"])
    # print(keys)
    return (keys)


k_s = get_keys(b_name, k_name)


# read CSV from bucket
def read_csv_from_keys(bucket_name, keys):
    avr_df_list = []

    for key in keys:
        s3_object = s3_client.get_object(Bucket=bucket_name, Key=key)

        s3_df = pd.read_csv(s3_object["Body"])
        # print(s3_df)

        avr_df_list.append(s3_df)
    return (avr_df_list)


avr_df_l = read_csv_from_keys(b_name, k_s)


def join_and_avarage_dfs(avr_df_list):
    # print(avr_df_list)
    df = pd.concat(avr_df_list)
    # print(df)
    avr_df = df.groupby('Species').mean()
    # print(avr_df)
    return (avr_df)


dts = join_and_avarage_dfs(avr_df_l)


def send_file_to_s3(bucket_name, save_name, file_name, df_to_send):
    str_buffer = io.StringIO()
    df_to_send.to_csv(str_buffer)

    # print(save_name + file_name)
    # print(str_buffer)

    s3_client.put_object(Body=str_buffer.getvalue(), Bucket=bucket_name, Key=save_name+file_name)


send_file_to_s3(b_name, s_name, f_name, dts)


