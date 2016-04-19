--Station'ssid and Password setup. You must change for your setting.
st-ssid="fucxy-test";
st-pw="a12341234";
--Initail config
wifi.setmode(3)
wifi.sta.autoconnect(0)

wifi.sta.config(st-ssid, st-pw)
wifi.sta.connect()
cfg={}
cfg.ssid="node_"
cfg.pwd="a12341234"
wifi.ap.config(cfg)
