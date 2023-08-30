## How do you design MQTT topics and payloads for smart washing machine

1. สถานะเครื่องซักผ้า
    - topic:v1cdti/app/get/1212312121/model-01/sn-001/
    - payload
        - {"STATUS": "POWER ON|START|STOP|FINISHED|POWERED OFF"}
1. เซนเซอร์ภายในเครื่องซักผ้า
    - topic:v1cdti/app/get/1212312121/model-01/sn-001
    - payload
        - {"temperature": "25.2"}
        - {"speed": "30"}
        - {"current": "40"}
        - {"pressure": "20"}
        - {"microphone": "2"}
        - {"co2 sensor": "5"}
        - {"weight": "2"}
        - {"detergent": "2"}
        - {"XMC4000": "6"}
        

 1. เซนเซอร์ภายนอกเครื่องซักผ้า
    - topic:v1cdti/app/get/1212312121/model-01/sn-001
    - payload
        - {"trustM": "3"}
        - {"temperature": "27.5"}
        - {"huminity": "18"}
        - {"m_touch": "0"}
        - {"vibration": "1"}
        - {"air": "100"}
        - {"current": "110"}



