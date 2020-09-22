#!/usr/bin/python3
import os, sys



pythoncfg = {
    'Injection': ['execFile','input','commands','subprocess'],
    'Risky API': ['pickle.load','eval']
}

javacfg = {
    'Injection': ['Runtime', 'ProcessBuilder', 'CommandLine','zookeeper.Shell'],
    'Path Traversal': ['getAbsolutePath'],
    'Deserialization': ['XMLDecoder', 'XStream','readObject','readObjectNoData','readResolve','readExternal','InvocationHandle','ObjectInputStream','java.lang.reflect.InvocationHandler','MethodHandler.invoke','Object.finalize'],
    'Weak Random': ['Java.util.Random'],
    'URL Injection': ['url=', 'href='],
    'XML External Entity (XXE)': ['DocumentBuilder','XMLInputFactory','SAXReader','SAXParser','SAXBuilder','XMLReader','DocumentHelper','XMLInputFactory','XMLStreamReader'],
    'URL authorization bypass': ['.getRequestURL','.getRequestURI'],
    'File-handling validation': ['ZipInputStream'],
    'ZIP of Death': ['ZipFile', 'ZipInputStream'],
    'Information Leakage': ['FileNotFoundException','JARException','MissingResourceException','acl.NotOwnerException','ConcurrentException','ModificationException','InsufficientResourceException','BindException','OutOfMemoryError','StackOverflowException','SQLException']
}

jscfg = {
    'Injection API': ['child_process.spawn', 'child_process.spawnSync','child_process.exec','child_process.execSync','child_process.execFile','child_process.execFileSync','child_process.fork'],
    'Risky API': ['eval','execScript']
}

generalcfg = {
    'Weak Encryption': ['Blowfish', 'DES', '3DES', 'RC4', 'ARC4',  'IDEA', 'ECB', 'CBC', 'SSL', 'ssl', 'TLS', 'tls', 'Base64', 'base64','RIPEMD', 'XOR'],
    'Weak Hashing': ['MD4', 'MD5', 'SHA1'],
    'Insecure Protocol': ['SSL',  'HTTP', 'http:', 'AMQP', 'FTP', 'ftp:', 'Telnet'],
    'Hardcoded Information': ['Password', 'password', 'passwd', 'pass', 'IP address', 'IP', 'email' 'Email', 'URL', 'url', 'mobile', 'Mobile', 'Full Name', 'FullName', 'fullname', 'lastname'],
    'Auth': ['JWT', 'Jwt', 'jwt', 'iss', 'exp', 'token', 'skey', 'Token', 'secret', 'cert']
}

cfg = {
    'python': pythoncfg,
    'java': javacfg,
    'generic': generalcfg
}


def search(type, path):
    config = cfg[type]
    for section in config:
        for value in config[section]:
            #print(section + ' ' + value)
            res = os.system("grep -r --silent '" + value + "' " + path)
            if res == 0:
                print(section + ': ''Found ' + value)


#search(javacfg, '/etc/passwd')
path = sys.argv[1]
type = sys.argv[2]


search(type, path)
