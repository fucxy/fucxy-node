--Gateway's ssid and Password setup. You must change for your setting.
gateway_ssid="fucxy-test";
gateway_pw="qwerty1qaz2wsx";
--Place for save the available station
sta_list={}
--Ap's init_config
ap_cfg={};
--Ap's ip config
ap_ip_cfg={}
--Ap's dhcp config
ap_dhcp_cfg ={}
--Other staff
sub_net_stage=1
online=0
wifi.setmode(3)
wifi.sta.autoconnect(0)
wifi.stopsmart()
wifi.sta.disconnect()
print("WSNSBS"..string.sub(crypto.toHex(crypto.encrypt("AES-ECB", "1qaz2wsx12345678", "WSNSBS")),0,9))
print("".."0".."0")
print(string.format("%x",node.chipid())

