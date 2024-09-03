# Homomorphic Encryption Schemes Comparison Tool

This project is a simple tool designed to help prospective explorers of Homomorphic Encryption gain valuable insights into its performance and make well-informed decisions about the resources needed for their respective implementations.

N.B The current version is console-based, the full fledged version would be hosted and also fully customizable, and schemes library would also be pluggable 

## Features

- Generates client balances using a distributed random number generator.
- Supports both plain and encrypted logic for financial operations to give proper context.
- Outputs results to an Excel file for further analysis.
- Uses `rich` for a user-friendly console interface.

## Requirements

- Python 3.7+
- `rich` for enhanced console output.
- `pandas` for data manipulation and export.

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/leodarkseid/Homomorphic-Encryption-Comparative-Tool

cd Homomorphic-Encryption-Comparative-Tool
```

### 2. Create a Virtual Environment
It’s recommended to create a virtual environment to manage your project dependencies; you can do that with,

`python3 -m venv venv
`
### 3. Activate the Virtual environment

### 4. Install dependencies

`pip install -r requirements.txt`

### 5. Run the Script

`python main.py`

## Usage

The script will prompt you to enter the number of clients for whom you want to generate balances. The script then performs various financial operations and saves the results to an Excel file named all.xlsx.

## Contributing

Contributions are welcome! If you have ideas for improvements or run into issues, feel free to open an issue or submit a pull request.

## License 
This project is licensed under the MIT License.
