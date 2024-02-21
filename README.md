
# TikTok Mass Reporter

This is a tool designed for mass reporting users on TikTok. It allows users to specify the number of threads for parallel processing and the type of report to be filed against the target user.

## Disclaimer

This tool is created for educational purposes and ethical use only. Any misuse of this tool for malicious purposes is not condoned. The developers of this tool are not responsible for any illegal or unethical activities carried out using this tool.

## Requirements

To run this tool, you need to have the following dependencies installed:

- `tls-client`
- `httpx`
- `requests`
- `fade`

You can install these dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository to your local machine.
2. Install the required dependencies as mentioned above.
3. Ensure you have a `config.json` file containing your configuration settings.
4. Run the `main.py` script.
5. Follow the prompts to specify the number of threads and the report type.
6. Provide the report link of the target user.
7. The tool will start reporting the user using multiple threads.

## Configuration

The `config.json` file should contain any necessary configurations, such as proxies.

```json
{
  "proxy": "http://username:password@proxy_ip:proxy_port"
}
```

## Contributing

Contributions are welcome! If you'd like to improve the tool, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```
