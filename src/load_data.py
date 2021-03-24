# read params
## process
## return dataframe
import os
from get_data import read_params, get_data
import argparse

def load_and_save(config_path):
	config = read_params(config_path)
	df = get_data(config_path)
	#Replace spaces with _
	new_cols = [col.replace(" ","_") for col in df.columns]
	raw_data_path=config["load_data"]["raw_dataset_csv"]
	#Get data to csv file
	df.to_csv(raw_data_path,sep=",",index=False,header=new_cols)
	#df.head()
	# print(new_cols)
	
if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)