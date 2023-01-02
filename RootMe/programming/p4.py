"""
Challenge: Uncompress me

HOW TO USE:
    1. Press enter till you get the "shellcode text"
    2. Press s and then enter, to send the pm to the bot
    3. Press enter, and you should get the password
Password:
tumasp0wned
"""

import socket
import re
import math
import base64
import zlib
import codecs

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
            res = re.search('r :\S+', res).group()
            res = res.replace("r :", "")
            result = base64.b64decode(res)
            result = zlib.decompress(result).decode()
            print("REPLYING ANSWER:  %s :!ep4 -rep %s" % (bot, result))
            irc.send(get_msg("PRIVMSG %s :!ep4 -rep %s" % (bot, result)))
        cmd = input('command: ')
        if cmd == 'e':
            run = False
        elif cmd == 's':
            irc.send(get_msg("PRIVMSG %s :!ep4" % bot))
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