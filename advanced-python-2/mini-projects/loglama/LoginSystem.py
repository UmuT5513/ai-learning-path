import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} - {levelname} - {message}",
                    style="{",
                    datefmt="%Y-%m-%d %H:%M",
                    filename="login_system.log",
                    filemode='a',
                    encoding='utf-8'
                    )

users = {}
keys = users.keys()
values = users.values()
def register(username, password):
    if username in keys:
        # WARNING: kullanıcı zaten kayıtlı
        logging.warning(f"{username=}: Kullanıcı zaten kayıtlı.")
    elif len(password) < 6:
        # ERROR: zayıf parola 
        logging.error(f"{password=} Zayıf parola. Parola 6 haneden kısa olamaz.")
    else:
        users[username] = password
        # INFO: kayıt başarılı
        print(users)
        logging.info("Kayıt başarılı")


def login(username, password):
    password_count=0
    if not users[username] == password:
        password_count += 1
        # WARNING: parola yanlış
        logging.warning(f"{password=} parola yanlış")
        
        if password_count == 3:
            # ERROR: 3 kere üst üste yanlış parola
            logging.error("3 kez üst üste yanlış kombinasyon denediniz.")
            password_count = 0
    else:
        logging.info("Giriş başarılı")

def main():
    run = True
    while run:
        flag = input("\n> Kayıt olmak için 1, Giriş yapmak için 0 a basın: ")
        if flag == "1":
            username = input("> Kullanıcı adı: ")
            password = input("> Parola: ")
            register(username, password)
        else:
            username = input("> Kullanıcı adı: ")
            password = input("> Parola: ")
            try:
                login(username, password)
            except KeyError:
                logging.warning(f"{username=}: Kullanıcı kayıtlı değil.")
            

        if input("\n> Çıkış için q devam etmek için herhangi bir karaktere basın: ") == "q":
            run = False
        else:
            continue
        

if __name__ == "__main__":
    main()

        

        
            