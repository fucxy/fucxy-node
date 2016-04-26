--Station'ssid and Password setup. You must change for your setting.
st_ssid="fucxy-test";
st_pw="1qaz2wsx123456";
--Ap's init_config
ap_cfg={};
--Ap's ip config
ap_ip_cfg={}
--Ap's dhcp config
ap_dhcp_cfg ={}
--Other staff
sub_net_stage=1
online=0
--Initail config
wifi.setmode(3)
wifi.sta.autoconnect(0)
wifi.stopsmart()
--Wifi ap setting
function ap_setting()
  wifi.ap.dhcp.stop()
  if(online==1) then
    ap_cfg.ssid="node_"..sub_net_stage..node.chipid()
  else
    ap_cfg.ssid="node_"..sub_net_stage..node.chipid()
  end
  ap_cfg.pwd="1qaz2wsx123456"..sub_net_stage
  wifi.ap.config(ap_cfg)
  --IP Setting
  ap_ip_cfg.ip = "192.168."..stage..".19"
  ap_ip_cfg.netmask = "255.255.255.0"
  ap_ip_cfg.gateway = ap_ip_cfg.ip
  wifi.ap.setip(ap_ip_cfg)
  --DHCP Setting
  dhcp_config.start = "192.168."..stage..".20"
  wifi.ap.dhcp.config(dhcp_config)
  wifi.ap.dhcp.start()
end
--Ap connect handler
wifi.eventmon.register(wifi.eventmon.AP_STACONNECTED, function(T) 
  print("\n\tAP - STATION CONNECTED".."\n\tMAC: "..T.MAC.."\n\tAID: "..T.AID)
end)
--wifi sta handler
function ap_connect(t)
  for k,v pairs(t) do
    print(k.." : "..v)
  end
end
wifi.sta.getap(ap_connect)
if(wifi.sta.status()==STATION_CONNECTING)
