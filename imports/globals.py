#!/usr/bin/env python

# Malware DB - the most awesome free malware database on the air
# Copyright (C) 2014, Yuval Nativ, Lahad Ludar, 5Fingers

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import sys
import os
import random


class init:

    def init(self):
        # Global Variables
        version = "0.6.0 Moat"
        appname = "theZoo"
        codename = "Moat"
        authors = "Yuval Nativ, Lahad Ludar, 5fingers"
        maintainers = [ "Shahak Shalev", "Yuval Nativ" ]
        github_add = "https://www.github.com/ytisf/theZoo"
        licensev = "GPL v3.0"
        fulllicense = appname + " Copyright (C) 2016 " + authors + "\n"
        fulllicense += "This program comes with ABSOLUTELY NO WARRANTY;" + \
            " for details type '" + sys.argv[0] + " -w'.\n"
        fulllicense += "This is free software, and you are welcome to redistribute it."

        usage = '\nUsage: ' + sys.argv[0] + \
            ' -s search_query -t trojan -p vb\n\n'
        usage += 'The search engine can search by regular search or '
        usage += 'using specified arguments:\n\n'
        usage += 'OPTIONS:\n   -h  --help\t\tShow this message\n'
        usage += '-t  --type\t\t'
        usage += 'Malware type, can be virus/trojan/botnet/spyware/ransomeware.'
        usage += '\n\t-p  --language\t'
        usage += 'Programming language, can be c/cpp/vb/asm/bin/java.\n'
        usage += '   -u  --update\t\t'
        usage += 'Update malware index. Rebuilds main CSV file. \n'
        usage += '   -s  --search\t\tSearch query for name or anything. \n'
        usage += '   -v  --version\tPrint the version information.\n'
        usage += '   -w\t\t\tPrint GNU license.\n'

        conf_folder = 'conf'
        eula_file = conf_folder + '/eula_run.conf'
        maldb_ver_file = conf_folder + '/db.ver'
        giturl = 'https://github.com/ytisf/theZoo/blob/master'


##########################################################
class Completer:
    def __init__(self, commands):
        self.commands = commands
        self.prefix = None

    def complete(self, prefix, index):
        if prefix != self.prefix:
            self.matchingCommand = [
                w for w in self.commands if w.startswith(prefix)
                ]
            self.prefix = prefix
        try:
            return self.matchingCommand[index]
        except IndexError:
            return None
################################################################


class vars:
    version = "0.6.0 'Moat'"
    appname = "Malware DB"
    authors = "Yuval Nativ, Lahad Ludar, 5fingers"
    maintainers = ["Shahak Shalev", "Yuval Nativ"]
    github_add = "https://www.github.com/ytisf/theZoo"
    licensev = "GPL v3.0"

    ############ DEBUGGING ###############
    #### SET TO ZERO BEFORE COMMIT #######

    # DEBUG_LEVEL 0 = NO DEBUGGING
    # DEBUG_LEVEL 1 = DEBUG DOWNLOADS
    # DEBUG_LEVEL 2 = DEBUG SQL QUERIES

    DEBUG_LEVEL = 0

    fulllicense = appname + " Copyright (C) 2017 " + authors + "\n"
    fulllicense += "This program comes with ABSOLUTELY NO WARRANTY;" + \
        " for details type '" + sys.argv[0] + " -w'.\n"
    fulllicense += "This is free software, and you are welcome to redistribute it."

    usage = '\nUsage: ' + sys.argv[0] + ' -s search_query -t trojan -p vb\n\n'
    usage += 'The search engine can search by regular search or using'
    usage += ' specified arguments:\n\nOPTIONS:\n'
    usage += '\t-h  --help\t\tShow this message\n'
    usage += '\t-t  --type\t\t'
    usage += 'Malware type, can be virus/trojan/botnet/spyware/ransomeware.\n'
    usage += '\t-p  --language\tProgramming language, can be '
    usage += 'c/cpp/vb/asm/bin/java.\n   -u  --update\t\t'
    usage += 'Update malware index. Rebuilds main CSV file. \n'
    usage += '\t-s  --search\t\tSearch query for name or anything. \n'
    usage += '\t-v  --version\tPrint the version information.\n'
    usage += '\t-w\t\t\tPrint GNU license.\n'

    # :todo: add filter usage

    opts = [
            ("type", (
                "virus",
                "worm",
                "ransomware",
                "botnet",
                "apt",
                "rootkit",
                "trojan",
                "exploitkit",
                "dropper"
            )),
            ("architecture", (
                "x86",
                "x64",
                "arm",
                "web"
            )),
            ("platform", (
                "win32",
                "win64",
                "android",
                "ios",
                "mac",
                "*nix32",
                "*nix64",
                "symbian"
            )),
            ("language", (
                "c",
                "cpp",
                "asm",
                "bin",
                "java",
                "apk",
                "vb",
                "php"
            )),
        ]

    conf_folder = 'conf'
    eula_file = conf_folder + '/eula_run.conf'
    maldb_ver_file = conf_folder + '/db.ver'
    db_path = conf_folder + "/maldb.db"
    giturl_dl = 'https://github.com/ytisf/theZoo/raw/master/'
    giturl = 'https://github.com/ytisf/theZoo'

    with open(maldb_ver_file, 'r') as f:
        db_ver = f.read()

    # ASCII Art is a must...
    # screen = random.randrange(1, 6)
    screen = 3

    if screen is 1:
        maldb_banner = "\n"
        maldb_banner += "        sMMs              oMMy      \n"
        maldb_banner += "        :ooooo/        /ooooo:      \n"
        maldb_banner += "        ```+MMd````````hMMo```      \n"
        maldb_banner += "        oNNNMMMNNNNNNNNMMMNNNs      \n"
        maldb_banner += "     /oodMMdooyMMMMMMMMyoodMMdoo/   \ttheZoo "
        maldb_banner += version + "\n"
        maldb_banner += "  `..dMMMMMy. :MMMMMMMM/  sMMMMMm..`\t DB ver. "
        maldb_banner += db_ver + "\n"
        maldb_banner += "  dmmMMMMMMNmmNMMMMMMMMNmmNMMMMMMmmm\n"
        maldb_banner += "  NMMyoodMMMMMMMMMMMMMMMMMMMMdoosMMM\t"
        maldb_banner += giturl + "\n"
        maldb_banner += "  NMM-  sMMMNNNNNNNNNNNNNNNMMy  .MMM\n"
        maldb_banner += "  NMM-  sMMy``````````````sMMy  .MMM\n"
        maldb_banner += "  ooo.  :ooooooo+    +ooooooo/  `ooo\n"
        maldb_banner += "           /MMMMN    mMMMM+         \n"
        maldb_banner += "\t" * 5 + " authors: " + authors + "\n"
        maldb_banner += "\t" * 5 + " maintained by: "
        maldb_banner += ", ".join(maintainers) + "\n"
        maldb_banner += "\t" * 5 + " github: " + giturl + "\n\n"

    elif screen is 2:
        maldb_banner = "           ____.----. \n"
        maldb_banner += " ____.----'          \ \n"
        maldb_banner += "  \                    \ \ttheZoo " + version + "\n"
        maldb_banner += "    \          ____.----'`--.__ \t" + giturl + "\n"
        maldb_banner += "     \___.----'          |     `--.____\n"
        maldb_banner += "    /`-._                |       __.-' \ \n"
        maldb_banner += "   /     `-._            ___.---'       \ \n"
        maldb_banner += "  /          `-.____.---'                \ \n"
        maldb_banner += " '_         /   |   \            __.--'--'\n"
        maldb_banner += "   `-._    /    |    \     __.--'     |\n"
        maldb_banner += "     | `-./     |     \_.-'           |\n"
        maldb_banner += "     |          |                     |\n"
        maldb_banner += "     |          |      Free Malwares  |\n"
        maldb_banner += "     |          |          & Hugs     |\n"
        maldb_banner += "_____|          |                     |______\n"
        maldb_banner += "     `-.        |  /\              _.-'\n"
        maldb_banner += "        `-.     |  || UP    __..--'\n"
        maldb_banner += "           `-.  |      __.-'\n"
        maldb_banner += "              `-|__.--'\n"

    elif screen is 3:
        maldb_banner = "    __  ___      __                               ____  ____\n"
        maldb_banner += "   /  |/  /___ _/ /      ______ _________        / __ \/ __ )\n"
        maldb_banner += "  / /|_/ / __ `/ / | /| / / __ `/ ___/ _ \______/ / / / __ |\n"
        maldb_banner += " / /  / / /_/ / /| |/ |/ / /_/ / /  /  __/_____/ /_/ / /_/ /\n"
        maldb_banner += "/_/  /_/\__,_/_/ |__/|__/\__,_/_/   \___/     /_____/_____/\n\n"
        maldb_banner += " " * 20 + " version: " + version + "\n"
        maldb_banner += " " * 20 + " db_version: " + db_ver + "\n"
        maldb_banner += " " * 20 + " built by: " + authors + "\n"
        maldb_banner += " " * 20 + " maintained by: " + ', '.join(maintainers)
        maldb_banner += "\n"
        maldb_banner += " " * 20 + " github: " + giturl + "\n\n"

    elif screen is 4:
        maldb_banner = "\n"
        maldb_banner += ".       ..       .\n"
        maldb_banner += "|\      ||      /|\n"
        maldb_banner += "| \     ||     / |\n"
        maldb_banner += "|  \    ||    /  |\n"
        maldb_banner += "|  :\___JL___/   |\n"
        maldb_banner += "|  :|##XLJ: :|   |\n"
        maldb_banner += "'\ :|###||: X|  /'\n"
        maldb_banner += "  \:|###||:X#| /\n"
        maldb_banner += "   |==========|\n"
        maldb_banner += "    |###XXX;;|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##Xn:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##Xn:: :|\n"
        maldb_banner += "    |##XX:: n|\n"
        maldb_banner += "    |##XX:: U|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##Xn:: :|\n"
        maldb_banner += "    |##XU:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: n|\n"
        maldb_banner += "    |##XX:: U|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##Xn:: :|\n"
        maldb_banner += "    |##XU:: :|\n"
        maldb_banner += "    |##Xn:: :|\t"
        maldb_banner += "theZoo " + version + "\n"
        maldb_banner += "    |##XU:: :|\t  " + giturl + "\n"
        maldb_banner += "    |##XX:: :|\tauthors: " + authors + "\n"
        maldb_banner += "    |##XX:: :|\tmaintained by: "
        maldb_banner += ', '.join(maintainers) + "\n"
        maldb_banner += "    |##XX:: :|\tgithub: " + giturl + "\n"
        maldb_banner += "    |##,_,: :|\n"
        maldb_banner += "    |./ T \.:|\n"
        maldb_banner += "    || o|o |:|\n"
        maldb_banner += "    ||  |  |:|\n"
        maldb_banner += "  .============.\n"
        maldb_banner += " .==============.\n"
        maldb_banner += ".================.\n\n"

    elif screen is 5:
        maldb_banner = "\n"
        maldb_banner += "_______________________________________\n"
        maldb_banner += "|\ ___________________________________ /|\n"
        maldb_banner += "| | _                               _ | |\n"
        maldb_banner += "| |(+)        _           _        (+)| |\n"
        maldb_banner += "| | ~      _--/           \--_      ~ | |\n"
        maldb_banner += "| |       /  /             \  \       | |\n"
        maldb_banner += "| |      /  |               |  \      | |\n"
        maldb_banner += "| |     /   |               |   \     | |\n"
        maldb_banner += "| |     |   |    _______    |   |     | |\n"
        maldb_banner += "| |     |   |    \     /    |   |     | |\n"
        maldb_banner += "| |     \    \_   |   |   _/    /     | |\n"
        maldb_banner += "| |      \     -__|   |__-     /      | |\n"
        maldb_banner += "| |       \_                 _/       | |\n"
        maldb_banner += "| |         --__         __--         | |\n"
        maldb_banner += "| |             --|   |--             | |\n"
        maldb_banner += "| |               |   |               | |\n"
        maldb_banner += "| |                | |                | |\n"
        maldb_banner += "| |                 |                 | |\n"
        maldb_banner += "| |                                   | |\n"
        maldb_banner += "| |            T H E  Z O O           | |\n"
        maldb_banner += "| |   I S   G O O D   F O R   Y O U   | |\n"
        maldb_banner += "| | _             %s      _ | |\n" % version
        maldb_banner += "| |(+)                             (+)| |\n"
        maldb_banner += "| | ~                               ~ | |\n"
        maldb_banner += "|/ ----------------------------------- \|\n"
        maldb_banner += "---------------------------------------\n"
        maldb_banner += "\tmaintained by: %s\n" % ', '.join(maintainers)
        maldb_banner += "\tgiturl: %s\n" % giturl
        maldb_banner += "\tauthors: %s\n" % authors
