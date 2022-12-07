import pandas as pd


def get_data():
    with open(r'raw data/health_data(raw).csv', encoding='utf-8') as input_file:
        reader = pd.read_csv(input_file)

        # Use health_data to store the state and its ranking
        # We need publicHealthFundingPerCapita data to generate its ranking
        health_data = pd.DataFrame(reader, columns=['state', 'publicHealthFundingPerCapita'])
        health_data = health_data.sort_values('publicHealthFundingPerCapita')

        health_data = health_data.set_index('state')
        health_data['HealthFund_ranking'] = [i for i in range(1, len(health_data)+1)]

        return (health_data['publicHealthFundingPerCapita'], health_data['HealthFund_ranking'].astype(int))

if __name__ == '__main__':
    print(get_data())
