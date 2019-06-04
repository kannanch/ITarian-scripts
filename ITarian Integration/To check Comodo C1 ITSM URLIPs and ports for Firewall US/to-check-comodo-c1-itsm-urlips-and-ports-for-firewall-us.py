import socket
import sys

subdomain = "test"


def check_server(address, port, type, nr):
    try:
        if nr == 1:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((address, port))
            s.shutdown(2)
            print("Success connecting to %s on port %s %s" % (address, port, type))
            return "Successful"
        if nr == 2:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(10)
            request = bytearray.fromhex(
                "ef070401002d201bab1c00197e02e5bc3c31cd48b5a9e77250e09e50345d003395856ce81f2b7382dee72602f798b642f14140")
            # print(request)
            s.sendto(request, (address, port))
            recv, svr = s.recvfrom(1024)
            s.shutdown(2)
            print("Success connecting to %s on port %s %s" % (address, port, type))
            return "Successful"
        if nr == 3:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(10)
            request = bytearray.fromhex("000100002112a442324b47584530545977646c6a")
            # print(request)
            s.sendto(request, (address, port))
            recv, svr = s.recvfrom(1024)
            s.shutdown(2)
            print("Success connecting to %s on port %s %s" % (address, port, type))
            return "Successful"
        if nr == 4:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(10)
            request = bytearray.fromhex("000300082112a44257474b612f2f7a6f633237530019000411000000")
            # print(request)
            s.sendto(request, (address, port))
            recv, svr = s.recvfrom(1024)
            s.shutdown(2)
            print("Success connecting to %s on port %s %s" % (address, port, type))
            return "Successful"
    except:
        print("Connection to %s on port %s failed: %s %s" % (address, port, sys.exc_info()[:2], type))
        return "Failed    "


print("Firewall US instance\r\n")
print("Comodo Client - Communication (CCC)")
check_server(subdomain + ".itsm-us1.comodo.com", 443, "HTTPS", 1)
check_server("mdmsupport.comodo.com", 443, "HTTPS", 1)
check_server("54.93.214.133", 443, "HTTPS", 1)
check_server("plugins.itsm-us1.comodo.com", 443, "HTTPS", 1)
check_server(subdomain + ".itsm-us1.comodo.com", 443, "HTTPS", 1)
check_server("xmpp.itsm-us1.comodo.com", 443, "HTTPS", 1)
check_server("one-us.comodo.com", 443, "HTTPS", 1)
check_server("download.comodo.com", 443, "HTTPS", 1)
check_server("download.comodo.com", 80, "HTTP", 1)
check_server("178.255.82.5", 443, "HTTPS", 1)
check_server("178.255.82.5", 80, "HTTP", 1)
check_server("cdn.download.comodo.com", 443, "HTTPS", 1)
check_server("cdn.download.comodo.com", 80, "HTTP", 1)
check_server("104.16.61.31", 443, "HTTPS", 1)
check_server("104.16.61.31", 80, "HTTP", 1)
check_server("104.16.60.31", 443, "HTTPS", 1)
check_server("104.16.60.31", 80, "HTTP", 1)
check_server("ocsp.comodoca.com", 80, "HTTP", 1)
check_server("crl.comodoca.com", 80, "HTTP", 1)
check_server("patchportal.one.comodo.com", 443, "HTTPS", 1)
check_server("23.229.69.170", 443, "HTTPS", 1)
check_server("cescollector.cwatchapi.com", 443, "HTTPS", 1)
print("Comodo Client - Security (CCS)")
check_server("fls.security.comodo.com", 4447, "UDP", 2)
check_server("fls.security.comodo.com", 53, "UDP", 2)
check_server("199.66.201.16", 4447, "UDP", 2)
check_server("199.66.201.16", 53, "UDP", 2)
check_server("fls.security.comodo.com", 4448, "TCP", 1)
check_server("fls.security.comodo.com", 80, "TCP", 1)
check_server("199.66.201.16", 4448, "TCP", 1)
check_server("199.66.201.16", 80, "TCP", 1)
check_server("valkyrie.comodo.com", 443, "HTTPS", 1)
check_server("cdn.download.comodo.com", 80, "HTTP", 1)
check_server("104.16.61.31", 80, "HTTP", 1)
check_server("104.16.60.31", 80, "HTTP", 1)
check_server("cdn.download.comodo.com", 443, "HTTPS", 1)
check_server("104.16.61.31", 443, "HTTPS", 1)
check_server("104.16.60.31", 443, "HTTPS", 1)
check_server("download.comodo.com", 80, "HTTP", 1)
check_server("178.255.82.5", 80, "HTTP", 1)
check_server("download.comodo.com", 443, "HTTPS", 1)
check_server("178.255.82.5", 443, "HTTPS", 1)
check_server("s3-eu-west-1.amazonaws.com", 443, "HTTPS", 1)
check_server(subdomain + ".itsm-us1.comodo.com", 443, "HTTPS", 1)
check_server("ocsp.comodoca.com", 80, "HTTP", 1)
check_server("crl.comodoca.com", 80, "HTTP", 1)
print("Comodo Remote Control")
check_server("xmpp.itsm-us1.comodo.com", 443, "HTTPS", 1)
check_server("stun.l.google.com", 19302, "UDP", 3)
check_server("18.196.107.208", 3478, "UDP", 4)
check_server("52.29.123.206", 3478, "UDP", 4)
check_server("34.232.133.48", 3478, "UDP", 4)
check_server("18.208.23.45", 3478, "UDP", 4)
