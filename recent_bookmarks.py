#!/usr/local/bin/python3

import pinboard
import json
from pathlib import Path

folder= Path("docs/links")

api_token="stuartcw:267212e5c7227eb97ffe"
pb = pinboard.Pinboard(api_token)


tags="!fromtwitter .NET | 0-todo 67P 公式サイト » 個人用ツールバーフォルダ – ACL2020 adidas ニュース一覧 Ajax amazon android ansible anti-spam API apollo Apollo appengine Architecture automation avfc 横浜F・マリノス 横浜FM 日本語 Bash blogging BLOGOLA blogola.jp BLOGOLA横浜FM book bot business C C# cancer Career caving celticfc CGI chart cheatsheet circuits cli command-line Computer concurrency cooking CountdownToMars covid covid19 daihyo data database datascience DAZN debugging delicious design development dictionary disk django dna dnd documentation dom earthquake ECMAScript elasticsearch electronics email English erlang ethernet Euro2016 excel exim explorer extension extensions facebook Facebook Favorites_Bar FC fcryukyu fcunion filetype:pdf find Firefox firefox:bookmarks firefox:toolbar FirefoxとMozillaのリンク firewall flash flask fmarinos food football for for:@twitter for:carter_bradford for:deusx for:joi_ito for:judell for:philgyford for:stuartcw framework Freeware fun Geek gekisaka git github go golang graphics grep GTD hacks Halloween Health html HTTP humor humour i18n ibm IFTTT ilo IM imported Internet interview iOS IRC jabber Japan Japanese Javascript jfa jpn jscript json Kanji kernel keyboard kibana kids Later LED lego lfc library Linux logstash mac macos macstoriesdeals mainframe make management marinos markdown mars Math mdm media:document memory Menieres messaging mib Microsoft Mobile monitoring Montedio MovableType Mozilla MSN MT Music nasa Network networking OID OpenSource oracle os osx OSX paper password patterns performance Perl phone PHP Physics PIC ping.fm Plugins Pluto PlutoFlyby pocket Podcast Popular postgres PostgreSQL procrastination programming Programming project projectmanagement Projects Python python3 QA rails RaspberryPi recipe recipes reddit reference Reference REST Rest router RPC rust sanfrecce Saved_Tabs scalability science scifi Search security shell soccer software Software Solaris SQLite sqllite startrek Stuxnet sysadmin syslog technology terminal ThankYouBoss time Tips To_Read tools travel tutorial twisted Typography ubuntu Unread usb Utilities utv via:ttscoff vimeo visualization vitamin-d Vmware web web_techstack Web2.0 webserver webservices WMI XML XP yokohama zelvia zen zxspectrum".split()
tags ="python"

def make_link(url,description):
    return "["+description+"]("+url+")"

with open(folder/Path("index.md"),"w") as index_file:

    for tag in tags:

        index_file.write("* "+make_link("links/"+tag+"_links",tag)+"\n")

        recents=pb.posts.recent(tag=[tag])

        tag_document_filename= Path(tag+"links.md")

        with open(folder/tag_document_filename,"w") as output_file:
            output_file.write("#"+tag+"\n")
            for bookmark in recents["posts"]:
                output_file.write("* "+make_link(bookmark.url,bookmark.description)+"\n")



