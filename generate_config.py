import ConfigParser
import io

#Sample code used from docs.python.org ConfigParser
config = ConfigParser.RawConfigParser(allow_no_value=True)

s1 = "General"
config.add_section(s1)
config.set(s1, 'broker_url','amqp://guest@localhost//')

s2 = "Download Settings"
config.add_section(s2)
config.set(s2, 'server_url','http://172.16.1.10:8000')

s3 = "FTP Settings"
config.add_section(s3)
config.set(s3, 'host','172.16.1.10')
config.set(s3, 'username','user_name')
config.set(s3, 'password','pa$$w0rd')
config.set(s3, 'root_dir', 'raid0')

#Write the config to file. This will be the name looked for
with open('my.config' , 'wb') as configfile:
    config.write(configfile)
