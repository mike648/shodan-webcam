import shodan

# Configuration
API_KEY = 'YOUR_SHODAN_API_KEY'  # Replace with your Shodan API key
SEARCH_TERM = 'webcamXP'  # Common term to find webcams, can be adjusted

# Initialize Shodan API
api = shodan.Shodan(API_KEY)

try:
    # Search Shodan for webcams
    results = api.search(SEARCH_TERM)

    # Show the results
    print('Results found: {}'.format(results['total']))
    for result in results['matches']:
        print('IP: {}'.format(result['ip_str']))
        print(result['data'])
        print('')
except shodan.APIError as e:
    print('Error: {}'.format(e))
