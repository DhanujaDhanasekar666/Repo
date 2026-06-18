from app import device_status

def test_device_status():
    assert device_status() == "IoT Device Connected Successfully"
