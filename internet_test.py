import speedtest


def get_internet_speed_info():
    servers = []

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download()
    s.upload()

    results_dict = s.results.dict()
    print results_dict
    download_mbps = round(results_dict["download"] / 1000000.0, 2)
    upload_mbps = round(results_dict["upload"] / 1000000.0, 2)
    server_name = results_dict["server"]["name"]
    ping = results_dict["ping"]
    timestamp = results_dict["timestamp"]

    return [timestamp, server_name, ping, download_mbps, upload_mbps]


if __name__ == '__main__':
    get_internet_speed_info()