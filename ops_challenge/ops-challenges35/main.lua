-- HEAD --

description = [[
        To check if the path works and see if the HTTP port is open
]]

author = "Jin Kim"
date = "11/20/2020"

-- RULE --

local http = require "http"
local shortport = require "shortport"
local stdnse = require("stdnse")

portrule = function(host,port)
        return port.number == 80 and
                port.state == "open"
end

-- ACTION --

action = function(host,port)
        path = stdnse.get_script_args('paths')

        prettyNow = os.date('%A, %B %d %Y at %I:%M:%S')
        print("Making the call to the main page")
        response = http.get(host, port.number, path)
        print("#=====================#")
        if response.status == 200 then
                print(path.. " PATH EXIST")
        else
                print(path.. " PATH DOESNT EXISTS")
        end
        print("#=====================#")
        return prettyNow.. " http port is open "
end

-- END --

-- Reference: https://gist.github.com/fschaefer/e8ebeb18b2d513494268 --
-- nmap --script=test.nse --script-args "paths=/mochi" 10.0.2.20 --
