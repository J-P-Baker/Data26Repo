"""

fish-market, fish-market-mon, fish-market-tues

create a csv, contains all averages for each fish species

store back in s3, data-eng-resources python/

"""
import boto3
import pandas as pd
import io

class FishMarket:

    s3_client = boto3.client("s3")
    s3_resource = boto3.resource("s3")

    def __init__(self, b_name = "data-eng-resources", k_name = "python/fish", s_name = "Data26/fish/", f_name = "JacobB.csv"):
        self.b_name = b_name
        self.k_name = k_name
        self.s_name = s_name
        self.f_name = f_name


    # get all keys with fish in them
    def get_keys(self, bucket_name, prefix):
        bucket_contents = self.s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

        keys = []

        for object in bucket_contents["Contents"]:
            keys.append(object["Key"])
        # print(keys)
        return (keys)


    # read CSV from bucket
    def read_csv_from_keys(self, bucket_name, keys):
        avr_df_list = []

        for key in keys:
            s3_object = self.s3_client.get_object(Bucket=bucket_name, Key=key)

            s3_df = pd.read_csv(s3_object["Body"])
            # print(s3_df)

            avr_df_list.append(s3_df)
        return (avr_df_list)


    def join_and_avarage_dfs(self, avr_df_list):
        # print(avr_df_list)
        df = pd.concat(avr_df_list)
        # print(df)
        avr_df = df.groupby('Species').mean()
        # print(avr_df)
        return (avr_df)


    def send_file_to_s3(self, bucket_name, save_name, file_name, df_to_send):
        str_buffer = io.StringIO()
        df_to_send.to_csv(str_buffer)

        # print(save_name + file_name)
        # print(str_buffer)

        self.s3_client.put_object(Body=str_buffer.getvalue(), Bucket=bucket_name, Key=save_name+file_name)
        print("5")


if __name__ == '__main__':
    print("0")
    jfm = FishMarket("data-eng-resources", "python/fish", "Data26/fish/", "JacobB.csv")
    print("1")
    k_s = jfm.get_keys(jfm.b_name, jfm.k_name)
    print("2")
    avr_df_l = jfm.read_csv_from_keys(jfm.b_name, k_s)
    print("3")
    dts = jfm.join_and_avarage_dfs(avr_df_l)
    print("4")
    jfm.send_file_to_s3(jfm.b_name, jfm.s_name, jfm.f_name, dts)
    print("Finish")


