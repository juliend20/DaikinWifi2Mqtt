MQTT_HOST = "localhost"
MQTT_PORT = 1883

MQTT_GATEWAY_BASE_TOPIC = "daikin/"
MQTT_GATEWAY_MESSAGE = "message"

MQTT_GATEWAY_STATUS_CMD = MQTT_GATEWAY_BASE_TOPIC + "status"
MQTT_GATEWAY_ERROR_CMD = MQTT_GATEWAY_BASE_TOPIC + "error"

MQTT_GATEWAY_CONTROL_CMD = MQTT_GATEWAY_BASE_TOPIC + "control"
MQTT_GATEWAY_REFRESH_CMD = MQTT_GATEWAY_BASE_TOPIC + "refresh"

MQTT_GATEWAY_CONTROL_RESULT = MQTT_GATEWAY_BASE_TOPIC + "result"
MQTT_GATEWAY_REFRESH_DATA = MQTT_GATEWAY_BASE_TOPIC + "data"
MQTT_GATEWAY_REFRESH_SENSOR = MQTT_GATEWAY_BASE_TOPIC + "sensor"

MQTT_GATEWAY_PUBLISH_TOPIC = MQTT_GATEWAY_BASE_TOPIC + "publish"

MQTT_GATEWAY_STATUS_START = "start"
MQTT_GATEWAY_STATUS_QUIT = "quit"

#   daikin/refresh      {"host": "http://127.0.0.1:5000"}
