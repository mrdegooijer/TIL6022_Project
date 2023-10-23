import requests

def read_github_file(username, repository, branch, filepath):
    url = f'https://raw.githubusercontent.com/{username}/{repository}/{branch}/{filepath}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        content = response.text
        return content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching file from GitHub: {e}")
        return None

# Example usage:
username = 'mrdegooijer'
repository = 'TIL6022_Project'
branch = 'main'  # or any other branch
#filepath_HS_Rdam = 'Data/Departures_HS_to_Rdam.xlsx'
#filepath_Rdam_HS = 'Data/Departures_Rdam_to_HS.xlsx'

#file_content = read_github_file(username, repository, branch, filepath)

#HS_Rdam_table = read_github_file(username, repository, branch, 'Data/Departures_HS_to_Rdam.xlsx')

Rdam_HS_table = r'https://github.com/mrdegooijer/TIL6022_Project/blob/main/Data/Departures_Rdam_to_HS.xlsx'

