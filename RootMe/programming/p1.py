"""
Challenge: Go back to college

HOW TO USE:
    1. Press enter till you get the "shellcode text"
    2. Press s and then enter, to send the pm to the bot
    3. Press enter, and you should get the password
Password:
jaimlefr0m4g
"""

import socket
import re
import math

server = 'irc.root-me.org'
port = 6667
nickname = 'Rither'
channel = "#root-me_challenge"
bot = "Candy"
run = True

def connect():
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc.connect((server, port))
    print('Connecting to: %s:%d' % (server, port))

    irc.send(get_msg("NICK %s" %nickname))
    irc.send(get_msg("USER %s %s bla :%s" % (nickname, nickname, nickname)))
    print('Joining: %s' % channel)
    irc.send(get_msg("JOIN %s" % channel))
    return irc

def main(irc):
    global run
    while run:
        text = irc.recv(2040)
        print(text)
        res = try_decode(text)
        if res == None:
            break
        if 'Candy!Candy@root-me.org PRIVMSG Rither' in res:
            text = text.decode()
            a = re.search('\:\d+', text).group()
            b = re.search(' \d+', text).group()
            num1 = a.replace(":", "")
            num2 = b.replace(" ", "")
            num2 = int(num2)
            num1 = math.sqrt(int(num1))
            result = round(num1 * num2, 2)
            print("REPLYING ANSWER:  %s :!ep1 -rep %s" % (bot, result))
            irc.send(get_msg("PRIVMSG %s :!ep1 -rep %s" % (bot, result)))
        cmd = input('command: ')
        if cmd == 'e':
            run = False
        elif cmd == 's':
            irc.send(get_msg("PRIVMSG %s :!ep1" % bot))
            print('Sending msg to bot: %s' % bot)

def try_decode(text):
    try:
        return text.decode()
    except:
        return None

def get_msg(msg):
    msg = "%s\r\n" % msg
    return msg.encode()


if __name__ == '__main__':
    irc = connect()
    main(irc)