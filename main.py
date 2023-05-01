import os
import pandas as pd
import igraph as ig

pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', 1000)


def load_data():
    path = os.path.join(os.getcwd(), 'data')
    shipping = pd.read_csv(os.path.join(path, 'Shipping_DB.csv'))
    sc_links = pd.read_csv(os.path.join(path, 'SC_summary.csv'))

    return shipping, sc_links


def print_info(data: pd.DataFrame):
    print(data.head(), '\n')
    print(data.info(), '\n')


def main():
    shipping, sc_links = load_data()
    # print_info(shipping)
    # print_info(sc_links)
    print(sc_links[sc_links['customer_ID'] == '000RCG-E'])


if __name__ == '__main__':
    main()