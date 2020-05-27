class User:
    def __init__(self, name, login, password, asset):
        self.name = name
        self.login = login
        self.password = password
        self.asset  = asset 

    def login (name, login, password):
        if login in account.keys():
            if password in account[login]:   
                    print (name + '您好:')
                    return 1

        else:   
            print ("帳號或密碼不正確")
            return -1
    def register (name, login, password):
        temp = User(name, login, password, 0)
        userlist.append(temp)
        if login not in account.keys():
            account[login] = password
        if name not in UserAsset.keys():
            UserAsset[name] = temp.asset
            print('帳戶註冊成功')
        else:
            print('會員帳號已存在,請重新註冊')
if __name__ == "__main__":
    
    flag = 0
    userlist =  list()
    account  =  dict()
    UserAsset = dict()
    while (flag != -1):
        operation = 0
        flag = input("註冊帳戶請按1, 已有帳戶請按2, 若要結束交易請按-1:")
        flag = int(flag)
        if (flag == 1):
            name     = input("請輸入用戶名稱:")
            login    = input("會員帳號:")
            password = input("會員密碼:")
            User.register (name, login, password)
        elif(flag == 2):
            name = input ("請輸入您的用戶名稱:")
            login = input("請輸入您的帳號:")
            password = input("請輸入您的密碼:")
            if (User.login(name, login, password) == 1):
                while (operation != -1):
                    operation = input("存款請按1:, 提款請按2:, 查詢帳戶餘額請按3, 結束交易請按-1:")
                    operation = int(operation)
                    if  (operation == 1):
                        deposit = input("請輸入存款金額並放入紙鈔:")
                        deposit = int(deposit)
                        UserAsset[name] = int(UserAsset[name])
                        UserAsset[name] = UserAsset[name] + deposit
                    elif(operation == 2):
                        withdraw = input("請輸入提款金額:")
                        withdraw = int(withdraw)
                        UserAsset[name] = int(UserAsset[name])
                        UserAsset[name] = UserAsset[name] - withdraw
                    elif(operation == 3):
                        UserAsset[name] = str(UserAsset[name])
                        print('您的餘額為:' + UserAsset[name] )
            else:
                continue

    
    print('交易完畢,感謝您的使用')
         


