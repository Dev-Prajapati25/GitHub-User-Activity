import requests, sys, json
from datetime import datetime
from rich.table import Table
from rich.console import Console

def main():
    username = get_username()
    response, status_code = fetch_response(username)

    if status_code == 200:
        result = get_result(response)
        pretty_print(username,result)
    else:
        print(f"{status_code} Error Occured")
        return

def get_result(response: list[dict]) -> list[dict]:
    '''
    OUTPUT Format
    id ; id
    Event : {eventtype}
    repo Name : {name of the repo}
    repo url : {url}
    Event date : (created_at)
    '''
    result = []
    event_id = 0
    for event in response:
        event_info = {}
        
        # Basic info
        event_info["event_id"] = str(event_id)
        event_info["event"] = event["type"]
        
        # Repo info
        repo_dir = event["repo"]["name"]
        repo_name = repo_dir.split('/')[1]
        event_info["repo_name"] = repo_name
        event_info["repo_url"] = event["repo"]["url"]

        # Date info

        # ISO 8601 string
        # 2025-10-29T18:15:54Z
        created_at = event["created_at"]

        # Parse ISO 8601 string to datetime
        try:
            dt_obj = datetime.fromisoformat(created_at)
        except ValueError:
            # Fallback for non-strict ISO 8601 or older Python versions
            # Adjust format string as needed for your specific ISO 8601 variations
            dt_obj = datetime.strftime(created_at, "%Y-%m-%dT%H:%M:%S")

        # Format datetime object to "day-month-year"
        event_date = dt_obj.strftime("%d-%m-%Y")

        event_info["event_date"] = event_date

        result.append(event_info)
        event_id += 1
    return result

def pretty_print(username, result):
    count = len(result)

    table = Table(title=f"{username} Github Events")
    
    table.add_column("Event Id", justify="center")
    table.add_column("Event", justify="center")
    table.add_column("Event Date", justify="center")
    table.add_column("Repo Name", justify="center")
    table.add_column("Repo URL", justify="center")

    for event in result:
        event_id = event["event_id"]
        event_name = event["event"]
        repo_name = event["repo_name"]
        repo_url = event["repo_url"]
        event_date = event["event_date"]

        table.add_row(event_id, event_name, event_date, repo_name, repo_url)

    console = Console()
    console.print(table)

def get_username():
    try:
        username = sys.argv[1]
    except IndexError:
        print("Error Occured: Provide GitHub username")
    except Exception as e:
        print(f"Error Occured: {e}")
    else:
        return username

def fetch_response(username:str):
    url = f"https://api.github.com/users/{username}/events"
    try:
        response = requests.get(url)
    except Exception as e:
        print(f"Error Occurred : {e}")
    else:
        return response.json(), response.status_code

if __name__=="__main__":
    main()