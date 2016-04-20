--Station'ssid and Password setup. You must change for your setting.
st_ssid="fucxy-test";
st_pw="1qaz2wsx123456";
--Ap's init_config
ap_cfg={};
ap_cfg.ssid="innode_"..node.chipid()
ap_cfg.pwd="1qaz2wsx"

--Initail config
wifi.setmode(3)
wifi.sta.autoconnect(0)
wifi.sta.config(st_ssid, st_pw)
wifi.ap.config(ap_cfg)
--wifi ap handler

