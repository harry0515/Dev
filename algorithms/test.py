{"status": 0,
 "msg": "",
 "links": [{"to_port_id": 4, "type": "multi_cluster_balance_2", "from_port_id": 1},
           {"to_port_id": 10, "type": "multi_cluster_balance_2", "from_port_id": 1}, ],

 "port_configuration": [
     {"port_display_id": "1", "rate": "10", "receiving": false, "port_name": "Port_1_1516655757", "mode": "Standard",
      "io": "I", "active": true, "time_stamp": "Y", "forwarding": false, "port_id": 1},
     {"port_display_id": "2", "rate": "10", "receiving": false, "port_name": "Port_2_1516655757", "mode": "Standard",
      "io": "O", "active": true, "time_stamp": "N", "forwarding": false, "port_id": 2}]}




{
  "swagger": "2.0",
  "info": {
    "description": "cVu API",
    "version": "1.0.0",
    "title": "cVu",
    "contact": {
      "email": "cpacket@cpacketnetworks.com"
    },
    "license": {
      "name": "Apache 2.0",
      "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
    }
  },
  "schemes": [
    "https"
  ],
  "host": "localhost",
  "responses": {
    "Unauthorized": {
      "description": "Unauthorized to perform this action"
    }
  },
  "tags": [
    {
      "name": "Authentication",
      "description": "cVu athentication APIs"
    },
    {
      "name": "Internal",
      "description": "Internal APIs"
    },
    {
      "name": "General",
      "description": "General purpose APIs"
    },
    {
      "name": "Counters",
      "description": "API related to port counters"
    }
  ],
  "paths": {
    "/version.json": {
      "get": {
        "summary": "Device version info",
        "tags": [
          "General"
        ],
        "responses": {
          "200": {
            "description": "Device version info",
            "schema": {
              "type": "object",
              "properties": {
                "firmware_version": {
                  "type": "string",
                  "description": "The software or firmware version",
                  "example": "18.1.1_T297.cVu560NG_MASTER.43751E.01052018/2E/2E/2E/2A"
                },
                "device_serial_number": {
                  "type": "string",
                  "description": "The serial number assigned to the device",
                  "example": "170026-24-A02"
                },
                "chassis_controller_version": {
                  "type": "string",
                  "description": "The version number of the device chassis",
                  "example": "1.1.7"
                },
                "hostname": {
                  "type": "string",
                  "description": "Hostname"
                },
                "backboard_serial_number": {
                  "type": "string",
                  "description": "Device backboard serial number"
                },
                "product_label": {
                  "type": "string",
                  "example": "cVu560NG_MASTER"
                },
                "switch": {
                  "$ref": "#/definitions/VersionSwitch"
                },
                "port_mode_versions": {
                  "$ref": "#/definitions/ArrayOfPortModeVersions"
                }
              }
            }
          }
        }
      }
    }
  },
  "definitions": {
    "Forbidden": {
      "type": "object",
      "properties": {
        "status": {
          "type": "integer",
          "example": 403
        },
        "msg": {
          "type": "string",
          "example": "NoAccess"
        }
      }
    },
    "VersionSwitch": {
      "type": "object",
      "description": "Version info of the internal switch",
      "properties": {
        "serial_number": {
          "type": "string",
          "example": "CPSFCR-13500007"
        },
        "version": {
          "type": "string",
          "example": "21740"
        }
      }
    },
    "ArrayOfPortModeVersions": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/PortModeVersion"
      }
    },
    "PortModeVersion": {
      "type": "object",
      "description": "Version info of the FPGA",
      "properties": {
        "portid": {
          "type": "string",
          "example": 5
        },
        "port_display_id": {
          "type": "string",
          "example": 2.1
        },
        "mode": {
          "type": "string",
          "example": "cBurst"
        },
        "mode_id": {
          "type": "string",
          "example": "JB_40G"
        },
        "mode_version": {
          "type": "string",
          "example": 42664
        },
        "subports": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/SubPortModeVersion"
          }
        }
      }
    },
    "SubPortModeVersion": {
      "type": "object",
      "properties": {
        "portid": {
          "type": "string",
          "example": 6
        },
        "port_display_id": {
          "type": "string",
          "example": 2.2
        }
      }
    }
  }
}