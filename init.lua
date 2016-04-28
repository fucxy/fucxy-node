--Station'ssid and Password setup. You must change for your setting.
sta_ssid="fucxy-test";
sta_pw="1qaz2wsx123456";
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
wifi.sta.disconnect()
--Wifi ap setting
function ap_setting()
  wifi.ap.dhcp.stop()
  if(online==1) then
    ap_cfg.ssid="node_"..sub_net_stage..node.chipid()
  else
    ap_cfg.ssid="innode_"..sub_net_stage..node.chipid()
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
  connect_id= 0
  for k,v pairs(t) do
    print(k.." : "..v)
    if (v==st_ssid) then
      connect_id=k;
    else if(connect_id==0&&string.sub(v,1,4)=="node") then
      connect_id=k;
    end
  end
  if(t[connect_id]==sta_ssid) then
    
  end
end
wifi.sta.getap(ap_connect)
if(wifi.sta.status()==STATION_CONNECTING) then
  online=1;
else

end
