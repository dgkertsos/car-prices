import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    
    url1 = 'https://raw.githubusercontent.com/dgkertsos/car-prices/main/data/car_prices_part_1.csv'
    url2 = 'https://raw.githubusercontent.com/dgkertsos/car-prices/main/data/car_prices_part_2.csv'
    url3 = 'https://raw.githubusercontent.com/dgkertsos/car-prices/main/data/car_prices_part_3.csv'
    url4 = 'https://raw.githubusercontent.com/dgkertsos/car-prices/main/data/car_prices_part_4.csv'
    
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    response3 = requests.get(url3)
    response4 = requests.get(url4)

    df1 = pd.read_csv(io.StringIO(response1.text), sep=';')
    df2 = pd.read_csv(io.StringIO(response2.text), sep=';')
    df3 = pd.read_csv(io.StringIO(response3.text), sep=';')
    df4 = pd.read_csv(io.StringIO(response4.text), sep=';')
    
    # return pd.read_csv(io.StringIO(response1.text), io.StringIO(response2.text), sep=';')
    df = pd.concat([df1, df2, df3, df4], axis=0)

    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'