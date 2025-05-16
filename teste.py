import speedtest as st


def test_speed():
    test = st.Speedtest()

    down_speed = test.download()
    down_speed = round(down_speed/10**6, 2)
    print(f"Download speed: {down_speed} Mbps")

    up_speed = test.upload()
    up_speed = round(up_speed/10**6, 2)
    print(f"Upload speed: {up_speed} Mbps")

    ping = test.results.ping
    print(f"Ping: {ping} ms")


test_speed()
