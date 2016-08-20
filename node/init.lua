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
id=string.format("%x",node.chipid())
--Wifi ap setting
function ap_setting()
  wifi.ap.dhcp.stop()
  if(online!=0) then
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
function sta_connect(t)
  count = #sta_list
  has_gateway=0
  for k =0,count do
    sta_list[k]=nil
  end
  count=0
  for k,v pairs(t) do
    print(k.." : "..v)
    if (v == gateway_ssid) then
       has_gateway = 1
    else if(string.sub(v,1,4)=="node") then
       sta_list[count] = v
       count = count + 1
    end
  end
  --Select node
  if(has_gateway == 1) then
    print("Gateway find!")
    wifi.sta.config(gateway_ssid,gateway_pw)
    wifi.sta.connect() 
  else if (#sta_list != 0) then 
     
  else
    print("Detect no node!!") 
  end
end

--Server Run
function Server_Start() 
   count = 0
end


--Main Runtime
--Initail config
wifi.setmode(3)
wifi.sta.autoconnect(0)
wifi.stopsmart()
wifi.sta.disconnect()
wifi.sta.getap(sta_connect)
wifi.sta.getap(ap_connect)
if(wifi.sta.status()==STATION_CONNECTING) then
  online=1;
else
  
end
--Done for wifi setting

server = net.createServer(net.UDP,80)

server.close()
wifi.sta.disconnect()
