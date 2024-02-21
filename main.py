import tls_client, httpx, requests
from datetime import datetime
import ctypes, json, os, time, random, re, sys
import concurrent.futures, fade, urllib

red = '\x1b[31m(-)\x1b[0m'
blue = '\x1b[34m(+)\x1b[0m'
green = '\x1b[32m(+)\x1b[0m'
yellow = '\x1b[33m(!)\x1b[0m'

ctypes.windll.kernel32.SetConsoleTitleW("TikTok Mass Reporter | Made With <3 By Joy")

banner = fade.fire("""
  _____ _ _    _____     _    
 |_   _(_) | _|_   _|__ | | __
   | | | | |/ / | |/ _ \'| |/ /
   | | | |   <  | | (_) |   < 
   |_| |_|_|\'_\' |_|\'___/|_|\'_\'
                 MASS REPORT TOOL""")

with open('config.json') as f:
    config = json.load(f)

class counter:
    success = 0
    failed = 0

class utils:
    @staticmethod
    def update_console_title():
        ctypes.windll.kernel32.SetConsoleTitleW(f"TikTok Mass Reporter | Sucess : {counter.success} | Failed : {counter.failed}")

    @staticmethod
    def get_proxies():
        with open('proxies.txt', 'w') as f:
            pass

        free_api = 'https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies'
        response = requests.get(free_api)
        
        if response.status_code == 200:
            with open('proxies.txt', 'a') as f:
                proxies = response.text.strip().split('\n')
                for proxy in proxies:
                    f.write(proxy.strip() + '\n')
        else:
            print(f"{utils.get_timestamp()} {red} Failed To Fetch Proxies!")

    @staticmethod
    def clear_console():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    @staticmethod
    def get_timestamp():
        time_idk = datetime.now().strftime('%H:%M:%S')
        timestamp = f'[\x1b[90m{time_idk}\x1b[0m]'
        return timestamp

def report(url, input_report_type):
    session = tls_client.Session(client_identifier="chrome112", random_tls_extension_order=True)

    if 'proxy' in config and config['proxy']:
        proxy = config['proxy']
        if "@" in proxy:
            user_pass, ip_port = proxy.split("@")
            user, password = user_pass.split(":")
            ip, port = ip_port.split(":")
            proxy_string = f"http://{user}:{password}@{ip}:{port}"
        else:
            ip, port = proxy.split(":")
            proxy_string = f"http://{ip}:{port}"
        
        session.proxies = {"http": proxy_string, "https": proxy_string}

    else:
        proxy = random.choice(open("proxies.txt", "r").readlines()).strip()
        ip, port = proxy.split(":")
        proxy_string = f"http://{ip}:{port}"
        session.proxies = {"http": proxy_string, "https": proxy_string}

    try:
        reason_format = re.search(r'reason=(\d+)', url)
        nickname_format = re.search(r'nickname=([^&]+)', url)
        if nickname_format:
            username_x = nickname_format.group(1)
            username = urllib.parse.unquote(username_x)
        if reason_format:
            reason_number = reason_format.group(1)
            report_url = url.replace(f"reason={reason_number}", f"reason={input_report_type}")
            report = session.get(report_url)
            if "Thanks for your feedback" in report.text:
                print(f"{utils.get_timestamp()} {green} Successfully Reported User : {username}")
                counter.success += 1
                utils.update_console_title()
            elif report.status_code == 200:
                print(f"{utils.get_timestamp()} {green} Successfully Reported User : {username}")
                counter.success += 1
                utils.update_console_title()
            else:
                print(f"{utils.get_timestamp()} {red} Unable To Report User : {username}")
                counter.failed += 1
                utils.update_console_title()
        else:
            pass
    except Exception as e:
        pass

if __name__ == "__main__":
    utils.clear_console(), print(banner)
    try:
        thread_count = int(input(f"{utils.get_timestamp()} {blue} Enter The Number Of Threads : "))
        print("")
    except ValueError:
        print(f"{utils.get_timestamp()} {red} Invalid Input, Please Enter A Valid Number Of Threads."), sys.exit()
    
    url = input(f"{utils.get_timestamp()} {blue} Enter The Report Link Of Target User : ")
    utils.clear_console(), print(banner)
    report_types = {
        1: (90013, "Violence"),
        2: (90014, "Sexual Abuse"),
        3: (90016, "Animal Abuse"),
        4: (90017, "Criminal Activities"),
        5: (9020, "Hate"),
        6: (9007, "Bullying"),
        7: (90061, "Suicide Or Self-Harm"),
        8: (90064, "Dangerous Content"),
        9: (90084, "Sexual Content"),
        10: (90085, "Porn"),
        11: (90037, "Drugs"),
        12: (90038, "Firearms Or Weapons"),
        13: (9018, "Sharing Personal Info"),
        14: (90015, "Human Exploitation"),
        15: (91015, "Under Age")
    }

    report_type = None
    for key, (code, option_name) in report_types.items():
        print(f"{key}. {option_name}")
    selected_serial = input(f"\n{utils.get_timestamp()} {blue} Enter The Number Of The Report Type : ")

    try:
        selected_serial = int(selected_serial)
        if selected_serial in report_types:
            report_type = report_types[selected_serial][0]
        else:
            print(f"{utils.get_timestamp()} {red} Invalid Input, Please Enter A Valid Report Type."), sys.exit()
    except ValueError:
        print(f"{utils.get_timestamp()} {red} Invalid Input, Please Enter A Valid Report Type."), sys.exit()
    
    utils.clear_console(), print(banner), utils.get_proxies()

    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_count) as executor:
        while True:
            executor.submit(report, url, report_type)
