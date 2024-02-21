
# TikTok Mass Reporter

<p align="center">
  <img src="https://i.imgur.com/e4AeCy9_d.webp?maxwidth=760&fidelity=grand" alt="Preview" width="600">
</p>
This is a tool designed for mass reporting users on TikTok. It allows users to specify the number of threads for parallel processing and the type of report to be filed against the target user.

## Features
- Fully Requests Based
- Undetected Reporter
- 14 Report Types
- Easy & Fast To Setup
- Multi Threading Support
- Auto Proxy Scraper

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

1. Clone or download the repository to your local machine
2. Install the required dependencies as mentioned above
3. Run the `start.bat` script
4. Follow the prompts to specify the number of threads and the report type
6. Provide the report link of the target user

## How To Get Report URL

1. Open the profile or video in desktop browser
2. Press `ctrl + shift + i` and open developer tools
3. Go to the network tab and press `ctrl + l`
4. Now report the user/video manually as soon as you report
you will see a new request which will contain the word `feedback`
5. Click on the request and copy the request url, thats  it!
   
## Configuration

If you want to use proxy youself then put in `config.json`, in this format.

```json
{
  "proxy": "http://username:password@proxy_ip:proxy_port"
}
```

## Preview


[![Star History Chart](https://api.star-history.com/svg?repos=JOY6IX9INE/TikTok-Mass-Reporter&type=Date)](https://star-history.t9t.io/#JOY6IX9INE/TikTok-Mass-Reporter&Date)
