# GitHub-User-Activity

A command-line tool to fetch and display recent public activity for any GitHub user. This script utilizes the GitHub Events API to retrieve data and presents it in a clean, formatted table in your terminal.

## Features

-   Fetches the 30 most recent public events for a specified GitHub user.
-   Extracts and displays key information: event type, date, repository name, and repository URL.
-   Uses the `rich` library to present the data in a readable and aesthetically pleasing table.
-   Simple command-line interface.

## Requirements

-   Python 3.13
-   `requests`
-   `rich`

## Installation

1.  Clone this repository to your local machine:
    ```sh
    git clone https://github.com/Dev-Prajapati25/GitHub-User-Activity.git
    ```

2.  Navigate into the cloned directory:
    ```sh
    cd GitHub-User-Activity
    ```

3.  Install the necessary Python packages:
    ```sh
    pip install -r requirements.txt
    ```
    Alternatively, you can install them manually:
    ```sh
    pip install requests rich
    ```

## Usage

Run the script from your terminal, providing a valid GitHub username as a command-line argument.

**Syntax:**
```sh
python main.py <username>
```

**Example:**
```sh
python main.py torvalds
```

## Output

The script will render a table in your terminal containing the user's recent activity. The table will have the following columns:

-   **Event Id**: A local sequential ID for the event.
-   **Event**: The type of the GitHub event (e.g., `PushEvent`, `CreateEvent`, `PullRequestEvent`).
-   **Event Date**: The date the event occurred, formatted as `DD-MM-YYYY`.
-   **Repo Name**: The name of the repository where the event took place.
-   **Repo URL**: The API URL for the repository.